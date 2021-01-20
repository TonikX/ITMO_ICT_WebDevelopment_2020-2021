<template>
    <div>
        <v-card v-if="!isLoading">
            <v-card-title>
                <div>Student Profile</div>
            </v-card-title>

            <v-card-text>
                <v-container>
                    <div>
                        <div>Student group</div>
                        <v-select
                            v-model="studentObj.student_class"
                            :items="allGroups"
                            label="Select your group"
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
                    <v-btn @click="patchStudent()" block outlined color="primary" dark>SAVE CHANGES</v-btn>
                </v-container>

                <v-flex v-if="error" xs10 offset-xs1>
                    <v-alert v-if="error" dense outlined type="error" mx-auto>
                        {{ error }}
                    </v-alert>
                </v-flex>
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
import DataService from "../services/DataService";


export default {
    name: "student-profile",
    computed: {
        user() {
            return this.$store.getters.GET_USER_OBJECT;
        },
    },
    components: {
        // TeacherClass,
    },
    data() {
        return {
            isLoading: true,
            error: null,
            userObj: "Я userObject",
            studentObj: null,
            allGroups: null,
        };
    },
    mounted() {
        DataService.getStudent(this.user.id)
            .then((response) => response.data)
            .then((tPr) => (this.studentObj = tPr))
            .then(() => (this.isLoading = false))
            .catch((err) => (this.error = err));

        DataService.getGroups()
            .then(response => response.data)
            .then(gr => this.allGroups = gr)
    },
    methods: {
        patchStudent() {
            console.log(this.studentObj)
            DataService.patchStudent(this.user.id, this.studentObj)
        }
    }
};
</script>
