import Vue from 'vue';

import Toasted from 'vue-toasted';

Vue.use(Toasted);

Vue.toasted.register(
  'error',
  message => {
    // if there is no message passed show default message
    if (!message) {
      return 'Erro Inesperado :(';
    }
    // if there is a message show it with the message
    return message;
  },
  {
    theme: 'bubble',
    position: 'top-center',
    type: 'error',
    icon: 'error_outline',
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
    icon: 'check_circle_outline',
    duration: 2800
  }
);
