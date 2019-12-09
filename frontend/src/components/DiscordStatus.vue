<template>
  <v-container>
    <v-row justify="end">
      <v-col xs="12" sm="10" md="8" lg="6" xl="6">
        <v-card class="atl-round-card" raised :loading="loading">
          <v-toolbar dark color="#363636">
            <v-toolbar-title class="discord-title">
              <v-icon left size="30" color="#668fcb">
                fab fa-discord
              </v-icon>
              Discord
            </v-toolbar-title>

            <v-btn icon :loading="loading" :disabled="loading" @click="getData" class="ml-2">
              <v-icon>fa-sync-alt</v-icon>
            </v-btn>

            <v-spacer />

            <v-btn outlined color="#668fcb" target="_blank" :href="inviteUrl">
              Entrar
              <v-icon small right>
                fas fa-external-link-alt
              </v-icon>
            </v-btn>
          </v-toolbar>

          <v-card-text>
            <!-- Notificações de Raids -->
            <DiscordStatusAlert type="success" icon="mdi-sword-cross" v-if="raidsStatus && raidsStatus.notifications">
              <v-row align="center">
                <v-col class="grow">
                  Notificações de Raids Habilitadas
                </v-col>

                <v-col class="shrink">
                  <v-btn outlined small>
                    Aplicar
                    <v-icon right small>
                      fas fa-angle-right
                    </v-icon>
                  </v-btn>
                </v-col>

                <v-col class="shrink" v-show="isAdmin">
                  <ConfirmModal
                    title="Desabilitar Notificações de Raids"
                    description="Tem certeza que deseja desabilitar as Notificações de Raids do Discord?"
                    :activated="disableRaidsModal"
                    :confirm-action="toggleRaidsStatus"
                    :cancel-action="() => disableRaidsModal = false"
                    :cancel-icon="false"
                  />
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn color="error" fab small dark v-on="on" @click="disableRaidsModal = true">
                        <v-icon>fas fa-times</v-icon>
                      </v-btn>
                    </template>
                    <span>Desabilitar</span>
                  </v-tooltip>
                </v-col>
              </v-row>
            </DiscordStatusAlert>

            <!-- Erro Notificações Raids -->
            <DiscordStatusAlert type="error" icon="mdi-sword-cross" v-else-if="errors.raidsStatus">
              Erro ao atualizar informações de Notificações de Raids
            </DiscordStatusAlert>

            <!-- Notificações Raids Desabilitadas -->
            <DiscordStatusAlert type="error" icon="mdi-sword-cross" v-else>
              <v-row align="center">
                <v-col class="grow">
                  Notificações de Raids Desabilitadas
                </v-col>

                <v-col class="shrink" v-show="isAdmin">
                  <ConfirmModal
                    title="Habilitar Notificações de Raids"
                    description="Tem certeza que deseja habilitar as Notificações de Raids do Discord?"
                    :activated="enableRaidsModal"
                    :confirm-action="toggleRaidsStatus"
                    :cancel-action="() => enableRaidsModal = false"
                    :cancel-icon="false"
                  />
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn color="success" fab small dark v-on="on" @click="enableRaidsModal = true">
                        <v-icon>fas fa-check</v-icon>
                      </v-btn>
                    </template>
                    <span>Habilitar</span>
                  </v-tooltip>
                </v-col>
              </v-row>
            </DiscordStatusAlert>

            <!-- Membros Autenticados do Discord -->
            <DiscordStatusAlert color="primary" icon="fas fa-user" v-if="users.length > 0">
              <v-row align="center">
                <v-col class="grow">
                  Membros Autenticados: {{ users.length }}
                </v-col>

                <v-col class="shrink" v-show="isAdmin">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn icon v-on="on">
                        <v-icon>fas fa-list</v-icon>
                      </v-btn>
                    </template>
                    <span>Listar Membros</span>
                  </v-tooltip>
                </v-col>
              </v-row>
            </DiscordStatusAlert>

            <!-- Erro Membros Autenticados -->
            <DiscordStatusAlert type="error" icon="fas fa-user" v-else-if="errors.users">
              Erro ao atualizar informações de Membros Autenticados
            </DiscordStatusAlert>

            <!-- Nenhum Membro Autenticado -->
            <DiscordStatusAlert type="error" icon="fas fa-user" v-else>
              Nenhum Membro Autenticado
            </DiscordStatusAlert>

            <!-- Amigo Secreto -->
            <DiscordStatusAlert color="success" icon="fas fa-gifts" v-if="secretSanta && secretSanta.activated">
              <v-row align="center">
                <v-col class="grow">
                  Amigo Secreto Ativo! {{ secretSanta.registered }} Membros Registrados
                </v-col>

                <v-col class="shrink">
                  <v-btn outlined small>
                    Entrar
                    <v-icon right small>
                      fas fa-plus
                    </v-icon>
                  </v-btn>
                </v-col>

                <v-col class="shrink" v-show="isAdmin">
                  <ConfirmModal
                    title="Desabilitar Amigo Secreto"
                    description="Tem certeza que deseja deixar o Amigo Secreto do Discord inativo?"
                    :activated="disableSecretSantaModal"
                    :confirm-action="toggleSecretSantaStatus"
                    :cancel-action="() => disableSecretSantaModal = false"
                    :cancel-icon="false"
                  />
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn color="error" fab small dark v-on="on" @click="disableSecretSantaModal = true">
                        <v-icon>fas fa-times</v-icon>
                      </v-btn>
                    </template>
                    <span>Desabilitar</span>
                  </v-tooltip>
                </v-col>
              </v-row>
            </DiscordStatusAlert>

            <!-- Erro Amigo Secreto -->
            <DiscordStatusAlert type="error" icon="fas fa-gifts" v-else-if="errors.secretSanta">
              Erro ao atualizar informações do Amigo Secreto
            </DiscordStatusAlert>

            <!-- Amigo Secreto Inativo -->
            <DiscordStatusAlert type="error" icon="fas fa-gifts" v-else>
              <v-row align="center">
                <v-col class="grow">
                  Amigo Secreto Inativo
                </v-col>

                <v-col class="shrink" v-show="isAdmin">
                  <ConfirmModal
                    title="Desabilitar Amigo Secreto"
                    description="Tem certeza que deseja habilitar o Amigo Secreto do Discord?"
                    :activated="enableSecretSantaModal"
                    :confirm-action="toggleSecretSantaStatus"
                    :cancel-action="() => enableSecretSantaModal = false"
                    :cancel-icon="false"
                  />
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn color="success" fab small dark v-on="on" @click="enableSecretSantaModal = true">
                        <v-icon>fas fa-check</v-icon>
                      </v-btn>
                    </template>
                    <span>Habilitar</span>
                  </v-tooltip>
                </v-col>
              </v-row>
            </DiscordStatusAlert>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

