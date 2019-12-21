<template>
  <v-container>
    <v-row justify="center">
      <v-col xs="12" sm="8" md="8" lg="4" xl="4">
        <v-card class="elevation-12">
          <v-toolbar dark color="#363636">
            <v-toolbar-title>
              <v-icon left size="32" color="#668fcb">
                fas fa-gifts
              </v-icon>
              <span class="hidden-md-and-down">
                Inscritos no Amigo Secreto
              </span>

              <span class="hidden-lg-and-up">
                Amigo Secreto
              </span>
            </v-toolbar-title>
          </v-toolbar>

          <v-card-text>
            <!-- API Error -->
            <v-alert v-if="apiError" type="error">
              {{ apiErrorMessage }}
            </v-alert>

            <v-list v-else three-line>
              <v-list-item-group>
                <template v-for="(user, index) in users">
                  <v-subheader
                    v-if="index === 0"
                    :key="user.id"
                    v-text="`${users.length} inscritos`"
                  />

                  <v-list-item
                    :key="user.id"
                  >
                    <v-list-item-avatar class="hidden-sm-and-down">
                      <v-img
                        :src="`https://secure.runescape.com/m=avatar-rs/${user.user.ingame_name.replace(/\s/g, '_')}/chat.png`"
                        :alt="`avatar${user.user.ingame_name}`"
                      />
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title v-text="user.user.ingame_name" />
                      <v-list-item-subtitle>
                        <v-icon small color="#668fcb">
                          fab fa-discord
                        </v-icon>
                        {{ user.user.discord_name }}

                        <!-- Presenteando -->
                        <span v-if="user.giving_to_user">
                          <br>
                          <v-tooltip bottom>
                            <template #activator="{ on }">
                              <v-icon v-on="on" color="#888" small>fas fa-gifts</v-icon>
                            </template>
                            <span>Presenteando</span>
                          </v-tooltip>
                          {{ user.giving_to_user.ingame_name }}
                        </span>
                      </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-icon class="hidden-sm-and-down">
                      <v-tooltip bottom>
                        <template #activator="{ on }">
                          <v-icon v-on="on" :color="user.receiving ? 'success accent-4' : 'error lighten-1'">
                            fas fa-gifts
                          </v-icon>
                        </template>
                        <span v-if="user.receiving">Recebendo Presente</span>
                        <span v-else>Não Recebendo Presente</span>
                      </v-tooltip>
                    </v-list-item-icon>
                  </v-list-item>

                  <v-divider v-if="index + 1 < users.length" :key="user.id" />
                </template>
              </v-list-item-group>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col xs="12" sm="8" md="8" lg="8" xl="8">
        <DiscordStatus />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

const DiscordStatus = () => import('@/components/discord/DiscordStatus.vue')
import api from '@/api'
import { DiscordApi } from '@/types'

@Component({
  components: { DiscordStatus }
})
export default class AmigoSecretoUsers extends Vue {
  private users: DiscordApi['SecretSantaUser'][] = []
  private apiError: boolean = false
  private apiErrorMessage: string = ''

  async mounted() {
    this.getUsers()
  }

  async getUsers() {
    try {
      this.users = await api.discord.secretSanta.users()
      this.apiError = false
    } catch (error) {
      this.apiError = true
      this.apiErrorMessage = error.response.data.detail
    }
  }
}
</script>
