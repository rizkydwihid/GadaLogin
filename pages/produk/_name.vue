<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-img
          :src= "require('assets/img/shopping.png')" 
          aspect-ratio="1.5"
        />

        <v-card-title primary-title>
          <div> 
            <h3 class="headline mb-0"> - {{ post.name }} - </h3>
          </div>
          <hr class="my-3">
        </v-card-title>
        <div class="text-xs-center"> <em>{{ post.content }}</em> </div>
        <br>
        <hr class="mr-3 ml-3">
        <br>
        <div class="text-xs-center">
        <span> Produk lainnya: </span>
          <span v-for="related in relatedPosts" :key="related.name">
            <br>
            <a :href="`/produk/${related.name}`">{{ related.name }}</a>
          </span>
        </div>
        <br>
      </v-card>
      <BottomNavbar />
    </v-flex>
  </v-layout>
</template>

<style scoped>
  .headline {
    text-align: center !important;
  }
</style>


<script>
import BottomNavbar from '~/components/BottomNavbar.vue'
// import Vuex from 'vuex'

export default {
  data () {
    return {
      name: this.$route.params.nama
    }
  },
  computed: {
    post() {
      return this.$store.state.produk.all.find(post => post.nama === this.name)
    },
    relatedPosts () {
      return this.$store.state.produk.all.filter(post => post.name !== this.name)
    }
  },
  components: {
    BottomNavbar
  }
}
</script>
