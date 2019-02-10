<template>
  <v-app :dark="darkTheme">
    <Toolbar :toolbar-items="filteredToolbarItems" :sidebar-items="filteredSidebarItems"></Toolbar>
    <v-content>
      <Loading></Loading>
      <transition name="fade" mode="out-in" @beforeLeave="beforeLeave">
        <v-container fluid>
          <router-view></router-view>
        </v-container>
      </transition>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>

  const Toolbar = () => import('./components/Toolbar');
  const Footer = () => import('./components/Footer');
  const Loading = () => import('./components/Loading');

  export default {
    name: 'App',
    components: {
      Footer,
      Toolbar,
      Loading
    },
    data: () => ({
      prevHeight: 0,
      toolbarItems: [
        {text: 'Entrar', path: {name: 'login'}, color: 'success', auth: false, icon: 'fa-sign-in-alt'},
        {text: 'Cadastro', path: {name: 'register'}, color: 'primary', auth: false, icon: 'fa-user-plus'},
        {text: 'Sair', path: {name: 'logout'}, color: 'error', auth: true, icon: 'fa-sign-out-alt'},
      ],
      sidebarItems: [
        {text: 'Novo Guia', path: {name: 'guides.new'}, color: 'success', auth: true, icon: 'fa-plus-square'},
        {text: 'Guias', path: {name: 'guides.list'}, color: 'orange', auth: 'any', icon: 'fa-list'},
      ]
    }),
    created() {
      if (this.$store.getters.isAuthenticated) {
        this.$store.dispatch('accountDetails').then()
      }
    },
    computed: {
      darkTheme() {
        return this.$store.getters.isDarkTheme
      },
      filteredToolbarItems: function () {
        /*
        Filters items based on if they are shown to authenticated users or not, according to if the user is
        authenticated or not.
        */

        let items = [];
        for (let i = 0; i < this.toolbarItems.length; i++) {
          if (this.toolbarItems[i].auth === this.$store.getters.isAuthenticated) {
            items.push(this.toolbarItems[i])
          } else if (this.toolbarItems[i].auth === 'any') {
            items.push(this.toolbarItems[i]);
          }
        }
        return items;
      },
      filteredSidebarItems: function () {
        /*
        Filters items based on if they are shown to authenticated users or not, according to if the user is
        authenticated or not.
        */
        let items = [];
        for (let i = 0; i < this.sidebarItems.length; i++) {
          if (this.sidebarItems[i].auth === this.$store.getters.isAuthenticated) {
            items.push(this.sidebarItems[i])
          } else if (this.sidebarItems[i].auth === 'any') {
            items.push(this.sidebarItems[i]);
          }
        }
        return items;
      }
    },
    methods: {
      beforeLeave(element) {
        this.prevHeight = getComputedStyle(element).height;
      },
      enter(element) {
        const {height} = getComputedStyle(element);

        element.style.height = this.prevHeight;

        setTimeout(() => {
          element.style.height = height;
        });
      },
      afterEnter(element) {
        element.style.height = 'auto';
      },
    },
  }
</script>

<style>
  body {
    font-family: "Open Sans",
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    Roboto,
    Oxygen-Sans,
    Ubuntu,
    Cantarell,
    "Helvetica Neue",
    Helvetica,
    Arial,
    sans-serif;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition-duration: 0.3s;
    transition-property: opacity;
    transition-timing-function: ease;
  }

  .fade-enter,
  .fade-leave-active {
    opacity: 0
  }
</style>