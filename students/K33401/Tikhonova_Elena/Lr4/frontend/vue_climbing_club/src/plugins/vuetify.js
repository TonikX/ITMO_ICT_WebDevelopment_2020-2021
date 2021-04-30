import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
          light: {
            primary: colors.deepOrange.accent1, 
            secondary: colors.grey.darken4, 
            accent: colors.deepOrange.accent1,
            mycolor: colors.grey.darken4, 
          },
          dark: {
              primary: colors.deepOrange.accent1,
              secondary: colors.deepOrange.accent1,
              accent: colors.deepOrange.accent1,
              info: colors.deepOrange.accent1,
          },
        },
      },
});
