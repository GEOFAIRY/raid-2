import Vue from 'vue'
import axios from 'axios'

import App from './App'
import router from './router'
import store from './store'

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = axios

Vue.config.productionTip = false

Vue.mixin({
  data: function() {
    return {
      serverAddress: 'http://127.0.0.1:5000/',
      token: null
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  store: store,
  render: (h) => h(App)
})
