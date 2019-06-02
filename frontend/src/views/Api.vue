<template xmlns:v-clipboard="">
  <v-sheet class="pa-5" elevation="6" fluid>
    <h1 class="pb-3">Documentação da API</h1>

    <v-tabs v-model="tabs">
      <v-tab
        v-for="tab in tabItems"
        :key="tab.title"
        :href="'#tab-' + tab.title"
        ripple
      >{{ tab.title }}</v-tab>

      <v-tabs-items v-model="currentItem">
        <v-tab-item v-for="tab in tabItems" :value="'tab-' + tab.title" :key="tab.title">
          <v-list two-line>
            <v-list-group
              v-for="endpoint in tab.endpoints"
              :key="endpoint.url"
              v-model="endpoint.active"
              no-action
            >
              <v-list-tile slot="activator">
                <v-tooltip bottom>
                  <v-btn
                    icon
                    slot="activator"
                    v-clipboard:copy="fullUrl(endpoint.url)"
                    v-clipb
                    oard:error="copyError"
                    v-clipboard:success="copySuccess"
                  >
                    <v-icon>fa-copy</v-icon>
                  </v-btn>
                  <span>Copiar URL</span>
                </v-tooltip>
                <v-list-tile-content>
                  <v-list-tile-title class="body-1">{{ endpoint.url }}</v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>

              <v-list-tile v-for="method in endpoint.methods" :key="method.text">
                <CodeDialog
                  v-if="method.parameters !== undefined"
                  title="Parâmetros"
                  :text="JSON.stringify(method.parameters, null, 2)"
                  activator-icon="info"
                ></CodeDialog>

                <CodeDialog
                  v-else-if="method.response !== undefined"
                  title="Resposta"
                  :text="JSON.stringify(method.response, null, 2)"
                  activator-icon="info"
                ></CodeDialog>

                <v-list-tile-content class="body-1">
                  <v-list-tile-title>
                    <strong>{{ method.method }}:</strong>

                    {{ method.text }}
                  </v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-list-group>
          </v-list>
        </v-tab-item>
      </v-tabs-items>
    </v-tabs>
  </v-sheet>
</template>

<script>
const CodeDialog = () => import("../components/CodeDialog");

export default {
  name: "Api",
  components: {
    CodeDialog
  },
  data: () => ({
    tabs: null,
    currentItem: "tab-Guias",
    tabItems: [
      {
        title: "Guias",
        endpoints: [
          {
            active: false,
            url: "/api/guides/",
            methods: [
              {
                method: "GET",
                text: "Listar Guias",
                response: [
                  {
                    url: "URL",
                    author: "URL",
                    title: "String",
                    slug: "String",
                    category: "String",
                    description: "String",
                    content: "String",
                    approved: "Boolean",
                    date_posted: "Date"
                  }
                ]
              },
              {
                method: "POST",
                text: "Criar Guia",
                parameters: {
                  title: "String",
                  category: "String",
                  description: "String",
                  content: "String"
                }
              }
            ]
          },
          {
            active: false,
            url: "/api/guides/<slug:str>/",
            methods: [
              {
                method: "GET",
                text: "Detalhes de Guia",
                response: {
                  url: "URL",
                  author: "URL",
                  title: "String",
                  slug: "String",
                  category: "String",
                  description: "String",
                  content: "String",
                  approved: "Boolean",
                  date_posted: "Date"
                }
              },
              {
                method: "PUT/PATCH",
                text: "Atualizar Guia (Autor do Guia e Admin+)",
                parameters: {
                  title: "String",
                  category: "String",
                  description: "String",
                  content: "String"
                }
              },
              {
                method: "DELETE",
                text: "Deletar Guia (Autor do Guia e Admin+)"
              }
            ]
          },
          {
            active: false,
            url: "/api/guides/<slug:str>/approve/",
            methods: [{ method: "POST", text: "Aprovar Guia (Mod+)" }]
          }
        ]
      },
      {
        title: "Usuários",
        endpoints: [
          {
            active: false,
            url: "/api/users/",
            methods: [
              {
                method: "GET",
                text: "Listar Usuários (Mod+)",
                response: [
                  {
                    url: "URL",
                    guides: "URL",
                    ingame_name: "String",
                    username: "String",
                    email: "String",
                    groups: "Array",
                    is_staff: "Boolean",
                    is_superuser: "Boolean"
                  }
                ]
              },
              {
                method: "POST",
                text: "Criar Usuário",
                parameters: {
                  username: "String",
                  password: "String",
                  email: "String",
                  ingame_name: "String"
                }
              }
            ]
          },
          {
            active: false,
            url: "/api/users/<id:int>",
            methods: [
              {
                method: "GET",
                text: "Detalhes de Usuário",
                response: {
                  url: "URL",
                  guides: "URL",
                  ingame_name: "String",
                  username: "String",
                  email: "String",
                  groups: "Array",
                  is_staff: "Boolean",
                  is_superuser: "Boolean"
                }
              },
              {
                method: "PUT/PATCH",
                text: "Atualizar Usuário (Próprio Usuário e Admin+)",
                parameters: {
                  username: "String",
                  password: "String",
                  email: "String",
                  ingame_name: "String"
                }
              },
              { method: "DELETE", text: "Deletar Usuário (Admin+)" }
            ]
          }
        ]
      },
      {
        title: "Jogadores",
        endpoints: [
          {
            active: false,
            url: "/api/players/",
            methods: [
              {
                method: "GET",
                text: "Listar Jogadores do Clã",
                response: [
                  {
                    url: "URL",
                    name: "String",
                    exp: "Number",
                    rank: "String"
                  }
                ]
              }
            ]
          },
          {
            active: false,
            url: "/api/players/<name:str>",
            methods: [
              {
                method: "GET",
                text: "Detalhes de Jogador do Clã",
                response: {
                  url: "URL",
                  name: "String",
                  exp: "Number",
                  rank: "String"
                }
              }
            ]
          }
        ]
      }
    ]
  }),
  methods: {
    copySuccess() {
      this.$toasted.global.success("URL Copiada com sucesso");
    },
    copyError() {
      this.$toasted.global.error("Erro ao tentar copiar URL");
    },
    fullUrl(url) {
      return process.env.VUE_APP_API_URL + url;
    }
  }
};
</script>
