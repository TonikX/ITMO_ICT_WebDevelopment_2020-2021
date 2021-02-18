<template>
  <div class="about">
<h1 align="center">Организация учебной части колледжа</h1>
    <br>
     <v-card dark
    class="mx-auto"
    max-width="700"
  >
    <v-card-text>
      <h4 id="-1">Вариант:</h4>
        <ul>
        <li>№12 из курса «Основы баз данных»</li>
        </ul>
        <br>
      <p align="center">Программная система, предназначенная для учебной части колледжа.
Обеспечивает хранение сведений о каждом преподавателе, о
дисциплинах, которые он преподает, номере закрепленного за ним кабинета, о
расписании занятий. В задачу диспетчера учебной части входит составление расписания.</p>
    </v-card-text>
  </v-card>
  </div>

</template>

<script>
export default {
  name: 'About',
  data: () => ({
    userData: {
      username: '',
      email: ''
    }
  }),
  methods: {
    async loadUserData () {
      try {
        const response = await this.axios
          .get('http://localhost:8000/auth/users/me/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('token')}`
            }
          })

        // if (response.status !== 200) {
        //   throw new Error(response.status)
        // }

        this.userData = response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },

  created () {
    this.loadUserData()
  }
}
</script>
