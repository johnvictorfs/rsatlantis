import Vue from 'vue';
import Router from 'vue-router';
import store from './store';

Vue.use(Router);

const redirectLogout = (to, from, next) => {
  store.dispatch('logout').then(() => next({ name: 'home' }));
  Vue.toasted.global.success('Você saiu da sua conta com sucesso');
};

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import(/* webpackChunkName: "homepage" */ './views/Homepage')
    },
    {
      path: '/entrar',
      name: 'login',
      component: () => import(/* webpackChunkName: "auth-login" */ './views/auth/Login')
    },
    {
      path: '/sair',
      name: 'logout',
      beforeEnter: redirectLogout
    },
    {
      path: '/registrar',
      name: 'register',
      component: () => import(/* webpackChunkName: "auth-register" */ './views/auth/Register')
    },
    {
      path: '/guias',
      name: 'guides.list',
      component: () => import(/* webpackChunkName: "guides-guidelist" */ './views/guides/GuideList')
    },
    {
      path: '/guias/novo',
      name: 'guides.new',
      meta: { auth: true },
      component: () => import(/* webpackChunkName: "guides-newguide" */ './views/guides/NewGuide')
    },
    {
      path: '/guias/atl/:slug',
      name: 'guides.detail',
      props: true,
      component: () => import(/* webpackChunkName: "guides-guidedetail" */ './views/guides/GuideDetail')
    },
    {
      path: '/docs/api',
      name: 'api-docs',
      component: () => import(/* webpackChunkName: "api" */ './views/Api')
    },
    {
      path: '/clan/list',
      name: 'clan-list',
      component: () => import(/* webpackChunkName: "clanlist" */ './views/ClanList')
    },
    {
      path: '/404',
      alias: '*',
      name: 'notfound',
      component: () => import(/* webpackChunkName: "notfound" */ './views/NotFound')
    },
    {
      path: '*',
      redirect: { name: 'notfound' }
    }
  ]
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(route => route.meta.auth);

  // Redirects user to login page if the page they are trying to access requires authentication, and they
  // are not logged in
  if (!store.getters.isAuthenticated && requiresAuth) {
    Vue.toasted.global.error('Você precisa estar conectado para fazer isso');
    next('/entrar/' + `?next=${to.path}`);
  } else {
    next();
  }
});

export default router;
