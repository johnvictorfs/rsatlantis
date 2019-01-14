import Vue from 'vue'
import Router from 'vue-router'
import store from './store'

Vue.use(Router);

const redirectLogout = (to, from, next) => {
  store.dispatch('logout').then(() => next({name: 'home'}));
  Vue.toasted.global.success('Você saiu da sua conta com sucesso');
};

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/Homepage')
    },
    {
      path: '/entrar',
      name: 'login',
      component: () => import('./views/auth/Login')
    },
    {
      path: '/sair',
      name: 'logout',
      beforeEnter: redirectLogout,
    },
    {
      path: '/registrar',
      name: 'register',
      component: () => import('./views/auth/Register')
    },
    {
      path: '/404',
      alias: '*',
      name: 'notfound',
      component: () => import ('./views/NotFound')
    },
    {
      path: '*',
      redirect: {name: 'notfound'}
    }
  ]
})