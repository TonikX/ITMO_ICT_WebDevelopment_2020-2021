<template>
    <div>
        <v-card v-if="!isLoading">
            <v-card-title>
                <div>Teacher Profile</div>
            </v-card-title>

            <v-card-text>
                <v-container>
                    <div>
                        <div>Teacher class</div>
                        <v-select
                            v-model="teacherObj.student_classes"
                            :items="allGroups"
                            label="Select Groups"
                            multiple
                            outlined
                        >
                            <template v-slot:selection="{ item, index }">
                                <v-chip>
                                    <span>{{ item.title }} {{ index }}</span>
                                </v-chip>
                            </template>
                            <template slot='item' slot-scope='{ item }'>
                                {{ item.title }}
                            </template>
                        </v-select>
                    </div>
                    <v-btn @click="patchTeacher()" block outlined color="primary" dark>SAVE CHANGES</v-btn>
                </v-container>

                <v-layout row wrap mt-7>
                    <v-flex offset-xs2 xs8>
                        <v-alert v-if="errors" dense outlined type="error" mx-auto>
                            {{ errors }}
                        </v-alert>
                    </v-flex>
                    <v-flex offset-xs1 xs10>
                        <SuccessAlert v-bind:message="success"></SuccessAlert>
                    </v-flex>
                </v-layout>
            </v-card-text>
        </v-card>
        <v-card v-else>
            <v-card-title>
                <div>Loading..Please wait</div>
            </v-card-title>
        </v-card>
    </div>
</template>

<script>
import DataService from "../services/DataService"

import SuccessAlert from "../components/SuccessAlert"
// import TeacherClass from "./TeacherClass.vue";

export default {
    name: "teacher-profile",
    computed: {
        user() {
            return this.$store.getters.GET_USER_OBJECT;
        },
    },
    components: {
        // TeacherClass,
        SuccessAlert
    },
    data() {
        return {
            isLoading: true,
            errors: null,
            success: null,
            userObj: "Я userObject",
            teacherObj: null,
            allGroups: null,
        };
    },
    mounted() {
        DataService.getTeacher(this.user.id)
            .then((response) => response.data)
            .then((tPr) => (this.teacherObj = tPr))
            .then(() => (this.isLoading = false))
            .catch((err) => (this.errors = err));

        DataService.getGroups()
            .then(response => response.data)
            .then(gr => this.allGroups = gr)
    },
    methods: {
        patchTeacher() {
            console.log("PatchTacher:",this.teacherObj)
            DataService.patchTeacher(this.user.id, this.teacherObj)
            .then(response => response.data)
            .then(res => this.success = res)
            .catch(err => this.errors = err.message)
        }
    }
};
</script>
