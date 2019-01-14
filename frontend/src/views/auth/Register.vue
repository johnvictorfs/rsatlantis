<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs12 sm8 lg5 md5>
        <v-card class="elevation-12">

          <v-toolbar dark color="blue">
            <v-toolbar-title>Crie sua conta</v-toolbar-title>
          </v-toolbar>

          <v-layout row fill-height justify-center align-center v-if="loading">
            <v-progress-circular :size="50" color="primary" indeterminate/>
          </v-layout>

          <v-container fluid grid-list-md>

            <v-form ref="form" v-model="valid" lazy-validation @keyup.native.enter="register">

              <v-text-field v-model="credentials.username" prepend-icon="person" :rules="rules.username" :counter="20"
                            type="text"
                            label="Usuário"
                            name="username"
                            maxlength="20"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.password" prepend-icon="email" counter
                            type="email"
                            label="Email"
                            name="email"
                            maxlength="70"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.password" prepend-icon="lock" :rules="rules.password" counter
                            type="password"
                            label="Senha"
                            name="password"
                            maxlength="70"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.password2" prepend-icon="lock" :rules="rules.password2" counter
                            :error-messages='passwordMissmatch()'
                            type="password"
                            label="Confirmar Senha"
                            name="password2"
                            maxlength="70"
                            required
              ></v-text-field>

              <div class="text-xs-center mt-3">
                <v-btn :disabled="!valid" @click="register" color="green">Registrar</v-btn>
              </div>

              <v-divider></v-divider>

              <div class="text-xs-center mt-3">
                <v-btn color="orange" small :to="{name: 'login'}">Já tenho uma conta</v-btn>
              </div>
            </v-form>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

  export default {
    name: 'Register',
    data: () => ({
      credentials: {},
      valid: true,
      loading: false,
      rules: {
        username: [
          v => !!v || "Campo de usuário é obrigatório",
          v => (v && v.length > 3) || "Usuário precisa ter pelo menos 4 caracteres",
          v => /^[a-zA-Z\-0-9]+$/.test(v) || "Usuário pode conter apenas letras e números"
        ],
        password: [
          v => !!v || "Campo de senha é obrigatório",
          v => (v && v.length > 7) || "Senha precisa ter pelo menos 8 caracteres",
        ],
        password2: [
          v => !!v || "Confirmação de senha é obrigatório",
        ]
      },
    }),

    methods: {
      register() {
        if (this.$refs.form.validate()) {}
      },
      passwordMissmatch() {
        return (this.credentials.password === this.credentials.password2) ? '' : 'Senhas precisam ser iguais'
      }
    }
  }
</script>