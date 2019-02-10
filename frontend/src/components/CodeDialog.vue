<template>
  <div>

    <v-dialog v-model="dialog" width="500">

      <v-btn icon ripple slot="activator">
        <v-icon color="grey lighten-1">{{ activatorIcon }}</v-icon>
      </v-btn>

      <v-card>
        <v-card-title class="headline" primary-title>
          {{ title }}
        </v-card-title>

        <v-card-text>
          <kbd>{{ text }}</kbd>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" flat @click="dialog = false">
            <v-icon left>fa-times</v-icon>
            Fechar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    name: "CodeDialog",
    props: {
      title: String,
      text: String,
      activatorIcon: String
    },
    data: () => ({
      dialog: false
    })
  }
</script>

<style scoped>

</style>