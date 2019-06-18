<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md8 lg6 xl6>
        <v-card class="elevation-12">
          <v-toolbar dark color="green">
            <v-toolbar-title>
              Entre na sua Conta
            </v-toolbar-title>
          </v-toolbar>

          <v-container fluid grid-list-md>
            <v-form ref="form" v-model="valid" lazy-validation @keyup.native.enter="login">
              <v-text-field autofocus v-model="credentials.username" prepend-icon="person" :rules="rules.username" :counter="20" type="text" label="Usuário" name="username" maxlength="20" required />

              <v-text-field v-model="credentials.password" prepend-icon="lock" :rules="rules.password" counter type="password" label="Senha" name="password" maxlength="70" required />

              <v-container>
                <v-toolbar color="grey darken-4" class="hidden-sm-and-down">
                  <v-btn color="primary" text small :to="{name: 'register'}">
                    Não tenho uma Conta
                    <v-icon right small>fa-user-plus</v-icon>
                  </v-btn>
                  <v-spacer></v-spacer>
                  <v-btn color="success" :disabled="!valid" @click="login">
                    Entrar
                    <v-icon right>check</v-icon>
                  </v-btn>
                </v-toolbar>
                <v-layout row class="hidden-md-and-up">
                  <v-flex xs12 offset-md8 class="mb-2">
                    <v-btn class="atl-login-btn mt-4 mb-3" block color="success" :disabled="!valid" @click="login">
                      Entrar
                      <v-icon right>check</v-icon>
                    </v-btn>
                  </v-flex>
                </v-layout>
                <v-layout row justify-end class="hidden-md-and-up">
                  <v-btn color="primary" text small :to="{name: 'register'}">
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

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

import { formatError } from '../../helpers/errors'

import { UserCredentials } from '../../store/types'

@Component({})
export default class Login extends Vue {
  credentials: UserCredentials = {}
  valid: boolean = true
  rules = {
    username: [
      (v: string) => !!v || 'Campo de usuário é obrigatório',
      (v: string) => (v && v.length > 3) || 'Usuário precisa ter pelo menos 4 caracteres',
      (v: string) => /^[a-zA-Z\-0-9]+$/.test(v) || 'Usuário pode conter apenas letras e números'
    ],
    password: [
      (v: string) => !!v || 'Campo de senha é obrigatório',
      (v: string) => (v && v.length > 7) || 'Senha precisa ter pelo menos 8 caracteres'
    ]
  }

  translateError(error: string) {
    if (error === 'Error: Network Error') {
      return 'Erro: Falha de Conexão'
    }
    return 'Erro Inesperado, tente novamente mais tarde'
  }

  async login() {
    if ((this.$refs.form as any).validate()) {
      try {
        await this.$store.dispatch('login', this.credentials)
        this.$router.push({ name: 'home' })
        this.$toasted.global.success('Você entrou na sua conta com sucesso!')
        if (this.$route.query.next) {
          // @ts-ignore
          // TODO: Mover isso para o store ou router.ts?
          // https://github.com/vuejs/vue-router/issues/1932
          this.$router.push(this.$route.query.next)
        }
      } catch (error) {
        this.$toasted.global.error(formatError(error))
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.atl-login-btn {
  height: 50px !important;
}
</style>
