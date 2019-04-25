<template>
<v-layout
  column
  justify-center
  align-center
  >
  <v-flex>
    <div class="produk text-xs-center"> <v-icon color="orange darken 2">local_mall</v-icon> PRODUK</div>
    <br>
    <v-card class="cardproduct">
      <v-img
          src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
          aspect-ratio="1.5"
        ></v-img>

        <v-card-title primary-title class="cardtitle">
          <div>
            <h5 class="headline mb-0"> Iphone X 128GB </h5>
            <div> <v-icon color="orange darken 2" size="15px">attach_money</v-icon>12.000.000 </div>
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
</style>

<script>
import BottomNavbar from '~/components/BottomNavbar.vue'

export default {
    components: {
        BottomNavbar
    }
}
</script>

