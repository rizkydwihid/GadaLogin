<template>
    <v-layout
    column
    >
    <v-flex>
      <div class="text-center mt-2">
        <!-- <logo />
        <vuetify-logo /> -->
        <center>
        <h2 class="judul"> Masuk sebagai Penjual </h2>
        </center>
        <br>
      </div>
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
        >
          <v-text-field
            class="fieldlogin"
            v-model="name"
            clearable
            :loading="loading"
            :rules="[rules.nameRules, rules.minuser]"
            label="Username"
            outline
          >
          </v-text-field>
          <v-text-field
            class="fieldlogin"
            v-model="password"
            :loading="loading"
            :rules="[rules.required, rules.min]"
            :append-icon="show1 ? 'visibility' : 'visibility_off'"
            :type="show1 ? 'text' : 'password'"
            label="Password"
            outline
            @click:append="show1 = !show1">
          </v-text-field>
      <div class="lupapass"> <a href="#">Lupa password? </a></div>
          <v-btn
            block
            large
            class="btnmasuk"
            :loading="loading"
            :disabled='!valid || loading'
            color="error"
            @click="submit"
          > Masuk
          </v-btn>
    
      <p class="keterangan"> Dengan masuk ke aplikasi, Anda telah menyetujui, <br> <a href="#"> Syarat dan Ketentuan</a> yang berlaku </p>
    
        </v-form>
    </v-flex>
    </v-layout>
</template>


<style scoped>
    .btnmasuk{
      margin-bottom: 5px;
      text-transform: capitalize;
    }
    .lupapass{
      color: red !important;
      text-align: right;
      margin-bottom: 15px;   
    }
    .fieldlogin >>> .v-input__control .v-input__slot {
      border: 1px solid ;
    }

    .fieldlogin >>> .v-text-field__slot input {
      margin-top: 0;
      height: 48px;
      max-height: 48px;
      font-size: 16px;
      padding: 0 5px;
    }
    .fieldlogin >>> .v-text-field__slot .v-label--active {
      -webkit-transform: translateY(-25px) scale(0.75);
      transform: translateY(-25px) scale(0.75);
      background: #fff;
      top: 18px;
      padding: 0 5px;
      height: 20px;
      line-height: 20px;
    }
    .fieldlogin.v-input--is-focused.primary--text >>> label,
    .fieldlogin.v-input--is-focused.primary--text >>> i {
      color: #51bcb8 !important;
    }
    .fieldlogin.v-input--is-focused.primary--text >>> .v-input__slot{
      color: #51bcb8 !important;
    }
    .fieldlogin >>> i
    {
      font-size: 16px;
    }
    .fieldlogin >>> .v-progress-linear__bar__indeterminate {
      background: #51bcb8 !important;
    }
    .keterangan{
      font-size: 12px;
      text-align: center;
      padding: 20px;
      padding-top: 0;
    }
</style>


<script>
  export default {
    data () {
      return {
        valid: true,
        show1: false,
        password: '',
        loading: false,
        rules: {
          // validasi untuk inputan password
          required: value => !!value || 'Kata sandi harus diisi',
          min: v => (v && v.length) >= 6 || 'Password harus lebih dari 6 karakter',

          // validasi untuk inputan username
          nameRules: value => !!value || 'Username harus diisi',
          minuser: v => (v && v.length >= 3) || 'Username harus lebih dari 3 karakter'
        }
      }
    },
    methods: {
      submit () {
        this.loading = true
        setTimeout(() => {
          this.loading = false
          this.$router.push("/produk")
        }, 2000)
      }
    }
  }
</script>