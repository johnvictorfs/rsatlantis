<template>
  <v-container>
    <v-row justify="center">
      <v-col xs="12" sm="8" md="8" lg="10" xl="4">
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
                <v-subheader
                  v-text="`${users.length} inscritos`"
                />
                <template v-for="(user, index) in users">
                  <v-list-item
                    @click.stop="event => openMenu(event, user.id)"
                    :key="user.id"
                  >
                    <v-list-item-avatar class="hidden-sm-and-down">
                      <v-img
                        :src="`https://secure.runescape.com/m=avatar-rs/${user.user.ingame_name.replace(/\s/g, '_')}/chat.png`"
                        :alt="`avatar${user.user.ingame_name}`"
                      />
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <!-- User Notes -->
                      <v-menu :close-on-content-click="false" :position-x="coordX" :position-y="coordY" v-model="menus[user.id].menu">
                        <UserAnnotation :user="user" @given="given => setGiven(user.id, given)" />
                      </v-menu>

                      <v-list-item-title>
                        <RunescapeIcon class="rs-icon" />
                        {{ user.user.ingame_name }}
                      </v-list-item-title>

                      <v-list-item-subtitle>
                        <v-icon small color="#668fcb">
                          fab fa-discord
                        </v-icon>
                        {{ user.user.discord_name }}
                      </v-list-item-subtitle>

                      <v-list-item-subtitle v-if="user.giving_to_user">
                        <!-- Presenteando -->
                        <v-tooltip bottom>
                          <template #activator="{ on }">
                            <v-icon v-on="on" color="#888" small>
                              fas fa-gifts
                            </v-icon>
                          </template>
                          <span>Presenteando</span>
                        </v-tooltip>
                        {{ user.giving_to_user.ingame_name }}
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

                    <v-list-item-icon>
                      <v-tooltip bottom>
                        <template #activator="{ on }">
                          <v-icon v-on="on" right :color="menus[user.id].given ? 'success accent-2' : 'error lighten-1'">
                            fas fa-check
                          </v-icon>
                        </template>

                        <span v-if="menus[user.id].given">Presente Entregue</span>
                        <span v-else>Presente Não-entregue</span>
                      </v-tooltip>
                    </v-list-item-icon>
                  </v-list-item>

                  <v-divider v-if="index + 1 < users.length" :key="index" />
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

const RunescapeIcon = () => import('@/icons/Runescape.vue')
const DiscordStatus = () => import('@/components/discord/DiscordStatus.vue')
const UserAnnotation = () => import('@/components/discord/UserAnnotation.vue')

import api from '@/api'
import { DiscordApi } from '@/types'

@Component({
  components: { DiscordStatus, RunescapeIcon, UserAnnotation }
})
export default class AmigoSecretoUsers extends Vue {
  private users: DiscordApi['SecretSantaUser'][] = []
  private menus: Record<number, Object> = {}

  private coordX: number = 0
  private coordY: number = 0

  private apiError: boolean = false
  private apiErrorMessage: string = ''

  async mounted(): Promise<void> {
    this.getUsers()
  }

  setGiven(id: number, given: boolean): void {
    /**
     * Marks an user as having given his Present already or not
     */
    this.$nextTick(() => this.$set(this.menus, id, { ...this.menus[id], given }))
  }

  openMenu(event: MouseEvent, id: number): void {
    /**
     * Open User Menu by ID and set Menu position the the current mouse pointer coords
     */
    event.preventDefault()

    this.$set(this.menus, id, { ...this.menus[id], menu: false })

    setTimeout(() => {
      this.coordX = event.clientX
      this.coordY = event.clientY

      // Open the Menu only on the next tick to prevent changing the coords
      // during its opening animation
      this.$nextTick(() => this.$set(this.menus, id, { ...this.menus[id], menu: true }))
    }, 100)
  }

  async getUsers(): Promise<void> {
    /**
     * Get data from registered Secret Santa Users
     */
    try {
      this.users = await api.discord.secretSanta.users()

      for (const user of this.users) {
        this.$set(this.menus, user.id, { menu: false, annotation: '', given: false })
      }

      this.apiError = false
    } catch (error) {
      this.apiError = true
      this.apiErrorMessage = error.response.data.detail
    }
  }
}
</script>

<style lang="scss">
$rs-icon-size: 19px;

.rs-icon {
  svg {
    &:hover {
      .background {
        transition: 0.3s;

        fill: #38738f !important;
      }
    }
  }
}
</style>
