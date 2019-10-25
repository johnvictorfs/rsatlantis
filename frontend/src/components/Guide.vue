<template>
  <v-hover>
    <template v-slot:default="{ hover }">
      <v-card class="elevation-12 mb-2 guide-card" color="grey darken-3" width="400">
        <v-toolbar color="light-blue darken-4">
          <v-btn color="light-green darken-3">
            <v-icon left>{{ authorIcon }}</v-icon>
            <strong>{{guide.author.name}}</strong>
          </v-btn>

          <v-spacer></v-spacer>
          <v-btn small :color="categoryColor">
            <v-icon small left>{{categoryIcon}}</v-icon>
            <strong>{{guide.category}}</strong>
          </v-btn>
        </v-toolbar>

        <v-img
          v-if="guide.title == 'Guia Yakamaru'"
          height="200"
          src="https://runescape.wiki/images/thumb/7/76/Raids_concept_art.png/441px-Raids_concept_art.png?92ae9">
        </v-img>
        <v-img
          v-if="guide.title == 'Guia de Jack of Trades'"
          height="200"
          src="https://vignette.wikia.nocookie.net/runescape2/images/d/d2/Legendary_jack_of_trades_aura_detail.png/revision/latest?cb=20170722142749">
        </v-img>
        <v-img
          v-if="guide.title == 'Guia AoD'"
          height="200"
          src="http://legends-br.com/wp-content/uploads/2017/09/aod-760x490.jpg">
        </v-img>
        <v-card-text>
          {{ guide.description }}
        </v-card-text>
        <v-card-actions class="guide-actions hidden-md-and-up">
          <v-btn class="mb-1" style="height: 45px" large color="primary" :to="{name: 'guides.detail', params: {slug: guide.slug}}">
            Ver Guia
            <v-icon right>fa-book-open</v-icon>
          </v-btn>
        </v-card-actions>
        <v-fade-transition>
          <v-overlay v-if="hover" absolute class="hidden-sm-and-down">
            <v-btn class="mb-1" color="primary" :to="{name: 'guides.detail', params: {slug: guide.slug}}">
              Ver Guia
              <v-icon right>fa-book-open</v-icon>
            </v-btn>
          </v-overlay>
        </v-fade-transition>
      </v-card>
    </template>
  </v-hover>
</template>

<script lang="ts">
import { Vue, Prop } from 'vue-property-decorator'
import Component from 'vue-class-component'

import { IGuide } from '@/types'

@Component({})
export default class Guide extends Vue {
  @Prop() private guide!: IGuide;

  get authorColor(): 'yellow darken-3' | 'error' | 'primary' {
    if (this.guide.author.isSuperUser) return 'yellow darken-3'
    if (this.guide.author.isAdmin) return 'error'
    return 'primary'
  }

  get authorIcon(): 'fa-user-shield' | 'account_circle' {
    if (this.guide.author.isSuperUser || this.guide.author.isAdmin) {
      return 'fa-user-shield'
    }
    return 'account_circle'
  }

  get categoryIcon(): 'mdi-sword-cross' | 'mdi-chart-bar' | 'mdi-notification-clear-all' {
    switch (this.guide.category) {
      case 'PvM':
        return 'mdi-sword-cross'
      case 'Habilidades':
        return 'mdi-chart-bar'
      default:
        return 'mdi-notification-clear-all'
    }
  }

  get categoryColor(): 'red darken-4' | 'green darken-1' | 'grey darken-3' {
    switch (this.guide.category) {
      case 'PvM':
        return 'red darken-4'
      case 'Habilidades':
        return 'green darken-1'
      default:
        return 'grey darken-3'
    }
  }
}
</script>

<style scoped>
.guide-card {
  border-radius: 12px;
}

.guide-title {
  font-size: 32px !important;
  margin-bottom: 10px;
}

.guide-actions {
  justify-content: center;
}
</style>
