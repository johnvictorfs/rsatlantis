<template>
  <v-container>
    <br/>
    <v-flex justify-center xs12 sm8 md4 offset-xs4>
      <v-alert :value="notFound" type="error">
        Guia '{{ slug }}' não encontrado
      </v-alert>
      <Guide v-if="showGuide" :guide="guide" :content="true" :details-button="false"></Guide>
    </v-flex>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

import api from '../../api'
const Guide = () => import('../../components/Guide.vue')

@Component({
  props: {
    slug: {
      type: String,
      default: ''
    }
  },
  components: { Guide }
})
export default class GuideDetail extends Vue {
  notFound: boolean = false
  showGuide: boolean = false
  guide = {}

  async mounted() {
    try {
      // @ts-ignore
      const { data: guide } = await this.$store.dispatch('guideDetails', this.slug)
      switch (guide.category) {
        case 'pvm':
          guide.category = 'PvM'
          break
        case 'skilling':
          guide.category = 'Habilidades'
          break
        default:
          guide.category = 'Outros'
      }
      this.guide = guide
      this.showGuide = true
      try {
        let { data: author } = await api.get(guide.author)
        this.guide = {
          ...this.guide,
          author: {
            name: author.username,
            isAdmin: author.is_staff,
            isSuperUser: author.is_superuser
          }
        }
      } catch (error) {
        this.guide = {
          ...this.guide,
          author: {
            name: 'N/A',
            isAdmin: false,
            isSuperUser: false
          }
        }
      }
    } catch (error) {
      this.notFound = true
    }
  }
}
</script>
