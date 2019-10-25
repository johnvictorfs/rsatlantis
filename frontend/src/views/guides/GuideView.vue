<template>
  <v-container>
    <v-alert border="top" type="error" transition="scale-transition" v-if="apiError">
      Guia '{{slug}}' não encontrado.
    </v-alert>

    <v-alert border="top" type="error" transition="scale-transition" v-if="!apiError && !guide.approved">
      Esse Guia não foi aprovado ainda.
    </v-alert>

    <GuideDetail :guide="guide" :author="author"></GuideDetail>
  </v-container>
</template>

<script lang="ts">
import { Vue, Prop } from 'vue-property-decorator'
import Component from 'vue-class-component'

import GuideDetail from '@/components/GuideDetail.vue'
import { IApiGuide, IApiUser } from '@/types'
import api from '@/api'

@Component({ components: { GuideDetail } })
export default class GuideView extends Vue {
  @Prop() private slug!: string;

  private guide: IApiGuide = {
    url: '',
    title: '',
    slug: '',
    category: '',
    description: '',
    content: '',
    approved: false,
    date_posted: '',
    author: ''
  };

  private author: IApiUser = {
    username: '',
    ingame_name: '',
    email: '',
    is_staff: false,
    is_superuser: false,
    url: '',
    guides: '',
    groups: []
  };

  private apiError: boolean = false;

  async created() {
    try {
      const { data: guide }: { data: IApiGuide } = await api.get(`guides/${this.slug}`)
      this.guide = guide
      const { data: author }: { data: IApiUser } = await api.get(guide.author)
      this.author = author
    } catch (error) {
      this.apiError = true
    }
  }

  get authorIcon(): 'fa-user-shield' | 'account_circle' {
    if (this.author.is_superuser || this.author.is_staff) {
      return 'fa-user-shield'
    }
    return 'account_circle'
  }

  get guideCategory(): 'PvM' | 'Habilidades' | 'Outros' {
    switch (this.guide.category) {
      case 'pvm' || 'PvM':
        return 'PvM'
      case 'skilling' || 'Habilidades':
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

