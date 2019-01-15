<template>
  <Centered>
    <v-card class="elevation-12">

      <v-toolbar dark color="green">
        <v-toolbar-title>Entre na sua Conta</v-toolbar-title>
      </v-toolbar>

      <v-container fluid grid-list-md>

        <v-form ref="form" v-model="valid" lazy-validation @keyup.native.enter="login">

          <v-text-field v-model="credentials.username" prepend-icon="person" :rules="rules.username" :counter="20"
                        type="text"
                        label="Usuário"
                        name="username"
                        maxlength="20"
                        required
          ></v-text-field>

          <v-text-field v-model="credentials.password" prepend-icon="lock" :rules="rules.password" counter
                        type="password"
                        label="Senha"
                        name="password"
                        maxlength="70"
                        required
          ></v-text-field>

          <div class="text-xs-center mt-3">
            <v-btn :disabled="!valid" @click="login" color="success">Entrar</v-btn>
          </div>

          <v-divider></v-divider>

          <div class="text-xs-center mt-3">
            <v-btn color="error" small :to="{name: 'register'}">Não tenho uma Conta</v-btn>
          </div>

        </v-form>
      </v-container>
    </v-card>
  </Centered>
</template>

<script>
  import Centered from '../../components/Centered'

  export default {
    name: 'Login',
    components: {
      Centered
    },
    data: () => ({
      credentials: {},
      valid: true,
      rules: {
        username: [
          v => !!v || "Campo de usuário é obrigatório",
          v => (v && v.length > 3) || "Usuário precisa ter pelo menos 4 caracteres",
          v => /^[a-zA-Z\-0-9]+$/.test(v) || "Usuário pode conter apenas letras e números"
        ],
        password: [
          v => !!v || "Campo de senha é obrigatório",
          v => (v && v.length > 7) || "Senha precisa ter pelo menos 8 caracteres",
        ]
      },
    }),
    methods: {
      translateError(error) {
        if (error === 'Error: Network Error') {
          return 'Erro: Falha de Conexão'
        }
        return error;
      },
      login() {
        this.$store.dispatch('login', this.credentials).then(() => {
          this.$router.push({name: 'home'});
          this.$toasted.global.success('Você entrou na sua conta com sucesso!');
        }).catch(error => {
          // Gets the first error message from the returned data
          let errorMessage = 'Erro inesperado :(';
          if (error.response !== undefined) {
            errorMessage = Object.values(error.response.data)[0];
          } else {
            errorMessage = error.toString();
          }
          this.$toasted.global.error(this.translateError(errorMessage));
        });
      }
    }
  }
</script>