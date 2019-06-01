<template>
  <v-card class="elevation-12 mb-2" color="grey darken-3">
    <v-card-title primary-title>
      <v-btn round absolute top left>
        <v-icon small left>{{ authorIcon }}</v-icon>
        {{ guide.author.name }}
      </v-btn>
      <v-btn small round absolute top right color="grey darken-1">
        {{ guide.category }}
      </v-btn>
      <div>
        <div class="headline guide-title">
          {{ guide.title }} asdasd asdasdasd asdasdasd asdasdasd
        </div>
        <span>
          {{ guide.description }}
        </span>
      </div>
    </v-card-title>

    <v-card-actions class="guide-actions">
      <v-btn class="atl-btn mb-1"  small color="primary" :to="{name: 'guides.detail', params: {slug: guide.slug}}">
        Ver Guia
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
    name: "Guide",
    props: {
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

<style scoped>
  .guide-title {
    font-size: 32px !important;
    margin-bottom: 10px;
  }

  .guide-actions {
    justify-content: center;
  }
</style>