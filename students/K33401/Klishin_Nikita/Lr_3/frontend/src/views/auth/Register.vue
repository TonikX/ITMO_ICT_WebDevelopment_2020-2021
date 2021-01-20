<template>
    <v-container fluid>
        <v-layout row wrap>
            <v-flex xs12 class="text-xs-center" mt-5>
                <h1>Sign Up</h1>
            </v-flex>
            <v-flex xs12 sm6 offset-sm3 mt-3>
                <v-form>
                    <v-container>
                        <v-flex>
                            <v-text-field
                                v-model="newUser.email"
                                name="email"
                                label="Email"
                                id="email"
                                type="email"
                                required
                            ></v-text-field>
                        </v-flex>
                        <v-flex>
                            <v-text-field
                                v-model="newUser.password"
                                name="password"
                                label="Password"
                                id="password"
                                type="password"
                                required
                            ></v-text-field>
                        </v-flex>
                        <v-flex>
                            <v-text-field
                                v-model="newUser.confPassword"
                                name="confirmPassword"
                                label="Confirm Password"
                                id="confirmPassword"
                                type="password"
                                required
                            ></v-text-field>
                        </v-flex>
                        <v-flex>
                            <v-container class="px-0" fluid>
                                <v-checkbox v-model="newUser.isTeacher" :label="`Teacher: ${newUser.isTeacher.toString()}`"></v-checkbox>
                            </v-container>
                        </v-flex>
                        <v-flex class="text-xs-center" mt-5>
                            <v-btn @click="register()" block outlined color="primary">Sign Up</v-btn>
                        </v-flex>
                    </v-container>
                </v-form>
                <v-layout row wrap mt-7>
                    <v-flex offset-xs2 xs8>
                        <v-alert v-if="errors" dense outlined type="error" mx-auto>
                            {{ errors }}
                        </v-alert>
                    </v-flex>
                    <v-flex offset-xs2 xs8>
                        <v-alert v-if="success" dense outlined type="success" mx-auto>
                            {{ success }}
                        </v-alert>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import DataService from '../../services/DataService';


export default {
    name: "",
    components: {
    },
    data() {
        return {
            newUser: {
                email: null,
                password: null,
                confPassword: null,
                isTeacher: false,
            },
            errors: null,
            success: null,
        };
    },
    methods: {
        register() {
            if (this.newUser.confPassword !== this.newUser.password) {
                this.errors = "Пароли не совпадают!";
            } else {
                console.log("Register");
                DataService.registerUser(this.newUser)
                .then(response => response.data)
                .then(res => {
                  this.success = res
                  this.errors = null
                })
                .catch(err => this.errors = err.message)
            }
        },
    },
};
</script>