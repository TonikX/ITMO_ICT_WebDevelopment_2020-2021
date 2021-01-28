// src/plugins/vuetify.js

import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#537072',
        secondary: '#f4ebdb',
        anchor: '#7b918e'
      }
    }
  }
})

export default vuetify
