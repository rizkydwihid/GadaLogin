<template>
  <v-card height="700px" flat>
    <div class="headline text-xs-center pa-5">
      {{ bottomNav }}
    </div>
    <v-bottom-nav
      :active.sync="bottomNav"
      :value="true"
      absolute
      color="transparent"
    >
      <v-btn
        color="teal"
        flat
        medium
        value="recent"
      >
        <span>Home</span>
        <v-icon>home</v-icon>
      </v-btn>

      <v-btn
        color="teal"
        flat
        medium
        value="produk"
      >
        <span>Produk</span>
        <v-icon>folder_open</v-icon>
      </v-btn>

      <v-btn
        color="teal"
        flat
        medium
        value="nearby"
        @click="submit"
      >
        <span>Keluar</span>
        <v-icon>logout</v-icon>
      </v-btn>
    </v-bottom-nav>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
        bottomNav: 'recent'
      }
    },
    methods: {
      submit () {
        this.$router.push("/")
        // this.$router.push("/produk")
      }
    }
  }
</script>
