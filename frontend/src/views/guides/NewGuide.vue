<template>
  <v-container fluid fill-height>
    <v-row justify="center">
      <v-col cols="12" lg="10" xs="12" sm="12">
        <v-card class="elevation-12">
          <v-toolbar dark color="green">
            <v-toolbar-title>Criar um Novo Guia</v-toolbar-title>
          </v-toolbar>

          <v-container fluid grid-list-md>
            <v-card-text>
              <v-form ref="form" v-model="valid">
                <v-text-field filled required label="Título" v-model="guide.title" :counter="25" maxlength="25" />

                <v-text-field filled required label="Descrição" v-model="guide.description" :counter="40" maxlength="40" />

                <v-select filled required label="Categoria" :items="categories" v-model="guide.category" />
              </v-form>

              <v-layout>
                <v-flex xs6>
                  <v-textarea
                    @keydown.prevent.tab="addTab($event)"
                    filled
                    auto-grow
                    name="input-7-4"
                    rows="10"
                    label="Conteúdo"
                    v-model="guide.content"
                    :value="markdownContent"
                  />
                </v-flex>
                <v-flex xs6>
                  <v-toolbar style="border-radius: 12px;" dark color="yellow darken-4">
                    <v-spacer />
                    <v-toolbar-title>
                      <h3>Preview</h3>
                    </v-toolbar-title>
                    <v-spacer />
                  </v-toolbar>
                  <GuideDetail :guide="guide" :author="currentUser" />
                </v-flex>
              </v-layout>
              <v-divider class="my-2" />
            </v-card-text>

            <v-card-actions>
              <v-layout>
                <v-flex xs10 offset-xs1 lg6 offset-lg3>
                  <v-btn
                    height="40"
                    outlined
                    rounded
                    block
                    color="success"
                    :disabled="!valid"
                    @click="submit"
                  >
                    Enviar
                    <v-icon right>
                      check
                    </v-icon>
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-card-actions>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Vue, Prop } from 'vue-property-decorator'
import Component from 'vue-class-component'
import marked from 'marked'

import GuideDetail from '@/components/GuideDetail.vue'

import { formatError } from '@/helpers/errors'
import { IGuide, GuideCategory } from '@/types'

@Component({ components: { GuideDetail } })
export default class NewGuide extends Vue {
  valid: boolean = true

  categories: Array<GuideCategory> = ['PvM', 'Habilidades', 'Outros']

  guide: IGuide = {
    title: '',
    description: '',
    category: '',
    content: ''
  }

  get markdownContent() {
    /**
     * https://marked.js.org/#/USING_ADVANCED.md
     */
    return marked(this.guide.content, { sanitize: true, breaks: true })
  }

  get currentUser() {
    const { auth } = this.$store.state
    if (auth) return auth.user
  }

  private addTab(event: Event): void {
    /**
     * Insert 4 spaces when pressing Space inside the
     * 'Content' text box
     */
    if (event) {
      event.preventDefault()
      document.execCommand('insertText', false, '    ')
    }
  }

  private async submit(): Promise<void> {
    /**
     * https://stackoverflow.com/a/52109899
     */
    if ((this.$refs.form as any).validate()) {
      switch (this.guide.category) {
        case 'PvM':
          this.guide.category = 'pvm'
          break
        case 'Habilidades':
          this.guide.category = 'skilling'
          break
        default:
          this.guide.category = 'others'
      }
      try {
        await this.$store.dispatch('publishGuide', { ...this.guide })
        this.$toasted.global.success('Seu guia foi publicado com sucesso! Ele estará disponível quando aprovado')
        this.$router.push({ name: 'guides.list' })
      } catch (error) {
        this.$toasted.global.error(formatError(error))
      }
    }
  }
}
</script>
