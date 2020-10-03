<template>
  <ModalCard>
    <template #title>
      Amigo Secreto do Discord
    </template>

    <template #description>
      <v-container>
        <v-form ref="form" v-model="valid" lazy-validation @keyup.native.enter="save">
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
                  :rules="rules.startDate"
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
              ref="startTimeMenuRef"
              v-model="startTimeMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="startTime"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="startTime"
                  :rules="rules.startTime"
                  :disabled="!startDate"
                  label="Tempo de Ínicio das Inscrições"
                  prepend-icon="access_time"
                  readonly
                  v-on="on"
                />
              </template>
              <v-time-picker
                light
                :disabled="!startDate"
                color="primary"
                header-color="primary"
                v-if="startTimeMenu"
                v-model="startTime"
                full-width
                @click:minute="$refs.startTimeMenuRef.save(startTime)"
              />
            </v-menu>
          </v-row>

          <hr class="mt-3 mb-3">

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
                  :rules="rules.endDate"
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

          <v-row justify="center">
            <v-menu
              ref="endTimeMenuRef"
              v-model="endTimeMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="endTime"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="endTime"
                  :rules="rules.endTime"
                  :disabled="!endDate"
                  label="Tempo do Sorteio"
                  prepend-icon="access_time"
                  readonly
                  v-on="on"
                />
              </template>
              <v-time-picker
                light
                :disabled="!endDate"
                color="primary"
                header-color="primary"
                v-if="endTimeMenu"
                v-model="endTime"
                full-width
                @click:minute="$refs.endTimeMenuRef.save(endTime)"
              />
            </v-menu>
          </v-row>

          <v-row class="mt-3">
            <v-text-field v-model="premioMinimo" :rules="rules.premioMinimo" maxlength="12" type="number" label="Valor Mínimo do Presente" filled />
          </v-row>
        </v-form>
      </v-container>
    </template>

    <template #actions>
      <v-spacer />

      <!-- Cancel Button -->
      <v-btn class="modal-btn ml-2" small text @click.stop="$emit('close')">
        Cancelar
      </v-btn>

      <!-- Save Button -->
      <v-btn class="modal-btn" small color="success darken-1" @click.stop="save">
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
// import moment from 'moment'
// import 'moment/locale/pt-br'

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
export default class EditSecretSanta extends Vue {
  secretSantaStatus: Discord['SecretSantaStatus'] | null = null

  today: string = new Date().toISOString().substr(0, 10)

  requiredField = (value: string) => !!value || 'Esse campo é obrigatório'

  valid: boolean = true

  rules: Record<string, Function[]> = {
    startTime: [this.requiredField],
    startDate: [this.requiredField],
    endTime: [this.requiredField],
    endDate: [this.requiredField],
    premioMinimo: [this.requiredField]
  }

  premioMinimo: string = '0'

  startTime: string = ''
  startDate: string = ''

  endTime: string = ''
  endDate: string = ''

  startDateMenu: boolean = false
  startTimeMenu: boolean = false

  endDateMenu: boolean = false
  endTimeMenu: boolean = false

  async mounted() {
    this.getSecretSantaStatus()
  }

  async getSecretSantaStatus() {
    try {
      this.secretSantaStatus = await api.discord.secretSanta.status()

      if (this.secretSantaStatus.startDate) {
        const startDate = new Date(this.secretSantaStatus.startDate)
        // this.startTime = moment(startDate, '', 'pt').format('HH:mm')
        this.startTime = 'startTime'
        this.startDate = startDate.toISOString().substr(0, 10)
      }

      if (this.secretSantaStatus.endDate) {
        const endDate = new Date(this.secretSantaStatus.endDate)
        // this.endTime = moment(endDate, '', 'pt').format('HH:mm')
        this.endTime = 'endTime'
        this.endDate = endDate.toISOString().substr(0, 10)
      }

      if (this.secretSantaStatus.premioMinimo) {
        this.premioMinimo = this.secretSantaStatus.premioMinimo.toString()
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
      if ((this.$refs.form as any).validate()) {
        // Convert date formats to ISO DateTime
        const isoStartDate = new Date(`${this.startDate} ${this.startTime}`).toISOString()
        const isoEndDate = new Date(`${this.endDate} ${this.endTime}`).toISOString()

        await api.discord.secretSanta.updateDates(isoStartDate, isoEndDate, this.premioMinimo)
        this.$toasted.global.success('Datas do Amigo Secreto atualizadas com sucesso!')
        this.$emit('close')
        this.$emit('update')
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
