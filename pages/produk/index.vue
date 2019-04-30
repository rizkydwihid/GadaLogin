<template>
<v-layout
  justify-center
  align-center
  >
  <v-flex>
    <div class="produk text-xs-center"> <v-icon color="orange darken 2">local_mall</v-icon> PRODUK</div>
    <br>
    <v-text-field
        v-model="search"
        append-icon="search"
        label="cari disini ..."
        single-line
        hide-details
    ></v-text-field>
    <br>
      <p class="no-results" v-if="noResults">Pencarian barang <span><b>" {{ search }} "</b></span> tidak ditemukan.</p>
    <v-card class="cardproduct text-xs-center" 
    v-for="produk in filteredList" :key="produk"
    >
      <v-img
          :src="require(`assets/img/${produk.pict}`)"
          aspect-ratio="1"
        ></v-img>

        <v-card-title primary-title class="cardtitle">
          <div>
            <h5 class="headline mb-0"> {{ produk.name }} </h5>
            <div><small> IDR {{ produk.harga }} </small></div>
          </div>
        </v-card-title>
    </v-card>
    <BottomNavbar />
  </v-flex>
</v-layout>
</template>


<style scoped>
@import url('https://fonts.googleapis.com/css?family=Raleway');
    .produk {
        font-weight: 900 !important;
        font-family: Raleway !important;
        font-size: 17px !important;
    }
    .cardproduct {
      border-radius: 5px !important;
      box-shadow: 5px !important;
      margin-bottom: 20px;
    }
    .headline {
      font-size: 15px !important;
    }
    .cardtitle {
      padding-top: 10px !important;
    }
    .card{
      background: transparent !important;
      border: 0 !important;
    }
    .no-results {
      color:gray;
      font-family: 'Raleway';
      font-size: 16px;
      letter-spacing: 0.06rem;
      text-align: center;
    }
    .no-results span{
      color: red;
    }
</style>

<script>
import BottomNavbar from '~/components/BottomNavbar.vue'
// import { store } from './store'

export default {
  data () {
    return {
      search : '',
      picture : 'iphonx.jpg',
      produkList: [
        { name : 'Iphone X 128GB', pict : 'iphonx.jpg', harga : 'Rp 12.000.000' },
        { name : 'Samsung S8', pict : 'ss-s8.jpg', harga : 'Rp 9.000.000' },
        { name : 'Samsung A7 2018', pict : 'a7.jpg', harga : 'Rp 5.000.000' },
        { name : 'Xiaomi Mi 8 Lite', pict : 'Mi-8-Lite.png', harga : 'Rp 2.900.000' },
        { name : 'Iphone 8 64GB', pict : 'iphone8.png', harga : 'Rp 4.500.000'}
      ]
    }
  },
  components: {
    BottomNavbar
  },
  computed: {
    allProduk() {
      return this.$store.getters.getBarang
    },
    filteredList() {
      return this.produkList.filter(post => {
        return post.name.toLowerCase().includes(this.search.toLowerCase())
      })
    },
    noResults() {
      return this.filteredList.length === 0;
    },
  }
}
</script>

