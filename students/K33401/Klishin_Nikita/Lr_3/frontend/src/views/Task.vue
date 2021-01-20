<template>
    <div>
        <div v-if="isLoading" class="">
            <v-progress-linear indeterminate height="25"> </v-progress-linear>
        </div>
        <v-container v-else class="mt-12">
            <v-row>
                <v-col md="8" class="pt-0">
                    <v-card class="mx-auto" elevation="2" outlined>
                        <!-- Title -->
                        <v-row class="ma-0">
                            <v-col md="8" offset-md="2">
                                <div class="text-h4 mt-5 mb-3">{{ task.title }} ID: {{ task.id }}</div>
                            </v-col>
                        </v-row>

                        <v-divider />

                        <!-- Description -->
                        <v-row class="mt-5 mb-5">
                            <v-col md="4" offset-md="4">
                                <div class="text-h5">
                                    {{ task.description }}
                                </div>
                            </v-col>
                        </v-row>

                        <v-divider />

                        <!-- Solution -->
                        <v-row v-if="showSolution && !user.is_teacher && isExecutor" class="mx-0 pa-3">
                            <v-col cols="12">
                                <v-form v-on:submit.prevent="sendSolution">
                                    <v-container fluid>
                                        <ErrorAlert v-bind:message="solution.solutionErrorMessage"></ErrorAlert>
                                        <SuccessAlert v-bind:message="solution.solutionSuccessMessage"></SuccessAlert>
                                        <v-row>
                                            <v-col cols="12">
                                                <label for="solutionTextarea" class="text-h5">Enter your solution</label>
                                                <v-textarea outlined class="mt-7" v-model="solution.data" id="solutionTextarea" rows="5" />
                                            </v-col>
                                            <v-col cols="12" class="pt-0">
                                                <v-btn @click="pushSolution()" block outlined color="primary">Submit</v-btn>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-form>
                            </v-col>
                        </v-row>
                        <v-row v-else>
                            <v-col md="12" class="mt-3">
                                <div class="text-subtitle-1">Вы не можете выполнять данное задание</div>
                            </v-col>
                        </v-row>

                        <v-list class="mb-7">
                            <!-- Show Solutions -->
                            <v-list-item v-if="showSolutions">
                                <v-list-item-content>
                                    <v-list-item-title>
                                        <div class="text-h5">Solutions</div>
                                    </v-list-item-title>
                                    <v-container>
                                            <v-row>
                                                <v-col md="4" class="text-center text-subtitle-1">Author</v-col>
                                                <v-col md="4" class="text-center text-subtitle-1">Solution</v-col>
                                                <v-col md="4" class="text-left text-subtitle-1">Score</v-col>
                                            </v-row>
                                            <v-divider></v-divider>
                                            <v-row v-for="(currentSolution, index) in solutions" :key="index" class="mt-1">
                                                <v-col md="4">
                                                    {{ currentSolution.executor.email }}
                                                </v-col>
                                                <v-col md="4">
                                                    {{ currentSolution.data }}
                                                </v-col>
                                                <!-- v-if="isInspector()" -->
                                                <v-col md="4">
                                                    <!-- <v-form>
                                                        <input v-model.number="currentSolution.score" type="number" id="score-field" />
                                                    </v-form> -->
                                                    <SolutionInspectionsList v-bind:solution_id="currentSolution.id" v-bind:isInspector="isInspector"></SolutionInspectionsList>
                                                </v-col>
                                            </v-row>
                                        </v-container>
                                    <!-- <v-row v-if="isInspector()">
                                        <v-btn @click="saveScores" outlined>Save scores</v-btn>
                                    </v-row> -->
                                </v-list-item-content>
                            </v-list-item>

                            <!-- Show Executors -->
                            <v-list-item v-if="showExecutors">
                                <v-list-item-content>
                                    <v-list-item-content-title><div class="text-h5">Executors</div></v-list-item-content-title>
                                    <div class="text-center" v-if="executors.length !== 0">
                                        <v-chip
                                            v-for="(executor, index) in executors"
                                            :key="index"
                                            class="ma-2"
                                            v-on:click="showUserInfo(executor.id)"
                                        >
                                            {{ executor.email }}
                                        </v-chip>
                                    </div>
                                    <div v-else>
                                        <div class="mt-3">No Executors</div>
                                    </div>
                                    <div v-if="user.is_teacher" class="mt-3">
                                        <ChangeExecutors></ChangeExecutors>
                                    </div>
                                </v-list-item-content>
                            </v-list-item>

                            <!-- Show Inspectors -->
                            <v-list-item v-if="showInspectors">
                                <v-list-item-content>
                                    <v-list-item-title><div class="text-h5">Inspectors</div></v-list-item-title>
                                    <div class="text-center">
                                        <div v-if="inspectors.length !== 0">
                                            <v-chip
                                                v-for="(inspector, index) in inspectors"
                                                :key="index"
                                                class="ma-2"
                                                v-on:click="showUserInfo(inspector.id)"
                                            >
                                                {{ inspector.email }}
                                            </v-chip>
                                        </div>
                                        <div v-else>
                                            <div class="mt-3">No Inspectors</div>
                                        </div>
                                    </div>
                                    <div v-if="user.is_teacher" class="mt-3">
                                        <ChangeInspectors></ChangeInspectors>
                                    </div>
                                </v-list-item-content>
                            </v-list-item>

                            <!-- Show Criteions -->
                            <v-list-item v-if="showCriterions">
                                <v-list-item-content>
                                    <v-list-item-title><div class="text-h5">Criterions</div></v-list-item-title>
                                    <div class="text-center">
                                        <v-list v-if="criterions.length !== 0">
                                            <v-list-item-group>
                                                <v-list-item v-for="(criterion, index) in criterions" :key="index" class="ma-2">
                                                    <v-row>
                                                        <v-col md="4"> {{ criterion.title }} </v-col>
                                                        <v-col md="4"> {{ criterion.description }} </v-col>
                                                        <v-col md="4"> {{ criterion.weight }} </v-col>
                                                    </v-row>
                                                </v-list-item>
                                            </v-list-item-group>
                                        </v-list>
                                        <div v-else>
                                            <div class="mt-3">No Criterions</div>
                                        </div>
                                    </div>
                                </v-list-item-content>
                            </v-list-item>

                            <!-- Edit -->
                            <v-list-item v-if="editor.visible">
                                <v-list-item-content>
                                    <v-form v-model="valid">
                                        <v-container>
                                            <v-row>
                                                <v-col md="4" class="d-flex justify-center align-center">
                                                    <div class="text-h5">Title</div>
                                                </v-col>
                                                <v-spacer></v-spacer>
                                                <v-col md="6">
                                                    <v-text-field v-model="task.title" :value="task.title"></v-text-field>
                                                </v-col>
                                            </v-row>
                                            <v-row>
                                                <v-col md="4" class="d-flex justify-center align-center">
                                                    <div class="text-h5">Description</div>
                                                </v-col>
                                                <v-spacer></v-spacer>
                                                <v-col md="6">
                                                    <v-text-field v-model="task.description" :value="task.description"></v-text-field>
                                                </v-col>
                                            </v-row>
                                            <v-row>
                                                <v-col md="4" class="d-flex justify-center align-center">
                                                    <div class="text-h5">Criterion</div>
                                                </v-col>
                                                <v-spacer></v-spacer>
                                                <v-col md="6">
                                                    <v-select
                                                        v-model="task.criterions"
                                                        :items="editor.avCriterions"
                                                        :menu-props="{
                                                            maxHeight: '400',
                                                        }"
                                                        label="Select"
                                                        multiple
                                                        hint="Select criterions for this task"
                                                        persistent-hint
                                                    >
                                                        <template slot="selection" slot-scope="{ item }">
                                                            {{ item.title }}
                                                        </template>
                                                        <template slot="item" slot-scope="{ item }">
                                                            {{ item.title }} - {{ item.description }}
                                                        </template>
                                                    </v-select>
                                                </v-col>
                                            </v-row>
                                            <v-row class="mt-3">
                                                <v-btn @click="patchTask()" block outlined color="primary" dark>SAVE</v-btn>
                                            </v-row>
                                        </v-container>
                                    </v-form>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list>
                        <!-- Remove task -->
                        <v-dialog v-model="removeDialog" max-width="350">
                            <v-card>
                                <v-card-title class="headline"> Удалить текущую задачу? </v-card-title>

                                <v-card-text>
                                    Это действие отменить невозможно
                                </v-card-text>

                                <v-card-actions>
                                    <v-spacer></v-spacer>

                                    <v-btn color="green darken-1" text @click="removeDialog = false"> Disagree </v-btn>

                                    <v-btn color="green darken-1" text @click="removeTask()"> Agree </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                        <UserInfo />
                    </v-card>
                </v-col>

                <v-spacer></v-spacer>

                <!-- Боковая панель -->
                <v-col md="3">
                    <v-row>
                        <v-card>
                            <v-list flat>
                                <v-list-item-group color="primary">
                                    <v-list-item @click="getSolutions()"> Show Solutions </v-list-item>
                                    <v-list-item>
                                        <div @click="showExecutors = !showExecutors">Show Executors</div>
                                    </v-list-item>
                                    <v-list-item>
                                        <div @click="showInspectors = !showInspectors">Show Inspectors</div>
                                    </v-list-item>
                                    <v-list-item>
                                        <div @click="showCriterions = !showCriterions">Show Criterions</div>
                                    </v-list-item>
                                    <v-list-item v-if="user.is_teacher" @click="showEditor()">
                                        <div>Edit</div>
                                    </v-list-item>
                                    <v-list-item v-if="user.is_teacher" @click="removeDialog = !removeDialog">
                                        <div>Remove</div>
                                    </v-list-item>
                                </v-list-item-group>
                            </v-list>
                        </v-card>
                    </v-row>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import DataService from "../services/DataService";

