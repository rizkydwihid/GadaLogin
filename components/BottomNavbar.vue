<template>
  <v-bottom-nav
      :value="true"
      fixed
      color="white"
    >
      
      <v-btn
        color="orange"
        flat
        value="product"
        @click="produk"
        small
      >
        <span class="bottnav"><b> Produk </b></span>
        <v-icon color="orange darken 2">local_mall</v-icon>
      </v-btn>

      <v-btn
        color="orange"
        flat
        value="news"
        @click="kategori"
        small
      >
        <span class="bottnav"><b> Kategori </b></span>
        <v-icon color="orange darken 2">view_list</v-icon>
      </v-btn>

      <v-btn
        color="orange"
        flat
        value="news"
        @click="news"
        small
      >
        <span class="bottnav"><b> News </b></span>
        <v-icon color="orange darken 2">trending_up</v-icon>
      </v-btn>

      <v-btn
        color="orange"
        flat
        value="exit"
        @click="keluar"
        small
      >
        <span class="bottnav"><b> Keluar </b></span>
        <v-icon color="orange darken 2">exit_to_app</v-icon>
      </v-btn>
    </v-bottom-nav>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Raleway');
  .bottnav {
    font-family: Raleway !important;
  }
</style>


<script>
  export default {
    data () {
      return {
        bottomNav: ''
      }
    },
    methods: {
      keluar () {
        this.$router.push("/")
      },
      produk () {
        this.$router.push("/produk")
      },
      kategori () {
        this.$router.push("/kategori")
      },
      news () {
        this.$router.push("/news")
      }
    }
  }
</script>
