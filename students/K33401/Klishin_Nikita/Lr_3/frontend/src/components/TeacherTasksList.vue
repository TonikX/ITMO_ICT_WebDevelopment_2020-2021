<template>
        <div v-if="tasks">
            <v-list-item v-for="(task, index) in tasks"
                :key="index" class="tasks-list-item"
                @click="redirectToTask(task.id)">
                <v-list-item-content>
                    <div class="text-body-1">{{ task.title }}</div>
                </v-list-item-content>
            </v-list-item>
        </div>
        <div v-else>
            No tasks
        </div>
</template>


<script>
import DataService from "../services/DataService";


export default {
    props: {
        user_id: Number,
    },
    data() {
        return {
            tasks: null,
        }
    },
    methods: {
        getTasks: function() {
            console.log("User id:", this.user_id)
            DataService.getTeacherTasks(this.user_id)
            .then(response => response.data)
            .then((response => this.tasks = response))
        },
        redirectToTask(id) {
          console.log("Task:", id)
          this.$router.push(`/task/${id}`)
        }
    },
    mounted() {
        this.getTasks()
    }
}
</script>