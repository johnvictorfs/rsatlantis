<template xmlns:v-clipboard="">
  <v-container>
    <v-sheet class="pa-5" elevation="6">
      <h1 class="pb-3">Documentação da API</h1>

      <v-tabs v-model="tabs">

        <v-tab v-for="tab in tabItems" :key="tab.title" :href="'#tab-' + tab.title" ripple>
          {{ tab.title }}
        </v-tab>

        <v-tabs-items v-model="currentItem">
          <v-tab-item v-for="tab in tabItems" :value="'tab-' + tab.title" :key="tab.title">
            <v-card flat>
              <v-card-text>
                <ul>
                  <li v-for="endpoint in tab.endpoints" :key="endpoint.url" class="pb-4">
                    <p class="subheading grey--text">
                      {{ endpoint.url }}
                      <v-btn v-clipboard:copy="endpoint.url"
                             v-clipboard:error="copyError"
                             v-clipboard:success="copySuccess"
                             icon
                      >
                        <v-icon>fa-copy</v-icon>
                      </v-btn>
                    </p>
                    <ul>
                      <li v-for="method in endpoint.methods" :key="method.text" class="mb-2">
                        <strong>{{ method.method }}:</strong> {{ method.text }}
                        <p v-if="method.parameters !== undefined">
                          <strong>Parâmetros: </strong>
                          <code>{{ JSON.stringify(method.parameters) }}</code>
                        </p>
                        <p v-else-if="method.response !== undefined">
                          <strong>Resposta: </strong>
                          <code>{{ JSON.stringify(method.response) }}</code>
                        </p>
                      </li>
                    </ul>
                    <v-divider></v-divider>
                  </li>
                </ul>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items>

      </v-tabs>

    </v-sheet>
  </v-container>
</template>

<script>
  export default {
    name: "Api",
    data: () => ({
      tabs: null,
      currentItem: 'tab-Guias',
      tabItems: [
        {
          title: 'Guias',
          endpoints: [
            {
              url: process.env.VUE_APP_API_URL + '/api/guides/',
              methods: [
                {
                  method: 'GET',
                  text: 'Listar Guias',
                  response: [{
                    url: 'String',
                    author: 'String',
                    title: 'String',
                    slug: 'String',
                    category: 'String',
                    description: 'String',
                    content: 'String',
                    approved: 'Boolean',
                    date_posted: 'Date'
                  }],
                },
                {
                  method: 'POST',
                  text: 'Criar Guia',
                  parameters: {title: 'String', category: 'String', description: 'String', content: 'String'}
                }
              ],
            },
            {
              url: process.env.VUE_APP_API_URL + '/api/guides/<slug>/',
              methods: [
                {
                  method: 'GET',
                  text: 'Detalhes de Guia',
                  response: {
                    url: 'String',
                    author: 'String',
                    title: 'String',
                    slug: 'String',
                    category: 'String',
                    description: 'String',
                    content: 'String',
                    approved: 'Boolean',
                    date_posted: 'Date'
                  }
                },
                {
                  method: 'PUT/PATCH',
                  text: 'Atualizar Guia (Autor do Guia e Admin+)',
                  parameters: {title: 'String', category: 'String', description: 'String', content: 'String'}
                },
                {method: 'DELETE', text: 'Deletar Guia (Autor do Guia e Admin+)'},
              ]
            },
            {
              url: process.env.VUE_APP_API_URL + '/api/guides/<slug>/approve/',
              methods: [{method: 'POST', text: 'Aprovar Guia (Mod+)'}],
            },
          ]
        },
        {
          title: 'Usuários', endpoints: [
            {
              url: process.env.VUE_APP_API_URL + '/api/guides/',
              methods: [
                {method: 'GET', text: 'Listar Guias', response: {title: 'String'}},
                {
                  method: 'POST',
                  text: 'Criar Guia',
                  parameters: {title: 'String', category: 'String', description: 'String', content: 'String'}
                }
              ],
            },
            {
              url: process.env.VUE_APP_API_URL + '/api/guides/<slug>/approve/',
              methods: [
                {
                  method: 'POST',
                  text: 'Aprovar Guia (Mod+)'
                }
              ],
            },
          ]
        }
      ]
    }),
    methods: {
      copySuccess() {
        this.$toasted.global.success('URL Copiada com sucesso');
      },
      copyError() {
        this.$toasted.global.error('Erro ao tentar copiar URL');
      }
    }
  }
</script>