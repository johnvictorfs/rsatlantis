<template>
  <v-container app>
    <br/>
    <ul>
      <v-flex v-for="guide in visibleGuides" :key="guide.slug" justify-center xs12 sm8 md4 offset-xs4>
        <Guide :guide="guide" :content="false" :details-button="true"></Guide>
        <br/>
        <br/>
      </v-flex>
      <v-layout justify-center>
        <v-pagination v-model="page" :length="pageLength" circle></v-pagination>
      </v-layout>
    </ul>
  </v-container>
</template>

<script>
  import Guide from '../../components/Guide'

  export default {
    name: "GuideList",
    components: {
      Guide
    },
    data: () => ({
      notFound: false,
      guides: [],
      page: 1,
      pageSize: 5
    }),
    created() {
      this.$store.dispatch('guideList', this.$route.params.slug).then(response => {
        for (const guide of response.data) {
          if (guide.category === 'pvm') {
            guide.category = 'PvM'
          } else if (guide.category === 'skilling') {
            guide.category = 'Habilidades'
          } else {
            guide.category = 'Outros'
          }

          this.$axios.get(guide.author).then(author => {
            guide.author = {
              name: author.data.username,
              isAdmin: author.data.is_staff,
              isSuperUser: author.data.is_superuser
            };
          }).catch(() => {
            guide.author = {
              name: 'N/A',
              isAdmin: false,
              isSuperUser: false
            };
          });
        }
        this.guides = response.data;
      }).catch(() => {
        this.notFound = true;
      })
    },
    computed: {
      visibleGuides() {
        return this.guides.slice(((this.page - 1) * this.pageSize), (this.page * this.pageSize));
      },
      pageLength() {
        return Math.ceil(this.guides.length / this.pageSize);
      }
    }
  }
</script>