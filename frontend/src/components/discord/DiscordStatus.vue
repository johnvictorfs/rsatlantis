<template>
  <v-container>
    <v-row justify="end">
      <v-col xs="12" sm="10" md="8" lg="6" xl="6">
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
              :user-actions="true"
              color="success"
              icon="mdi-sword-cross"
              v-if="raidsStatus && raidsStatus.notifications && !errors.raidsStatus"
            >
              <template #content>
                Notificações de Raids Ativas
              </template>

              <template #admin-actions v-if="isAdmin">
                <ConfirmModal
                  title="Desabilitar Notificações de Raids"
                  description="Tem certeza que deseja desabilitar as Notificações de Raids do Discord?"
                  :activated="disableRaidsModal"
                  :confirm-action="toggleRaidsStatus"
                  :cancel-action="() => disableRaidsModal = false"
                  :cancel-icon="false"
                />
                <v-tooltip bottom>
                  <template #activator="{ on }">
                    <v-btn icon fab small dark v-on="on" @click.end="disableRaidsModal = true">
                      <v-icon>fas fa-times</v-icon>
                    </v-btn>
                  </template>
                  <span>Desabilitar</span>
                </v-tooltip>
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

            <!-- Erro Notificações Raids -->
            <StatusCard color="error" icon="mdi-sword-cross" v-else-if="errors.raidsStatus">
              <template #content>
                Erro ao atualizar informações de Notificações de Raids
              </template>
            </StatusCard>

            <!-- Notificações Raids Desabilitadas -->
            <StatusCard color="error" icon="mdi-sword-cross" :admin-actions="isAdmin" v-else>
              <template #content>
                Notificações de Raids Desabilitadas
              </template>

              <template #admin-actions v-if="isAdmin">
                <ConfirmModal
                  title="Habilitar Notificações de Raids"
                  description="Tem certeza que deseja habilitar as Notificações de Raids do Discord?"
                  :activated="enableRaidsModal"
                  :confirm-action="toggleRaidsStatus"
                  :cancel-action="() => enableRaidsModal = false"
                  :cancel-icon="false"
                />
                <v-tooltip bottom>
                  <template #activator="{ on }">
                    <v-btn icon fab small dark v-on="on" @click.end="enableRaidsModal = true">
                      <v-icon>fas fa-check</v-icon>
                    </v-btn>
                  </template>
                  <span>Habilitar</span>
                </v-tooltip>
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

              <template #admin-actions v-if="isAdmin">
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

            <!-- Erro Membros Autenticados -->
            <StatusCard color="error" icon="fas fa-user" v-else-if="errors.users">
              <template #content>
                Erro ao atualizar informações de Membros Autenticados
              </template>
            </StatusCard>

            <!-- Nenhum Membro Autenticado -->
            <StatusCard color="error" icon="fas fa-user" v-else>
              <template #content>
                Nenhum Membro Autenticado
              </template>
            </StatusCard>

            <!-- Amigo Secreto -->
            <StatusCard
              color="success"
              :user-actions="true"
              :admin-actions="isAdmin"
              icon="fas fa-gifts"
              v-if="secretSanta && secretSanta.activated && !errors.secretSanta"
            >
              <template #content>
                <div class="mb-3">
                  <strong>
                    Amigo Secreto
                  </strong>
                </div>

                <div v-if="secretSanta.startDate">
                  <strong>Ínicio das Inscrições:</strong> {{ formattedSecretSantaStartDate }}
                </div>
                <div v-else>
                  Amigo Secreto Ativo, inscrições abertas em breve
                </div>

                <div v-if="secretSanta.endDate">
                  <strong>Sorteio:</strong> {{ formattedSecretSantaEndDate }}
                </div>
              </template>

              <template #user-actions>
                <v-row justify="center">
                  <v-btn outlined small class="mb-2">
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
                <!-- Disable Secret Santa Modal -->
                <ConfirmModal
                  title="Desabilitar Amigo Secreto"
                  description="Tem certeza que deseja deixar o Amigo Secreto do Discord inativo?"
                  :activated="disableSecretSantaModal"
                  :confirm-action="toggleSecretSantaStatus"
                  :cancel-action="() => disableSecretSantaModal = false"
                  :cancel-icon="false"
                />

                <!-- Edit Secret Santa Modal -->
                <v-dialog v-model="editSecretSantaModal" scrollable max-width="500">
                  <EditSecretSanta :cancel="() => editSecretSantaModal = false" :after-update="getSecretSantaStatus" />
                </v-dialog>

                <v-tooltip bottom>
                  <template #activator="{ on }">
                    <v-btn
                      class="mb-2"
                      icon
                      fab
                      small
                      dark
                      v-on="on"
                      @click.end="disableSecretSantaModal = true"
                    >
                      <v-icon>fas fa-times</v-icon>
                    </v-btn>
                  </template>
                  <span>Desabilitar</span>
                </v-tooltip>

                <v-tooltip bottom>
                  <template #activator="{ on }">
                    <v-btn
                      icon
                      fab
                      small
                      dark
                      v-on="on"
                      @click.end="editSecretSantaModal = true"
                    >
                      <v-icon>fas fa-edit</v-icon>
                    </v-btn>
                  </template>
                  <span>Editar</span>
                </v-tooltip>
              </template>
            </StatusCard>

            <!-- Erro Amigo Secreto -->
            <StatusCard color="error" icon="fas fa-gifts" v-else-if="errors.secretSanta">
              <template #content>
                Erro ao atualizar informações do Amigo Secreto
              </template>
            </StatusCard>

            <!-- Amigo Secreto Inativo -->
            <StatusCard :admin-actions="isAdmin" color="error" icon="fas fa-gifts" v-else>
              <template #content>
                Amigo Secreto Inativo
              </template>

              <template #admin-actions v-if="isAdmin">
                <ConfirmModal
                  title="Habilitar Amigo Secreto"
                  description="Tem certeza que deseja habilitar o Amigo Secreto do Discord?"
                  :activated="enableSecretSantaModal"
                  :confirm-action="toggleSecretSantaStatus"
                  :cancel-action="() => enableSecretSantaModal = false"
                  :cancel-icon="false"
                />
                <v-tooltip bottom>
                  <template #activator="{ on }">
                    <v-btn icon fab small dark v-on="on" @click.end="enableSecretSantaModal = true">
                      <v-icon>fas fa-check</v-icon>
                    </v-btn>
                  </template>
                  <span>Habilitar</span>
                </v-tooltip>
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

    formatDate(date: string | null): string | null {
    /**
     * Format date as /d/m/y
     */
      if (!date) return null

      const formattedDate = new Date(date)

      const timeLeft = moment(formattedDate, '', 'pt').fromNow()

      return moment(formattedDate, '', 'pt').format('dddd, D [de] MMMM [às] HH:mm') + ', ' + timeLeft
    }

    get isAdmin() {
      return this.$store.getters.isAdmin
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
