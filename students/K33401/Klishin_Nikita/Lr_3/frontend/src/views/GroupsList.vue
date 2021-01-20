<template>
    <div>
        <v-container>
            <v-row class="mt-7">
                <v-col cols="12">
                    <v-card>
                        <v-card-title>
                            <v-col cols="12">
                                <div class="text-h4">Student classes</div>
                            </v-col>
                        </v-card-title>
                        <v-divider></v-divider>
                        <v-container>
                            <v-row>
                                <v-col md="6">
                                    <v-list>
                                        <v-list-item-group>
                                            <v-list-item
                                            v-for="group of groups"
                                            :key="group.id"
                                            @click="setActiveGroup(group.id)">
                                            <v-container>
                                                <div class="d-flex justify-space-around">
                                                    <div>
                                                        {{ group.title }}
                                                    </div>
                                                </div>
                                            </v-container>
                                        </v-list-item>
                                        </v-list-item-group>
                                    </v-list>
                                </v-col>
                                <v-divider vertical></v-divider>
                                <v-col md="6" class="ml-n1">
                                    <div v-if="currentGroupId == -1">
                                        Select group...
                                    </div>
                                    <div v-else>
                                        <v-container>
                                            <v-row class="mb-1">
                                                <v-col md="6">
                                                    <div class="text-subtitle-1">Group ID</div>
                                                </v-col>
                                                <v-col md="6">
                                                    {{ currentGroup.id }}
                                                </v-col>
                                            </v-row>
                                            <v-divider></v-divider>
                                            <v-row class="mt-1 mb-1">
                                                <v-col md="6">
                                                    <div class="text-subtitle-1">Number</div>
                                                </v-col>
                                                <v-col md="6">
                                                    {{ currentGroup.title }}
                                                </v-col>
                                            </v-row>
                                            <v-divider></v-divider>
                                            <v-row class="mt-1">
                                                <v-col md="6">
                                                    <div class="text-subtitle-1">Teacher</div>
                                                </v-col>
                                                <v-col md="6">
                                                    <div v-if="currentGroup.teacher">
                                                        {{ currentGroup.teacher }}
                                                    </div>
                                                    <div v-else>
                                                        Teacher is not selected
                                                    </div>
                                                </v-col>
                                            </v-row>
                                        </v-container>
                                    </div>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import DataService from "../services/DataService";

export default {
    mounted() {
        if (!this.$store.getters.IS_AUTHENTICATED) {
            this.$router.push("/login");
        }
        DataService.getGroups()
            .then((response) => response.data)
            .then((vs) => (this.groups = vs));
    },
    computed: {
        currentGroup() {
            return this.groups.filter((group) => group.id === this.currentGroupId)[0]
        }
    },
    data() {
        return {
            groups: null,
            newTask: {
                title: null,
                description: null,
                criterions: null,
                executors: [],
                inspections: [],
                status: 0,
            },
            currentGroupId: -1,
            errors: null,
            success: null,
        };
    },
    methods: {
        setActiveGroup(groupd_id) {
            this.currentGroupId = groupd_id
        },
        pushTask() {
            console.log("AddTask -> Push task:", this.newTask);
            DataService.addTask(JSON.stringify(this.newTask))
                .then((response) => {
                    console.log(response);
                    return response;
                })
                .then((response) => (this.success = response))
                .catch((err) => (this.errors = err.response.data));
        },
    },
};
</script>