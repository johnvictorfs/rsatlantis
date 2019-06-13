<template>
  <v-hover>
    <template v-slot:default="{ hover }">
      <v-card class="elevation-12 mb-2" color="grey darken-3" width="400">
        <v-list-item>
          <v-list-item-avatar color="grey">
            <v-icon>{{ authorIcon }}</v-icon>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="headline">{{ guide.title }}</v-list-item-title>
            <v-list-item-subtitle>— {{ guide.author.name }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-img height="200" src="https://runescape.wiki/images/thumb/7/76/Raids_concept_art.png/441px-Raids_concept_art.png?92ae9"></v-img>
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

<script>
export default {
  name: 'Guide',
  props: {
    guide: {
      type: Object,
      default: () => {}
    }
  },

  computed: {
    authorColor() {
      if (this.guide.author.isSuperUser) {
        return 'yellow darken-3'
      }
      if (this.guide.author.isAdmin) {
        return 'error'
      }
      return 'primary'
    },
    authorIcon() {
      if (this.guide.author.isSuperUser) {
        return 'fa-user-shield'
      }
      if (this.guide.author.isAdmin) {
        return 'fa-user-shield'
      }
      return 'account_circle'
    }
  }
}
</script>

<style scoped>
.guide-title {
  font-size: 32px !important;
  margin-bottom: 10px;
}

.guide-actions {
  justify-content: center;
}
</style>
