<template>
    <div>
        <v-text-field
            v-model="t_tag"
            :counter="10"
            label="검색할 Tag를 입력하세요"
        ></v-text-field>
        <v-btn color="info" @click="get_tagedGame('FPS')">게임 검색</v-btn>
        <table id="firstTable">
            <thead>
                <tr>
                <th>NAME</th>

                </tr>
            </thead>
            <tbody>
                <tr v-for="comp in list" v-bind:key ='comp'>
                <td> <router-link :to="{ name: 'SingleGameInfo', params: { t_appid: comp[0]} }">{{comp[1]}}</router-link></td>
                </tr>
            </tbody>
        </table>

    </div>
    
</template>

<script>
import axios from 'axios'
import get_taged_game from '../modules/GetTagedGame'
export default {
  name: 'App',
  components: {
      
  },
  data () {
    return {
        t_tag : 'Action',
        list : [],
    }
  },

  methods: {
    get_tagedGame(tag){
        const baseURI = 'http://localhost:5000/db/searchTag/';

        axios.get(baseURI+tag).then((response)=>{

            console.log(get_taged_game(response.data['list']))

            this.list = get_taged_game(response.data['list'])
        })
    }
  }
}
</script>