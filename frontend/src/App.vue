<template>
  <v-app>
    <Toolbar :toolbar-items="filteredToolbarItems" :sidebar-items="filteredSidebarItems" />

    <v-content>
      <v-container fluid class="mb-3">
        <Loading />

        <transition name="fade" mode="out-in">
          <router-view />
        </transition>
      </v-container>
    </v-content>

    <Footer />
  </v-app>
</template>

<script lang="ts">
import Component from 'vue-class-component'
import Vue from 'vue'

import { ToolbarItem } from '@/types'

const Toolbar = () => import('@/components/Toolbar.vue')
const Footer = () => import('@/components/Footer.vue')
const Loading = () => import('@/components/Loading.vue')

@Component({ components: { Footer, Toolbar, Loading } })
export default class App extends Vue {
  prevHeight: number = 0
  toolbarItems: Array<ToolbarItem> = [
    { text: 'Entrar', path: { name: 'login' }, color: 'success', auth: false, icon: 'fa-sign-in-alt' },
    { text: 'Cadastro', path: { name: 'register' }, color: 'primary', auth: false, icon: 'fa-user-plus' },
    { text: '', path: { name: 'logout' }, color: 'error', auth: true, icon: 'fa-sign-out-alt' }
  ]
  sidebarItems: Array<ToolbarItem> = [
    { text: 'Novo Guia', path: { name: 'guides.new' }, color: 'success', auth: true, icon: 'fa-plus-square' },
    { text: 'Guias', path: { name: 'guides.list' }, color: '#7ba658', auth: 'any', icon: 'fa-list' },
    { text: 'Membros', path: { name: 'clan-list' }, color: 'primary', auth: 'any', icon: 'fa-users' }
  ]

  async created() {
    await this.$store.dispatch('accountDetails')
  }

  get filteredToolbarItems() {
    /**
     * Filters items based on if they are shown to authenticated users or not
     */
    const items = []

    for (let i = 0; i < this.toolbarItems.length; i++) {
      const auth = this.toolbarItems[i].auth

      if (auth === this.$store.getters.isAuthenticated || auth === 'any') {
        items.push(this.toolbarItems[i])
      }
    }

    return items
  }

  get filteredSidebarItems() {
    /**
     * Filters items based on if they are shown to authenticated users or not, according to if the user is
     * authenticated or not.
     */
    const items = []
    for (let i = 0; i < this.sidebarItems.length; i++) {
      if (this.sidebarItems[i].auth === this.$store.getters.isAuthenticated) {
        items.push(this.sidebarItems[i])
      } else if (this.sidebarItems[i].auth === 'any') {
        items.push(this.sidebarItems[i])
      }
    }
    return items
  }
}
</script>

<style lang="scss">
body {
  font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial,
    sans-serif;
}

.atl-round-btn {
  border-width: 2px;
}

.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}

.atl-round-toolbar {
  border-radius: 18px !important;
}

/**
 * Remove arrows from input with type 'number'
 *
 * https://stackoverflow.com/questions/3790935/can-i-hide-the-html5-number-input-s-spin-box
 */
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
input[type="number"] {
  -moz-appearance: textfield;
}
</style>
