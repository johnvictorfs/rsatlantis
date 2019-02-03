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
                            box
                            :counter="20"
                            type="text"
                            label="Usuário"
                            name="username"
                            maxlength="20"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.email" prepend-icon="email" :rules="rules.email" counter
                            box
                            type="email"
                            label="Email"
                            name="email"
                            maxlength="70"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.password1" prepend-icon="lock" :rules="rules.password" counter
                            box
                            type="password"
                            label="Senha"
                            name="password"
                            maxlength="70"
                            required
              ></v-text-field>
              <v-text-field v-model="credentials.password2" prepend-icon="lock" :rules="rules.password2" counter
                            box
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
                Entrar
                <v-icon right>fa-sign-in-alt</v-icon>
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn color="primary" small :disabled="!userFormValid" @click="secondPage">
                Continuar
                <v-icon right>arrow_right</v-icon>
              </v-btn>
            </v-toolbar>

          </v-stepper-content>

          <v-stepper-content step="2">

            <v-form ref="form2" v-model="ingameFormValid" @submit.prevent="register">

              <v-text-field v-model="credentials.ingame_name" prepend-icon="person" :rules="rules.ingame_name"
                            box
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

              <v-btn flat small @click="registerStep = 1">
                <v-icon left>arrow_left</v-icon>
                Voltar
              </v-btn>

              <v-spacer></v-spacer>

              <v-btn :disabled="!validForms" small @click="register" color="success">
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

  const Centered = () => import('../../components/Centered');
  const isInClan = () => import('../../helpers/runescape');
  const formatError = () => import('../../helpers/errors');

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
      secondPage() {
        if (this.$refs.form.validate()) {
          this.registerStep = 2;
        }
      },
      register() {
        if (this.$refs.form.validate() && this.$refs.form2.validate()) {
          isInClan(this.credentials.ingame_name).then(isInClan => {
            if (isInClan) {
              this.$store.dispatch('createAccount', this.credentials).then(() => {
                this.$router.push({name: 'login'});
                this.$toasted.global.success('Conta criada com sucesso, entre agora!')
              }).catch(error => {
                this.registerStep = 1;
                this.$toasted.global.error(formatError(error));
              })
            } else {
              this.$toasted.global.error('Você precisa estar no Clã Atlantis para criar uma conta')
            }
          }).catch(() => {
            this.$toasted.global.error('Erro ao acessar a API do RuneScape. Tente novamente mais tarde');
          });

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