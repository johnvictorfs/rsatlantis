"use strict";

import Vue from 'vue';
import axios from "axios";

// Full config:  https://github.com/axios/axios#request-config

let config = {
  baseURL: process.env.baseURL || process.env.apiUrl || process.env.VUE_APP_API_URL || "",
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken'
  // timeout: 60 * 1000, // Timeout
  // withCredentials: true, // Check cross-site Access-Control
};

const _axios = axios.create(config);

_axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
_axios.interceptors.response.use(
  function(response) {
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    return Promise.reject(error);
  }
);

Plugin.install = function(Vue) {
  Vue.axios = _axios;
  window.axios = _axios;
  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return _axios;
      }
    },
    $axios: {
      get() {
        return _axios;
      }
    },
  });
};

Vue.use(Plugin);

if (localStorage.getItem('TOKEN')) {
  Vue.axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('TOKEN')}`;
}

export default Plugin;