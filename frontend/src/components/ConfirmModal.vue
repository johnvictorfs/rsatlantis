<template>
  <v-dialog v-model="activated" persistent max-width="500">
    <v-card class="atl-round">
      <v-card-title class="headline" v-if="title">{{title}}</v-card-title>
      <v-card-text v-if="description">{{description}}</v-card-text>
      <v-card-actions>
        <v-spacer/>
        <v-btn class="modal-btn" small text @click="cancelAction">
          <v-icon left v-if="cancelIcon">{{cancelIcon}}</v-icon>
          {{cancelText}}
        </v-btn>
        <v-btn class="modal-btn" small color="success darken-1" @click="confirmAction">
          <v-icon left v-if="confirmIcon">{{confirmIcon}}</v-icon>
          {{confirmText}}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { Vue, Prop } from 'vue-property-decorator'
import Component from 'vue-class-component'


@Component({})
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
