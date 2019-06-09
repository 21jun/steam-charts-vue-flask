<template>
    <div>
        <table id="firstTable">
            <thead>
                <tr>
                <th>Tag</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="tag in tags" v-bind:key ='tag'>
                <td>{{tag[0]}}</td>
                </tr>
            </tbody>
        </table>

    </div>
    
</template>


<script>
import axios from 'axios'

export default {
  name: 'App',
  components: {

  },
  data () {
    return {
        tags:[],
    }
  },
  created() {
      this.get_allTag()
  },

  methods: {
    get_allTag(){
        const baseURI = 'http://localhost:5000/db/alltag';

        axios.get(baseURI).then((response)=>{
            this.tags = response.data['list']
        })
    }
  }
}
</script>