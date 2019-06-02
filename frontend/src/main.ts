import Vue from 'vue';
import tinymce from 'vue-tinymce-editor';
import VueClipboard from 'vue-clipboard2';

import './plugins/axios';
import './plugins/vuetify';
import './plugins/toasted';

import 'vuetify/dist/vuetify.min.css';
import '@fortawesome/fontawesome-free/css/all.css';

import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;
Vue.use(VueClipboard);
Vue.component('tinymce', tinymce);

new Vue({ router, store, render: h => h(App) }).$mount('#app');
