<template>
  <v-layout row fill-height justify-center align-center v-if="loading">
    <v-progress-circular :size="50" color="primary" indeterminate/>
  </v-layout>
</template>

<script>
  export default {
    name: "Loading",
    computed: {
      loading() {
        return this.$store.state.loading.loading;
      }
    }
  }
</script>