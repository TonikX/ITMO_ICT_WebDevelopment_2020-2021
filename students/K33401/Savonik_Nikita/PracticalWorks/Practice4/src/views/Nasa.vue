<template>
 <section>
   <v-row>
     <v-col cols="6" class="mx-auto">
       <epic-item-card
         v-for="epicItem in epicItems"
         :key="epicItem.identifier"
         :epic-item="epicItem"
         class="my-2"
       />
     </v-col>
   </v-row>
 </section>
</template>

<script>
import EpicItemCard from '../components/EpicItemCard'

const apiKey = 'TMLngtnNldfIzjAc3bKg70UypY6h7eZcf2NfN4AN'
const apiUrl = 'https://api.nasa.gov/EPIC'

export default {
  name: 'Nasa',
  components: { EpicItemCard },

  data: () => ({
    epicItems: []
  }),

  methods: {

    async getEpicItems () {
      try {
        const response = await this.axios
          .get(`${apiUrl}/api/natural?api_key=${apiKey}`)
        if (response.status !== 200) {
          throw new Error(response.error)
        }

        const epicItems = response.data.map((epicItem) => {
          const date = new Date(epicItem.date)

          const year = date.getFullYear()

          const month = String(date.getMonth() + 1).length > 1
            ? date.getMonth() + 1
            : `0${date.getMonth() + 1}`

          const day = String(date.getDate()).length > 1
            ? date.getDate()
            : `0${date.getDate()}`

          epicItem.date = `${year}/${month}/${day}`

          epicItem.image = `${apiUrl}/archive/natural/${epicItem.date}/png/${epicItem.image}.png?api_key=${apiKey}`

          return epicItem
        })

        this.epicItems = epicItems
      } catch (e) {
        console.error('API is not responding', e)
      }
    }
  },
  created () {
    this.getEpicItems()
  }

}
</script>

<style scoped>

</style>
