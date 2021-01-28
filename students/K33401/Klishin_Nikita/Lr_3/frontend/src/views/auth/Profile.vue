<template>
    <v-container mt-5>
        <!-- Заголовок "Profile page" -->
        <v-row>
            <v-col md="12" class="px-0">
                <v-card class="mx-0" dark>
                    <v-card-text class="py-2">
                        <div class="text-h5 white--text">Profile page</div>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row class="mt-5">
            <!-- Personal info -->
            <v-col md="5" class="px-0">
                <v-row>
                    <v-col>
                        <PersonalProfile></PersonalProfile>
                    </v-col>
                </v-row>
                <v-row class="mt-3">
                    <v-col v-if="user.is_teacher">
                        <TeacherProfile></TeacherProfile>
                    </v-col>
                    <v-col v-else>
                        <StudentProfile></StudentProfile>
                    </v-col>
                </v-row>
            </v-col>

            <v-spacer></v-spacer>

            <v-col md="6" class="px-0">
                <!-- Students tabs -->
                <v-card v-if="!user.is_teacher">
                    <v-tabs class="mt-0" grow dark v-model="currentTab">
                        <v-tab> Task to execute </v-tab>
                        <v-tab-item>
                            <ExecutionTasksList></ExecutionTasksList>
                        </v-tab-item>
                        <v-tab> Task to inspect </v-tab>
                        <v-tab-item>
                            <InspectionTasksList></InspectionTasksList>
                        </v-tab-item>
                    </v-tabs>
                </v-card>
                <!-- Teacher tabs -->
                <v-card v-else>
                    <v-card-text>
                        <div class="mb-2 text-h5 text-center">Teacher tasks</div>
                        <v-divider></v-divider>
                        <v-list>
                            <TeacherTasksList v-bind:user_id="user.id"></TeacherTasksList>
                        </v-list>
                    </v-card-text>
                </v-card>
                <v-row class="mt-1">
                <v-col md="12">
                    <v-btn block outlined to="/add" color="primary">ADD TASK</v-btn>
                </v-col>
        </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
// import DataService from "../../services/DataService";
import ExecutionTasksList from "../../components/ExecutionTasksList.vue";
import InspectionTasksList from "../../components/InspectionTasksList.vue";
import TeacherTasksList from "../../components/TeacherTasksList.vue";
import PersonalProfile from "../../components/PersonalProfile.vue";
import TeacherProfile from "../../components/TeacherProfile";
import StudentProfile from "../../components/StudentProfile";

export default {
    name: "mainPage",
    components: {
        ExecutionTasksList,
        InspectionTasksList,
        TeacherTasksList,
        PersonalProfile,
        TeacherProfile,
        StudentProfile,
    },
    computed: {
        isAuthenticated() {
            return this.$store.getters.IS_AUTHENTICATED;
        },
        user() {
            return this.$store.getters.GET_USER_OBJECT;
        },
    },
    data() {
        return {
            currentTab: null,
        };
    },
    methods: {
        redirectToTask(id) {
            console.log("Task:", id);
            this.$router.push(`/task/${id}`);
        },
    },
    mounted() {
        if (!this.isAuthenticated) {
            this.$router.push("/login");
        }
    },
};
</script>

<style>
.mydark {
    background: #1e1e1e;
    color: aliceblue;
}
</style>
