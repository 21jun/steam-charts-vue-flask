import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TopGameChart from '@/components/TopGameChart'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/TopGameChart',
      name: 'TopGameChart',
      component: TopGameChart 
    },
  ]
})
