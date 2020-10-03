<template>
  <v-img
    lazy-src="@/assets/images/default_runescape_chat.png"
    max-width="80%"
    max-height="80%"
    :src="`https://secure.runescape.com/m=avatar-rs/${playerName.replace(/\s/g, '_')}/chat.png`"
    :alt="`avatar${playerName}`"
  >
    <template v-slot:placeholder>
      <v-row class="fill-height ma-0" align="center" justify="center">
        <v-progress-circular indeterminate color="grey lighten-5" />
      </v-row>
    </template>
  </v-img>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'RunescapeChatHead',
  props: {
    playerName: {
      type: String,
      default: ''
    }
  }
})
</script>
