import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import pt from 'vuetify/src/locale/pt'

import RunescapeIcon from '@/icons/Runescape.vue'

Vue.use(Vuetify)

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
    values: {
      runescape: {
        component: RunescapeIcon
      }
    }
  },
  theme: {
    dark: true
  },
  lang: {
    locales: { pt },
    current: 'pt'
  }
})
