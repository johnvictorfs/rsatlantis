import Vue from 'vue'
import Router from 'vue-router'
import store from './store'

Vue.use(Router)

const redirectLogout = (to: any, from: any, next: any) => {
  store.dispatch('logout').then(() => next({ name: 'home' }))
  Vue.toasted.global.success('Você saiu da sua conta com sucesso')
}

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import(/* webpackChunkName: "homepage" */ './views/Homepage.vue')
    },
    {
      path: '/entrar',
      name: 'login',
      component: () => import(/* webpackChunkName: "auth-login" */ './views/auth/Login.vue')
    },
    {
      path: '/sair',
      name: 'logout',
      beforeEnter: redirectLogout
    },
    {
      path: '/registrar',
      name: 'register',
      component: () => import(/* webpackChunkName: "auth-register" */ './views/auth/Register.vue')
    },
    {
      path: '/guias',
      name: 'guides.list',
      component: () => import(/* webpackChunkName: "guides-guidelist" */ './views/guides/GuideList.vue')
    },
    {
      path: '/guias/novo',
      name: 'guides.new',
      meta: { auth: true },
      component: () => import(/* webpackChunkName: "guides-newguide" */ './views/guides/NewGuide.vue')
    },
    {
      path: '/guias/atl/:slug',
      name: 'guides.detail',
      props: true,
      component: () => import(/* webpackChunkName: "guides-guidedetail" */ './views/guides/GuideDetail.vue')
    },
    {
      path: '/docs/api',
      name: 'api-docs',
      component: () => import(/* webpackChunkName: "api" */ './views/Api.vue')
    },
    {
      path: '/clan/list',
      name: 'clan-list',
      component: () => import(/* webpackChunkName: "clanlist" */ './views/ClanList.vue')
    },
    {
      path: '/404',
      alias: '*',
      name: 'notfound',
      component: () => import(/* webpackChunkName: "notfound" */ './views/NotFound.vue')
    },
    {
      path: '*',
      redirect: { name: 'notfound' }
    }
  ]
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(route => route.meta.auth)

  // Redirects user to login page if the page they are trying to access requires authentication, and they
  // are not logged in
  if (!store.getters.isAuthenticated && requiresAuth) {
    Vue.toasted.global.error('Você precisa estar conectado para fazer isso')
    next('/entrar/' + `?next=${to.path}`)
  } else {
    next()
  }
})

export default router
