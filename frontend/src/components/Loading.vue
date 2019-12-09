<template>
  <v-overlay :value="loading">
    <v-progress-circular indeterminate size="64" />
  </v-overlay>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

@Component({})
export default class Loading extends Vue {
  get loading() {
    return this.$store.state.loading.loading
  }
}
</script>
