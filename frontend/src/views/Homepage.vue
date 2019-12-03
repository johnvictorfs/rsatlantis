<template>
  <v-layout>
    <DiscordStatus/>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

const DiscordStatus = () => import('@/components/DiscordStatus.vue')

@Component({
  components: { DiscordStatus }
})
export default class HomePage extends Vue {}
</script>
