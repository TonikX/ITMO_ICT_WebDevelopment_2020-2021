<template>
    <div d-flex class="mt-7" >
        <div>
        Вы действительно хотите выйти?
    </div>
    <v-btn class="mt-2"
        v-on:click="logout" 
        width="140px"
        depressed
        color="primary"
    >
      Да
    </v-btn>
    </div>
</template>


<script>


export default {
    methods: {
        logout() {
            this.$store.commit('SET_AUTHENTIICATED', false)
            this.$router.push('/')
        }
    }
}
</script>