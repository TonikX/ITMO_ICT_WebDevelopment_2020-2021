<template>
  <v-row  justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="#005B7C"
          dark
          v-bind="attrs"
          v-on="on"
          v-on:click="setValues"
          text
        >
          Изменить данные
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Изменение данных</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
              >
                <v-text-field
                  label="Имя"
                  required
                  v-model="first_name"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Фамилия"
                  v-model="last_name"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Адрес"
                  v-model="address"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="#005B7C"
            text
            v-on:click="dialog = false"
          >
            Закрыть
          </v-btn>
          <v-btn
            color="#005B7C"
            text
            v-on:click="updateData"
          >
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
export default {
  data: () => ({
    dialog: false,
    first_name: null,
    last_name: null,
    address: null
  }),
  props: {
    info: Object
  },
  methods: {
    /**
     * Установка значений в форме
     */
    setValues () {
      this.first_name = this.info.first_name
      this.last_name = this.info.last_name
      this.address = this.info.address
    },
    /**
     * Обновление значений в базе данных
     */
    updateData () {
      this.info.first_name = this.first_name
      this.info.last_name = this.last_name
      this.info.address = this.address
      this.dialog = false
    }
  }
}
</script>
