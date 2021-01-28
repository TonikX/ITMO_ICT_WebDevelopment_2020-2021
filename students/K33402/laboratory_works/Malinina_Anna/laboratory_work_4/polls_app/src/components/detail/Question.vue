<template>
  <v-card
    elevation="2"
  >
    <v-container
      class="d-flex flex-column justify-start"
    >
      <v-card-text>
        {{ question.description }}
      </v-card-text>

      <v-radio-group
        v-model="radioGroup"
          @change="emitEventChanged"
      >
        <v-row v-for="(answer1, index) in question.answer_set"
               :key="answer1.id">
          <v-col>
        <v-radio
          :label="`${answer1.description}`"
          :value="answer1"
        ></v-radio>
          </v-col>
          <v-col v-if="isMy && answer_statistic.find(({answer})=>answer === answer1.id)" cols="1">
            {{answer_statistic.find(({answer})=>answer === answer1.id).count}}
          </v-col>
        </v-row>
      </v-radio-group>

    </v-container>
  </v-card>
</template>

<script>

  import {BASE_URL, TOKEN_KEY} from "../../variables";

export default {
  name: 'Question',
  props: {
    question: Object,
    isMy: Boolean,
    pollId: Number
  },
  data () {
    return {
      radioGroup: Object,
      answer_statistic: []
    }
  },
  methods: {
    /**
     * Отправляет событие выбора варианта ответа
     */
    emitEventChanged () {
      console.log(this.radioGroup)
      this.$emit('CustomEventInputChanged', this.radioGroup)
    },
    /**
     * получает статистику ответа
     */
    async getStatistic (answerId) {
      const token = sessionStorage.getItem(TOKEN_KEY)
      let config = {}
      if (token) {
        config = {
          headers:
            {
              Authorization: `Token ${token}`
            }
        }
      }
      await this.axios.get(`${BASE_URL}/polls/statistic?answer=${answerId}`, config)
      .then((response) => {
        console.log({
          answer: answerId,
          count: response.data.length
        })
        this.answer_statistic.push({
          answer: answerId,
          count: response.data.length
        })
        console.log(this.answer_statistic.find(({answer})=>answerId === answer))
      }, (error) => {
        console.log(error)
      })
    }
  },
  created() {
    for(let answer of this.question.answer_set){
      console.log(answer)
      this.getStatistic(answer.id)
    }
  }
}
</script>

<style scoped>

</style>
