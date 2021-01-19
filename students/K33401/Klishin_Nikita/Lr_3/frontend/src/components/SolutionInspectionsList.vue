<template>
    <div>
        <v-btn outlined color="primary" dark @click="showDialog(true)"> SHOW INSPECTIONS </v-btn>
        <v-dialog v-model="visible" scrollable max-width="540px">
            <v-card v-if="!isLoading">
                <v-card-title>Inspections</v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                    <v-list>
                        <v-list-item>
                            <v-row>
                                <v-col md="6"><div class="text-subtitle-1">Inspector</div></v-col>
                                <v-spacer></v-spacer>
                                <v-col md="4"><div class="text-subtitle-1">Score</div></v-col>
                            </v-row>
                        </v-list-item>
                        <v-list-item v-for="inspection of inspections" :key="inspection.id">
                            <v-row>
                                <v-col md="6">
                                    <div>{{ inspection.inspector.email }}</div>
                                </v-col>
                                <v-spacer></v-spacer>
                                <v-col md="4">
                                    <div>{{ inspection.score }}</div>
                                </v-col>
                            </v-row>
                        </v-list-item>
                        <v-divider v-if="newInspectionEditor"></v-divider>
                        <v-list-item v-if="newInspectionEditor">
                            <v-row class="mt-1">
                                <v-col md="4">
                                    <v-text-field v-model="newInspection.score" label="Put your score" type="number" required></v-text-field>
                                </v-col>
                                <v-spacer></v-spacer>
                                <v-col md="4" class="d-flex align-center">
                                    <v-btn @click="addInspection()" block outlined color="primary" dark>SAVE</v-btn>
                                </v-col>
                            </v-row>
                        </v-list-item>
                    </v-list>
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-btn color="blue darken-1" text @click="visible = false"> Close </v-btn>
                    <v-btn v-if="isInspector" color="blue darken-1" text @click="newInspectionEditor = true"> Add </v-btn>
                </v-card-actions>
            </v-card>
            <v-card v-else>
                <v-card-title primary-title> Loading... </v-card-title>
            </v-card>
        </v-dialog>
    </div>
</template>
<script>
export default {
    props: {
        solution_id: Number,
        isInspector: Boolean,
    },
    computed: {
        isLoading() {
            return this.$store.getters.GET_CURRENT_TASK_INSPECTION_LAODING;
        },
        inspections() {
            return this.$store.getters.GET_CURRENT_TASK_INSPECTIONS[this.solution_id];
        },
    },
    data() {
        return {
            visible: false,
            inspectors: [
                {
                    email: "4343",
                },
            ],
            teacherStudents: null,
            newInspectionEditor: false,
            newInspection: {
                solution: this.solution_id,
                score: null,
                inspector: null,
            }
        };
    },
    methods: {
        showDialog(isShow) {
            if (isShow) {
                this.visible = true;
                console.log("SolutionInspectors ->", this.solution_id);
                this.$store.dispatch("LOAD_INSPECTIONS", this.solution_id);
            }
        },
        addInspection() {
            this.newInspection.inspector = this.$store.getters.GET_USER_OBJECT
            console.log("Add Inspection:", this.newInspection);
            this.$store.dispatch("PUSH_INSPECTION", {id: this.solution_id, data: this.newInspection})
            this.newInspectionEditor = false
        },
    },
};
</script>
