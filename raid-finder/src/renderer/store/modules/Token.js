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
  }
}

const actions = {
  LOGIN({commit, token}) {
    commit('LOGIN', token)
  }
}

export default {
  state,
  mutations,
  actions
}
