const SERVER_URL = process.VUE_APP_SERVER_URL
export default {
  URL: SERVER_URL,
  ROUTES: {
    signup: '/accounts/signup/',
    login: '/accounts/api-token-auth/',
  }
}