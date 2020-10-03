<template>
  <v-container>
    <v-row justify="center">
      <v-col xs="12" sm="8" md="8" lg="8" xl="8">
        <v-card class="elevation-12 login-card">
          <v-toolbar dark color="green">
            <v-toolbar-title>
              Entre na sua Conta
            </v-toolbar-title>

            <v-spacer />

            <v-btn color="#7289da" @click="loginWithDiscord">
              <v-icon left>
                fab fa-discord
              </v-icon>
              Entrar com Discord
            </v-btn>
          </v-toolbar>

          <v-container fluid grid-list-md>
            <v-form ref="form" v-model="valid" lazy-validation @keyup.native.enter="login">
              <v-text-field
                autofocus
                v-model="credentials.username"
                prepend-icon="person"
                :rules="rules.username"
                :counter="20"
                type="text"
                label="Usuário"
                name="username"
                maxlength="20"
                required
              />

              <v-text-field
                v-model="credentials.password"
                prepend-icon="lock"
                :rules="rules.password"
                counter
                type="password"
                label="Senha"
                name="password"
                maxlength="70"
                required
              />

              <v-container class="mt-4">
                <v-toolbar color="#2d2e2d" class="atl-round-toolbar hidden-sm-and-down">
                  <v-btn color="primary" text small :to="{name: 'register'}">
                    Não tenho uma Conta
                    <v-icon right small>
                      fa-user-plus
                    </v-icon>
                  </v-btn>
                  <v-spacer />
                  <v-btn color="success" :disabled="!valid" @click="login">
                    Entrar
                    <v-icon right>
                      check
                    </v-icon>
                  </v-btn>
                </v-toolbar>
                <v-layout row class="hidden-md-and-up">
                  <v-flex xs12 offset-md8 class="mb-2">
                    <v-btn class="login-btn mt-4 mb-3" block color="success" :disabled="!valid" @click="login">
                      Entrar
                      <v-icon right>
                        check
                      </v-icon>
                    </v-btn>
                  </v-flex>
                </v-layout>

                <v-layout row class="hidden-md-and-up">
                  <v-btn color="primary" text small :to="{name: 'register'}">
                    Não tenho uma Conta
                    <v-icon right small>
                      fa-user-plus
                    </v-icon>
                  </v-btn>
                </v-layout>
              </v-container>
            </v-form>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

import api from '@/api'
import { formatError } from '@/helpers/errors'
import { UserCredentials } from '@/store/types'

@Component({})
export default class Login extends Vue {
  credentials: UserCredentials = { username: '', password: '' }

  valid: boolean = true

  rules = {
    username: [
      (value: string) => !!value || 'Campo de usuário é obrigatório',
      (value: string) => (value && value.length > 3) || 'Usuário precisa ter pelo menos 4 caracteres',
      (value: string) => /^[a-zA-Z\-0-9]+$/.test(value) || 'Usuário pode conter apenas letras e números'
    ],
    password: [
      (value: string) => !!value || 'Campo de senha é obrigatório',
      (value: string) => (value && value.length > 7) || 'Senha precisa ter pelo menos 8 caracteres'
    ]
  }

  async login() {
    if ((this.$refs.form as any).validate()) {
      await this.$store.dispatch('login', this.credentials)

      this.$router.push({ name: 'home' })

      if (this.$route.query.next) {
        // @ts-ignore
        // TODO: Mover isso para o store ou router.ts?
        // https://github.com/vuejs/vue-router/issues/1932
        this.$router.push(this.$route.query.next)
      }
    }
  }

  async loginWithDiscord() {
    const data = await api.discord.discordOauth()
    console.log(data.authorization_url)
    console.log(data)
    window.location.href = data.authorization_url
  }
}
</script>

<style lang="scss" scoped>
.login-card {
  border-radius: 12px !important;
}

.login-btn {
  height: 50px !important;
}
</style>
