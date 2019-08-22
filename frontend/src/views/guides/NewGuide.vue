<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md8 lg8 xl8>
        <v-card class="elevation-12">

          <v-toolbar dark color="green">
            <v-toolbar-title>Criar um Novo Guia</v-toolbar-title>
          </v-toolbar>

          <v-container fluid grid-list-md>

            <v-card-text>
              <v-form ref="form" v-model="valid">
                <v-text-field filled required label="Título" v-model="guide.title" :counter="25" maxlength="25"></v-text-field>

                <v-text-field filled required label="Descrição" v-model="guide.description" :counter="40"
                              maxlength="40"></v-text-field>

                <v-select filled required label="Categoria" :items="categories" v-model="guide.category"></v-select>
              </v-form>

              <v-layout>
                <v-flex xs6>
                  <v-textarea
                    filled
                    auto-grow
                    name="input-7-4"
                    rows="10"
                    label="Conteúdo"
                    v-model="guide.content"
                    :value="markdownContent"
                  ></v-textarea>
                </v-flex>
                <v-flex xs6>
                  <v-card>
                    <v-toolbar dark color="yellow darken-3">
                      <v-toolbar-title>Preview</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                      <div v-html="markdownContent"></div>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
              <v-divider class="my-2"></v-divider>
            </v-card-text>
            <v-card-actions>
              <v-layout>
                <v-flex xs10 offset-xs1 lg6 offset-lg3>
                  <v-btn height="40" outlined rounded block color="success" :disabled="!valid" @click="submit">
                    Enviar
                    <v-icon right>check</v-icon>
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-card-actions>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

// https://stackoverflow.com/a/35961176
declare const require: any
const marked = require('marked')

import { formatError } from '../../helpers/errors'

@Component({})
export default class NewGuide extends Vue {
  valid: boolean = true
  categories: Array<string> = ['PvM', 'Habilidades', 'Outros']
  guide = {
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

  async submit() {
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
        await this.$store.dispatch('publishGuide', { ...this.guide, content: this.markdownContent })
        this.$toasted.global.success('Seu guia foi publicado com sucesso! Ele estará disponível quando aprovado')
        this.$router.push({ name: 'home' })
      } catch (error) {
        this.$toasted.global.error(formatError(error))
      }
      this.guide.content = this.markdownContent()
      this.$store.dispatch('publishGuide', this.guide).then(() => {
        this.$toasted.global.success('Seu guia foi publicado com sucesso! Ele estará disponível quando aprovado')
        this.$router.push({ name: 'home' })
      }).catch((error) => {
        this.$toasted.global.error(formatError(error))
      })
    }
  }
}
</script>
