<template>
    <v-card>
        <div v-if="executionTasks">
            <v-list-item v-for="(task, index) in executionTasks"
                :key="index" class="tasks-list-item"
                @click="redirectToTask(task.id)">
                <v-list-item-content>
                    <a style="background: none">
                        {{ task.title }}
                    </a>
                </v-list-item-content>
            </v-list-item>
        </div>
        <div v-else>
            No tasks to execute
        </div>
    </v-card>
</template>


<script>
import DataService from "../services/DataService";


export default {
    data() {
        return {
            executionTasks: null,
        }
    },
    methods: {
        getTasksToExecute: function() {
            DataService.getExecutionTasks()
            .then(response => response.data)
            .then((response => this.executionTasks = response))
        },
        redirectToTask(id) {
          console.log("Task:", id)
          this.$router.push(`/task/${id}`)
        }
    },
    mounted() {
        this.getTasksToExecute()
    }
}
</script>