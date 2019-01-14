import Vue from 'vue';

import Toasted from 'vue-toasted';

Vue.use(Toasted);

// register the toast with the custom message
Vue.toasted.register('error',
  (message) => {
    // if there is no message passed show default message
    if (!message) {
      return "Erro Inesperado :("
    }
    // if there is a message show it with the message
    return message;
  },
  {
    position: 'top-center',
    type: 'error',
    icon: 'error_outline',
    duration: 2200
  }
);

Vue.toasted.register('success',
  (message) => {
    if (!message) {
      return "Sucesso :)"
    }
    return message;
  },
  {
    position: 'top-center',
    type: 'success',
    icon: 'check_circle_outline',
    duration: 2200
  }
);