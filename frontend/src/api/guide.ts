import api from '.';

export default {
  publishGuide(post: any) {
    if (post.category === 'PvM') {
      post.category = 'pvm';
    } else if (post.category === 'Habilidades') {
      post.category = 'skilling';
    } else {
      post.category = 'other';
    }
    return api.post('/api/guides/', post);
  },
  guideList() {
    return api.get('/api/guides/');
  },
  guideDetails(slug: string) {
    return api.get(`/api/guides/${slug}/`);
  }
};
