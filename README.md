# SellerLogin

> Login page Gada with Nuxt.JS
Link apps : https://rdhapps.herokuapp.com/

Dynamic route : /produk/gadget, /produk/aksesoris

Link apps : https://rdhapps.herokuapp.com/
Dynamic route : /produk/gadget, /produk/aksesoris

## Build Setup

``` bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, checkout [Nuxt.js docs](https://nuxtjs.org).

===========================================================

## Buat bot telegram

```bash
1. Buka telegram, search @BotFather
2. ketikkan '/newbot'
3. isikan nama bot dan username bot telegram
4. BotFather akan mengirimkan bot token
5. bot telegram berhasil dibuat

```

===========================================================

## Setting Webhook

``` bash
# url bot telegram
https://api.telegram.org/bot820797611:AAHv78eRIbvplSc-M5RvUvmCZryIE1_Fjzk

# setting webhook telegram
https://api.telegram.org/bot820797611:AAHv78eRIbvplSc-M5RvUvmCZryIE1_Fjzk/setWebhook?url=https://b64663d3.ngrok.io

# url webhook || 
# url webhook di dapat ketika file webhook di jalankan
https://b64663d3.ngrok.io

```

===========================================================

## Running file webhook

``` bash
# berkas file
folder : webhook_listener

# virtual env
boleh menggunakan virtual environtment

# run file
command --> honcho start

requirement --> pip3 install -r requirements.txt

```

===========================================================

## Outgoing webhook netlify

``` bash
# pilihan outgoing webhook
Add Notification --> Slack Integration --> pilih event deploy netlify [started/ successed] --> paste "url webhook"

```