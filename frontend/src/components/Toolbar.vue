<template>
  <v-layout>
    <v-navigation-drawer v-model="sidebar" fixed clipped app>
      <v-list class="pt-0" dense>

        <v-list-tile dense v-for="item in sidebarItems" :key="item.text" :to="item.path">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.text }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <v-toolbar app dark fixed clipped-left align-center>
      <v-toolbar-side-icon class="hidden-md-and-up" @click="toggleSideBar"></v-toolbar-side-icon>

      <router-link :to="{name: 'home'}">
        <img class="logo logo--desktop" src="../assets/atlantis_logo.png" alt="logo"/>
      </router-link>

      <v-btn icon @click="toggleTheme">
        <v-icon>fa-palette</v-icon>
      </v-btn>

      <v-spacer></v-spacer>

      <v-toolbar-items class="hidden-sm-and-down">
        <v-chip label color="indigo" text-color="white" :value="isAuthenticated">
          <v-avatar class="indigo darken-2">
            <v-icon small>{{ userIcon }}</v-icon>
          </v-avatar>
          {{ username }}
        </v-chip>
        <v-btn flat v-for="item in toolbarItems" :key="item.text" :to="item.path">
          <v-icon left :color="item.color">{{ item.icon }}</v-icon>
          {{ item.text }}
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </v-layout>

</template>

<script>

  export default {
    name: "Toolbar",
    props: {
      'sidebarItems': Array,
      'toolbarItems': Array
    },
    data: () => ({
      sidebar: true
    }),
    methods: {
      toggleTheme() {
        if (this.isDarkTheme) {
          this.$store.dispatch('changeTheme', 'light').then()
        } else {
          this.$store.dispatch('changeTheme', 'dark').then()
        }
      },
      toggleSideBar() {
        this.sidebar = !this.sidebar;
      }
    },
    computed: {
      isAuthenticated() {
        return this.$store.getters.isAuthenticated
      },
      isDarkTheme() {
        return this.$store.getters.isDarkTheme
      },
      isAdmin() {
        return this.$store.state.auth.isAdmin
      },
      username() {
        return this.$store.state.auth.username
      },
      userIcon() {
        if (this.isAdmin) {
          return 'fa-hammer'
        }
        return 'account_circle'
      }
    }
  }
</script>