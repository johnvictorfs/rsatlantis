<template>
  <v-layout>
    <v-container>
      <v-row justify="center">
        <v-col xs="12" sm="10" md="8" lg="6" xl="6">
          <Events />
        </v-col>

        <v-col xs="12" sm="10" md="8" lg="6" xl="6">
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
const ClueHiscores = () => import('@/components/hiscores/ClueHiscores.vue')
const Events = () => import('@/components/Events.vue')

@Component({
  components: { DiscordStatus, ClueHiscores, Events }
})
export default class HomePage extends Vue {}
</script>

<style lang="scss">
.container {
  max-width: 1385px;
}
</style>
