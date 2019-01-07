<template>
  <v-layout>
    <v-footer class="white--text text-xs-center" height="auto">
      <v-flex>
        &copy;{{ currentYear }} — <strong>John Victor</strong>
      </v-flex>
    </v-footer>
  </v-layout>
</template>

<script>
  export default {
    name: "Footer",
    data: () => ({
      currentYear: new Date().getFullYear()
    }),
  }
</script>

<style scoped>
  footer {
    width: 100%;
  }
</style>