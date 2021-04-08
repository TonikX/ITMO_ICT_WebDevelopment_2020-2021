<template>
    <div class="columns is-multiline">
            <div
                class="column is-3"
                v-for="movie in movies"
                v-bind:key="movie.id"
            >
                <div class="box">
                    <h3 class="is-size-4 mb-4 has-text-centered">{{ movie.title }}</h3>
                      <img class="card-image mb-4" :src=" require('../images/' + movie.id + '.jpg')" alt="img">
                    <router-link :to="{ name: 'Detail', params: { id: movie.id }}" class="button is-light">Подробнее</router-link>
                </div>
            </div>
        </div>

</template>

<script>
import axios from 'axios'
export default {
    name: 'Movies',
    data() {
        return {
            movies: []
        }
    },
    mounted() {
        this.getClients()
    },
    methods: {
        getClients() {
            axios
                .get('/api/v1/movies/')
                .then(response => {
                    for (let i = 0; i < response.data.length; i++) {
                        this.movies.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    },
}
</script>

<style scoped>
    .box {
        width: 250px;
        height: 500px;
}
    .card-image {
        width: 220px;
        height: 320px;
    }
</style>