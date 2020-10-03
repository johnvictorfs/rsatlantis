<template>
  <v-layout>
    <v-container>
      <v-row justify="center">
        <v-col xs="12" sm="10" md="8" lg="8" xl="6">
          <ClueHiscores />
        </v-col>
      </v-row>
    </v-container>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

const ClueHiscores = () => import('@/components/hiscores/ClueHiscores.vue')

@Component({
  components: { ClueHiscores }
})
export default class Hiscores extends Vue {}
</script>
