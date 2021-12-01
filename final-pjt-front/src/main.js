import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import VueMoment from 'vue-moment'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/css.css'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

Vue.use(VueMoment)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
