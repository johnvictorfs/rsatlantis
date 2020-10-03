<template>
  <v-card class="atl-round-card" raised>
    <v-toolbar dark color="#363636">
      <v-toolbar-title>
        <v-icon left size="32" color="#9E826B">
          fas fa-scroll
        </v-icon>
        Pergaminhos de Dicas
      </v-toolbar-title>

      <v-btn icon class="ml-2 mb-2">
        <v-icon height="18" width="18">
          fa-sync-alt
        </v-icon>
      </v-btn>

      <template v-slot:extension>
        <v-tabs v-model="tab" align-with-title>
          <v-tabs-slider color="success" />

          <v-tab v-for="clueType in data" :key="clueType.type">
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
                    <v-img max-width="80%" max-height="80%" :src="`https://secure.runescape.com/m=avatar-rs/${player.name.replace(/\s/g, '_')}/chat.png`" />
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
const mockData = [
  {
    type: 'Mestres',
    name: 'master',
    image: 'https://runescape.wiki/images/6/68/Sealed_clue_scroll_%28master%29.png?f1baf',
    color: '#a32512',
    players: [
      {
        clan_rank: 1,
        global_rank: 178,
        name: 'morguibruh',
        count: 667
      },
      {
        clan_rank: 2,
        global_rank: 214,
        name: 'MVitor',
        count: 620
      },
      {
        clan_rank: 3,
        global_rank: 656,
        name: 'mainkaisa',
        count: 327
      },
      {
        clan_rank: 4,
        global_rank: 1288,
        name: 'Weiss',
        count: 224
      },
      {
        clan_rank: 5,
        global_rank: 1730,
        name: 'Krazyboy',
        count: 188
      }
    ]
  },
  {
    type: 'Elites',
    name: 'elite',
    image: 'https://runescape.wiki/images/a/a9/Sealed_clue_scroll_%28elite%29.png?82229',
    color: '#db5e4b',
    players: [
      {
        clan_rank: 1,
        global_rank: 222,
        name: 'MVitor',
        count: 2108
      },
      {
        clan_rank: 2,
        global_rank: 885,
        name: 'Weiss',
        count: 1124
      },
      {
        clan_rank: 3,
        global_rank: 2399,
        name: 'Rupo RS',
        count: 674
      },
      {
        clan_rank: 4,
        global_rank: 3469,
        name: 'Betinhu',
        count: 541
      },
      {
        clan_rank: 5,
        global_rank: 4419,
        name: 'xJxPxGx',
        count: 466
      }
    ]
  },
  {
    type: 'Díficeis',
    name: 'hard',
    image: 'https://runescape.wiki/images/7/7a/Sealed_clue_scroll_%28hard%29.png?64dd1',
    color: '#d19630',
    players: []
  },
  {
    type: 'Médios',
    name: 'medium',
    image: 'https://runescape.wiki/images/5/5d/Sealed_clue_scroll_%28medium%29.png?577ea',
    color: '#c7bf20',
    players: []
  },
  {
    type: 'Facéis',
    name: 'easy',
    image: 'https://runescape.wiki/images/1/1c/Sealed_clue_scroll_%28easy%29.png?c6759',
    color: '#2ac938',
    players: []
  }
]

const lastUpdated = new Date()

import Vue from 'vue'
import Component from 'vue-class-component'

import { Nullable } from '@/types'

@Component({})
export default class ClueHiscores extends Vue {
  data = mockData;
  typeSelected = 0;
  tab: Nullable<number> = null;

  mounted() {
    console.log(this.data)
  }

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
