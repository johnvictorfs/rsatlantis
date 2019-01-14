<template>
  <v-footer class="white--text text-xs-center" dark>
    <v-flex>
      &copy;{{ new Date().getFullYear() }} — <strong>
      <a target="_blank" class="link link--external" href="https://github.com/johnvictorfs/">
        John Victor
      </a>
    </strong>
    </v-flex>
  </v-footer>
</template>

<script>
  export default {
    name: "Footer",
  }
</script>