<template>
  <v-card elevation="2">
    <v-row class="d-flex align-center text-center mx-2" fluid>
      <v-col class="mx-auto">
        <v-card-title>Вопрос {{this.index + 1}}</v-card-title>
      </v-col>
      <v-col cols="1" class="mx-auto">
        <v-icon style="cursor: pointer" v-show="index > 0" @click="removeQuestion(index)">mdi-close</v-icon>
      </v-col>
    </v-row>
    <v-row class="d-flex align-center text-center mx-2" fluid>
      <v-col class="mx-auto">
        <v-text-field
          v-model="description"
          label="Описание"
          required
          @change="emitEventChanged"
        />
      </v-col>
    </v-row>
    <v-row class="d-flex align-center text-center mx-2" justify="center" fluid
           v-for="(answer, index) in answer_set"
           :key="answer.id">
      <v-col class="mx-auto">
        <v-text-field
          v-model="answer.description"
          label="Вариант ответа"
          required
          outlined
          dense
        />
      </v-col>
      <v-col cols="1" v-show="index > 1" class="align-content-center">
          <v-icon color="red" @click="removeAnswer(index)">mdi-minus</v-icon>
      </v-col>
    </v-row>
    <v-card-text @click="addAnswer" style="margin-bottom: 16px; cursor: pointer; color: deepskyblue">
      Добавить вариант ответа
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'Question',
  props: {
    answer_set: Array,
    question: Object,
    index: Number
  },
  data: () => ({
    description: ''
  }),
  methods: {
    addAnswer () {
      this.answer_set.push({
        description: ''
      })
    },
    removeAnswer (index) {
      this.answer_set.splice(index, 1)
    },
    removeQuestion (index) {
      console.log(index)
      this.$emit('RemoveQuestion', index)
    },
    emitEventChanged () {
      console.log('description')
      this.$emit('Description', { index: this.index, description: this.description })
    }
  }
}
</script>

<style scoped>

</style>
