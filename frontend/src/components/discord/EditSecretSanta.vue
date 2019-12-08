<template>
  <ModalCard>
    <template #title>
      Amigo Secreto do Discord
    </template>

    <template #description>
      <v-container>
        <v-row justify="center">
          <v-menu
            v-model="startDateMenu"
            :close-on-content-click="false"
            transition="scale-transition"
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="formattedStartDate"
                label="Data de Ínicio das Inscrições"
                prepend-icon="event"
                readonly
                v-on="on"
              />
            </template>
            <v-date-picker :min="today" light header-color="primary" color="primary" v-model="startDate" @input="startDateMenu = false" />
          </v-menu>
        </v-row>

        <v-row justify="center">
          <v-menu
            v-model="endDateMenu"
            :close-on-content-click="false"
            transition="scale-transition"
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                :disabled="!startDate"
                v-model="formattedEndDate"
                label="Data do Sorteio"
                prepend-icon="event"
                readonly
                v-on="on"
              />
            </template>
            <v-date-picker :min="startDate" light header-color="primary" color="primary" v-model="endDate" @input="endDateMenu = false" />
          </v-menu>
        </v-row>
      </v-container>
    </template>

    <template #actions>
      <v-spacer />

      <!-- Cancel Button -->
      <v-btn class="modal-btn ml-2" small text @click.end="cancel">
        Cancelar
      </v-btn>

      <!-- Save Button -->
      <v-btn class="modal-btn" small color="success darken-1" @click.end="save">
        <v-icon small left>
          fas fa-save
        </v-icon>
        Salvar
      </v-btn>
    </template>
  </ModalCard>
</template>

<script lang="ts">
import { Vue, Prop } from 'vue-property-decorator'
import Component from 'vue-class-component'

import { Discord } from '@/types'
import api from '@/api'

const ModalCard = () => import('@/components/ModalCard.vue')

interface IEditSecretSantaModal {
  activated: boolean
  startMenu: boolean
  endMenu: boolean
  startDateSecretSanta: Date | null
  endDateSecretSanta: Date | null
  formattedStartDateSecretSanta: string
  formattedEndDateSecretSanta: string
}

@Component({
  components: { ModalCard }
})
export default class ConfirmModal extends Vue {
  @Prop() cancel!: Function
  @Prop() afterUpdate!: Function

  secretSantaStatus: Discord['SecretSantaStatus'] | null = null

  today: string = new Date().toISOString().substr(0, 10)

  startDate: string = ''
  endDate: string = ''

  startDateMenu: boolean = false
  endDateMenu: boolean = false

  async mounted() {
    this.getSecretSantaStatus()
  }

  async getSecretSantaStatus() {
    try {
      this.secretSantaStatus = await api.discord.secretSanta.status()

      if (this.secretSantaStatus.startDate) {
        this.startDate = new Date(this.secretSantaStatus.startDate).toISOString().substr(0, 10)
      }

      if (this.secretSantaStatus.endDate) {
        this.endDate = new Date(this.secretSantaStatus.endDate).toISOString().substr(0, 10)
      }
    } catch (error) {
      this.$toasted.global.error('Erro ao atualizar dados do Amigo Secreto')
    }
  }

  formatDate(date: string): string | null {
    /**
     * Format date as /d/m/y
     */
    if (!date) return null

    const [year, month, day] = date.split('-')
    return `${day}/${month}/${year}`
  }

  async save() {
    /**
     * Save Secret Santa with Updated Dates
     */
    try {
      if (this.startDate && this.endDate) {
        await api.discord.secretSanta.updateDates(this.startDate, this.endDate)
        this.$toasted.global.success('Datas do Amigo Secreto atualizadas com sucesso!')
        this.cancel()
        this.afterUpdate()
      } else {
        this.$toasted.global.error('Você precisa selecionar uma Data de Ínicio e uma Data de Sorteio!')
      }
    } catch (error) {
      this.$toasted.global.error('Erro ao atualizar Datas do Amigo Secreto')
    }
  }

  get formattedStartDate(): string | null {
    return this.formatDate(this.startDate)
  }

  get formattedEndDate(): string | null {
    return this.formatDate(this.endDate)
  }
}
</script>

<style lang="scss" scoped>
  .modal-btn {
    border-radius: 8px !important;
  }
</style>
