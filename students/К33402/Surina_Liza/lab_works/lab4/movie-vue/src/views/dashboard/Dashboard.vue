<template>
    <div class="page-dashboard">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">Все кино</h1>
                <Movies
                />
            </div>
        </div>
    </div>
</template>

<script>
    import Movies from "./Movies";
        export default {
        name: "Catalog",
        components: {Movies},
        props: {},
        data() {
          return {

          }},
    }
</script>

<style scoped>

</style>