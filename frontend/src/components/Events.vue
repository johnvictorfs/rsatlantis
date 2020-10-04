<template>
  <v-card class="atl-round-card" raised>
    <v-toolbar dark color="#363636">
      <v-toolbar-title class="toolbar-title">
        <v-icon left size="32" color="#668fcb">
          fab fa-calendar
        </v-icon>
        Eventos
      </v-toolbar-title>

      <v-btn icon disabled class="ml-2">
        <v-icon height="18" width="18">
          fa-sync-alt
        </v-icon>
      </v-btn>

      <v-spacer />

      <v-btn icon disabled color="success" v-if="isAdmin">
        <v-icon>fas fa-plus-square</v-icon>
      </v-btn>
    </v-toolbar>

    <v-timeline dense>
      <v-timeline-item :color="getColor(evento)" v-for="evento in formattedEvents" :key="evento.id" :icon="getIcon(evento)">
        <v-card dark class="mr-4">
          <v-toolbar dark :color="getColor(evento)">
            <v-toolbar-title>
              {{ evento.title }}
            </v-toolbar-title>

            <v-card-subtitle>
              {{ formattedDate(evento.date) }}
            </v-card-subtitle>

            <v-spacer />

            <v-btn icon disabled v-if="isAdmin">
              <v-icon>fas fa-edit</v-icon>
            </v-btn>
          </v-toolbar>

          <v-img v-if="evento.image" height="120" :src="evento.image" />

          <v-chip v-if="evento.beneficiente" color="success" class="ma-3" small>
            <v-icon small left>
              fas fa-hand-holding-usd
            </v-icon>
            Beneficiente
          </v-chip>

          <v-card-text v-if="evento.description" v-html="urlify(evento.description)" />
        </v-card>
      </v-timeline-item>
    </v-timeline>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

import { formatDistance, format, isAfter } from 'date-fns'
import { ptBR } from 'date-fns/locale'

import { ClanEvent } from '@/types'
import mockEventos from '@/mocks/events.json'

@Component({})
export default class Events extends Vue {
  eventos: ClanEvent[] = mockEventos

  get formattedEvents() {
    const now = new Date()

    // @ts-ignore  
    return this.eventos.sort((a, b) => new Date(a.date) - new Date(b.date)).filter(evento => {
      const eventoDate = new Date(evento.date)

      return !isAfter(now, eventoDate)
    })
  }

  get isAdmin() {
    return this.$store.getters.isAdmin
  }

  urlify(text: string): string {
    const urlRegex = /(https?:\/\/[^\s]+)/g

    return text.replace(urlRegex, url => '<a href="' + url + '">' + url + '</a>')
  }

  formattedDate(dateStr: string) {
    const date = new Date(dateStr)

    const distance = formatDistance(date, new Date(), { addSuffix: true, locale: ptBR })
    const dateFormatted = format(date, 'dd/MM - HH:mm', { locale: ptBR })

    return `${dateFormatted}, ${distance}`
  }

  getIcon(evento: ClanEvent) {
    switch (evento.type) {
      case 'in-game':
        return '$runescape'
      case 'off-game':
        return 'fas fa-table-tennis'
    }

    return '$runescape'
  }

  getColor(evento: ClanEvent): string {
    switch(evento.type) {
      case 'in-game':
        return 'primary darken-3'
      case 'off-game':
        return 'teal darken-3'
    }

    return 'primary darken-3'
  }
}
</script>

<style lang="scss">
.toolbar-title {
  font-family: Rubik, "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI",
  Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial,
  sans-serif;

  font-size: 23px;
}
</style>