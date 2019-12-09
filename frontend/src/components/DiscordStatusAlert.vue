<template>
  <v-row>
    <v-col class="ml-3 mr-3 mb-0">
      <v-alert
        border="left"
        prominent
        class="atl-round"
        dense
        transition="scale-transition"
        :type="type"
        :color="color"
        :icon="icon"
      >
        <slot />
      </v-alert>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Component from 'vue-class-component'
import { Vue, Prop } from 'vue-property-decorator'

@Component({})
export default class DiscordStatusAlert extends Vue {
  @Prop() private type!: string;
  @Prop() private color!: string;
  @Prop() private icon!: string;
}
</script>
