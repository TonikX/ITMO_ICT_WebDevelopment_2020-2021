<template>
  <div class="page">
    <div class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3 d-flex flex-column">
        <h3 class="mt-5 mb-0 pb-2">{{user.name}}'s Wishlist ♥️</h3>
        <p class="pb-5 mb-0 border-bottom">Hey! This is your friend's wishlist. If you want to gift something — click Reserve button and other friends will not duplicate the gift.</p>
        <Item
          v-for="item in user.items"
          :key="item.id"
          v-bind:id="item.id"
          v-bind:title="item.title"
          v-bind:status="item.status"
          v-bind:context="'public'"
          v-on:reserveItem="reserveItem"
          v-on:unreserveItem="unreserveItem" />
      </div>
    </div>
  </div>
  </div>

</template>

<script>
import Item from '../components/Item';

export default {
  name: "Wishlist",
  components: {Item},
  data() {
    return {
      user: {
        name: '',
        email: '',
        items: []
      }
    }
  },
  methods: {
    /**
     * Резервирование пункта вишлиста
     * @param {string} id
     */
    reserveItem(id) {
      this.updateItem(id, 'RESERVED');
    },

    /**
     * Отмена резерва пункта вишлиста
     * @param {string} id
     */
    unreserveItem(id) {
      this.updateItem(id, 'WAITING');
    },

    /**
     * Обновление пункта вишлиста - используется функциями reserveItem(id) и
     * unserserveItem(id) для резервации и отмены
     * @param {string} id
     * @param {string} newStatus
     */
    updateItem(id, newStatus) {
      for (let i = 0; i < this.user.items.length; i++) {
        if (this.user.items[i].id === id) {
          this.user.items[i].status = newStatus;
          const item = this.user.items[i];

          fetch('/api/updateItem', {
            method: 'POST',
            body: JSON.stringify({
              itemId: item._id,
              newTitle: item.title,
              newStatus: newStatus,
              userId: this.$route.params.userId
            })
          })
        }
      }
    }
  },

  /**
   * Получение UserId из URL и загрузка из БД остальных данных
   */
  mounted() {
    const userId = this.$route.params.userId;

    if (!userId) {
      this.$router.push({name: "Hello"});
    } else {
      fetch('/api/findUser', {
        method: 'POST',
        body: JSON.stringify({userId: userId})
      })
        .then(response => response.json())
        .then(data => {
          if ('errors' in data || !data['data']['findUserByID']) {
            console.log(data);
            this.$router.push({name: "Hello"});
          } else {
            const answer = data['data']['findUserByID'];
            this.user.name = answer['name']
            this.user.email = answer['email']

            for (const item of answer['items']['data']) {
              this.user.items.push({
                id: this.user.items.length,
                _id: item['_id'],
                title: item['title'],
                status: item['status']
              })
            }
          }
        })
        .catch(error => {
          console.log(error);
          alert('Error occured!');
        })
    }
  }
}
</script>
