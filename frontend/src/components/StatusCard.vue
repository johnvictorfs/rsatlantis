<template>
  <v-row>
    <!-- Desktop Card -->
    <v-col class="ml-2 mr-2 hidden-sm-and-down">
      <v-alert
        border="left"
        prominent
        dense
        class="status-alert"
        transition="scale-transition"
        :type="type"
        :color="color"
        :icon="icon"
      >
        <v-row align="center">
          <v-col class="grow">
            <slot name="content" />
          </v-col>

          <v-col class="shrink" v-if="userActions">
            <slot name="user-actions" />
          </v-col>

          <v-col class="shrink" v-if="adminActions">
            <slot name="admin-actions" />
          </v-col>
        </v-row>
      </v-alert>
    </v-col>

    <!-- Mobile Card -->
    <v-col cols="12" class="hidden-md-and-up">
      <div class="ml-1 mr-1">
        <v-card small elevation="10" :color="color" shaped class="status-card">
          <v-list-item>
            <v-list-item-avatar :color="color + ' lighten-1'" class="avatar-icon ma-3">
              <v-icon>{{ icon }}</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>
              <div class="status-card-title">
                <slot name="content" />
              </div>
            </v-list-item-content>
          </v-list-item>

          <v-card-actions v-if="adminActions || userActions">
            <v-col class="shrink" v-if="adminActions">
              <slot name="admin-actions" />
            </v-col>

            <v-spacer />

            <v-col class="shrink" v-if="userActions">
              <slot name="user-actions" />
            </v-col>
          </v-card-actions>
        </v-card>
      </div>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Component from 'vue-class-component'
import { Vue, Prop } from 'vue-property-decorator'

@Component({})
export default class DiscordStatusCard extends Vue {
  @Prop() private type!: string;
  @Prop() private color!: string;
  @Prop() private icon!: string;
  @Prop({ default: false }) private adminActions!: boolean;
  @Prop({ default: false }) private userActions!: boolean;
}
</script>

<style lang="scss" scoped>
.status-card-title {
  font-size: 18px;
}

.status-alert {
  margin-bottom: 2px !important;
}
</style>
