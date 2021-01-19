<template>
<div>
    <v-container>
        <v-row class="mt-7">
            <v-col cols="12"><div class="text-h4">Add task page</div></v-col>
        </v-row>
        <v-row class="mt-7">
            <v-col cols="12" offset-md="3" md="6">
                <v-form lazy-validation>
                    <v-container>
                        <v-row>
                            <v-text-field v-model="newTask.title" label="Title" aria-required=""></v-text-field>
                        </v-row>
                        <v-row>
                            <v-textarea
                                v-model="newTask.description"
                                name="input-7-1"
                                label="Description"
                                hint="Enter task description">
                            </v-textarea>
                        </v-row>
                        <v-row class="mt-2">
                            <v-select
                                v-model="newTask.criterions"
                                :items="criterion.options"
                                item-value="id"
                                item-text="title"
                                :menu-props="{ maxHeight: '400' }"
                                label="Select"
                                multiple
                                hint="Select criterions for this task"
                                persistent-hint>
                                <template slot='selection' slot-scope='{ item }'>
                                    {{ item.title }}
                                </template>
                                <template slot='item' slot-scope='{ item }'>
                                    {{ item.title }} - {{ item.description }}
                                </template>
                            </v-select>
                        </v-row>
                        <v-row class="mt-9">
                            <v-btn @click.prevent="pushTask()" block outlined color="primary">Add task</v-btn>
                        </v-row>
                        <v-row v-if="errors">
                            <v-alert v-if="errors" dense outlined type="error" mx-auto>
                                {{ errors }} 
                            </v-alert>
                            <v-alert v-if="errors" dense outlined type="error" mx-auto>
                                {{ errors }} 
                            </v-alert>
                        </v-row>
                    </v-container>
                </v-form>
            </v-col>
        </v-row>
    </v-container>
</div>
</template>

<script>
import DataService from "../services/DataService"


export default {
    mounted() {
        if(!this.$store.getters.IS_AUTHENTICATED) {
            this.$router.push("/login")
        }
        DataService.getCriterions()
        .then(response => response.data)
        .then(vs => this.criterion.options = vs)
    },
    data() {
        return {
            criterion: {
                options: [
                    "First option",
                    "Second option",
                    "Third option"
                ]
            },
            newTask: {
                title: null,
                description: null,
                criterions: null,
                executors: [],
                inspections: [],
                status: 0
            },
            errors: null,
            success: null,
        }
    },
    methods: {
        pushTask() {
            console.log("AddTask -> Push task:", this.newTask)
            DataService.addTask(JSON.stringify(this.newTask))
            .then(response => {
                console.log(response)
                return response
            })
            .then(response => this.success = response)
            .catch(err => this.errors = err.response.data)
        }
    }
}
</script>
