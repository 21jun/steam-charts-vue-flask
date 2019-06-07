<template>
  <div>
    <input-form></input-form>
    <h1>{{name}}</h1>
    <v-btn small color="primary" @click="get_applist()">검색</v-btn>
    <table id="firstTable">
      <thead>
        <tr>
          <th>Name</th>
          <th>AppID</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="app in list" v-bind:key ='app'>
          <td>{{app[0]}}</td>
          <td>{{app[1]}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import InputForm from './InputForm'
import get_app_list from '../modules/GetApplist'
import ApplistTable from './ApplistTable'
export default {
  name: 'App',
  components: {
    InputForm
  },
  data () {
    return {
      name : '초기값',
      list : [],
    }
  },
  created() {
    this.$EventBus.$on('game-name-pass', this.setGameName)
  },

  methods: {
    setGameName : function(text)
    {
      this.name = text
    },
    get_applist(){
        const baseURI = 'http://localhost:5000/db/applist/';

        axios.get(baseURI+this.name).then((response)=>{
            console.log(get_app_list(response.data['list']))
            this.list = get_app_list(response.data['list'])
        })
    }
  }
}
</script>
