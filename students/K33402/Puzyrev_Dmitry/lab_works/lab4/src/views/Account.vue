<template>
  <div class="page">
    <nav class="navbar navbar-expand-lg navbar-dark bg-danger justify-content-end">
      <span class="navbar-text">
        Logged in as <span class="username">{{ user.name }}</span>
      </span>
    </nav>
    <div class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3 d-flex flex-column">
        <h3 class="mt-4 mb-0 border-bottom pb-4">Your Wishlist</h3>
        <Item
          v-for="item in user.items"
          :key="item.id"
          v-bind:id="item.id"
          v-bind:title="item.title"
          v-bind:status="item.status"
          v-bind:context="'private'"
          v-on:removeItem="removeItem" />
        
        <div class="input-group mb-3 mt-4">
          <input type="text" class="form-control" placeholder="" v-model="newItemTitle">
          <div class="input-group-append">
            <button class="btn btn-danger" type="button" @click="addItem">+ Add Item</button>
          </div>
        </div>

        <div class="share">
          <h3>Ready to share? Just copy a link!</h3>
          <input type="text" class="link" :value="`https://heuristic-lovelace-97d277.netlify.app/wishlist/${user.id}`">
        </div>
      </div>
    </div>
  </div>
  </div>

</template>

<script>
import Item from '../components/Item';

export default {
  name: "Account",
  components: {Item},
  data() {
    return {
      newItemTitle: '',
      user: {
        id: '',
        name: '',
        email: '',
        items: []
      }
    }
  },
  methods: {
    /**
     * Добавление пункта в вишлист из поля ввода - берем значение из поля ввода
     * и добавляем в качестве пункта вишлиста (сначала в приложение, потом сразу
     * запрос в БД)
     */
    addItem() {
      if (this.newItemTitle) {
        this.user.items.push({
          id: this.user.items.length,
          title: this.newItemTitle,
          status: 'WAITING',
        });

        const newTitle = this.newItemTitle;
        const insertedItem = this.user.items[this.user.items.length - 1];
        this.newItemTitle = '';

        fetch('/api/addItem', {
          method: 'POST',
          body: JSON.stringify({userId: this.user.id, title: newTitle})
        })
          .then(response => response.json())
          .then(data => {
            if ('errors' in data) {
              alert('Error occured!');
              console.log(data);
            } else {
              const answer = data['data']['createItem'];
              insertedItem._id = answer['_id'];
            }
          })
          .catch(error => {
            console.log(error);
            alert('Error occured!');
          })
      }
    },

    /**
     * Удаление пункта из вишлиста
     * @param {string} id
     */
    removeItem(id) {
      for (let i = 0; i < this.user.items.length; i++) {
        if (this.user.items[i].id === id) {

          const ID = this.user.items[i]._id;
          this.user.items.splice(i, 1);

          fetch('/api/removeItem', {
            method: 'POST',
            body: JSON.stringify({itemId: ID})
          })
          .then(response => response.json())
          .then(data => {
            console.log(data);
          })
          .catch(error => {
            console.log(error);
          })
        }
      }
    }
  },

  /**
   * После создания страницы пробуем достать UserId из local storage,
   * по которому в свою очередь скачиваем остальную информацию уже из БД
   */
  mounted() {
    const myStorage = window.localStorage;
    this.user.id = myStorage.getItem('userId');

    if (!this.user.id) {
      this.$router.push({name: "Hello"});
    } else {
      fetch('/api/findUser', {
        method: 'POST',
        body: JSON.stringify({userId: this.user.id})
      })
        .then(response => response.json())
        .then(data => {
          if ('errors' in data || !data['data']['findUserByID']) {
            alert('Error!');
            console.log(data);
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

<style lang="scss" scoped>
  .username {
    color: #fff;
  }

  .share {
    border: 2px solid red;
    border-radius: 10px;
    padding: 10px 20px;
    margin-top: 50px;

    h3 {
      font-size: 18px;
      margin-top: 10px;
    }

    .link {
      width: 100%;
      background: #ccc;
      border: none;
      border-radius: 5px;
      padding: 5px 10px;
    }
  }
</style>