import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'raid-selector',
      component: require('@/components/RaidSelector/RaidSelector').default
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
