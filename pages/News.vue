<template>
<v-layout
  justify-center
  align-center
  >
  <v-flex>
    <div class="titeltrend text-xs-center"> <v-icon color="orange darken 2">trending_up</v-icon> TRENDING </div>
    <br>
    <v-card v-for="article in trending" :key="article.title" class="trend mb-4" >
      <v-img
          :src="article.urlToImage"
          aspect-ratio="2.75"
        ></v-img>

        <v-card-title primary-title >
          <div>
            <h5 class="title mb-0"> {{ article.title }} </h5>
            <br>
            <small class="author right mr-2"> {{ article.author }} </small>
            <br>
            <hr class="mr-2 ml-2">
            <br>
            <div class="justify-content-center align-center"> 
                <small> {{ article.content }} </small>
            </div>
          </div>
        </v-card-title>
    </v-card>
    <br>
    <BottomNavbar />
  </v-flex>
</v-layout>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Raleway');
    .title {
        font-size: 13px !important;
        font-family: Raleway !important;
        text-align: center !important;
        font-weight: 600 !important;
    }
    .trend {
        border-radius: 8px !important;
        box-shadow: 5px black !important;
    }
    .author {
        font-size: 8px;
    }
    .titeltrend {
        font-weight: 900 !important;
        font-family: Raleway !important;
        font-size: 17px !important;
    }
</style>


<script>
import BottomNavbar from '~/components/BottomNavbar.vue'
// import axios from 'axios'

  export default {
    components: {
      BottomNavbar
    },
    // async asyncData () {
    //   const {data} = await axios.get('https://newsapi.org/v2/everything?q=apple&from=2019-04-24&to=2019-04-24&sortBy=popularity&apiKey=318272093cec43d480e5dbe696027306')
    //   return {articles:data.articles}
    // }
    async asyncData({ $axios }) {
        const ip = await $axios.$get('https://newsapi.org/v2/everything?q=apple&from=2019-04-24&to=2019-04-24&sortBy=popularity&apiKey=318272093cec43d480e5dbe696027306')
        return { trending: ip.articles }
}
  }
</script>
