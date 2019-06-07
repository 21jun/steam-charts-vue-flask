<template>
    <div>
        <button @click="get_maxPlayer(570)">@@@@@@@@@@@@@</button>
        <button @click="get_tagsInfo(570)">#############</button>
        <bars
        :data="this.max_player"
        :gradient="['#ffbe88', '#ff93df']"
        :barWidth="5"
        :growDuration="1">
        </bars>
        
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
        max_player:0,
        tags : []
    }
  },

  methods: {
    get_maxPlayer(appid){
        const baseURI = 'http://localhost:5000/db/maxPlayer/';

        axios.get(baseURI+appid).then((response)=>{

            console.log(get_max_player(response.data['player_count']))

            this.max_player = get_max_player(response.data['player_count'])
        })
    },
    get_tagsInfo(appid){
        const baseURI = 'http://localhost:5000/db/tags/';

        axios.get(baseURI+appid).then((response)=>{

            console.log(get_tags(response.data['tags']))

            this.tags = get_tags(response.data['tags'])
        })
    }
  }
}
</script>