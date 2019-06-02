<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md8 lg6 xl5>
        <v-card class="elevation-12">
          <v-toolbar dark color="green">
            <v-toolbar-title>
              Entre na sua Conta
            </v-toolbar-title>
          </v-toolbar>

          <v-container fluid grid-list-md>
            <v-form ref="form" v-model="valid" lazy-validation @keyup.native.enter="login">
              <v-text-field v-model="credentials.username" prepend-icon="person" :rules="rules.username" :counter="20" type="text" label="Usuário" name="username" maxlength="20" required />

              <v-text-field v-model="credentials.password" prepend-icon="lock" :rules="rules.password" counter type="password" label="Senha" name="password" maxlength="70" required />

              <v-container>
                <v-layout row>
                  <v-flex xs12>
                    <v-btn class="atl-login-btn mt-4 mb-3" block color="success" :disabled="!valid" @click="login">
                      Entrar
                      <v-icon right>check</v-icon>
                    </v-btn>
                  </v-flex>
                </v-layout>
                <v-layout row justify-end>
                  <v-btn class="atl-btn" color="primary" flat small :to="{name: 'register'}">
                    Não tenho uma Conta
                    <v-icon right small>fa-user-plus</v-icon>
                  </v-btn>
                </v-layout>
              </v-container>
            </v-form>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { formatError } from '../../helpers/errors';

export default {
  name: 'Login',
  data: () => ({
    credentials: {},
    valid: true,
    rules: {
      username: [
        v => !!v || 'Campo de usuário é obrigatório',
        v =>
          (v && v.length > 3) || 'Usuário precisa ter pelo menos 4 caracteres',
        v =>
          /^[a-zA-Z\-0-9]+$/.test(v) ||
          'Usuário pode conter apenas letras e números'
      ],
      password: [
        v => !!v || 'Campo de senha é obrigatório',
        v => (v && v.length > 7) || 'Senha precisa ter pelo menos 8 caracteres'
      ]
    }
  }),
  methods: {
    translateError(error) {
      if (error === 'Error: Network Error') {
        return 'Erro: Falha de Conexão';
      }
      return 'Erro Inesperado, tente novamente mais tarde';
    },
    async login() {
      if (this.$refs.form.validate()) {
        try {
          await this.$store.dispatch('login', this.credentials);
          this.$router.push({ name: 'home' });
          this.$toasted.global.success('Você entrou na sua conta com sucesso!');
          if (this.$route.query.next) {
            this.$router.push(this.$route.query.next);
          }
        } catch (error) {
          this.$toasted.global.error(formatError(error));
        }
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.atl-login-btn {
  height: 45px;
}
</style>
