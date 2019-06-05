import api from '.';

type credentials = {
  username: string;
  password: string;
  email: string;
  ingame_name: string;
};

export default {
  login(username: string, password: string) {
    return api.post('/api/auth/login/', { username, password });
  },
  logout() {
    return api.post('/api/auth/logout/', {});
  },
  createAccount(credentials: credentials) {
    return api.post('/api/users/', {
      username: credentials.username,
      password: credentials.password,
      email: credentials.email,
      ingame_name: credentials.ingame_name
    });
  },
  changeAccountPassword(password1: string, password2: string) {
    return api.post('/api/auth/password/change/', { password1, password2 });
  },
  sendAccountPasswordResetEmail(email: string) {
    return api.post('/api/auth/password/reset/', { email });
  },
  resetAccountPassword(uid: string, token: string, new_password1: string, new_password2: string) {
    return api.post('/api/auth/password/reset/confirm/', {
      uid,
      token,
      new_password1,
      new_password2
    });
  },
  getAccountDetails() {
    return api.get('/api/users/current/');
  },
  updateAccountDetails(data: credentials) {
    return api.patch('/api/auth/user/', data);
  },
  verifyAccountEmail(key: string) {
    return api.post('/api/registration/verify-email/', { key });
  }
};
