<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-toolbar color="error">
            <v-icon left>
              fas fa-exclamation-triangle
            </v-icon>
            <strong>Nada interessante acontece.</strong>
          </v-toolbar>

          <v-card-text class="text-center">
            <h3 class="mb-4">
              Página não encontrada :(
            </h3>
            <v-btn color="light-blue" to="/" right>
              <v-icon left>
                fa-home
              </v-icon>
              Ínicio
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

@Component({})
export default class NotFound extends Vue {}
</script>
