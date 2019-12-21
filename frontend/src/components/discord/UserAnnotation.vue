<template>
  <v-card>
    <v-toolbar color="primary">
      <v-toolbar-title>
        {{ user.user.ingame_name }}
      </v-toolbar-title>

      <v-spacer />

      <transition name="fade" mode="out-in">
        <span key="entregue" v-if="given">Entregue</span>
        <span key="nao-entregue" v-else>Não Entregue</span>
      </transition>

      <v-btn icon :color="given ? 'success accent-2' : 'error lighten-1'" @click="toggleGiven">
        <v-icon>
          fas fa-check
        </v-icon>
      </v-btn>
    </v-toolbar>

    <v-card-text>
      <div class="mb-3">
        <!-- Presenteando -->
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-icon v-on="on" color="#888" small>
              fas fa-gifts
            </v-icon>
          </template>
          <span>Presenteando</span>
        </v-tooltip>

        <span class="font-weight-light">
          {{ user.giving_to_user.ingame_name }}
        </span>
      </div>

      <v-divider class="mb-3" />

      <v-textarea
        v-model="text"
        label="Anotações"
        clearable
        filled
        auto-grow
        name="anotacoes"
        rows="5"
      />
    </v-card-text>
  </v-card>
</template>


<script lang="ts">
import { Vue, Prop } from 'vue-property-decorator'
import Component from 'vue-class-component'

import { DiscordApi } from '@/types'

@Component({})
export default class UserAnnotation extends Vue {
  @Prop() private user!: DiscordApi['SecretSantaUser']

  private given: boolean = false

  public text: string = ''

  toggleGiven(): void {
    this.given = !this.given

    this.$emit('given', this.given)
  }
}
</script>
