<template>
  <v-layout>
    <v-container>
      <v-row justify="end">
        <v-col xs="12" sm="10" md="8" lg="8" xl="6">
          <DiscordStatus />
        </v-col>
      </v-row>
    </v-container>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

const DiscordStatus = () => import('@/components/discord/DiscordStatus.vue')

@Component({
  components: { DiscordStatus }
})
export default class HomePage extends Vue {}
</script>
