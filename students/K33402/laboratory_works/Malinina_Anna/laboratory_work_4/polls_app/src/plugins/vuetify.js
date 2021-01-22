import Vue from 'vue'
import Vuetify from 'vuetify/lib/framework'
// import * as colors from 'vuetify'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#8FBC8F',
        secondary: '#FFF',
        accent: '#8c9eff',
        error: '#b71c1c',
        background: '#DCDCDC'
      }
    }
  }
})
