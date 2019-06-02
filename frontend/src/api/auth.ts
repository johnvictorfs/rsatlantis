import Vue from 'vue';

type credentials = {
  username: string;
  password: string;
  email: string;
  ingame_name: string;
};

export default {
  login(username: string, password: string) {
    return Vue.axios.post('/api/auth/login/', { username, password });
  },
  logout() {
    return Vue.axios.post('/api/auth/logout/', {});
  },
  createAccount(credentials: credentials) {
    return Vue.axios.post('/api/users/', {
      username: credentials.username,
      password: credentials.password,
      email: credentials.email,
      ingame_name: credentials.ingame_name
    });
  },
  changeAccountPassword(password1: string, password2: string) {
    return Vue.axios.post('/api/auth/password/change/', { password1, password2 });
  },
  sendAccountPasswordResetEmail(email: string) {
    return Vue.axios.post('/api/auth/password/reset/', { email });
  },
  resetAccountPassword(uid: string, token: string, new_password1: string, new_password2: string) {
    return Vue.axios.post('/api/auth/password/reset/confirm/', {
      uid,
      token,
      new_password1,
      new_password2
    });
  },
  getAccountDetails() {
    return Vue.axios.get('/api/users/current/');
  },
  updateAccountDetails(data: credentials) {
    return Vue.axios.patch('/api/auth/user/', data);
  },
  verifyAccountEmail(key: string) {
    return Vue.axios.post('/api/registration/verify-email/', { key });
  }
};
