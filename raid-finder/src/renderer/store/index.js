import Vue from 'vue'
import Vuex from 'vuex'

import { createPersistedState, createSharedMutations } from 'vuex-electron'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
    createSharedMutations()
  ],
  strict: process.env.NODE_ENV !== 'production',
  state: {
    isLoggedIn: false,
    token: null
  },
  mutations: {
    login(state, token) {
      state.token = token
      state.isLoggedIn = true
    },
    logout(state) {
      state.token = null
      state.isLoggedIn = false
    }
  },
  actions: {
    login(context, token) {
      context.commit('login', token)
    }
  }
})
