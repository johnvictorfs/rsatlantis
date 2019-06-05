import Vue from 'vue';

import Toasted, { ToastOptions } from 'vue-toasted';

Vue.use(Toasted);

Vue.toasted.register(
  'error',
  message => {
    if (!message) {
      return 'Erro Inesperado :(';
    }
    return message;
  },
  {
    theme: 'bubble',
    position: 'top-center',
    type: 'error',
    icon: { name: 'error_outline', after: true },
    duration: 2800
  }
);

Vue.toasted.register(
  'success',
  message => {
    if (!message) {
      return 'Sucesso :)';
    }
    return message;
  },
  {
    theme: 'bubble',
    position: 'top-center',
    type: 'success',
    icon: { name: 'check_circle_outline', after: true },
    duration: 2800
  }
);
