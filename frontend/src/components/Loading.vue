<template>
  <v-dialog v-model="$store.state.loading.loading" hide-overlay persistent width="80">
    <v-card>
      <v-card-text>
        <v-progress-circular :size="50" color="primary" indeterminate class="mb-0"/>
      </v-card-text>
    </v-card>
  </v-dialog>
  <!--<v-layout row fill-height justify-center align-center v-if="loading">-->
  <!--<v-progress-circular :size="50" color="primary" indeterminate/>-->
  <!--</v-layout>-->
</template>

<script>
export default {
  name: "Loading",
  computed: {
    loading() {
      return this.$store.state.loading.loading;
    }
  }
};
</script>
