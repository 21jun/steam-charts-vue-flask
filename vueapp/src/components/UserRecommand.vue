<template>
    <div>
        <v-text-field
            v-model="tag"
            :counter="10"
            label="Tag를 입력해주세요"
        ></v-text-field>
        <v-text-field
            v-model="tag2"
            :counter="10"
            label="Tag를 입력해주세요"
        ></v-text-field>
        <v-text-field
            v-model="tag3"
            :counter="10"
            label="Tag를 입력해주세요"
        ></v-text-field>
        <v-text-field
            v-model="min"
            :counter="10"
            label="최소 동접자수를 입력해주세요"
        ></v-text-field>
        <v-btn color="info" @click="get_recommandGame(tag, tag2, tag3,min)">추천 게임 불러오기</v-btn>
        
        <table id="firstTable">
            <thead>
                <tr>
                <th>name</th>
                <th>최고동접자수</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="game in recommand_games" v-bind:key ='game'>
                <td>{{game[1]}}</td>
                <td>{{game[2]}}</td>
                </tr>
            </tbody>
        </table>

    </div>
    
</template>


<script>
import axios from 'axios'
import get_recommand_game from '../modules/GetRecommandGame'

export default {
  name: 'App',
  components: {

  },
  data () {
    return {
        tag: 'Action',
        tag2: 'RTS',
        tag3: 'FPS',
        min: 0,
        recommand_games:[],
    }
  },
  created() {
      this.t_appid = this.$route.params.t_appid;
      //this.get_maxPlayer(this.t_appid)
      //this.get_tagsInfo(this.t_appid)
  },

  methods: {
    get_recommandGame(tag, tag2, tag3, min){
        const baseURI = 'http://localhost:5000/db/recommand/';
        console.log(baseURI + tag + '/' + tag2 + '/' + tag3 +'/' + min)
        axios.get(baseURI + tag + '/' + tag2 + '/' + tag3 +'/' + min).then((response)=>{

            this.recommand_games = []
            console.log(response)
            //console.log(baseURI + tag + '/' + min)
            //console.log(get_recommand_game(response.data['list']))
            this.recommand_games = get_recommand_game(response.data['list'])
        })
    },
  }
}
</script>