import Vue from 'vue';

export default {
  publishGuide(post) {
    if (post.category === 'PvM') {
      post.category = 'pvm';
    } else if (post.category === 'Habilidades') {
      post.category = 'skilling';
    } else {
      post.category = 'other';
    }
    return Vue.axios.post('/api/guides/', post);
  },
  guideList() {
    return Vue.axios.get('/api/guides/');
  },
  guideDetails(slug) {
    return Vue.axios.get(`/api/guides/${slug}/`);
  }
};
