<template>
  <v-app-bar app dark fixed class="app-bar" hide-on-scroll>
    <v-app-bar-nav-icon class="hidden-md-and-up" @click="toggleSideBar" />

    <v-toolbar-title>
      <router-link :to="{name: 'home'}">
        <v-img src="@/assets/images/atlantis_logo.png" class="mt-1" />
      </router-link>
    </v-toolbar-title>

    <v-btn outlined v-for="item in sidebarItems" :key="item.text" class="hidden-sm-and-down ml-2" :color="item.color" :to="item.path">
      <v-icon left :color="item.color">
        {{ item.icon }}
      </v-icon>
      {{ item.text }}
    </v-btn>

    <v-spacer />

    <v-chip class="user-label hidden-sm-and-down" label color="indigo" text-color="white" v-if="isAuthenticated">
      <v-avatar left class="indigo darken-2">
        <v-icon small>
          {{ userIcon }}
        </v-icon>
      </v-avatar>
      {{ username }}
    </v-chip>

    <v-btn rounded class="ml-3 shadow-hover hidden-sm-and-down" v-for="item in toolbarItems" :key="item.text" :color="item.color" :to="item.path">
      <v-icon :left="!!item.text" class="ml-1" v-if="item.icon">
        {{ item.icon }}
      </v-icon>
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
    return this.$store.getters.isAdmin
  }

  get username() {
    const { auth } = this.$store.state
    if (auth) return auth.user.username
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
.atl-toolbar-btn {
  border-radius: 10px !important;
}

.user-label {
  border-radius: 12px !important;
  padding-left: 16px;
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
