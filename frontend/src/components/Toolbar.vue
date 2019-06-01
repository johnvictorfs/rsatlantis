<template>
  <v-layout>

    <v-toolbar app dark fixed clipped-left align-center>
      <v-toolbar-side-icon class="hidden-md-and-up" @click="toggleSideBar"></v-toolbar-side-icon>

      <router-link :to="{name: 'home'}">
        <img class="logo logo--desktop" src="../assets/atlantis_logo.png" alt="logo"/>
      </router-link>

      <v-btn class="atl-btn" :color="item.color" flat v-for="item in sidebarItems" :key="item.text" :to="item.path">
        <v-icon left :color="item.color">{{ item.icon }}</v-icon>
        {{ item.text }}
      </v-btn>

      <v-spacer></v-spacer>

      <v-toolbar-items class="hidden-sm-and-down">
        <v-chip class="user-label" label color="indigo" text-color="white" :value="isAuthenticated">
          <v-avatar class="indigo darken-2">
            <v-icon small>{{ userIcon }}</v-icon>
          </v-avatar>
          {{ username }}
        </v-chip>
        <v-btn :color="item.color" class="atl-round-btn" round outline v-for="item in toolbarItems" :key="item.text"
               :to="item.path">
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
      toggleSideBar() {
        this.sidebar = !this.sidebar;
      }
    },
    computed: {
      isAuthenticated() {
        return this.$store.getters.isAuthenticated
      },
      isAdmin() {
        return this.$store.state.auth.isAdmin
      },
      username() {
        return this.$store.state.auth.username
      },
      userIcon() {
        if (this.isAdmin) {
          return 'fa-user-cog'
        }
        return 'fa-user'
      }
    }
  }
</script>

<style scoped>
  .user-label {
    padding-left: 10px;
    font-size: 18px;
    height: 40px;
    align-self: center;
    font-family: "Roboto Condensed", "Courier New", Courier, monospace;
  }
</style>
