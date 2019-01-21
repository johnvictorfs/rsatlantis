import Vue from 'vue'
import tinymce from 'vue-tinymce-editor'

import './plugins/vuetify'
import './plugins/axios'
import './plugins/toasted'

import 'vuetify/dist/vuetify.min.css'

import router from './router'

import App from './App.vue'
import store from './store'

Vue.config.productionTip = false;

Vue.component('tinymce', tinymce);

new Vue({
  render: h => h(App),
  store,
  router,
}).$mount('#app');
