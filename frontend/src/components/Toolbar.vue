<template>
  <v-toolbar app dark fixed clipped-left align-center>
    <v-toolbar-side-icon class="hidden-md-and-up"></v-toolbar-side-icon>

    <router-link :to="{ name: 'home' }">
      <img class="logo logo--desktop" src="../assets/atlantis_logo.png" alt="logo"/>
    </router-link>

    <v-btn icon @click="toggleTheme">
      <v-icon>fa-palette</v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    <v-toolbar-items class="hidden-sm-and-down">

      <v-chip label color="indigo" text-color="white" :value="isAuthenticated">
        <v-avatar>
          <v-icon small>{{ userIcon() }}</v-icon>
        </v-avatar>
        {{ username }}
      </v-chip>

      <v-btn flat v-for="item in authItems(isAuthenticated)" :key="item.text" :to="item.path">
        <v-icon left :color="item.color">{{ item.icon }}</v-icon>
        {{ item.text }}
      </v-btn>
    </v-toolbar-items>

  </v-toolbar>
</template>

<script>

  export default {
    name: "Toolbar",
    data: () => ({
      items:
        [
          {text: 'Entrar', path: {name: 'login'}, color: 'green', auth: false, icon: 'fa-sign-in-alt'},
          {text: 'Cadastro', path: {name: 'register'}, color: 'blue', auth: false, icon: 'fa-user-plus'},
          {text: 'Sair', path: {name: 'logout'}, color: 'red', auth: true, icon: 'fa-sign-out-alt'},
        ]
    }),
    methods: {
      authItems(auth) {
        return this.items.filter(function (item) {
          return item.auth === auth;
        });
      },
      toggleTheme() {
        if (this.isDarkTheme) {
          this.$store.dispatch('changeTheme', 'light').then()
        } else {
          this.$store.dispatch('changeTheme', 'dark').then()
        }
      },
      userIcon() {
        if (this.isAdmin) {
          return 'fa-hammer'
        }
        return 'account_circle'
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
        return this.$store.state.isAdmin
      },
      username() {
        return this.$store.state.username
      }
    }
  }
</script>