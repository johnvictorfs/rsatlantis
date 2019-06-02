<template>
  <v-app dark>
    <Toolbar :toolbar-items="filteredToolbarItems" :sidebar-items="filteredSidebarItems"></Toolbar>
    <v-content>
      <transition name="fade">
        <v-container fluid>
          <Loading></Loading>
          <router-view></router-view>
        </v-container>
      </transition>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>


<script lang="ts">
const Toolbar = () => import('./components/Toolbar.vue');
const Footer = () => import('./components/Footer.vue');
const Loading = () => import('./components/Loading.vue');

import Vue from 'vue';
export default Vue.extend({
  name: 'App',
  components: {
    Footer,
    Toolbar,
    Loading
  },
  data: () => ({
    prevHeight: 0,
    toolbarItems: [
      { text: 'Entrar', path: { name: 'login' }, color: 'success', auth: false, icon: 'fa-sign-in-alt' },
      { text: 'Cadastro', path: { name: 'register' }, color: 'primary', auth: false, icon: 'fa-user-plus' },
      { text: 'Sair', path: { name: 'logout' }, color: 'error', auth: true, icon: 'fa-sign-out-alt' }
    ],
    sidebarItems: [
      { text: 'Novo Guia', path: { name: 'guides.new' }, color: 'success', auth: true, icon: 'fa-plus-square' },
      { text: 'Guias', path: { name: 'guides.list' }, color: 'orange', auth: 'any', icon: 'fa-list' },
      { text: 'Membros', path: { name: 'clan-list' }, color: 'primary', auth: 'any', icon: 'fa-users' }
    ]
  }),
  async created() {
    if (this.$store.getters.isAuthenticated) {
      await this.$store.dispatch('accountDetails');
    }
  },
  computed: {
    filteredToolbarItems() {
      /**
       * Filters items based on if they are shown to authenticated users or not, according to if the user is
       * authenticated or not.
       */
      const items = [];
      for (let i = 0; i < this.toolbarItems.length; i++) {
        if (this.toolbarItems[i].auth === this.$store.getters.isAuthenticated) {
          items.push(this.toolbarItems[i]);
        } else if (this.toolbarItems[i].auth === 'any') {
          items.push(this.toolbarItems[i]);
        }
      }
      return items;
    },
    filteredSidebarItems() {
      /**
       * Filters items based on if they are shown to authenticated users or not, according to if the user is
       * authenticated or not.
       */
      const items = [];
      for (let i = 0; i < this.sidebarItems.length; i++) {
        if (this.sidebarItems[i].auth === this.$store.getters.isAuthenticated) {
          items.push(this.sidebarItems[i]);
        } else if (this.sidebarItems[i].auth === 'any') {
          items.push(this.sidebarItems[i]);
        }
      }
      return items;
    }
  }
});
</script>

<style lang="scss">
body {
  font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial,
    sans-serif;
}

.v-btn {
  border-radius: 8px;
}

.v-btn--round {
  margin-left: 8px !important;
  border-radius: 50px;
}

.v-btn--round.v-btn--outline {
  border-width: 2px !important;
}

.v-card {
  border-radius: 8px;
}
</style>
