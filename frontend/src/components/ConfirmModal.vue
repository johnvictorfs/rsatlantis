<template>
  <v-dialog v-model="activated" persistent max-width="500">
    <ModalCard>
      <!-- Dialog Title -->
      <template #title v-if="title">
        {{ title }}
      </template>

      <!-- Dialog Description -->
      <template #description v-if="description">
        {{ description }}
      </template>

      <!-- Dialog Actions -->
      <template #actions>
        <v-spacer />

        <!-- Cancel Button -->
        <v-btn class="modal-btn" small text @click.end="cancelAction">
          <v-icon left v-if="cancelIcon">
            {{ cancelIcon }}
          </v-icon>
          {{ cancelText }}
        </v-btn>

        <!-- Confirm Button -->
        <v-btn class="modal-btn" small color="success darken-1" @click.end="confirmAction">
          <v-icon small left v-if="confirmIcon">
            {{ confirmIcon }}
          </v-icon>
          {{ confirmText }}
        </v-btn>
      </template>
    </ModalCard>
  </v-dialog>
</template>

<script lang="ts">
import { Vue, Prop } from 'vue-property-decorator'
import Component from 'vue-class-component'

const ModalCard = () => import('@/components/ModalCard.vue')

@Component({
  components: { ModalCard }
})
export default class ConfirmModal extends Vue {
  @Prop() private activated!: boolean
  @Prop() private title?: string
  @Prop() private description?: string
  @Prop() private confirmAction!: Function
  @Prop() private cancelAction!: Function
  @Prop({ default: 'Confirmar' }) private confirmText!: string
  @Prop({ default: 'Cancelar' }) private cancelText!: string
  @Prop({ default: 'fas fa-times' }) private cancelIcon!: string | boolean
  @Prop({ default: 'fas fa-check' }) private confirmIcon!: string | boolean
}
</script>

<style lang="scss" scoped>
.modal-btn {
  border-radius: 8px !important;
}
</style>
