<template>
  <v-container>
    <v-layout justify-center>
      <v-flex xs12 sm8 lg5 md5>
        <v-card dark>
          <v-toolbar color="red">
            <v-toolbar-title>
              <strong>
                <v-icon left>warning</v-icon>
                404 - Nada interessante acontece
              </strong>
            </v-toolbar-title>
          </v-toolbar>
          <v-layout justify-center class="text-xs-center">
            <v-container fluid grid-list-md>
              <h3 class="mb-2">Página não encontrada :(</h3>
              <v-btn color="light-blue" to="/" right>
                <v-icon left dark>fa-home</v-icon>
                Ínicio
              </v-btn>
            </v-container>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: "NotFound"
  }
</script>
