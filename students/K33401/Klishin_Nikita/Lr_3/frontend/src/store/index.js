import Vue from 'vue'
import Vuex from 'vuex'

import DataService from "../services/DataService"

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        authentification: {
            authentificated: false,
            token: null,
            userObject: null
        },
        userInfoModal: {
            visible: false,
            id: null,
            loading: false,
            model: null
        },
        currentTask: { // current task
            loading: true,
            taskId: null,
            title: null,
            taskObj: null,
            baseTaskObj: { },
            teacherStudents: null,
            criterions: null,

            solutionInspections: { },
            inspectionsLoading: true
        },
        allCriterions: null, // TODO переделать критерии
    },
    actions: {
        LOGIN: (context, login_token) => {
            context.commit('SET_AUTHENTIICATION_TOKEN', login_token)
            DataService.getUser(login_token)
            .then(response => response.data)
            .then(user => context.state.authentification.userObject = user)
            .then(() => context.commit('SET_AUTHENTIICATED', true))
        }, // TODO add logout
        LOAD_CRITERIONS: (context) => { // TODO можно не доделывать
            if (!context.state.allCriterions) {
                DataService.getCriterions()
                .then(response => response.data)
                .then(res => context.state.allCriterions = res)
            }
        },
        LOAD_INSPECTIONS: (context, solution_id) => {
            console.log("Store -> LOAD_INSPECTIONS:", solution_id)
            if (!context.state.currentTask.solutionInspections[solution_id]) {
                context.state.currentTask.inspectionsLoading = true
                DataService.getInspections(solution_id)
                .then(response => response.data)
                .then(res => context.state.currentTask.solutionInspections[solution_id] = res)
                .then(() => context.state.currentTask.inspectionsLoading = false)
            }
        },
        SET_USER_INFO_MODAL_ID: (context, id) => {
            if (context.state.userInfoModal.id !== id || !context.getters.GET_USER_INFO_MODAL_MODEL) { //поправить
                console.log("here")
                context.commit('SET_USER_INFO_MODAL_LOADING', true)
                DataService.getStudent(id)
                .then(response => response.data)
                .then(stidentObj => context.commit('SET_USER_INFO_MODAL_MODEL', stidentObj))
                .then(() => context.commit('SET_USER_INFO_MODAL_LOADING', false))
            }
        },
        SET_CURRENT_TASK_ID: (context, task_id) => {
            if (task_id !== context.state.currentTask.taskId || context.state.currentTask.taskObj === null) {
                context.state.currentTask.loading = true,
                context.state.currentTask.taskId = task_id
                DataService.getTask(task_id)
                .then(response => response.data)
                .then(taskData => context.state.currentTask.taskObj = taskData)
                .then(() => Object.assign(context.state.currentTask.baseTaskObj, context.state.currentTask.taskObj))
                .then(() => context.state.currentTask.loading = false)
            }
        },
        REFRESH_CURRENT_TASK: (context) => {
            DataService.getTask(context.state.currentTask.taskId)
                .then(response => response.data)
                .then(taskData => context.state.currentTask.taskObj = taskData)
        },
        PATCH_CURRENT_TASK: (context) => {
            let formedTask = { }
            Object.assign(formedTask, context.state.currentTask.taskObj)
            console.log("Cur task:", formedTask)
            formedTask.criterions = formedTask.criterions.map(criterion => criterion.id)
            console.log("Formed cur task:", formedTask)
            DataService.patchTask(context.state.currentTask.taskId, formedTask)
        },
        REMOVE_CURRENT_TASK: (context) => {
            console.log("Store -> Remove current task:", context.state.currentTask.taskId);
            DataService.removeTask(context.state.currentTask.taskId)
            context.state.currentTask.taskId = null
            context.state.currentTask.taskObj = null
            context.state.currentTask.baseTaskObj = { }
            context.state.currentTask.criterions = null
        },
        PATCH_USER: (context) => {
            DataService.patchUser(context.state.authentification.userObject)
        },
        PUSH_INSPECTION: (context, inspectionData) => {
            console.log("Store -> push inp:", inspectionData.data)
            DataService.pushInspection(inspectionData.id, {
                solution: inspectionData.data.solution,
                score: inspectionData.data.score,
                inspector: inspectionData.data.inspector.id,
            })
            .then(context.commit('ADD_INSPECTION', inspectionData))
        }
    },
    mutations: {
        SET_AUTHENTIICATION_TOKEN: (state, authToken) => {
            state.authentification.token = authToken
        },
        SET_AUTHENTIICATED: (state, paylaod) => {
            state.authentification.authentificated = paylaod
        },
        SET_USER_INFO_MODAL_VISIBILITY: (state, setVisible) => {
            state.userInfoModal.visible = setVisible
        },
        SET_USER_INFO_MODAL_LOADING: (state, setLoading) => {
            state.userInfoModal.loading = setLoading
        },
        SET_USER_INFO_MODAL_ID: (state, id) => {
            state.userInfoModal.id = id
        },
        SET_USER_INFO_MODAL_MODEL: (state, studentObj) => {
            state.userInfoModal.model = studentObj;
        },
        ADD_INSPECTION: (state, inspectionData) => {
            state.currentTask.solutionInspections[inspectionData.id].push(inspectionData.data)
        }
    },
    getters: {
        IS_AUTHENTICATED(state) {
            return state.authentification.authentificated
        },
        GET_USER_TOKEN(state) {
            return state.authentification.token
        },
        GET_USER_OBJECT(state) {
            return state.authentification.userObject
        },
        GET_USER_INFO_MODAL_VISIBILITY(state) {
            return state.userInfoModal.visible
        },
        GET_USER_INFO_MODAL_LOADING(state) {
            return state.userInfoModal.loading
        },
        GET_USER_INFO_MODAL_ID(state) {
            return state.userInfoModal.id
        },
        GET_USER_INFO_MODAL_MODEL(state) {
            return state.userInfoModal.model
        },
        GET_CURRENT_TASK_ID(state) {
            return state.currentTask.taskId
        },
        GET_CURRENT_TASK(state) {
            return state.currentTask.taskObj
        },
        IS_CURRENT_TASK_BASE(state) {
            return state.currentTask.baseTaskObj
        },
        GET_CURRENT_TASK_LOADING(state) {
            return state.currentTask.loading
        },
        GET_CURRENT_TASK_INSPECTORS(state) {
            return state.currentTask.taskObj.inspections
        },
        GET_CURRENT_TASK_EXECUTORS(state) {
            return state.currentTask.taskObj.executors
        },
        GET_CURRENT_TASK_CRITERIONS(state) {
            return state.currentTask.taskObj.criterions
        },
        GET_CURRENT_TASK_INSPECTION_LAODING(state) {
            return state.currentTask.inspectionsLoading
        },
        GET_CURRENT_TASK_INSPECTIONS(state) {
            return state.currentTask.solutionInspections
        }
    },

    modules: {

    }
})