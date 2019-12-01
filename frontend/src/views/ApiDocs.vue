<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" lg="8" md="10" sm="12">
        <v-card class="api-card mt-2" elevation="6">
          <v-toolbar class="text-center" color="#353434">
            <v-spacer/>
            <v-toolbar-title>
              <h2 style="font-family: Rubik;">Documentação da API</h2>
            </v-toolbar-title>
            <v-spacer/>
          </v-toolbar>

          <v-tabs center-active v-model="tab" color="light-blue" background-color="deep-gray accent-4">
            <v-tabs-slider/>
            <v-tab href="#guides-api" ripple @click="updateBaseUrls">Guias</v-tab>
            <v-tab href="#users-api" ripple @click="updateBaseUrls">Usuários</v-tab>

            <v-tab-item value="guides-api">
              <div class="markdown-render">
                <Guide />
              </div>
            </v-tab-item>

            <v-tab-item value="users-api">
              <div class="markdown-render">
                <Users />
              </div>
            </v-tab-item>
          </v-tabs>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

// @ts-ignore
import Guide from '@/assets/docs/api/guides.md'

// @ts-ignore
import Users from '@/assets/docs/api/users.md'

@Component({ components: { Guide, Users } })
export default class ApiDocs extends Vue {
  tab = null;

  mounted() {
    this.updateBaseUrls()
  }

  private updateBaseUrls() {
    /**
     * Replace all mentions of '{base_url}' in the markdown HTML to the
     * actual API's base url
     */
    setTimeout(() => {
      const apiElements = document.getElementsByClassName('markdown-render')

      for (let i = 0; i < apiElements.length; ++i) {
        apiElements[i].innerHTML = apiElements[i].innerHTML.replace(/{base_url}/g, process.env.VUE_APP_API_URL || '')
        apiElements[i].innerHTML = apiElements[i].innerHTML.replace(/✔️/g, '<i class="v-icon notranslate fa fa-check theme--dark"></i>')
        apiElements[i].innerHTML = apiElements[i].innerHTML.replace(/❌/g, '<i class="v-icon notranslate fa fa-times theme--dark"></i>')
      }
    }, 1000)
  }
}
</script>

<style lang="scss">
@import '@/assets/css/markdown.scss';

.api-card {
  border-radius: 25px !important;
}
</style>
