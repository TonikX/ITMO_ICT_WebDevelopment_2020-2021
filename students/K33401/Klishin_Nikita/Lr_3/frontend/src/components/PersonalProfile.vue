<template>
    <v-card>
        <v-card-text class="text-center">
            <dir class="text-h4 pt-5 pb-2">Personal information</dir>
        </v-card-text>
        <v-divider></v-divider>
        <v-row class="my-1">
            <v-col md="6">
                <div>E-mail address:</div>
            </v-col>
            <v-col md="6">
                <div>{{ user.email }}</div>
            </v-col>
        </v-row>
        <v-divider />
        <v-row class="my-1">
            <v-col md="6">
                <div class="d-flex justify-center">
                    <div>Имя:</div>
                </div>
            </v-col>
            <v-col md="6">
                <v-text-field v-model="user.name"></v-text-field>
            </v-col>
        </v-row>
        <v-divider />
        <v-row class="my-1">
            <v-col md="6">
                <div>Фамилия:</div>
            </v-col>
            <v-col md="6">
                <v-text-field v-model="user.surname"></v-text-field>
            </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-row class="my-1">
            <v-col md="6">
                <div>ID:</div>
            </v-col>
            <v-col md="6">
                <div>{{ user.id }}</div>
            </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-row class="mt-1">
            <v-col md="12">
                <div v-if="user.is_teacher" class="text-subtitle-1">
                    Teacher
                </div>
                <div v-else class="text-subtitle-1">Student</div>
            </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-row class="mt-3">
            <v-col offset-md="1" md="10">
                <v-btn @click="patchPersonalInfo()" block outlined color="primary" dark>SAVE CHANGES</v-btn>
            </v-col>
        </v-row>
    </v-card>
</template>


<script>
export default {
    computed: {
        user() {
            return this.$store.getters.GET_USER_OBJECT
        }
    },
    methods: {
        patchPersonalInfo() {
            this.$store.dispatch('PATCH_USER')
        }
    }
}
</script>
