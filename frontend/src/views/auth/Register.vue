<template>
  <v-container fluid fill-height>
    <v-row justify="center">
      <v-col xs="12" sm="8" md="8" lg="6" xl="6">
        <v-card class="elevation-12 register-card">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Crie sua conta</v-toolbar-title>
          </v-toolbar>

          <v-stepper v-model="registerStep">
            <v-stepper-header>
              <v-stepper-step :complete="registerStep > 1" step="1">Detalhes de Usuário</v-stepper-step>

              <v-divider/>

              <v-stepper-step :complete="registerStep > 2" step="2">Detalhes de Jogo</v-stepper-step>

              <v-divider/>
            </v-stepper-header>

            <v-stepper-items>
              <v-stepper-content step="1">
                <v-form ref="form" v-model="userFormValid" @keydown.native.enter="secondPage">
                  <v-text-field
                    v-model="credentials.username"
                    autofocus
                    prepend-icon="person"
                    :rules="rules.username"
                    filled
                    :counter="20"
                    type="text"
                    label="Usuário"
                    name="username"
                    maxlength="20"
                    required
                  />
                  <v-text-field
                    v-model="credentials.email"
                    prepend-icon="email"
                    :rules="rules.email"
                    counter
                    filled
                    type="email"
                    label="Email"
                    name="email"
                    maxlength="70"
                    required
                  />
                  <v-text-field
                    v-model="credentials.password"
                    prepend-icon="lock"
                    :rules="rules.password"
                    counter
                    filled
                    type="password"
                    label="Senha"
                    name="password"
                    maxlength="70"
                    required
                  />
                  <v-text-field
                    v-model="credentials.password2"
                    prepend-icon="lock"
                    :rules="rules.password2"
                    counter
                    filled
                    :error-messages="passwordMissmatch"
                    type="password"
                    label="Confirmar Senha"
                    name="password2"
                    maxlength="70"
                    required
                  />
                </v-form>
                <v-container>
                  <v-toolbar color="grey darken-4" class="atl-round-toolbar hidden-sm-and-down">
                    <v-btn color="success" text small :to="{name: 'login'}">
                      Já tenho uma conta
                      <v-icon right>fa-sign-in-alt</v-icon>
                    </v-btn>
                    <v-spacer />
                    <v-btn color="primary" :disabled="!userFormValid" @click="secondPage">
                      Continuar
                      <v-icon right>arrow_right</v-icon>
                    </v-btn>
                  </v-toolbar>
                  <v-layout row class="hidden-md-and-up">
                    <v-flex xs12 offset-md8 class="mb-2">
                      <v-btn color="primary" class="continue-btn mt-2 mb-3" block :disabled="!userFormValid" @click="secondPage">
                        Continuar
                        <v-icon right>arrow_right</v-icon>
                      </v-btn>
                    </v-flex>
                  </v-layout>
                  <v-layout row class="hidden-md-and-up">
                    <v-btn color="success" text small :to="{name: 'login'}">
                      Já tenho uma conta
                      <v-icon right small>fa-sign-in-alt</v-icon>
                    </v-btn>
                  </v-layout>
                </v-container>

              </v-stepper-content>

              <v-stepper-content step="2">
                <v-form ref="form2" v-model="ingameFormValid" @submit.prevent="register">
                  <v-text-field
                    v-model="credentials.ingame_name"
                    prepend-icon="person"
                    :rules="rules.ingame_name"
                    filled
                    :counter="12"
                    type="text"
                    label="Nome no jogo"
                    name="ingame_username"
                    maxlength="12"
                    required
                  />
                </v-form>

                <br>
                <v-toolbar>
                  <v-btn text @click="registerStep = 1">
                    <v-icon left>arrow_left</v-icon>Voltar
                  </v-btn>

                  <v-spacer />

                  <v-btn :disabled="!validForms" @click="register" color="success">
                    Registrar
                    <v-icon right>check</v-icon>
                  </v-btn>
                </v-toolbar>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

import { UserCredentials } from '@/store/types'
import { isInClan } from '@/helpers/runescape'
import { formatError } from '@/helpers/errors'

@Component({})
export default class Register extends Vue {
  registerStep: number = 0
  credentials: UserCredentials = { username: '', password: '' }
  userFormValid: boolean = false
  ingameFormValid: boolean = false
  rules = {
    email: [
      (v: string) => !!v || 'Campo de email é obrigatório',
      (v: string) => /.+@.+/.test(v) || 'Email precisa ser válido'
    ],
    username: [
      (v: string) => !!v || 'Campo de usuário é obrigatório',
      (v: string) => (v && v.length > 3) || 'Usuário precisa ter pelo menos 4 caracteres',
      (v: string) => /^[a-zA-Z\-0-9]+$/.test(v) || 'Usuário pode conter apenas letras e números'
    ],
    password: [
      (v: string) => !!v || 'Campo de senha é obrigatório',
      (v: string) => (v && v.length > 7) || 'Senha precisa ter pelo menos 8 caracteres'
    ],
    password2: [(v: string) => !!v || 'Confirmação de senha é obrigatório'],
    ingame_name: [(v: string) => !!v || 'Nome no Jogo é obrigatório']
  }

  secondPage() {
    if ((this.$refs.form as any).validate()) {
      this.registerStep = 2
    }
  }

  async register() {
    if ((this.$refs.form as any).validate() && (this.$refs.form2 as any).validate()) {
      try {
        const inClan = isInClan(this.credentials.ingame_name)

        if (inClan) {
          try {
            this.$store.dispatch('createAccount', this.credentials)
            this.$router.push({ name: 'login' })
            this.$toasted.global.success('Conta criada com sucesso, entre agora!')
          } catch (error) {
            this.registerStep = 1
            this.$toasted.global.error(formatError(error))
          }
        } else {
          this.$toasted.global.error('Você precisa estar no Clã Atlantis para criar uma conta')
        }
      } catch (error) {
        this.$toasted.global.error('Erro ao acessar a API do RuneScape. Tente novamente mais tarde')
      }
    } else if (!(this.$refs.form as any).validate()) {
      // Go back to first page of form if it failed to validate, else stay on the same page
      this.registerStep = 1
    }
  }

  get passwordMissmatch() {
    return this.credentials.password === this.credentials.password2 ? [] : [
      'Senhas precisam ser iguais'
    ]
  }
  get validForms() {
    return this.userFormValid && this.ingameFormValid
  }
}
</script>

<style lang="scss" scoped>
.register-card {
  border-radius: 12px !important;
}

.continue-btn {
  height: 50px !important;
}
</style>

