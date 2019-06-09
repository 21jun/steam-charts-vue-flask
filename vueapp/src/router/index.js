import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TopGameChart from '@/components/TopGameChart'
import DetailPage from '@/components/DetailPage'
import SingleGameInfo from '@/components/SingleGameInfo'
import TagLists from '@/components/TagLists'
import UserRecommand from '@/components/UserRecommand'
import ReviewPage from '@/components/ReviewPage'
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
    {
      path: '/SingleGameInfo/:t_appid',
      name: 'SingleGameInfo',
      component: SingleGameInfo,
    },
    {
      path: '/TagLists',
      name: 'TagLists',
      component: TagLists 
    },
    {
      path: '/UserRecommand',
      name: 'UserRecommand',
      component: UserRecommand 
    },
    {
      path: '/ReviewPage',
      name: 'ReviewPage',
      component: ReviewPage 
    },
  ]
})
