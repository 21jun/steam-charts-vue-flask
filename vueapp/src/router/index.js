import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TopGameChart from '@/components/TopGameChart'
import DetailPage from '@/components/DetailPage'
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
    {
      path: '/DetailPage',
      name: 'DetailPage',
      component: DetailPage 
    },
  ]
})
