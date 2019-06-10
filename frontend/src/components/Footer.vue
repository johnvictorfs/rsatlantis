<template>
  <v-footer dark padless>
    <v-card class="flex" text tile>
      <v-card-title>
        <v-flex text-xs-center>
          <v-btn
            @mouseleave="item.colorUse = 'white'"
            @mouseover="item.colorUse = item.color"
            :key="item.path"
            :href="item.path"
            class="mx-3"
            v-for="item in items"
            icon
            target="_blank"
            style="text-decoration: none;">
            <v-icon :color="item.colorUse">{{ item.icon }}</v-icon>
          </v-btn>
          <v-btn icon>
            <a :href="clanUrl" target="_blank" style="text-decoration: none;" >
              <RunescapeIcon />
            </a>
          </v-btn>
        </v-flex>
      </v-card-title>
      <v-card-actions class="blue darken-1 justify-center">
        &copy;{{ new Date().getFullYear() }} —
        <strong>
          Atlantis
          <v-btn icon>
            <a href="https://github.com/johnvictorfs/" target="_blank" style="text-decoration: none;">
              <v-icon color="white">fab fa-github</v-icon>
            </a>
          </v-btn>
          <v-btn rounded small :to="{name: 'api-docs'}">
            <v-icon small left>fa-code</v-icon>API
          </v-btn>
        </strong>
      </v-card-actions>
    </v-card>
  </v-footer>
</template>

<script>
import RunescapeIcon from '../icons/Runescape'

export default {
  name: 'Footer',
  components: { RunescapeIcon },
  data: () => ({
    clanUrl: 'http://services.runescape.com/m=clan-home/clan/Atlantis',
    items: [
      {
        icon: 'fab fa-discord',
        path: 'https://discordapp.com/invite/d7gquc',
        color: '#7289da',
        colorUse: ''
      },
      {
        icon: 'fab fa-facebook-f',
        path: 'https://www.facebook.com/groups/196808473833963/',
        color: '#4267b2',
        colorUse: ''
      },
      {
        icon: 'fab fa-whatsapp',
        path: 'https://chat.whatsapp.com/DlsVHmXyrS49z823VJTtOT',
        color: '#4fce5d',
        colorUse: ''
      },
      {
        icon: 'fab fa-youtube',
        path: 'https://www.youtube.com/channel/UCecHF0mm4_wxlF-Ef_NWClQ/',
        color: '#ef4c4c',
        colorUse: ''
      }
    ]
  })
}
</script>
