import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.http = Vue.prototype.$http = axios

Vue.mixin({
  data: function() {
    return {
      serverAddress: 'http://127.0.0.1:5000/'
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
