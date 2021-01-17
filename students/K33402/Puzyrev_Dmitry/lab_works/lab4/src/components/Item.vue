<template>
  <div class="wrapper width-100 d-flex flex-row justify-content-between pb-2 pt-2 border-bottom">
    <div class="title d-flex flex-row align-items-center justify-content-start">
      <span>{{ title }}</span>
      <span class="badge badge-danger ml-2" v-if="status === 'RESERVED'">Reserved</span>
    </div>
    <div class="controls">
      <div v-if="context === 'public'">
        <button class="btn btn-danger btn-sm animate-grow" v-if="status === 'WAITING'" @click="reserveItem(id)">Reserve</button>
        <button class="btn btn-dark btn-sm" v-if="status === 'RESERVED'" @click="unreserveItem(id)">Unreserve</button>
      </div>
      <div v-else-if="context === 'private'">
        <button class="btn btn-danger btn-sm mr-1" @click="removeItem(id)">Gifted</button>
        <button class="btn btn-dark btn-sm" @click="removeItem(id)" :disabled="status === 'RESERVED'">X</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Item',
  props: {
    id: Number,
    title: String,
    status: String,
    context: String
  },
  methods: {
    /**
     * Удаление пункта вишлиста
     * @param {string} id
     */
    removeItem(id) {
      this.$emit('removeItem', id);
    },

    /**
     * Резервирование пункта вишлиста
     * @param {string} id
     */
    reserveItem(id) {
      this.$emit('reserveItem', id);
    },

    /**
     * Отмена резерва пункта вишлиста
     * @param {string} id
     */
    unreserveItem(id) {
      this.$emit('unreserveItem', id);
    },
  }
}
</script>

<style lang="scss" scoped>
  .animate-grow {
    animation: animate_grow 2s infinite;
  }
  .animate-grow:hover {
    animation: none;
  }
  
  @keyframes animate_grow {
    0% {
      transform: scale3d(1, 1, 1);
    }
    50% {
      transform: scale3d(1.1, 1.1, 1.1);
    }
    100% {
      transform: scale3d(1, 1, 1);
    }
  }
</style>
