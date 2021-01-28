<template>
    <div>
        <v-list v-if="inspectionTasks">
            <v-list-item v-for="(task, index) in inspectionTasks"
                :key="index" class="tasks-list-item"
                @click="redirectToTask(task.id)">
                <v-list-item-content>
                    <a style="background: none">
                        {{ task.title }}
                    </a>
                </v-list-item-content>
            </v-list-item>
        </v-list>
        <v-list v-else>
            <v-list-item>
                <v-list-item-content>No tasks to inspect</v-list-item-content>
            </v-list-item>
        </v-list>
    </div>
</template>


<script>
import DataService from "../services/DataService";


export default {
    data() {
        return {
            inspectionTasks: null,
        }
    },
    methods: {
        getTasksToInspect: function() {
            DataService.getInspectionTasks()
            .then(response => response.data)
            .then((response => this.inspectionTasks = response))
            .then(() => console.log(this.inspectionTasks))
        },
        redirectToTask(id) {
          console.log("Task:", id)
          this.$router.push(`/task/${id}`)
        }
    },
    mounted() {
        this.getTasksToInspect()
    }
}
</script>