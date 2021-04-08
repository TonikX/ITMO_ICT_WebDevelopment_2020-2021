import axios from "axios";
import {ADD_COMMENT} from "../../../help/lr4Front/src/redux/comments/types";
import {GET_FLIGHTS} from "../../../help/lr4Front/src/redux/data/types";
import {DEL_PLACE, GET_PLACE} from "../../../help/lr4Front/src/redux/places/types";
import {INVALID_TOKEN, LOAD_USER, LOGIN_USER, LOGOUT_USER, REGISTER_USER} from "../src/redux/auth/types";
import {tokenConfig} from "../src/redux/auth/authActions";
import {ADD_COMMENTS, GET_COMMENTS} from "../src/redux/feedBack/types";
import {GET_HOTELS} from "../src/redux/hotels/types";
import {GET_ROOMS} from "../src/redux/rooms/types";
import {ADD_RESERVATIONS, DELETE_BOOKING, GET_BOOKING} from "../src/redux/booking/types";

/**
 *
 * @param {username} - объект вида {username: String}
 * @param {password} - объект вида {password: String}
 * изменяет состяние переменной token
 */
export const login = (username, password) => dispatch => {
    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }
    const body = JSON.stringify({username, password})

    axios.post(URL + '/auth/token/login/', body, config)
        .then(res => {
            dispatch({
                type: LOGIN_USER,
                payload: res.data
            })
        }).catch(err => console.log(err));
}

/**
 *
 * @returns {function(*, *=): void}
 * делаеь запрос на логаут, после запрос, полученный токен не дейситителен
 */
export const logout = () => (dispatch, getState) => {
    axios.post(URL + '/auth/token/logout/', null, tokenConfig(getState)).then(res => {
        dispatch({
            type: LOGOUT_USER,
        })
    }).catch(err => {
        dispatch({
            type: INVALID_TOKEN,
        })
    })
}

/**
 *
 * @param {username} - объект вида {username: String}
 * @param {password} - объект вида {password: String}
 * @returns {function(*): void}
 * делает запрос на регистрацию пользователя
 */
export const register = (username, password) => dispatch => {
    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }
    const body = JSON.stringify({username, password})

    axios.post(URL + '/auth/users/', body, config).then(res => {
        dispatch({
            type: REGISTER_USER,
            payload: res.data
        })
    }).catch(err => console.log(err))

}


/**
 *
 * @returns {function(*, *=): void}
 * делает запрос на данные пользователя
 */
export const loadUser = () => (dispatch, getState) => {
    axios.get(URL + '/auth/users/me/', tokenConfig(getState)).then(res => {
        dispatch({
            type: LOAD_USER,
            payload: res.data
        })
    }).catch(err => console.log(err))
}


/**
 *
 * @param String comment
 * @param int id
 * @param int id
 * @returns {function(*): void}
 * делает запрос на добавление комментария и изменяеняе тмасив comments
 */
export const addComments = (raining, text, hotel, user) => dispatch => {

    const data = {
        "Rating": raining,
        "text": text,
        "hotel": hotel,
        "author": user
    }
    console.log(data)
    axios.post(URL + '/api/commentsSet/', data)
        .then(res => {
            dispatch({
                type: ADD_COMMENTS,
                payload: res.data
            })
        }).catch(err => console.log(err));
}

/**
 * Делает запрос на список комментариев
 * @returns {function(*, *): void}
 */
export const getFeetBack = (id) => dispatch => {

    axios.get(URL + `/api/comments/?hotel=${id}`)
        .then(res => {
            dispatch({
                type: GET_COMMENTS,
                payload: res.data
            })
        }).catch(err => console.log(err));
}



/**
 * Делает запрос на список отелеей
 * @param id
 * @returns {function(*): void}
 */
export const getHotels = (username, password) => dispatch => {

    axios.get(URL + '/api/hotels')
        .then(res => {
            dispatch({
                type: GET_HOTELS,
                payload: res.data
            })
        }).catch(err => console.log(err));
}


/**
 * Делает запрос комнаты
 * @param id
 * @returns {function(*): void}
 */
export const getRooms = (id) => dispatch => {

    axios.get(URL + `/api/roomSet/?hotel=${id}`)
        .then(res => {
            dispatch({
                type: GET_ROOMS,
                payload: res.data
            })
        }).catch(err => console.log(err));
}

/**
 * Делает запрос на добавление резервации
 * @param idRoom
 * @param idUser
 * @param CheckIn
 * @param CheckOut
 * @returns {function(*): void}
 */
export const addBooking = (idRoom, idUser,CheckIn, CheckOut ) => dispatch => {

    const data = {
        "CheckIn": CheckIn,
        "CheckOut": CheckOut,
        "room": idRoom,
        "guest": idUser
    }
    axios.post(URL + `/api/bookingSet/`, data)
        .then(res => {
            dispatch({
                type: ADD_RESERVATIONS,
                payload: res.data
            })
        }).catch(err => console.log(err));
}
/**
 * Делает запрос на удаление резервации
 * @param idBook:int
 * @returns {function(*): void}
 */
export const delBooking = (idBook) => dispatch => {
    axios.delete(URL + `/api/bookingSet/${idBook}`)
        .then(res => {
            dispatch({
                type: DELETE_BOOKING,
                payload: idBook
            })
        }).catch(err => console.log(err));
}
/**
 * Делает запрос на список резераваций
 * @param userId:int
 * @returns {function(*): void}
 */
export const getBooking = (userId) => dispatch => {
    axios.get(URL + `/api/booking/?guest=${userId}`)
        .then(res => {
            dispatch({
                type: GET_BOOKING,
                payload: res.data
            })
        }).catch(err => console.log(err));
}