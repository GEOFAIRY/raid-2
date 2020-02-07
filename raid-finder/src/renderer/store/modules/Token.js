const state = {
  isLoggedIn: false,
  token: null
}

const mutations = {
  LOGIN(state, token) {
    state.token = token
    state.isLoggedIn = true
  },
  LOGOUT(state) {
    state.token = null
    state.isLoggedIn = false
  },
  TEST(state) {
    state.token = 'test passed'
    state.isLoggedIn = true
  }
}

const actions = {
  LOGIN({commit}, token) {
    commit('LOGIN', token)
  },
  LOGOUT({commit}) {
    commit('LOGOUT')
  },
  TEST({commit}) {
    commit('TEST')
  }
}

export default {
  state,
  mutations,
  actions
}
