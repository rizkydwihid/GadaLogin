<template>
<v-layout
  justify-center
  align-center
  >
  <v-flex>
      <div class="helppp text-xs-center"> <v-icon color="orange darken 2">help</v-icon> HELP </div>
      <br>
    <blockquote class="help">
      <span>Apa saja yang ada disini? </span><br>
      <hr class="mr-3 ml-3">
      <br>
      <p> 
        <small>
          Anda dapat melihat produk-produk yang kami jual. Banyak sekali produk yang kami tawarkan untuk anda, dan 
          anda dapat melihat semua produk yang kami jual pada menu <b>"Product".</b>
        </small>
      </p> 
    </blockquote>
    <BottomNavbar />
  </v-flex>
</v-layout>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Raleway');
  .help {
    font-family: Raleway;
    text-align: center !important;
  }
  .helppp {
    font-weight: 900 !important;
    font-family: Raleway !important;
    font-size: 17px !important;
  }
</style>


<script>
  import BottomNavbar from '~/components/BottomNavbar.vue'

  export default {
    components: {
      BottomNavbar
    }
  }
</script>
