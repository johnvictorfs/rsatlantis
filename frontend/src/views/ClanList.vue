<template>
  <v-layout align-center justify-center>
    <v-flex xs12 sm10 md8 xl6>
      <v-alert
        slot="apiError"
        :value="apiError"
        color="error"
        icon="warning"
        transition="scale-transition"
        class="mb-3"
      >
        Não foi possível acessar os dados de Membros do Clã. Tente
        novamente mais tarde :(
      </v-alert>

      <v-card class="clan-list-card" v-if="!apiError">
        <v-toolbar dark color="grey darken-3">
          <v-toolbar-title class="clan-list-title">
            <h2 class="clan-list-title hidden-sm-and-down">
              Membros do Clã
            </h2>
            <h4 class="clan-list-title hidden-md-and-up">
              Membros do Clã
            </h4>
          </v-toolbar-title>

          <v-spacer />

          <!-- Desktop Update Clans button -->
          <v-btn :loading="loading" :disabled="loading" class="update-btn hidden-sm-and-down" @click="updateClanList" color="blue-grey darken-4">
            <v-icon color="white" left>
              fa-sync-alt
            </v-icon>Atualizar
          </v-btn>

          <!-- Mobile Update Clans icon -->
          <v-btn
            small
            fab
            :loading="loading"
            :disabled="loading"
            class="hidden-md-and-up"
            @click="updateClanList"
            color="blue-grey darken-4"
          >
            <v-icon small color="white">
              fa-sync-alt
            </v-icon>
          </v-btn>
        </v-toolbar>

        <v-text-field
          class="mx-4 mb-2"
          v-model="search"
          append-icon="search"
          label="Pesquisar"
          single-line
          hide-details
        />

        <v-data-table
          :loading="loading"
          :headers="headers"
          :items="members"
          :search="search"
          :items-per-page="10"
          :page.sync="page"
          locale="pt-BR"
          loading-text="Carregando..."
          no-data-text="Nenhum Membro Encontrado"
          @page-count="pageCount = $event"
          class="mx-2 elevation-1 clan-list-table"
          hide-default-footer
          :custom-sort="memberSort"
          sort-by="translated_rank"
          :sort-desc="true"
        >
          <template v-slot:item.name="{ item }">
            <v-layout row class="text-xs-center">
              <v-flex xs1>
                <v-avatar class="hidden-sm-and-down ml-2" tile>
                  <RunescapeChatHead :player-name="item.name" />
                </v-avatar>
              </v-flex>
              <v-flex xs10 class="mt-3 mr-5">
                {{ item.name }}
              </v-flex>
            </v-layout>
          </template>
          <template v-slot:item.translated_rank="{ item }">
            <div class="mr-4">
              <img style="vertical-align: middle;" :src="getRankIcon(item.rank)" :alt="`rank_${item.rank}`">
              <span>
                {{ item.translated_rank }}
              </span>
            </div>
          </template>
          <template v-slot:progress>
            <v-progress-linear color="green" :height="4" indeterminate />
          </template>
          <v-alert slot="no-results" :value="true" color="error" class="mt-3">
            Nenhum resultado encontrado para "{{ search }}"
          </v-alert>
        </v-data-table>
        <div class="text-xs-center pt-2 pb-2 light-grey-background hidden-sm-and-down">
          <v-pagination v-model="page" :length="pageCount" :total-visible="10" color="grey darken-4" />
        </div>
        <div class="text-xs-center pt-2 pb-2 light-grey-background hidden-md-and-up">
          <v-pagination v-model="page" :length="pageCount" :total-visible="6" color="grey darken-4" />
        </div>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

import api from '@/api'
import { IPlayer } from '@/types'

const RunescapeChatHead = () => import('@/components/RunescapeChatHead.vue')

@Component({
  components: { RunescapeChatHead }
})
export default class ClanList extends Vue {
  loading = false
  apiError = false
  search = ''
  page = 1
  pageCount = 0
  itemsPerPage = 15
  headers = [
    { text: 'Nome', value: 'name', align: 'center' },
    { text: 'Rank', value: 'translated_rank', align: 'center' },
    { text: 'Exp', value: 'exp', align: 'center' }
  ]
  members: IPlayer[] = []

  mounted() {
    this.updateClanList(false)
  }

  commaSeparatedVal(num: number | string): string {
    /**
     * Formats numbers into Comma-separated numbers (as a string)
     *
     * 123456789 -> '123,456,789'
     * '123456789' -> '123,456,789'
     */
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  }

  getRankIcon(rank: string): string {
    /**
     * Get the Rank Icon image by name
     */
    return require(`../assets/clan_ranks/${rank}.png`)
  }

  memberSort(items: any[], sortBy: string[], sortDesc: boolean[]) {
    if (sortBy[0] === 'translated_rank') {
      /**
       * Sort by rank based on in-game patents
       * https://stackoverflow.com/a/14872766
       * https://stackoverflow.com/a/54612408
       */
      const ordering: any = {}
      const sortOrder: Array<string> = [
        'Owner',
        'Deputy Owner',
        'Overseer',
        'Coordinator',
        'Organiser',
        'Admin',
        'General',
        'Captain',
        'Lieutenant',
        'Sergeant',
        'Corporal',
        'Recruit'
      ]

      for (let i = 0; i < sortOrder.length; ++i) {
        ordering[sortOrder[i]] = i
      }

      const newsItems = items.sort((a: any, b: any) => (ordering[a.rank] - ordering[b.rank]) || a.rank.localeCompare(b.rank))
      if (!sortDesc[0]) return newsItems.reverse()
      return newsItems
    } else if (sortBy[0] === 'name') {
      /**
       * Just sort by name normally, alphabetically
       */
      const newItems = items.sort((a, b) => a.name.localeCompare(b.name))
      if (!sortDesc[0]) return newItems.reverse()
      return newItems
    } else if (sortBy[0] === 'exp') {
      /**
       * Sort Clan Members based on their Clan Exp, needs the
       * comma-separated values to be converted to Integers before
       * running any comparisons
       */
      const newItems = items.sort((a, b) => {
        const expA = parseInt(a.exp.replace(/,/g, ''))
        const expB = parseInt(b.exp.replace(/,/g, ''))

        return expA - expB
      })
      if (!sortDesc[0]) return newItems.reverse()
      return newItems
    }
    return items
  }


  async updateClanList(notification: boolean = true) {
    try {
      this.loading = true
      const players = await api.players.all()
      this.members = players.map(player => ({ ...player, exp: this.commaSeparatedVal(player.exp) }))
      this.apiError = false
      if (notification) {
        this.$toasted.global.success('Membros do Clã atualizados com sucesso!')
      }
    } catch (error) {
      this.apiError = true
    } finally {
      this.loading = false
    }
  }
}
</script>

<style lang="scss" scoped>
.clan-list-title {
  font-family: Rubik, "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI",
  Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial,
  sans-serif;;
}

.clan-list-card {
  border-radius: 14px !important;
}

.update-btn {
  border-radius: 8px;
}

.light-grey-background {
  background: #3a3939;
  border-bottom-left-radius: 14px;
  border-bottom-right-radius: 14px;
}
</style>
