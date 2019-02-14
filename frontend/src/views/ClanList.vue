<template>
  <v-layout align-center justify-center>
    <v-flex xs12 sm8 md6>
      <v-alert slot="apiError" :value="apiError" color="error" icon="warning" transition="scale-transition">
        Não foi possível acessar o Banco de Dados de Membros do Clã. Tente novamente mais tarde :(
      </v-alert>

      <v-card>
        <v-card-title>
          <v-toolbar dark color="grey darken-2">
            <v-toolbar-title>Membros do Clã</v-toolbar-title>

            <v-spacer></v-spacer>

            <!-- Desktop Update Clans button -->
            <v-btn small :disabled="loading" @click="updateClanList" class="hidden-sm-and-down">
              <v-icon color="white" left small>fa-sync-alt</v-icon>
              Atualizar
            </v-btn>

            <!-- Mobile Update Clans icon -->
            <v-btn fab small :disabled="loading" @click="updateClanList" class="hidden-md-and-up">
              <v-icon small color="white">fa-sync-alt</v-icon>
            </v-btn>

          </v-toolbar>

          <v-spacer></v-spacer>

          <v-text-field v-model="search" append-icon="search" label="Pesquisar" single-line
                        hide-details></v-text-field>
        </v-card-title>
        <div>
          <v-data-table :headers="headers" :items="members" :search="search" :rows-per-page-items="rows_per_page"
                        disable-initial-sort align="center" :pagination.sync="pagination" hide-actions
                        class="elevation-1">
            <template slot="items" slot-scope="props">
              <td class="text-xs-center">{{ props.item.name }}</td>
              <td class="text-xs-center">{{ props.item.translated_rank }}</td>
              <td class="text-xs-center">{{ props.item.exp | commaSeparatedVal }}</td>
            </template>
            <v-alert slot="no-results" :value="true" color="error">
              Nenhum resultado encontrado para "{{ search }}".
            </v-alert>
          </v-data-table>
          <div class="text-xs-center pt-2 light-grey-background">
            <v-pagination v-model="pagination.page" :length="pages" color="grey darken-4"></v-pagination>
          </div>
        </div>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  import clan from '../api/clan'

  export default {
    name: "ClanList",
    data: () => ({
      pagination: {},
      selected: [],
      apiError: false,
      search: '',
      rows_per_page: [10, 20, {"text": "$vuetify.dataIterator.rowsPerPageAll", "value": -1}],
      headers: [
        {text: 'Nome', value: 'name', align: 'center'},
        {text: 'Rank', value: 'translated_rank', align: 'center'},
        {text: 'Exp', value: 'exp', align: 'center'}
      ],
      members: []
    }),
    mounted() {
      this.updateClanList(false);
    },
    computed: {
      loading() {
        return this.$store.state.loading.loading;
      },
      pages() {
        if (this.pagination.rowsPerPage == null ||
          this.pagination.totalItems == null
        ) return 0;
        return Math.ceil(this.pagination.totalItems / this.pagination.rowsPerPage);
      }
    },
    filters: {
      commaSeparatedVal(num) {
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }
    },
    methods: {
      updateClanList(notification = true) {
        this.$store.dispatch('setLoading').then();
        clan.clanList().then(response => {
          this.members = response.data;
          this.apiError = false;
          this.pagination.totalItems = this.members.length;
          if (notification) {
            this.$toasted.global.success('Membros do Clã atualizados com sucesso!');
          }
        }).catch(() => {
          this.apiError = true;
        }).finally(() => {
          this.$store.dispatch('removeLoading').then();
        })
      }
    }
  }
</script>

<style scoped>
  .light-grey-background {
    background: #757575
  }
</style>