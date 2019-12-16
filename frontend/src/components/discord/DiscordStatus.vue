<template>
  <v-container>
    <v-row justify="end">
      <v-col xs="12" sm="10" md="8" lg="8" xl="6">
        <v-card class="atl-round-card" raised :loading="loading">
          <!-- Discord Status Toolbar -->
          <v-toolbar dark color="#363636">
            <v-toolbar-title class="discord-title">
              <v-icon left size="32" color="#668fcb">
                fab fa-discord
              </v-icon>
              Discord
            </v-toolbar-title>

            <v-btn icon :loading="loading" :disabled="loading" @click.end="getData" class="ml-2">
              <v-icon height="18" width="18">
                fa-sync-alt
              </v-icon>
            </v-btn>

            <v-spacer />

            <!-- Mobile Discord Invite -->
            <v-btn icon class="hidden-md-and-up" color="#668fcb" target="_blank" :href="inviteUrl">
              <v-icon>fas fa-external-link-alt</v-icon>
            </v-btn>

            <!-- PC Discord Invite -->
            <v-btn outlined class="hidden-sm-and-down" color="#668fcb" target="_blank" :href="inviteUrl">
              Entrar
              <v-icon small right>
                fas fa-external-link-alt
              </v-icon>
            </v-btn>
          </v-toolbar>

          <v-card-text>
            <!-- Notificações de Raids -->
            <StatusCard
              :admin-actions="isAdmin"
              :user-actions="isAuthenticated"
              color="success"
              icon="mdi-sword-cross"
              v-if="raidsStatus && raidsStatus.notifications && !errors.raidsStatus"
            >
              <template #content>
                Notificações de Raids Ativas
              </template>

              <template #admin-actions>
                <v-dialog v-model="disableRaidsModal" max-width="500">
                  <template #activator="data">
                    <v-tooltip bottom>
                      <template #activator="{ on }">
                        <v-btn icon fab small dark v-on="on" @click.stop="disableRaidsModal = true">
                          <v-icon>fas fa-times</v-icon>
                        </v-btn>
                      </template>
                      <span>Desabilitar</span>
                    </v-tooltip>
                  </template>
                  <ConfirmModal
                    title="Desabilitar Notificações de Raids"
                    description="Tem certeza que deseja desabilitar as Notificações de Raids do Discord?"
                    v-model="disableRaidsModal"
                    @confirm="toggleRaidsStatus"
                    @close="disableRaidsModal = false"
                    :cancel-icon="false"
                  />
                </v-dialog>
              </template>

              <template #user-actions>
                <v-btn outlined small>
                  Aplicar
                  <v-icon right small>
                    fas fa-angle-right
                  </v-icon>
                </v-btn>
              </template>
            </StatusCard>


            <!-- Notificações Raids Desabilitadas -->
            <StatusCard color="error" icon="mdi-sword-cross" :admin-actions="isAdmin" v-else-if="raidsStatus && !raidsStatus.notifications && !errors.raidsStatus">
              <template #content>
                Notificações de Raids Desabilitadas
              </template>

              <template #admin-actions>
                <v-dialog v-model="enableRaidsModal" max-width="500">
                  <template #activator="data">
                    <v-tooltip bottom>
                      <template #activator="{ on }">
                        <v-btn icon fab small dark v-on="on" @click.stop="enableRaidsModal = true">
                          <v-icon>fas fa-check</v-icon>
                        </v-btn>
                      </template>
                      <span>Habilitar</span>
                    </v-tooltip>
                  </template>
                  <ConfirmModal
                    title="Habilitar Notificações de Raids"
                    description="Tem certeza que deseja habilitar as Notificações de Raids do Discord?"
                    v-model="enableRaidsModal"
                    @confirm="toggleRaidsStatus"
                    @close="enableRaidsModal = false"
                    :cancel-icon="false"
                  />
                </v-dialog>
              </template>
            </StatusCard>

            <!-- Erro Notificações Raids -->
            <StatusCard color="error" icon="mdi-sword-cross" v-else>
              <template #content>
                Erro ao atualizar informações de Notificações de Raids
              </template>
            </StatusCard>

            <!-- Membros Autenticados do Discord -->
            <StatusCard
              :admin-actions="isAdmin"
              color="primary"
              icon="fas fa-user"
              v-if="users.length > 0 && !errors.users"
            >
              <template #content>
                Membros Autenticados: {{ users.length }}
              </template>

              <template #admin-actions>
                <v-tooltip bottom>
                  <template #activator="{ on }">
                    <v-btn icon v-on="on">
                      <v-icon>fas fa-list</v-icon>
                    </v-btn>
                  </template>
                  <span>Listar Membros</span>
                </v-tooltip>
              </template>
            </StatusCard>

            <!-- Nenhum Membro Autenticado -->
            <StatusCard color="error" icon="fas fa-user" v-else-if="users.length === 0 && !errors.users">
              <template #content>
                Nenhum Membro Autenticado
              </template>
            </StatusCard>

            <!-- Erro Membros Autenticados -->
            <StatusCard color="error" icon="fas fa-user" v-else>
              <template #content>
                Erro ao atualizar informações de Membros Autenticados
              </template>
            </StatusCard>

            <!-- Amigo Secreto -->
            <StatusCard
              color="success"
              :user-actions="isAuthenticated"
              :admin-actions="isAdmin"
              icon="fas fa-gifts"
              v-if="secretSanta && secretSanta.activated && !errors.secretSanta"
            >
              <template #content>
                <div class="mb-3">
                  <strong>
                    Amigo Secreto
                  </strong>
                  ({{ secretSanta.registered }} membros registrados)
                </div>

                <div v-if="secretSanta.startDate">
                  <strong>Ínicio das Inscrições:</strong> {{ formattedSecretSantaStartDate }}
                </div>
                <div v-else>
                  Amigo Secreto Ativo, inscrições abertas em breve
                </div>

                <div v-if="secretSanta.endDate">
                  <strong>Evento:</strong> {{ formattedSecretSantaEndDate }}
                </div>
                <div v-if="secretSanta.endDate">
                  <strong>Local:</strong> Fortaleza do Clã
                </div>
                <div v-if="secretSanta.endDate && secretSanta.premioMinimo">
                  <strong>Prêmio Mínimo:</strong> {{ secretSanta.premioMinimo }}
                </div>
              </template>

              <template #user-actions>
                <v-row justify="center">
                  <v-btn outlined small class="mb-2 mr-2">
                    Entrar
                    <v-icon right small>
                      fas fa-plus
                    </v-icon>
                  </v-btn>

                  <v-tooltip bottom>
                    <template #activator="{ on }">
                      <v-btn rounded outlined small v-on="on">
                        <v-icon small>
                          fas fa-info
                        </v-icon>
                      </v-btn>
                    </template>
                    <span>Informações</span>
                  </v-tooltip>
                </v-row>
              </template>

              <template #admin-actions v-if="isAdmin">
                <v-dialog v-model="disableSecretSantaModal" max-width="500px">
                  <template #activator="data">
                    <v-tooltip bottom>
                      <template #activator="{ on }">
                        <v-btn
                          class="mb-2"
                          icon
                          fab
                          small
                          dark
                          v-on="on"
                          @click.stop="disableSecretSantaModal = true"
                        >
                          <v-icon>fas fa-times</v-icon>
                        </v-btn>
                      </template>
                      <span>Desabilitar</span>
                    </v-tooltip>
                  </template>

                  <!-- Disable Secret Santa Modal -->
                  <ConfirmModal
                    title="Desabilitar Amigo Secreto"
                    description="Tem certeza que deseja deixar o Amigo Secreto do Discord inativo?"
                    v-model="disableSecretSantaModal"
                    @confirm="toggleSecretSantaStatus"
                    @close="disableSecretSantaModal = false"
                    :cancel-icon="false"
                  />
                </v-dialog>

                <!-- Edit Secret Santa Modal -->
                <v-dialog v-model="editSecretSantaModal" scrollable max-width="500">
                  <template #activator="data">
                    <v-tooltip bottom>
                      <template #activator="{ on }">
                        <v-btn
                          icon
                          fab
                          small
                          dark
                          v-on="on"
                          @click.stop="editSecretSantaModal = true"
                        >
                          <v-icon>fas fa-edit</v-icon>
                        </v-btn>
                      </template>
                      <span>Editar</span>
                    </v-tooltip>
                  </template>

                  <EditSecretSanta @close="editSecretSantaModal = false" @update="getSecretSantaStatus" />
                </v-dialog>
              </template>
            </StatusCard>

            <!-- Amigo Secreto Inativo -->
            <StatusCard :admin-actions="isAdmin" color="error" icon="fas fa-gifts" v-else-if="secretSanta && !secretSanta.activated && !errors.secretSanta">
              <template #content>
                Amigo Secreto Inativo
              </template>

              <template #admin-actions>
                <v-dialog v-model="enableSecretSantaModal" max-width="500">
                  <template #activator="data">
                    <v-tooltip bottom>
                      <template #activator="{ on }">
                        <v-btn icon fab small dark v-on="on" @click.stop="enableSecretSantaModal = true">
                          <v-icon>fas fa-check</v-icon>
                        </v-btn>
                      </template>
                      <span>Habilitar</span>
                    </v-tooltip>
                  </template>

                  <ConfirmModal
                    title="Habilitar Amigo Secreto"
                    description="Tem certeza que deseja habilitar o Amigo Secreto do Discord?"
                    v-model="enableSecretSantaModal"
                    @confirm="toggleSecretSantaStatus"
                    @close="enableSecretSantaModal = false"
                    :cancel-icon="false"
                  />
                </v-dialog>
              </template>
            </StatusCard>

            <!-- Erro Amigo Secreto -->
            <StatusCard color="error" icon="fas fa-gifts" v-else>
              <template #content>
                Erro ao atualizar informações do Amigo Secreto
              </template>
            </StatusCard>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'
