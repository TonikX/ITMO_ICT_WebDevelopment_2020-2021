import axios from "axios"
import store from '../store'

const http = axios.create({
  baseURL: "http://localhost:8003",
  headers: {
    "Content-type": "application/json",
    "Access-Control-Allow-Origin": '*',
  }
})

class DataService {
  get(url, params) {
    if (params) {
      return http.get(url, params);
    } else {
      return http.get(url)
    }
  }

  post(url, data) {
    return http.post(url, data);
  }

  patch(url, data) {
    return http.patch(url, data);
  }

  getInspections(solution_id) {
    return http.get(`api/solution_inspections/${solution_id}/`)
  }

  pushInspection(solution_id, inspectionData) {
    console.log("DS -> ", inspectionData)
    return http.post(`api/solution_inspections/${solution_id}/`, inspectionData)
  }

  registerUser(userData) {
    return http.post('auth/users/', userData);
  }

  patchUser(userData) {
    const t = 'Token ' + store.getters.GET_USER_TOKEN
    return http.patch(`auth/users/me/`, userData, {
      headers: {
        Authorization: t
      }
    });
  }

  addTask(taskData) {
    return http.post('api/tasks/', taskData, {
      headers: {
        Authorization: 'Token ' + localStorage.getItem('token')
      }
    })
  }

  getTaskExecutors(task_id) {
    return http.get(`api/task/${task_id}/executors/`)
  }

  getTaskInspectors(task_id) {
    return http.get(`api/task/${task_id}/inspectors/`)
  }

  patchTask(task_id, taskData) {
    return http.patch(`api/task/${task_id}/`, taskData)
  }

  removeTask(task_id) {
    return http.delete(`api/task/${task_id}/`)
  }

  patchTaskInspectors(task_id, inspectorsList) {
    return http.patch(`api/task/${task_id}/inspectors/`, inspectorsList)
  }

  patchTaskExecutors(task_id, inspectorsList) {
    return http.patch(`api/task/${task_id}/executors/`, inspectorsList)
  }

  getTeacherStudents(user_id) {
    return http.get(`api/teacher/${user_id}/students/`)
  }

  getGroups() {
    return http.get('api/students_classes/')
  }

  getCriterions() {
    return http.get('api/criterions/')
  }

  addCriterion(criterionData) {
    return http.post('api/criterions/', criterionData)
  }

  getTaskSolutions(task_id) {
    return http.get(`/api/task/${task_id}/solutions/`, {
      headers: {
        Authorization: 'Token ' + store.getters.GET_USER_TOKEN
      },
    })
  }

  addTaskSolution(task_id, solution) {
    return http.post(`api/task/${task_id}/solutions/`, solution)
  }

  getTeacherTasks(user_id) { // id пользователя учителя
    return http.get(`/api/teacher/${user_id}/tasks/`)
  }

  getTeacher(user_id) {
    return http.get(`/api/teacher/${user_id}/`)
  }

  patchTeacher(user_id, teacherData) {
    const t = 'Token ' + store.getters.GET_USER_TOKEN
    return http.patch(`/api/teacher/${user_id}/`, teacherData, {
      headers: {
        Authorization: t
      }
    })
  }

  getStudent(user_id) {
    return http.get(`/api/student/${user_id}/`)
  }

  patchStudent(user_id, studentData) {
    const t = 'Token ' + store.getters.GET_USER_TOKEN
    return http.patch(`/api/student/${user_id}/`, studentData, {
      headers: {
        Authorization: t
      }
    })
  }

  getAllTasks() {
    return http.get("/api/tasks/");
  }

  getTask(id) {
    return http.get(`/api/task/${id}/`);
  }

  login(data) {
    return http.post("auth/token/login", data);
  }

  getMe() {
    return http.get("api/tasks/")
  }

  create(data) {
    return http.post("/tutorials", data);
  }

  getExecutionTasks() {
    return http.get("/api/my_execution_tasks/", {
      headers: {
        Authorization: 'Token ' + store.getters.GET_USER_TOKEN
      }
    })
  }

  getInspectionTasks() {
    return http.get("/api/my_inspection_tasks/", {
      headers: {
        Authorization: 'Token ' + store.getters.GET_USER_TOKEN
      }
    })
  }

  getUser(token) {
    return http.get("/auth/users/me/", {
      headers: {
          Authorization: 'Token ' + token
      }
    })
  }


//   update(id, data) {
//     return http.put(`/tutorials/${id}`, data);
//   }

//   delete(id) {
//     return http.delete(`/tutorials/${id}`);
//   }

//   deleteAll() {
//     return http.delete(`/tutorials`);
//   }

//   findByTitle(title) {
//     return http.get(`/tutorials?title=${title}`);
//   }
}

export default new DataService();