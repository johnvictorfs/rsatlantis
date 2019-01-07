<template>
  <v-app dark>
    <Toolbar></Toolbar>
    <router-view></router-view>
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