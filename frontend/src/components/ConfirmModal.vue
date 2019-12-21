<template>
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
      <v-btn class="modal-btn" small text @click.stop="$emit('close')">
        <v-icon left v-if="cancelIcon">
          {{ cancelIcon }}
        </v-icon>
        {{ cancelText }}
      </v-btn>

      <!-- Confirm Button -->
      <v-btn class="modal-btn" small color="success darken-1" @click.stop="$emit('confirm')">
        <v-icon small left v-if="confirmIcon">
          {{ confirmIcon }}
        </v-icon>
        {{ confirmText }}
      </v-btn>
    </template>
  </ModalCard>
</template>

<script lang="ts">
import { Vue, Prop, Watch } from 'vue-property-decorator'
import Component from 'vue-class-component'

const ModalCard = () => import('@/components/ModalCard.vue')

@Component({
  components: { ModalCard }
})
export default class ConfirmModal extends Vue {
  @Prop() private title?: string
  @Prop() private description?: string
  @Prop() private value!: boolean

  @Prop({ default: 'Confirmar' }) private confirmText!: string
  @Prop({ default: 'Cancelar' }) private cancelText!: string
  @Prop({ default: 'fas fa-times' }) private cancelIcon!: string | boolean
  @Prop({ default: 'fas fa-check' }) private confirmIcon!: string | boolean

  dialog: boolean = this.value

  @Watch('value')
  onValueChanged(val: boolean, oldVal: boolean) {
    /**
     * Update dialog v-model value when this component's v-model value changes
     */
    this.dialog = val
  }

  @Watch('dialog')
  onDialogChange(val: boolean, oldVal: boolean) {
    /**
     * Emit close event when dialog is closed
     */
    if (!val) {
      this.$emit('close')
    }
  }
}
</script>

<style lang="scss" scoped>
.modal-btn {
  border-radius: 8px !important;
}
</style>
