<template>
    <div class="page-client">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Все кино</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'Detail', params: { id: film.id }}" aria-current="true">{{ film.title }}</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">

            <div class="column is-12">
                <h2 class="subtitle">Описание</h2>
                <div class="column is-6 is-offset-3">
                    <img :src="require('../images/' + this.$route.params.id + '.jpg')" alt="img">
                </div>
                <h3 class="title has-text-centered"><strong>{{ film.title }}</strong></h3>
                 <p class="has-text-centered" v-if="film.tagline">{{ film.tagline }}</p><br>
                <p class="has-text-centered" v-if="film.year || film.country"> {{ film.country }} ({{ film.year }})</p>
                <p class="has-text-centered" v-if="film.directors">{{ film.directors }}</p><br><br>
                <p  v-if="film.description">{{ film.description }}</p>
            </div>
        </div>
        <Review :reviews="film.reviews" :movie="film.id" @reLoad="getClient"/>
    </div>
</template>

<script>
import axios from 'axios'
import Review from "./Review";
export default {
    name: 'Detail',
    components: {Review},
    data () {
        return {
            film: {
            }
        }
    },
    mounted() {
        this.getClient()
    },
    methods: {
        getClient() {
            const movieID = this.$route.params.id
            axios
                .get(`/api/v1/movies/${movieID}/`)
                .then(response => {
                    this.film = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },

    },
    computed: {
    }
}
</script>