import moment from 'moment'
import 'moment/locale/pt-br'

import { Discord } from '@/types'
import api from '@/api'

const StatusCard = () => import('@/components/StatusCard.vue')
const ConfirmModal = () => import('@/components/ConfirmModal.vue')
const ModalCard = () => import('@/components/ModalCard.vue')
const EditSecretSanta = () => import('@/components/discord/EditSecretSanta.vue')


  @Component({
    components: { StatusCard, ConfirmModal, ModalCard, EditSecretSanta }
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
    editSecretSantaModal = false

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
        this.errors.raidsStatus = false
      } catch (error) {
        this.errors.raidsStatus = true
      }
    }

    async getUsersData() {
      try {
        this.users = await api.discord.users()
        this.errors.users = false
      } catch (error) {
        this.errors.users = true
      }
    }

    async getSecretSantaStatus() {
      try {
        this.secretSanta = await api.discord.secretSanta.status()
        this.errors.secretSanta = false
      } catch (error) {
        this.errors.secretSanta = true
      }
    }

    async getData() {
      /**
       * Get all Discord Status Data from API
       */
      this.loading = true

      // Get all data, then set loading to false
      const promises = [
        new Promise(resolve => resolve(this.getRaidsStatus())),
        new Promise(resolve => resolve(this.getUsersData())),
        new Promise(resolve => resolve(this.getSecretSantaStatus()))
      ]

      await Promise.all(promises)
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

    formatDate(date: string | null): string | null {
      /**
       * Format date as /d/m/y
       */
      if (!date) return null

      const formattedDate = new Date(date)

      const timeLeft = moment(formattedDate, '', 'pt').fromNow()

      return moment(formattedDate, '', 'pt').format('D [de] MMMM [às] HH:mm') + ', ' + timeLeft
    }

    get isAdmin() {
      return this.$store.getters.isAdmin
    }

    get isAuthenticated() {
      return this.$store.getters.isAuthenticated
    }

    get formattedSecretSantaStartDate(): string | null {
      /**
       * Start Date of Secret Santa as d/m/y
       */
      if (this.secretSanta) {
        return this.formatDate(this.secretSanta.startDate)
      }
      return null
    }

    get formattedSecretSantaEndDate(): string | null {
      /**
       * End Date of Secret Santa as d/m/y
       */
      if (this.secretSanta) {
        return this.formatDate(this.secretSanta.endDate)
      }
      return null
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
