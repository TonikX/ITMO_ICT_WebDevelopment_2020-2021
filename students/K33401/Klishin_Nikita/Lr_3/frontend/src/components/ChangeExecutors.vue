<template>
    <div>
        <v-btn block outlined color="primary" dark @click="visible = !visible"> CHANGE </v-btn>
        <v-dialog v-model="visible" scrollable max-width="300px">
            <v-card v-if="!isLoading">
                <v-card-title>Select executors</v-card-title>
                <v-divider></v-divider>
                <v-card-text style="height: 300px">
                    <v-select
                        v-model="executors"
                        :items="teacherStudents"
                        :menu-props="{ maxHeight: '400' }"
                        multiple
                        hint="Pick executors"
                        persistent-hint
                        item-value="id"
                        item-text="title"
                    >
                        <template slot="selection" slot-scope="{ item }">
                            {{ item.email }}
                        </template>
                        <template slot="item" slot-scope="{ item }"> {{ item.email }} </template>
                    </v-select>
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-btn color="blue darken-1" text @click="visible = false"> Close </v-btn>
                    <v-btn color="blue darken-1" text @click="pushExecutors()"> Save </v-btn>
                </v-card-actions>
            </v-card>
            <v-card v-else>
                <v-card-title primary-title>
                    Loading...
                </v-card-title>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import DataService from "../services/DataService";
export default {
    computed: {
        user() {
            return this.$store.getters.GET_USER_OBJECT;
        },
    },
    watch: {
        items: function () {
            return this.teacherStudents;
        },
    },
    data() {
        return {
            isLoading: true,
            visible: false,
            executors: null,
            teacherStudents: null,
        };
    },
    mounted() {
        console.log("Mounted");
        DataService.getTaskExecutors(this.$store.getters.GET_CURRENT_TASK_ID)
            .then((response) => response.data)
            .then((executorsData) => (this.executors = executorsData))
            .then(() => this.isLoading = false)
        DataService.getTeacherStudents(this.user.id)
            .then((response) => response.data)
            .then((studentsData) => (this.teacherStudents = studentsData.map((studentData => studentData.user))))
    },
    methods: {
        pushExecutors() {
            console.log("PushExecutors:", this.executors)
            DataService.patchTaskExecutors(this.$store.getters.GET_CURRENT_TASK_ID, this.executors)
            .then(this.visible = false)
            .then(this.$store.dispatch('REFRESH_CURRENT_TASK'))
        }
    }
};
</script>
