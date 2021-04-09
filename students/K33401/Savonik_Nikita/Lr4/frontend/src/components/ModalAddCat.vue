<template>

  <v-row style="width: 100%; margin-top: 3%" justify="center" align="center">
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
          text
        >
          <h3> Добавить кота </h3>
        </v-btn>
      </template>
      <v-card>
        <v-form @submit.prevent="AddCat" >
        <v-card-title>
          <span class="headline">Добавление данных кота</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="6">
                <v-text-field
                  label="Имя"
                  v-model="name"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  label="Порода"
                  v-model="breed"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="6"
              >
                <v-text-field
                  label="Цена"
                  required
                  v-model="price"
                ></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  label="Ссылка на фото"
                  v-model="pic"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea
                  type="textarea"
                  label="Описание"
                  v-model="description"
                  required
                ></v-textarea>
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
          <v-btn type="submit"
            color="#005B7C"
            text
          >
            Сохранить
          </v-btn>
        </v-card-actions>
          </v-form>
      </v-card>
    </v-dialog>
  </v-row>

</template>
<script>
const url = 'http://127.0.0.1:8000/api/cats/create/'
console.log(url)
export default {
  data: () => ({
    dialog: null,
    name: null,
    breed: null,
    price: null,
    description: null,
    pic: ''
  }),
  methods: {
    /**
     * Отправка пост запроса на создание кошки
     * @constructor
     */
    AddCat () {
      this.axios.post(url, {
        breed: this.breed,
        name: this.name,
        price: this.price,
        description: this.description,
        pic: this.pic
      },
      { headers: { Authorization: `Token ${localStorage.getItem('token')}` } }).then(response => {
        if (response.status === 201) {
          this.$router.go()
        }
      })
    }
  }
}
</script>
