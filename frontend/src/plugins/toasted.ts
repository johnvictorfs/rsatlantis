import Vue from 'vue'

import Toasted from 'vue-toasted'

Vue.use(Toasted)

Vue.toasted.register(
  'error',
  message => message ? message : 'Erro Inesperado :(',
  {
    className: 'vue-toasted vue-toasted-error',
    theme: 'toasted-primary',
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
    className: 'vue-toasted vue-toasted-success',
    theme: 'toasted-primary',
    position: 'top-center',
    type: 'success',
    // @ts-ignore https://github.com/shakee93/vue-toasted/issues/132
    icon: { name: 'check_circle_outline', after: true },
    duration: 2800
  }
)
