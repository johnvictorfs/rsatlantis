import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import pt from 'vuetify/src/locale/pt'

Vue.use(Vuetify)

export default new Vuetify({
  icons: {
    iconfont: 'mdi'
  },
  theme: {
    dark: true
  },
  lang: {
    locales: { pt },
    current: 'pt'
  }
})
