import Vue from 'vue'
import Router from 'vue-router'
import store from './store/index'

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
      path: '/guias',
      name: 'guides.list',
      component: () => import('./views/guides/GuideList'),
    },
    {
      path: '/guias/novo',
      name: 'guides.new',
      meta: {auth: true},
      component: () => import('./views/guides/NewGuide')
    },
    {
      path: '/guias/atl/:slug',
      name: 'guides.detail',
      props: true,
      component: () => import('./views/guides/GuideDetail')
    },
    {
      path: '/docs/api',
      name: 'api-docs',
      component: () => import('./views/Api')
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