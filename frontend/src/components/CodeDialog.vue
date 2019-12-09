<template>
  <v-dialog v-model="dialog" width="500">
    <v-btn slot="activator" icon ripple>
      <v-icon color="grey lighten-1">
        {{ activatorIcon }}
      </v-icon>
    </v-btn>

    <v-card>
      <v-card-title class="headline" primary-title>
        {{ title }}
      </v-card-title>

      <v-card-text>
        <kbd>{{ text }}</kbd>
      </v-card-text>

      <v-divider />

      <v-card-actions>
        <v-spacer />
        <v-btn color="error" text @click="dialog = false">
          <v-icon left>
            fa-times
          </v-icon>Fechar
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'CodeDialog',
  props: {
    title: {
      type: String,
      default: ''
    },
    text: {
      type: String,
      default: ''
    },
    activatorIcon: {
      type: String,
      default: ''
    }
  },
  data: () => ({
    dialog: false
  })
}
</script>
