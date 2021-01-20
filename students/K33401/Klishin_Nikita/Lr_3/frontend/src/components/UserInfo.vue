<template>
    <v-layout row justify-center>
        <v-dialog width="500" persistent v-model="visible">
            <v-skeleton-loader v-if="isLoading" class="mx-auto"  type="image"></v-skeleton-loader>
            <v-card v-else>
                <v-card-text>
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-title class="headline mt-4">
                                {{ student.user.email }}
                            </v-list-item-title>
                            <v-list-item-subtitle class="text-body-1 mt-7">
                                <div v-if="!student.user.is_teacher">Student</div>
                                <div v-else>Teacher</div>
                            </v-list-item-subtitle>
                            <v-list-item-subtitle class="text-subtitle-1 mt-3">
                                Class: {{ student.student_class.title }}
                            </v-list-item-subtitle>
                        </v-list-item-content>

                        <v-list-item-avatar tile size="80" color="grey"></v-list-item-avatar>
                    </v-list-item>  
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" @click="close()">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-layout>
</template>


<script>
    export default {
        computed: {
            visible() {
                console.log("visible");
                return this.$store.getters.GET_USER_INFO_MODAL_VISIBILITY;
            },
            isLoading() {
                return this.$store.getters.GET_USER_INFO_MODAL_LOADING;
            },
            student() {
                return this.$store.getters.GET_USER_INFO_MODAL_MODEL;
            },
        },
        methods: {
            close() {
                this.$store.commit("SET_USER_INFO_MODAL_VISIBILITY", false);
            },
        },
        data() {
            return {
            };
        },
    };
</script>