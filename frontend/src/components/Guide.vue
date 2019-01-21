<template>
  <v-card class="elevation-12" light>
    <v-toolbar dark color="primary">
      <v-btn round absolute top left :color="authorColor">
        <v-icon small left>{{ authorIcon }}</v-icon>
        {{ guide.author.name }}
      </v-btn>
      <v-toolbar-title>
        {{ guide.title }}
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-chip>
        {{ guide.category }}
      </v-chip>

    </v-toolbar>
    <v-toolbar light>
      <v-toolbar-title>
        {{ guide.description }}
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn right small color="primary" v-if="detailsButton" :to="{name: 'guide-detail', params: {slug: guide.slug}}">
        Ver Guia
      </v-btn>
    </v-toolbar>
    <v-divider></v-divider>
    <v-card-text class="headline" v-if="content">
      <div v-html="guide.content"></div>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: "Guide",
    props: {
      detailsButton: Boolean,
      content: Boolean,
      guide: Object,
    },
    computed: {
      authorColor() {
        if (this.guide.author.isSuperUser) {
          return 'yellow darken-3';
        } else if (this.guide.author.isAdmin) {
          return 'error';
        } else {
          return 'primary';
        }
      },
      authorIcon() {
        if (this.guide.author.isSuperUser) {
          return 'fa-user-shield';
        } else if (this.guide.author.isAdmin) {
          return 'fa-user-shield';
        } else {
          return 'account_circle';
        }
      }
    }
  }
</script>