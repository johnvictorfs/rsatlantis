<template>
  <v-container>
    <v-card class="guide-card">
      <v-toolbar color="light-blue darken-2">
        <v-spacer />
        <v-toolbar-title>
          <h2 class="guide-title">{{guide.title}}</h2>
        </v-toolbar-title>
        <v-spacer />
      </v-toolbar>

      <v-toolbar color="light-blue darken-4">
        <v-btn color="light-green darken-3 mr-3">
          <v-icon left>{{ authorIcon }}</v-icon>
          <strong>{{author.username}}</strong>
        </v-btn>

        <v-spacer />

        <p class="guide-description pt-4">{{guide.description}}</p>

        <v-spacer />

        <v-btn :color="categoryColor">
          <v-icon left>{{categoryIcon}}</v-icon>
          <strong>{{guideCategory}}</strong>
        </v-btn>

      </v-toolbar>
      <v-card-text>
        <div class="markdown-render mb-0" v-html="markdownContent"></div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Vue, Prop } from 'vue-property-decorator'
import Component from 'vue-class-component'
import marked from 'marked'

import { IGuide, IUser } from '@/types'
import api from '@/api'

@Component({})
export default class GuideDetail extends Vue {
  @Prop() private guide!: IGuide;
  @Prop() private author!: IUser;

  get markdownContent(): string {
    return marked(this.guide.content)
  }

  get authorIcon(): 'fa-user-shield' | 'account_circle' {
    if (this.author.is_superuser || this.author.is_staff) {
      return 'fa-user-shield'
    }
    return 'account_circle'
  }

  get guideCategory(): 'PvM' | 'Habilidades' | 'Outros' {
    switch (this.guide.category) {
      case 'pvm':
      case 'PvM':
        return 'PvM'
      case 'skilling':
      case 'Habilidades':
        return 'Habilidades'
      default:
        return 'Outros'
    }
  }

  get categoryIcon(): 'mdi-sword-cross' | 'mdi-chart-bar' | 'mdi-notification-clear-all' {
    switch (this.guideCategory) {
      case 'PvM':
        return 'mdi-sword-cross'
      case 'Habilidades':
        return 'mdi-chart-bar'
      default:
        return 'mdi-notification-clear-all'
    }
  }

  get categoryColor(): 'red darken-4' | 'green darken-1' | 'grey darken-3' {
    switch (this.guideCategory) {
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

<style lang="scss">
@import '@/assets/css/markdown.scss';

.author-name {
  font-size: 19px;
  font-weight: bold;
}

.guide-description {
  font-size: 22px;
}

.guide-title {
  font-family: Rubik;
}

.guide-card {
  border-radius: 10px;
}
</style>
