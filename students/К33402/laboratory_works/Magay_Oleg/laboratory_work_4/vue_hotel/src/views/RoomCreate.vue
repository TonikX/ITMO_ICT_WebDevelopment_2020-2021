<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="5" class="mx-auto">
          <v-text-field
            label="Введите номер"
            v-model="addForm.number"
          />
          <v-text-field
            label="Введите телефон"
            v-model="addForm.phone"
          />
          <v-text-field
            label="Введите цену"
            v-model="addForm.price"
          />
          <v-select
            label="Выберите статус"
            v-model="addForm.status"
            :items="opts"
            item-text="label"
            item-value="code">
            <option v-for="opt in opts" :key="opt.id">
              {{ opt.label }}
            </option>
          </v-select>
          <v-text-field
            label="Введите прибыль с номера"
            v-model="addForm.total"
          />
          <v-select
            label="Выберите тип"
            v-model="addForm.type"
            :items="types"
            item-text="label"
            item-value="code">
            <option v-for="type in types" :key="type.id">
              {{ type.label }}
            </option>
          </v-select>
          <v-btn color="primary" @click="add">add</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'RoomCreate',
  data: () => ({
    opts: [{ label: 'свободно', code: 'free' }, { label: 'занято', code: 'busy' }],
    types: [{ label: 'одноместный', code: 'one' }, { label: 'двуместный', code: 'two' }, { label: 'трехместный', code: 'three' }],
    addForm: {
      number: '',
      phone: '',
      price: '',
      status: '',
      total: '',
      type: ''
    }
  }),
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/room/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