import { Discord } from '@/types'
import api from '@/api'
const DiscordStatusAlert = () => import('@/components/DiscordStatusAlert.vue')
const ConfirmModal = () => import('@/components/ConfirmModal.vue')

@Component({
  components: { DiscordStatusAlert, ConfirmModal }
})
export default class DiscordStatus extends Vue {
  raidsStatus: Discord['RaidsStatus'] | null = null

  users: Discord['DiscordUser'][] = []

  secretSanta: Discord['SecretSantaStatus'] | null = null

  inviteUrl: string = 'https://discord.gg/2aYDY8N'

  loading: boolean = false

  enableRaidsModal = false
  disableRaidsModal = false
  disableSecretSantaModal = false
  enableSecretSantaModal = false

  errors = {
    raidsStatus: false,
    users: false,
    secretSanta: false
  }

  async mounted() {
    this.getData()
  }

  async getRaidsStatus() {
    try {
      this.raidsStatus = await api.discord.raids.status()
    } catch (error) {
      this.errors.raidsStatus = true
    }
  }

  async getUsersData() {
    try {
      this.users = await api.discord.users()
    } catch (error) {
      this.errors.users = true
    }
  }

  async getSecretSantaStatus() {
    try {
      this.secretSanta = await api.discord.secretSanta.status()
    } catch (error) {
      this.errors.secretSanta = true
    }
  }

  async getData() {
    /**
     * Get all Discord Status Data from API
     */
    this.loading = true

    await this.getRaidsStatus()
    await this.getUsersData()
    await this.getSecretSantaStatus()

    this.loading = false
  }

  async toggleRaidsStatus() {
    try {
      await api.discord.raids.toggle()
      this.getRaidsStatus()
      this.$toasted.global.success('Status de Notificações de Raids atualizado com sucesso!')
    } catch (error) {
      this.$toasted.global.error('Erro ao atualizar Status de Notificações de Raids')
    } finally {
      this.enableRaidsModal = false
      this.disableRaidsModal = false
    }
  }

  async toggleSecretSantaStatus() {
    try {
      await api.discord.secretSanta.toggle()
      this.getSecretSantaStatus()
      this.$toasted.global.success('Status do Amigo Secreto atualizado com sucesso!')
    } catch (error) {
      this.$toasted.global.error('Erro ao atualizar Status do Amigo Secreto')
    } finally {
      this.enableSecretSantaModal = false
      this.disableSecretSantaModal = false
    }
  }

  get isAdmin() {
    return this.$store.state.auth.user.isAdmin
  }
}
</script>

<style lang="scss" scoped>
.discord-title {
  font-family: Rubik, "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI",
  Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial,
  sans-serif;

  font-size: 23px;
}
</style>
