<template>
  <v-footer dark height="auto">

    <v-layout justify-center wrap>

      <v-btn v-for="item in items" :key="item.path" class="mx-3" icon>
        <a v-if="item.external" :href="item.path" target="_blank" style="text-decoration: none;">
          <v-icon color="white" dark size="24px">{{ item.icon }}</v-icon>
        </a>
        <router-link v-if="!item.external" :to="item.path">
          <v-icon color="white" dark size="24px">{{ item.icon }}</v-icon>
        </router-link>
      </v-btn>
      <v-btn icon>
        <a href="http://services.runescape.com/m=clan-home/clan/Atlantis" target="_blank"
           style="text-decoration: none;">
          <RunescapeIcon></RunescapeIcon>
        </a>
      </v-btn>


      <v-flex primary py-1 text-xs-center white--text xs12>
        &copy;{{ new Date().getFullYear() }} —
        <strong>
          John Victor
          <v-btn icon>
            <a href="https://github.com/johnvictorfs/" target="_blank" style="text-decoration: none;">
              <v-icon color="white">fab fa-github</v-icon>
            </a>
          </v-btn>
        </strong>
      </v-flex>

    </v-layout>
  </v-footer>
</template>


<!--<template>-->
<!--<v-footer dark>-->
<!--<v-flex>-->
<!--<v-card class="white&#45;&#45;text">-->
<!--<v-card-title class="teal justify-center">-->
<!--<v-btn v-for="item in items" :key="item.path" class="mx-3" icon>-->
<!--<a v-if="item.external" :href="item.path" target="_blank" style="text-decoration: none;">-->
<!--<v-icon color="white" dark size="24px">{{ item.icon }}</v-icon>-->
<!--</a>-->
<!--<router-link v-if="!item.external" :to="item.path">-->
<!--<v-icon size="24px">{{ item.icon }}</v-icon>-->
<!--</router-link>-->
<!--</v-btn>-->
<!--<v-btn icon>-->
<!--<a href="http://services.runescape.com/m=clan-home/clan/Atlantis" target="_blank" style="text-decoration: none;">-->
<!--<RunescapeIcon></RunescapeIcon>-->
<!--</a>-->
<!--</v-btn>-->
<!--</v-card-title>-->
<!--<v-divider></v-divider>-->
<!--<v-card-actions class="grey darken-3 justify-center">-->
<!--&copy;{{ new Date().getFullYear() }} —-->
<!--<strong>-->
<!--&lt;!&ndash;&ndash;&gt;-->
<!--John Victor-->
<!--<a target="_blank" href="https://github.com/johnvictorfs/" style="text-decoration: none;">-->
<!--<v-icon small>fab fa-github</v-icon>-->
<!--</a>-->
<!--</strong>-->
<!--</v-card-actions>-->
<!--</v-card>-->
<!--</v-flex>-->
<!--</v-footer>-->
<!--</template>-->

<script>
  import RunescapeIcon from '../icons/Runescape'

  export default {
    name: "Footer",
    components: {RunescapeIcon},
    data: () => ({
      items: [
        {icon: 'fab fa-discord', path: 'https://discordapp.com/invite/d7gquc', external: true},
        {icon: 'fab fa-facebook-f', path: 'https://www.facebook.com/groups/196808473833963/', external: true},
        {icon: 'fab fa-whatsapp', path: 'https://chat.whatsapp.com/DlsVHmXyrS49z823VJTtOT', external: true},
        {icon: 'fab fa-youtube', path: 'https://www.youtube.com/channel/UCecHF0mm4_wxlF-Ef_NWClQ/', external: true}
      ]
    })
  }
</script>