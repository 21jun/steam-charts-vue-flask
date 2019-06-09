<template>
    <div>
        <v-text-field
            v-model="t_appid"
            :counter="10"
            label="게임의 id를 입력하세요"
        ></v-text-field>
        <v-btn color="info" @click="get_maxPlayer(t_appid)">사용자수 통계</v-btn>
        <v-btn color="info" @click="get_tagsInfo(t_appid)">게임 Tag 불러오기</v-btn>

        <H1>{{name}}</H1>
        <h2>개발사  : {{developer}}</h2>
        <h2>퍼블리셔: {{publisher}}</h2>
        <GChart
            type="ColumnChart"
            :data="max_player"
            :options="chartOptions"
        />
        
        <table id="firstTable">
            <thead>
                <tr>
                <th>Tag</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="tag in tags" v-bind:key ='tag'>
                <td>{{tag}}</td>
                </tr>
            </tbody>
        </table>

    </div>
    
</template>


<script>
import axios from 'axios'
import get_max_player from '../modules/GetMaxPlayer'
import get_tags from '../modules/GetTags'

export default {
  name: 'App',
  components: {

  },
  data () {
    return {
        max_player:[1,2,3,4,5,6,7,8,10],
        tags : [],
        developer:'',
        publisher:'',
        release_date:'',
        t_appid : 570,
        name : '',
        chartOptions: {
            chart: {
            title: 'Company Performance',
            subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            }
        }
    }
  },
  created() {
      this.t_appid = this.$route.params.t_appid;
      this.get_maxPlayer(this.t_appid)
      this.get_tagsInfo(this.t_appid)
  },

  methods: {

    get_gameInfo(appid){
        const baseURI = 'http://localhost:5000/db/info/';

        axios.get(baseURI+appid).then((response)=>{
            //console.log(response.data['name'])
            this.developer = response.data['info'][0][0]
            this.publisher = response.data['info'][0][1]
            this.release_date = response.data['info'][0][2]
        })
    },
    
    get_gameName(appid){
        const baseURI = 'http://localhost:5000/db/name/';

        axios.get(baseURI+appid).then((response)=>{
            //console.log(response.data['name'])
            this.name = response.data['name'][0][0]
        })
    },

    get_maxPlayer(appid){

        this.get_gameName(appid);
        this.get_gameInfo(appid);

        const baseURI = 'http://localhost:5000/db/maxPlayer/';

        axios.get(baseURI+appid).then((response)=>{

            //console.log(get_max_player(response.data['player_count']))

            this.max_player = get_max_player(response.data['player_count'])
        })
        console.log(this.max_player)
    },

    get_tagsInfo(appid){
        const baseURI = 'http://localhost:5000/db/tags/';

        axios.get(baseURI+appid).then((response)=>{

            //console.log(get_tags(response.data['tags']))

            this.tags = get_tags(response.data['tags'])
        })
    }
  }
}
</script>