<template>
  <v-app :dark="darkTheme">
    <Toolbar></Toolbar>
    <v-content>
      <router-view></router-view>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
  import Toolbar from './components/Toolbar'
  import Footer from './components/Footer'

  export default {
    name: 'App',
    components: {
      Footer,
      Toolbar
    },
    computed: {
      darkTheme() {
        return this.$store.getters.isDarkTheme
      }
    }
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
</style>