<template>
  <div id='app'>
    <v-date-picker v-model="picker" :landscape=true ></v-date-picker>
    <v-btn color="info" @click="get_playerCount(t_date)">playerCount</v-btn>
    <GChart
      :settings="{packages: ['bar']}"    
      :data="players"
      :options="chartOptions"
      :createChart="(el, google) => new google.charts.Bar(el)"
      @ready="onChartReady"
    />
  </div>
</template>

<script>
import axios from 'axios'
import { GChart } from 'vue-google-charts'
import get_player_count from '../modules/GetPlayerCount'
import Datepicker from 'v-calendar';


export default {
  name: 'App',
  components: {
    GChart,
    Datepicker
  },
  data () {
    return {
      picker: new Date().toISOString().substr(0, 10),
      chartsLib: null, 
      players : [],
      t_date : '20190321',
      state : {
        date: new Date(2016, 9,  16)
      },
    }
  },
  created() {
    this.get_playerCount(this.t_date)
  },
  watch:  {
    picker: function (picker) {
      console.log(picker.replace(/-/gi,''))
      this.t_date = picker.replace(/-/gi,'')
    }
  },
  computed: {
    chartOptions () {
      if (!this.chartsLib) return null
      return this.chartsLib.charts.Bar.convertOptions({
        chart: {
          title: '오늘의 Top 20 게임',
          subtitle: ''
        },
        bars: 'horizontal', // Required for Material Bar Charts.
        hAxis: { format: 'decimal' },
        height: 800,
        colors: ['#1b9e77', '#d95f02', '#7570b3']
      })
    }
  },
  methods: {
    onChartReady (chart, google) {
      this.chartsLib = google
    },
    get_playerCount(date){
        const baseURI = 'http://localhost:5000/db/playerCount/';

        axios.get(baseURI+date).then((response)=>{
            //console.log(response)
            //this.chartData = get_app_list(response.data['applist'])
            console.log(get_player_count(response.data['player_count']))
            //console.log(this.chartData)
            this.players = get_player_count(response.data['player_count'])
        })
    }
  }
}
</script>
