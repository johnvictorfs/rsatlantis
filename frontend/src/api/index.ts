import axios from 'axios';

// Full config:  https://github.com/axios/axios#request-config

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || '',
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken'
});

api.interceptors.request.use(response => response, error => Promise.reject(error));
api.interceptors.response.use(response => response, error => Promise.reject(error));

if (localStorage.getItem('TOKEN')) {
  api.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('TOKEN')}`;
}

export default api;
