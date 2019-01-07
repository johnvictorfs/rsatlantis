import Vue from 'vue'

import './plugins/vuetify'

import 'vuetify/dist/vuetify.min.css'

import router from './router'

import App from './App.vue'

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router: router
}).$mount('#app');
