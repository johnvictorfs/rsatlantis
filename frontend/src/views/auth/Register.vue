<template>
  <Centered>
    <v-card class="elevation-12">

      <v-toolbar dark color="primary">
        <v-toolbar-title>Crie sua conta</v-toolbar-title>
      </v-toolbar>

      <v-stepper v-model="registerStep">
        <v-stepper-header>
          <v-stepper-step :complete="registerStep > 1" step="1">Detalhes de Usuário</v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step :complete="registerStep > 2" step="2">Detalhes de Jogo</v-stepper-step>

          <v-divider></v-divider>

        </v-stepper-header>

        <v-stepper-items>

          <v-stepper-content step="1">

            <v-form ref="form" v-model="userFormValid" @keydown.native.enter="secondPage">

              <v-text-field v-model="credentials.username" prepend-icon="person" :rules="rules.username"
                            :counter="20"
                            type="text"
                            label="Usuário"
                            name="username"
                            maxlength="20"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.email" prepend-icon="email" :rules="rules.email" counter
                            type="email"
                            label="Email"
                            name="email"
                            maxlength="70"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.password1" prepend-icon="lock" :rules="rules.password" counter
                            type="password"
                            label="Senha"
                            name="password"
                            maxlength="70"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.password2" prepend-icon="lock" :rules="rules.password2" counter
                            :error-messages='passwordMissmatch'
                            type="password"
                            label="Confirmar Senha"
                            name="password2"
                            maxlength="70"
                            required
              ></v-text-field>
            </v-form>
            <br/>
            <v-toolbar>
              <v-btn color="primary" flat small :to="{name: 'login'}">
                Já tenho uma conta
                <v-icon right>fa-sign-in-alt</v-icon>
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn color="primary" :disabled="!userFormValid" @click="secondPage">
                Continuar
                <v-icon right>arrow_right</v-icon>
              </v-btn>
            </v-toolbar>

          </v-stepper-content>

          <v-stepper-content step="2">

            <v-form ref="form2" v-model="ingameFormValid" @submit.prevent="register">

              <v-text-field v-model="credentials.ingame_name" prepend-icon="person" :rules="rules.ingame_name"
                            :counter="12"
                            type="text"
                            label="Nome no jogo"
                            name="ingame_username"
                            maxlength="12"
                            required
              ></v-text-field>
            </v-form>

            <br/>
            <v-toolbar>

              <v-btn flat @click="registerStep = 1">
                <v-icon left>arrow_left</v-icon>
                Voltar
              </v-btn>

              <v-spacer></v-spacer>

              <v-btn :disabled="!validForms" @click="register" color="success">
                Registrar
                <v-icon right>check</v-icon>
              </v-btn>

            </v-toolbar>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>

    </v-card>
  </Centered>
</template>

<script>
  /** @namespace this.credentials.username **/
  /** @namespace this.credentials.password1 **/
  /** @namespace this.credentials.password2 **/
  /** @namespace this.credentials.email **/
  /** @namespace this.credentials.ingame_name **/
  import Centered from '../../components/Centered'

  export default {
    name: 'Register',
    components: {
      Centered
    },
    data: () => ({
      registerStep: 0,
      credentials: {},
      userFormValid: false,
      ingameFormValid: false,
      rules: {
        email: [
          v => !!v || 'Campo de email é obrigatório',
          v => /.+@.+/.test(v) || 'Email precisa ser válido'
        ],
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
        ],
        ingame_name: [
          v => !!v || "Nome no Jogo é obrigatório",
        ]
      },
    }),

    methods: {
      translateError(error) {
        if (error === 'Error: Network Error') {
          return 'Erro: Falha de Conexão'
        }
        return error
      },
      secondPage() {
        if (this.$refs.form.validate()) {
          this.registerStep = 2;
        }
      },
      register() {
        if (this.$refs.form.validate() && this.$refs.form2.validate()) {
          this.$store.dispatch('createAccount', this.credentials).then(() => {
            this.$router.push({name: 'login'});
            this.$toasted.global.success('Conta criada com sucesso, entre agora!')
          }).catch(error => {
            this.registerStep = 1;
            let errorMessage = 'Erro inesperado :(';
            if (error.response !== undefined) {
              errorMessage = Object.values(error.response.data)[0];
            } else {
              errorMessage = error.toString();
            }
            this.$toasted.global.error(this.translateError(errorMessage));
          })
        } else if (!this.$refs.form.validate()) {
          // Go back to first page of form if it failed to validate, else stay on the same page
          this.registerStep = 1;
        }
      }
    },
    computed: {
      passwordMissmatch() {
        return (this.credentials.password1 === this.credentials.password2) ? [] : ['Senhas precisam ser iguais']
      },
      validForms() {
        return this.userFormValid && this.ingameFormValid;
      }
    }
  }
</script>