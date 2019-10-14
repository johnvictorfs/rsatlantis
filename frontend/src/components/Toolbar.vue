<template>
  <v-app-bar app dark fixed class="app-bar">
    <v-app-bar-nav-icon class="hidden-md-and-up" @click="toggleSideBar" />

    <v-toolbar-title>
      <router-link :to="{name: 'home'}">
        <v-img src="@/assets/atlantis_logo.png" class="mt-1" />
      </router-link>
    </v-toolbar-title>

    <v-btn v-for="item in sidebarItems" :key="item.text" class="atl-toolbar-btn hidden-sm-and-down" :color="item.color" text :to="item.path">
      <v-icon left :color="item.color">{{ item.icon }}</v-icon>
      {{ item.text }}
    </v-btn>

    <v-spacer />

    <v-chip class="user-label hidden-sm-and-down" label color="indigo" text-color="white" v-if="isAuthenticated">
      <v-avatar left class="indigo darken-2">
        <v-icon small>{{ userIcon }}</v-icon>
      </v-avatar>
      {{ username }}
    </v-chip>

    <v-btn rounded class="ml-3 shadow-hover atl-round-btn hidden-sm-and-down" v-for="item in toolbarItems" :key="item.text" :color="item.color" :to="item.path">
      <v-icon left>{{ item.icon }}</v-icon>
      {{ item.text }}
    </v-btn>
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

@Component({
  props: {
    sidebarItems: {
      type: Array,
      default: () => []
    },
    toolbarItems: {
      type: Array,
      default: () => []
    }
  }
})
export default class Toolbar extends Vue {
  sidebar: boolean = true

  get isAuthenticated() {
    return this.$store.getters.isAuthenticated
  }
  get isAdmin() {
    const { auth } = this.$store.state
    if (auth) return auth.isAdmin
  }
  get username() {
    const { auth } = this.$store.state
    if (auth) return auth.username
  }
  get userIcon() {
    return this.isAdmin ? 'fa-user-cog' : 'fa-user'
  }

  toggleSideBar() {
    this.sidebar = !this.sidebar
  }
}
</script>

<style lang="scss" scoped>
.user-label {
  padding-left: 10px;
  font-size: 18px;
  height: 40px;
  align-self: center;
  font-family: "Roboto Condensed", "Courier New", Courier, monospace;
}

.app-bar {
  z-index: 999 !important;
}

.shadow-hover:hover {
  box-shadow: 0 7px 10px rgba(0,0,0,0.25), 0 7px 7px rgba(0,0,0,0.22);
}
</style>
