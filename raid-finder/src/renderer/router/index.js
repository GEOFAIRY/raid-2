import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: require('@/components/Login/Login').default
    },
    {
      path: '/raids',
      name: 'raid-selector',
      component: require('@/components/RaidSelector/RaidSelector').default
    },
    {
      path: '/games/:raidId',
      name: 'game-selector',
      component: require('@/components/GameSelector/GameSelector').default
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
