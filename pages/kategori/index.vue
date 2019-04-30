<template>
<v-layout
  justify-center
  align-center
  >
  <v-flex>
    <div class="kategori text-xs-center"> <v-icon color="orange darken 2">view_list</v-icon> KATEGORI</div>
    <br>
    <v-tabs fixed-tabs>
        <v-tab> Gadget </v-tab>
        <v-tab> Aksesoris </v-tab>
    </v-tabs>

    <BottomNavbar />
  </v-flex>
</v-layout>    
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Raleway');
    .kategori {
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