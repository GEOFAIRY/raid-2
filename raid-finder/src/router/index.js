import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import RaidSelector from '../views/RaidSelector.vue'
import GameSelector from '../views/GameSelector.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/raids',
    name: 'raid-selector',
    component: RaidSelector
  },
  {
    path: '/games/:raidId',
    name: 'game-selector',
    component: GameSelector
  }
]

const router = new VueRouter({
  routes
})

export default router
