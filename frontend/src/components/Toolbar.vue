<template>
  <v-layout>
    <v-toolbar app dark fixed clipped-left align-center>
      <v-toolbar-side-icon class="hidden-md-and-up" @click="toggleSideBar" />

      <router-link :to="{name: 'home'}">
        <img class="logo logo--desktop" src="../assets/atlantis_logo.png" alt="logo">
      </router-link>

      <v-btn v-for="item in sidebarItems" :key="item.text" class="atl-toolbar-btn" :color="item.color" flat :to="item.path">
        <v-icon left :color="item.color">{{ item.icon }}</v-icon>
        {{ item.text }}
      </v-btn>

      <v-spacer />

      <v-toolbar-items class="hidden-sm-and-down">
        <v-chip class="atl-user-label" label color="indigo" text-color="white" :value="isAuthenticated">
          <v-avatar class="indigo darken-2">
            <v-icon small>{{ userIcon }}</v-icon>
          </v-avatar>
          {{ username }}
        </v-chip>
        <v-btn v-for="item in toolbarItems" :key="item.text" class="atl-toolbar-btn" :color="item.color" round outline :to="item.path">
          <v-icon left :color="item.color">{{ item.icon }}</v-icon>
          {{ item.text }}
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'Toolbar',
  props: {
    sidebarItems: {
      type: Array,
      default: []
    },
    toolbarItems: {
      type: Array,
      default: []
    }
  },
  data: () => ({
    sidebar: true
  }),
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    isAdmin() {
      return this.$store.state.auth.isAdmin;
    },
    username() {
      return this.$store.state.auth.username;
    },
    userIcon() {
      return this.isAdmin ? 'fa-user-cog' : 'fa-user';
    }
  },
  methods: {
    toggleSideBar() {
      this.sidebar = !this.sidebar;
    }
  }
})
</script>

<style lang="scss" scoped>
.atl-user-label {
  padding-left: 10px;
  font-size: 18px;
  height: 40px;
  align-self: center;
  font-family: "Roboto Condensed", "Courier New", Courier, monospace;
}

.atl-toolbar-btn {
  height: 38px !important;
}
</style>
