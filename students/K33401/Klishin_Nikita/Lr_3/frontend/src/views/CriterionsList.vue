<template>
    <div>
        <v-container>
            <v-card class="mt-7">
                <v-list>
                    <v-list-item v-for="criterion of criterions" :key="criterion.id">
                        <v-container>
                            <div class="d-flex justify-space-around">
                                <div>{{ criterion.title }}</div>
                                <div>{{ criterion.description }}</div>
                                <div>{{ criterion.weight }}</div>
                            </div>
                        </v-container>
                    </v-list-item>
                </v-list>
                <v-divider></v-divider>
                <v-row justify="center" class="mt-2 pb-1">
                    <v-dialog v-model="dialog" persistent max-width="600px">
                        <template v-slot:activator="{ on, attrs }">
                            <v-col offset-md="1" md="10">
                                <v-btn color="primary" block outlined dark v-bind="attrs" v-on="on"> ADD CRITERION </v-btn>
                            </v-col>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="headline">Criterion</span>
                            </v-card-title>
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12">
                                            <v-text-field v-model="newCritarion.title" label="Title" required type="text"></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field
                                                v-model="newCritarion.description"
                                                label="Description"
                                                type="text"
                                                required
                                            ></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field
                                                v-model="newCritarion.weight"
                                                label="Weight"
                                                type="number"
                                                required
                                            ></v-text-field>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="dialog = false"> Close </v-btn>
                                <v-btn color="blue darken-1" text @click="pushCriterion()"> Save </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-row>
                <v-row>
                    <v-col class="d-flex justify-center" offset-md="2" md="8">
                        <SuccessAlert v-bind:message="success"></SuccessAlert>
                    </v-col>
                </v-row>
            </v-card>
        </v-container>
    </div>
</template>


<script>
import DataService from "../services/DataService";

import SuccessAlert from "../components/SuccessAlert";

export default {
    components: {
        SuccessAlert,
    },
    data() {
        return {
            criterions: null,
            dialog: false,
            newCritarion: {
                title: null,
                description: null,
                weight: null,
            },
            success: null,
        };
    },
    mounted() {
        DataService.getCriterions()
            .then((response) => response.data)
            .then((vs) => (this.criterions = vs));
    },
    methods: {
        pushCriterion() {
            console.log("PushCriterion");
            DataService.addCriterion(this.newCritarion) //TODO обработка ошибок
            .then(response => response.status)
            .then(res => this.success = res)
            this.dialog = false;
        },
    },
};
</script>
