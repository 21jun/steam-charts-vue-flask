// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Bars from 'vuebars'
import VueGoogleCharts from 'vue-google-charts'
import Vuetify from 'vuetify'
import '../node_modules/vuetify/dist/vuetify.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.config.productionTip = false
Vue.use(Bars)
Vue.use(VueGoogleCharts)
Vue.use(Vuetify)
Vue.use(router)

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
})