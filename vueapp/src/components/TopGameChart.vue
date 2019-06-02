<template>
  <div id='app'>
    <!-- 20190321 변수화 시키기 -->
  <button @click="get_playerCount('20190321')">playerCount</button>
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


export default {
  name: 'App',
  components: {
    GChart
  },
  data () {
    return {
      chartsLib: null, 
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        ['Year', 'Sales', 'Expenses', 'Profit'],
        ['2014', 1000, 400, 200],
        ['2015', 1170, 460, 250],
        ['2016', 660, 1120, 300],
        ['2017', 1030, 540, 350]
      ],
      players : []
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
