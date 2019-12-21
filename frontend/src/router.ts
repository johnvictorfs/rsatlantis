import Vue from 'vue'
import Router from 'vue-router'

import store from '@/store'

Vue.use(Router)

const redirectLogout = (to: any, from: any, next: any) => {
  store.dispatch('logout').then(() => next({ name: 'home' }))
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
      component: () => import(/* webpackChunkName: "guides-guidedetail" */ './views/guides/GuideView.vue')
    },
    {
      path: '/clan/list',
      name: 'clan-list',
      component: () => import(/* webpackChunkName: "clanlist" */ './views/ClanList.vue')
    },
    {
      path: '/amigo_secreto/inscritos',
      name: 'amigo-secreto-users',
      component: () => import(/* webpackChunkName: "amigo-secreto-users" */ './components/AmigoSecretoUsers.vue')
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
  const requiresAdmin = to.matched.some(route => route.meta.admin)
  const requiresSuperUser = to.matched.some(route => route.meta.superUser)

  // Redirects user to login page if the page they are trying to access requires authentication, and they
  // are not logged in
  if (!store.getters.isAuthenticated && requiresAuth) {
    Vue.toasted.global.error('Você precisa estar conectado para fazer isso')
    next('/entrar/' + `?next=${to.path}`)
  } else if ((!store.getters.isAdmin && requiresAdmin) || (!store.getters.isSuperUser && requiresSuperUser)) {
    // Redirects User to hompage if page requires Admin or Superuser and he isn't
    Vue.toasted.global.error('Você não tem permissões para fazer isso')
    next('/')
  } else {
    next()
  }
})

export default router
