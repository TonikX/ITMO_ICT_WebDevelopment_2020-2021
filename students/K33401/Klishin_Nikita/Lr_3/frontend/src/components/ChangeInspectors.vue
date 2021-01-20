<template>
    <div>
        <v-btn block outlined color="primary" dark @click="visible = !visible"> CHANGE </v-btn>
        <v-dialog v-model="visible" scrollable max-width="300px">
            <v-card v-if="!isLoading">
                <v-card-title>Select inspectors</v-card-title>
                <v-divider></v-divider>
                <v-card-text style="height: 300px">
                    <v-select
                        v-model="inspectors"
                        :items="teacherStudents"
                        :menu-props="{ maxHeight: '400' }"
                        multiple
                        hint="Pick inspectors"
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
                    <v-btn color="blue darken-1" text @click="pushInspectors()"> Save </v-btn>
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
            inspectors: [
                {
                    email: "4343"
                }
            ],
            teacherStudents: null,
        };
    },
    mounted() {
        console.log("Mounted");
        DataService.getTaskInspectors(this.$store.getters.GET_CURRENT_TASK_ID)
            .then((response) => response.data)
            .then((inspectorsData) => (this.inspectors = inspectorsData))
            .then(() => this.isLoading = false)
        DataService.getTeacherStudents(this.user.id)
            .then((response) => response.data)
            .then((studentsData) => (this.teacherStudents = studentsData.map((studentData => studentData.user))))
    },
    methods: {
        pushInspectors() {
            console.log("PushInspectors:", this.inspectors)
            DataService.patchTaskInspectors(this.$store.getters.GET_CURRENT_TASK_ID, this.inspectors)
            .then(this.visible = false)
            .then(this.$store.dispatch('REFRESH_CURRENT_TASK'))
        }
    }
};
</script>
