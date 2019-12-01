import Vue from 'vue'

import Toasted from 'vue-toasted'

Vue.use(Toasted)

Vue.toasted.register(
  'error',
  message => message ? message : 'Erro Inesperado :(',
  {
    theme: 'bubble',
    position: 'top-center',
    type: 'error',
    // @ts-ignore https://github.com/shakee93/vue-toasted/issues/132
    icon: { name: 'error_outline', after: true },
    duration: 2800
  }
)

Vue.toasted.register(
  'success',
  message => message ? message : 'Sucesso :)',
  {
    theme: 'bubble',
    position: 'top-center',
    type: 'success',
    // @ts-ignore https://github.com/shakee93/vue-toasted/issues/132
    icon: { name: 'check_circle_outline', after: true },
    duration: 2800
  }
)
