<template>
    <div>
        <v-text-field
            v-model="appid"
            :counter="10"
            label="검색할 게임의 ID를 입력하세요"
        ></v-text-field>
        <v-btn color="info" @click="get_reviewInfo(appid)">추천 게임 불러오기</v-btn>
        <h2>최근 게임 평점 추이 (0~100%)</h2>
        <trend
            :data=trend_data_recent_p
            :gradient="['#6fa8dc', '#42b983', '#2c3e50']"
            auto-draw
            smooth
        >
        </trend>
        <h2>전체 기간 게임 평점 추이 (0~100%)</h2>
        <trend
            :data=trend_data_all_p
            :gradient="['#ff0000', '#dc143c', '#ff7f00']"
            auto-draw
            smooth
        >
        </trend>
        <h2>리뷰 갯수</h2>
        <GChart
            type="ColumnChart"
            :data="trend_data_count"
            :options="chartOptions"
        />
    </div>
    
</template>


<script>
import axios from 'axios'
import get_review_info from '../modules/GetReviewInfo'

export default {
  name: 'App',
  components: {

  },
  data () {
    return{
        trend_data_recent_p:[],
        trend_data_all_p:[],
        trend_data_count:[],
        appid: 570,
        reviews:[],
        chartOptions: {
            chart: {
            title: 'Company Performance',
            subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            }
        },
    }
  },
  created() {
      this.t_appid = this.$route.params.t_appid;
      //this.get_maxPlayer(this.t_appid)
      //this.get_tagsInfo(this.t_appid)
  },

  methods: {
    set_recentTrendData(raw){
        this.trend_data_recent_p = []
        raw.forEach(element => {
            this.trend_data_recent_p.push(element[3])
        });
    },
    set_allTrendData(raw){
        this.trend_data_all_p = []
        raw.forEach(element => {
            this.trend_data_all_p.push(element[5])
        });
    },
    set_countTrendData(raw){
        this.trend_data_count = []
        this.trend_data_count.push(['Date','Count'])
        
        raw.forEach(element => {
            this.trend_data_count.push([element[6], element[4]])
        });
        console.log(this.trend_data_count)
    },
    get_reviewInfo(appid){
        const baseURI = 'http://localhost:5000/db/review/';
        axios.get(baseURI + appid).then((response)=>{
            this.reviews = get_review_info(response.data['list'])
        })

        this.set_recentTrendData(this.reviews)
        this.set_allTrendData(this.reviews)
        this.set_countTrendData(this.reviews)
    },
  }
}
</script>