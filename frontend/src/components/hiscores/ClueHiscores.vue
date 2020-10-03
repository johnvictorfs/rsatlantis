<template>
  <v-card class="atl-round-card" raised>
    <v-toolbar dark color="#363636">
      <v-toolbar-title>
        <v-icon left size="32" color="#9E826B">
          fas fa-scroll
        </v-icon>
        Pergaminhos de Dicas
      </v-toolbar-title>

      <v-btn icon class="ml-2 mb-2" disabled>
        <v-icon height="18" width="18">
          fa-sync-alt
        </v-icon>
      </v-btn>

      <template v-slot:extension>
        <v-tabs v-model="tab" align-with-title>
          <v-tabs-slider color="success" />

          <v-tab v-for="clueType in data" :key="clueType.type" :disabled="clueType.disabled">
            <v-img class="mr-1" height="24" width="24" :src="clueType.image" />
            {{ clueType.type }}
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="clueType in data" :key="clueType.type">
        <v-card flat>
          <v-list>
            <v-list-item-group>
              <v-list-item v-for="(player, i) in clueType.players" :key="i">
                <v-list-item-avatar>
                  <v-avatar size="48" color="primary darken-2">
                    <RunescapeChatHead :player-name="player.name" />
                  </v-avatar>
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title>
                    {{ player.name }}
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    <strong>Quantidade:</strong> {{ commaSeparatedVal(player.count) }}
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    <strong>Ranking Global:</strong> {{ commaSeparatedVal(player.global_rank) }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script lang="ts">
const RunescapeChatHead = () => import('@/components/RunescapeChatHead.vue')

import mockData from '@/mocks/clueHiscores.json' 

const lastUpdated = new Date()

import Vue from 'vue'
import Component from 'vue-class-component'

import { Nullable } from '@/types'

@Component({
  components: { RunescapeChatHead }
})
export default class ClueHiscores extends Vue {
  data = mockData;
  typeSelected = 0;
  tab: Nullable<number> = null;

  commaSeparatedVal(num: number | string): string {
    /**
     * Formats numbers into Comma-separated numbers (as a string)
     *
     * 123456789 -> '123,456,789'
     * '123456789' -> '123,456,789'
     */
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  }
}
</script>
