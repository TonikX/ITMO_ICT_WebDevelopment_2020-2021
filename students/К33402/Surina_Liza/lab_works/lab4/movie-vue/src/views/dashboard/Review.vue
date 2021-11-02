<template>
    <div class="row">
        <div class="columns">
            <div class="column is-4 is-offset-16">
                <hr>
                <h6 class="subtitle">
                    Оставить отзыв
                </h6>
                <form action="#" method="get" class="mt-4" id="formReview">
                    <div class="d-sm-flex">
                        <div class="col-sm-6 form-group p-0 editContent">
                            <label>Имя</label>
                            <input type="email" class="input" id="contactusername"
                                   required="" v-model="name">
                        </div>
                        <div class="col-sm-6 form-group ml-sm-3 editContent">
                            <label>Email</label>
                            <input type="email" class="input" id="contactemail"
                                   required="" v-model="email">
                        </div>
                    </div>
                    <div class="form-group editContent">
                        <label>Ваш комментарий</label>
                        <textarea class="textarea is-large" placeholder="Комментарий" v-model="text">
                        </textarea>
                    </div><br>

                    <button type="button" class="button is-light"
                            @click="sendReview()">
                        Отправить
                    </button>
                </form>
            </div>
        </div>
        <br>
            <h1 class="subtitle">Комментарии</h1>
        <div class="media py-5 review" v-for="review in reviews" :key="review.id">
            <div class="box">
                <strong>Пользователь: </strong> {{review.name}}
                <p class="mt-2 editContent" v-html="review.text"></p>
                <div class="media mt-5 editContent" v-for="child in review.children">
                    <a class="pr-3" href="#">
                    </a>
                    <div class="media-body">
                        <h5 class="mt-0 editContent">{{child.name}}</h5>
                        <p class="mt-2 editContent" v-html="child.text"></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Review",
        props: ["reviews", "movie"],
        data() {
            return {
                name: '',
                email: '',
                text: '',
                parent: null
            }
        },
        methods: {
            async sendReview() {
                let data = {
                    name: this.name,
                    email: this.email,
                    text: this.text,
                    parent: this.parent,
                    movie: this.movie
                }
                fetch(`${this.$store.getters.getServerUrl}/review/`,
                    {
                        method: "POST",
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    }
                ).then(response => {
                    this.$emit('reLoad')
                    this.clearForm()
                })
            },
            addParent(id) {
                this.parent = id
            },
            clearForm() {
                this.name = ''
                this.email = ''
                this.text = ''
                this.parent = null
            }
        }
    }
</script>

<style scoped>
    .review {
        width: 100%;
    }
</style>