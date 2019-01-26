<template>
  <v-app :dark="darkTheme">
    <Toolbar :items="filteredToolbarItems"></Toolbar>
    <v-content>
      <Loading></Loading>
      <transition name="fade" mode="out-in" @beforeLeave="beforeLeave">
        <router-view></router-view>
      </transition>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
  import Toolbar from './components/Toolbar'
  import Footer from './components/Footer'
  import Loading from './components/Loading'

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
        {text: 'Guias', path: {name: 'guides.list'}, color: 'orange', auth: 'any', icon: 'fa-list'},
        {text: 'Entrar', path: {name: 'login'}, color: 'success', auth: false, icon: 'fa-sign-in-alt'},
        {text: 'Cadastro', path: {name: 'register'}, color: 'primary', auth: false, icon: 'fa-user-plus'},
        {text: 'Novo Guia', path: {name: 'guides.new'}, color: 'success', auth: true, icon: 'fa-plus-square'},
        {text: 'Sair', path: {name: 'logout'}, color: 'error', auth: true, icon: 'fa-sign-out-alt'},
      ],

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
        let items = [];
        for (let i = 0; i < this.toolbarItems.length; i++) {
          if (this.toolbarItems[i].auth === this.$store.getters.isAuthenticated) {
            items.push(this.toolbarItems[i])
          } else if (this.toolbarItems[i].auth === 'any') {
            items.push(this.toolbarItems[i]);
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