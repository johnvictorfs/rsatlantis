import Vue from 'vue'
import Router from 'vue-router'
import store from './store'

Vue.use(Router);

const redirectLogout = (to, from, next) => {
  store.dispatch('logout').then(() => next({name: 'home'}));
  Vue.toasted.global.success('Você saiu da sua conta com sucesso');
};

const router = new Router({
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
      path: '/guia/novo/',
      name: 'guide-new',
      meta: {auth: true},
      component: () => import('./views/guides/NewGuide')
    },
    {
      path: '/guia/detalhes/:slug/',
      name: 'guide-detail',
      props: true,
      component: () => import('./views/guides/GuideDetail')
    },
    {
      path: '/guia/lista/',
      name: 'guide-list',
      component: () => import('./views/guides/GuideList')
    },
    {
      path: '/404',
      alias: '*',
      name: 'notfound',
      component: () => import('./views/NotFound')
    },
    {
      path: '*',
      redirect: {name: 'notfound'}
    }
  ]
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((route) => route.meta.auth);

  // Redirects user to login page if the page they are trying to access requires authentication, and they
  // are not logged in
  if (!store.getters.isAuthenticated && requiresAuth) {
    Vue.toasted.global.error('Você precisa estar conectado para fazer isso');
    next('/entrar/' + `?next=${to.path}`)
  } else {
    next()
  }
});

export default router;