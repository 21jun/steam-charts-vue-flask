<template>
  <div class="hello">
    <H2>출력창</H2>
    <h1>{{this.msg}}</h1>
    <button @click="callTest('firstAttribute')">FIRST</button>
    <br>
    <br>
    <button @click="callTest('secondAttribute')">SECOND</button>
    <br>
    <br>
    <div v-for="board in my_boards" :key=board>
      <h2>{{board[0]}}</h2>
      <h4>{{board[1]}}</h4>
    </div>
    <button @click="getBoardList">BOARD</button>
    <button @click="get_applist">applist</button>


    <GChart
        type="ColumnChart"
        :settings="{packages: ['bar']}"  
        :data="chartData"
        :options="chartOptions"
    />

    <bars
      :data="[1, 2, 5, 9, 5, 10, 3, 5, 8, 12, 1, 8, 2, 9, 10, 2, 9, 4, 5, 6, 7, 3, 2, 3, 5]"
      :gradient="['#ffbe88', '#ff93df']"
      :barWidth="5"
      :growDuration="1">
    </bars>

  </div>
</template>

<script>
import axios from 'axios'
import get_app_list from '../modules/GetApplist'

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: "0",
      my_boards:[],
      players : [],
      
      chartData: [
        ['Name', 'appid'],
        ['2014', 1000],
        ['2015', 1170],
        ['2016', 660],
        ['2017', 1030]
      ],
      chartOptions: {
        chart: {
          title: "Today's top 10 games",
          subtitle: '',
        }
      }
    }
  },
  methods:{
    callTest(pick){
      console.log("clicked")
      axios({
        method: "get",
        url: "/test"
      }).then((response)=>{
        console.log(response)
        this.msg = response.data[pick]
      })
    },
    getBoardList(){
      console.log("clicked")
      axios({
        method: "get",
        url: "/board/list"
      }).then((response)=>{
        console.log(response)
        this.my_boards = response.data['boards']
      })
    },

    get_applist(){
      axios({
        method: "get",
        url: "/db/applist"
      }).then((response)=>{
        //console.log(response)
        //this.chartData = get_app_list(response.data['applist'])
        console.log(get_app_list(response.data['applist']))
        console.log(this.chartData)

        this.chartData = get_app_list(response.data['applist'])

      })
    },
  }
}
</script>