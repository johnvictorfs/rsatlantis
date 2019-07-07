<template>
  <v-layout align-center justify-center>
    <v-flex xs12 sm8 md5>
      <v-alert
        slot="apiError"
        :value="apiError"
        color="error"
        icon="warning"
        transition="scale-transition"
        class="mb-3"
      >
        Não foi possível acessar o Banco de Dados de Membros do Clã. Tente
        novamente mais tarde :(
      </v-alert>

      <v-card v-if="!apiError">
        <v-toolbar dark color="grey darken-2">
          <v-toolbar-title>Membros do Clã</v-toolbar-title>

          <v-spacer></v-spacer>

          <!-- Desktop Update Clans button -->
          <v-btn small :disabled="loading" class="hidden-sm-and-down" @click="updateClanList">
            <v-icon color="white" left small>fa-sync-alt</v-icon>Atualizar
          </v-btn>

          <!-- Mobile Update Clans icon -->
          <v-btn fab :disabled="loading" class="hidden-md-and-up" @click="updateClanList">
            <v-icon small color="white">fa-sync-alt</v-icon>
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
          <!-- :search="search" -->
          <!-- :rows-per-page-items="rows_per_page" -->
            <!-- :pagination.sync="pagination" -->

          <v-data-table
            :loading="loading"
            :headers="headers"
            :items="members"
            :search="search"
            loading-text="Carregando..."
            class="mx-2 elevation-1"
            :items-per-page="5"
            :page.sync="page"
            hide-default-footer
            @page-count="pageCount = $event"
          >
            <template v-slot:item.translated_rank="{ item }">
                <img
                  :src="require(`../assets/clan_ranks/${item.rank}.png`)"
                  :alt="'rank_' + item.rank"
                />
                {{ item.translated_rank }}
            </template>
            <template v-slot:progress>
              <v-progress-linear color="green" :height="4" indeterminate></v-progress-linear>
            </template>
            <v-alert slot="no-results" :value="true" color="error" class="mt-3">
              Nenhum resultado encontrado para "{{ search }}"
            </v-alert>
          </v-data-table>
          <div class="text-xs-center pt-2">
            <v-pagination v-model="page" :length="pageCount" :total-visible="10"></v-pagination>
          </div>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

import api from '../api'

@Component({})
export default class ClanList extends Vue {
  loading = false
  pagination = {}
  selected = []
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
  members = []

  mounted() {
    this.updateClanList(false)
  }

  // get pages() {
  //   if (
  //     this.pagination.rowsPerPage == null ||
  //     this.pagination.totalItems == null
  //   ) {
  //     return 0
  //   }
  //   return Math.ceil(this.pagination.totalItems / this.pagination.rowsPerPage)
  // }

  commaSeparatedVal(num: number): string {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  }

  async updateClanList(notification = true) {
    try {
      this.loading = true
      const { data } = await api.get('players')
      this.members = data.map((player: any) => ({ ...player, exp: this.commaSeparatedVal(player.exp) }))
      this.apiError = false
      // @ts-ignore
      this.pagination.totalItems = this.members.length
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
.light-grey-background {
  background: #757575;
}
</style>