import UserInfo from "../components/UserInfo.vue";
import ChangeInspectors from "../components/ChangeInspectors.vue";
import ChangeExecutors from "../components/ChangeExecutors.vue";
import SuccessAlert from "../components/SuccessAlert";
import ErrorAlert from "../components/ErrorAlert";
import SolutionInspectionsList from "../components/SolutionInspectionsList";

export default {
    components: {
        UserInfo,
        ChangeInspectors,
        ChangeExecutors,
        SuccessAlert,
        ErrorAlert,
        SolutionInspectionsList,
    },

    name: "taskView",
    computed: {
        isAuthenticated() {
            return this.$store.getters.IS_AUTHENTICATED;
        },
        isLoading() {
            return this.$store.getters.GET_CURRENT_TASK_LOADING;
        },
        user() {
            return this.$store.getters.GET_USER_OBJECT;
        },
        executors() {
            return this.$store.getters.GET_CURRENT_TASK_EXECUTORS;
        },
        inspectors() {
            return this.$store.getters.GET_CURRENT_TASK_INSPECTORS;
        },
        task() {
            return this.$store.getters.GET_CURRENT_TASK;
        },
        criterions() {
            return this.$store.getters.GET_CURRENT_TASK_CRITERIONS;
        },
        isExecutor() {
            return this.task.executors.map((executor) => executor.email).includes(this.user.email);
        },
        isInspector() {
            return this.task.inspections.map((inspector) => inspector.email).includes(this.user.email);
        }
    },
    data() {
        return {
            taskId: this.$route.params.id,
            solutions: null,

            showSolution: true,
            showSolutions: false,
            showExecutors: false,
            showInspectors: false,
            showCriterions: false,

            editor: {
                visible: false,
                avCriterions: null,
            },

            solution: {
                // данные решения задачи
                data: null,
                solutionErrorMessage: null,
                solutionSuccessMessage: null,
            },

            removeDialog: false,
        };
    },
    methods: {
        pushSolution: function () {
            let postData = {
                data: this.solution.data,
                user: this.user,
            };
            DataService.addTaskSolution(this.taskId, postData)
                .then((response) => (this.solution.solutionSuccessMessage = response.data))
                .then(() => (this.showSolution = false))
                .then(() => this.refreshSolutions())
                .catch((err) => (this.solutions.solutionErrorMessage = err.message));
        },
        patchTask() {
            this.$store.dispatch("PATCH_CURRENT_TASK");
        },
        removeTask() {
            this.removeDialog = false;
            this.$store.dispatch("REMOVE_CURRENT_TASK")
            this.$router.push('/')
        },
        showUserInfo: function (student_id) {
            this.$store.commit("SET_USER_INFO_MODAL_VISIBILITY", true);
            this.$store.dispatch("SET_USER_INFO_MODAL_ID", student_id);
        },
        showEditor: function () {
            if (this.editor.visible) {
                this.editor.visible = false;
            } else {
                if (!this.editor.avCriterions) {
                    DataService.getCriterions()
                        .then((response) => response.data)
                        .then((d) => (this.editor.avCriterions = d))
                        .then((this.editor.visible = true));
                } else {
                    this.editor.visible = true;
                }
            }
        },
        refreshSolutions: function () {
            return DataService.getTaskSolutions(this.task.id).then((response) => (this.solutions = response.data));
        },

        getSolutions: function () {
            if (this.showSolutions === true) {
                this.showSolutions = false;
            } else {
                if (this.solutions === null) {
                    this.refreshSolutions().then((this.showSolutions = true));
                }
                this.showSolutions = true;
            }
        },
    },
    mounted() {
        if (!this.isAuthenticated) {
            // если аноним
            this.$router.push("/login");
        }

        this.$store.dispatch("SET_CURRENT_TASK_ID", this.taskId);
    },
};
</script>

<style scoped>
td {
    height: 17px;
}
</style>
