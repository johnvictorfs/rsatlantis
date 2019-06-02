<template>
  <v-card class="elevation-12">

    <v-toolbar dark color="green">
      <v-toolbar-title>Criar um Novo Guia</v-toolbar-title>
    </v-toolbar>

    <v-container fluid grid-list-md>

      <v-card-text>
        <v-form ref="form" v-model="valid">
          <v-text-field box required label="Título" v-model="guide.title" :counter="25" maxlength="25"></v-text-field>

          <v-text-field box required label="Descrição" v-model="guide.description" :counter="40"
                        maxlength="40"></v-text-field>

          <v-select box required label="Categoria" :items="categories"></v-select>
        </v-form>

        <tinymce id="d1" v-model="guide.content" :other_options="tinymce" :plugins="tinymce.plugins"></tinymce>

        <v-divider class="my-2"></v-divider>

      </v-card-text>

      <v-btn outline round block color="success" :disabled="!valid" @click="submit">
        Enviar
        <v-icon right>check</v-icon>
      </v-btn>

    </v-container>
  </v-card>
</template>

<script>
import { formatError } from '../../helpers/errors';

const Centered = () => import('../../components/Centered');

export default {
  name: 'NewGuide',
  components: { Centered },
  data: () => ({
    valid: true,
    tinymce: {
      language_url: 'https://cdn.jsdelivr.net/npm/tinymce-i18n@18.12.25/langs/pt_BR.js',
      height: 500,
      plugins: [
        'advlist autolink lists link image charmap preview hr anchor pagebreak',
        'searchreplace visualblocks visualchars code',
        'insertdatetime media nonbreaking save table contextmenu directionality',
        'template paste textcolor colorpicker textpattern imagetools toc emoticons hr codesample',
      ],
    },
    categories: ['PvM', 'Habilidades', 'Outros'],
    guide: {
      title: '',
      description: '',
      category: '',
      content: '',
    },
  }),
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        this.$store.dispatch('publishGuide', this.guide).then(() => {
          this.$toasted.global.success('Seu guia foi publicado com sucesso! Ele estará disponível quando aprovado');
          this.$router.push({ name: 'home' });
        }).catch((error) => {
          this.$toasted.global.error(formatError(error));
        });
      }
    },
  },
};
</script>

<style scoped>

</style>
