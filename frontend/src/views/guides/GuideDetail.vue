<template>
  <v-container>
    <br/>
    <v-flex justify-center xs12 sm8 md4 offset-xs4>
      <v-alert :value="notFound" type="error">
        Guia '{{ slug }}' não encontrado
      </v-alert>
      <Guide v-if="showGuide" :guide="guide" :content="true" :details-button="false"></Guide>
    </v-flex>
  </v-container>
</template>

<script>
const Guide = () => import('../../components/Guide');

export default {
  name: 'GuideDetail',
  props: {
    slug: String
  },
  components: {
    Guide
  },
  data: () => ({
    notFound: false,
    guide: {},
    showGuide: false
  }),
  created() {
    this.$store.dispatch('guideDetails', this.slug).then((response) => {
      if (response.category === 'pvm') {
        response.data.category = 'PvM';
      } else if (response.category === 'skilling') {
        response.data.category = 'Habilidades';
      } else {
        response.data.category = 'Outros';
      }
      this.$axios.get(response.data.author).then((author) => {
        response.data.author = {
          name: author.data.username,
          isAdmin: author.data.is_staff,
          isSuperUser: author.data.is_superuser
        };
        this.guide = response.data;
        this.showGuide = true;
      }).catch(() => {
        response.data.author = {
          name: 'N/A',
          isAdmin: false,
          isSuperUser: false
        };
        this.guide = response.data;
        this.showGuide = true;
      });
    }).catch(() => {
      this.notFound = true;
    });
  }
};
</script>

<style scoped>

</style>
