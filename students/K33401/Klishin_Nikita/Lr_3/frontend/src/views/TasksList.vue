<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card dark class="py-2">
                    <div class="text-h4">Tasks List</div>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col md="5">
                <v-card dark class="py-3 list-wrapper">
                    <div v-for="(task, index) in tasks" :key="index" class="list-item" :class="{ active: index == currentIndex }">
                        <div class="bn" @click="setActiveTask(task, index)">
                            {{ task.title }}
                        </div>
                    </div>
                </v-card>
            </v-col>

            <v-spacer></v-spacer>

            <v-col md="6">
                <v-card dark class="py-3">
                    <v-container>
                        <div v-if="currentTask">
                            <v-row class="mb-2">
                                <v-col cols="12">
                                    <div class="text-h6">Task detail information</div>
                                </v-col>
                            </v-row>
                            <v-divider></v-divider>
                            <v-row class="mt-2">
                                <div class="col-md-5">
                                    <label><strong>Title:</strong></label>
                                </div>
                                <div class="col-md-7">
                                    {{ currentTask.title }}
                                </div>
                            </v-row>
                            <v-row>
                                <div class="col-md-5">
                                    <label><strong>Description:</strong></label>
                                </div>
                                <div class="col-md-7">
                                    {{ currentTask.description }}
                                </div>
                            </v-row>
                            <v-row>
                                <div class="col-md-5">
                                    <label><strong>Status:</strong></label>
                                </div>
                                <div class="col-md-7">
                                    {{ currentTask.status }}
                                </div>
                            </v-row>
                        </div>
                        <div v-else>
                            <br />
                            <p>Please click on a Task...</p>
                        </div>
                    </v-container>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import "../assets/TasksList.css";

import DataService from "../services/DataService";

export default {
    name: "tasksList",
    data() {
        return {
            tasks: [],
            currentTask: null,
            currentIndex: -1,
            title: "Что-то(title)",
        };
    },
    methods: {
        retrieveTasks() {
            DataService.getAllTasks()
                .then((response) => {
                    this.tasks = response.data;
                    console.log(response.data);
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        setActiveTask(task, index) {
            this.currentTask = task;
            this.currentIndex = index;
        },
    },
    mounted() {
        this.retrieveTasks();
    },
};
</script>

<style scoped>
.bn {
    background: none;
}
</style>


