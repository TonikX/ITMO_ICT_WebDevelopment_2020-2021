import axios from "axios";
import {ADD_CITY, DELETE_CITYS, GET_CITYS, UPDATE_CITY} from "./FlexAir3/frontend/src/actions/types";

/**
 * Делает GET запрос на список аэропортов и присваивает данные о них в переменнюу payload
 * @returns {function(*, *=): void}
 */
export const getAirlines = () => (dispatch, getState) =>{
    axios.get('/api/airlines/',tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_AIRLINES,
                payload: res.data
            })
        }).catch(err => console.log(err))
}

/**
 * Делает запрос DELETE на аэрапорт по id, и присваивает id переменной payload
 * @param id
 * @returns {function(*, *=): void}
 */
export const deleteAirlines = id => (dispatch, getState) =>{
    axios.delete(`/api/airlines/${id}`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: DELETE_AIRLINES,
                payload: id
            })
        }).catch(err => console.log(err))
}


/**
 * Делает POST запрос на добавление аэропорта  именеи airline и присваивает полученные данные в переменную payload
 * @param airline
 * @returns {function(*, *=): void}
 */
export const addAirplanes = (airline) => (dispatch, getState) => {
    axios.post(`/api/airlines/`, airline, tokenConfig(getState)).then(res => {
        dispatch({
            type: ADD_AIRLANES,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}


/**
 * Делает GET запрос на таблицу городов и передает данные переменной payload
 * @returns {function(*): void}
 */
export const getCitys = () => (dispatch) =>{
    console.log('getCitys')
    axios.get('/api/citys/')
        .then(res => {
            dispatch({
                type: GET_CITYS,
                payload: res.data
            })
        }).catch(err => console.log(err))
}

/**
 * Делает DELETE запрос по id и присваивает id переменной payload
 * @param id
 * @returns {function(*): void}
 */
export const deleteCity = id => (dispatch) =>{
    axios.delete(`/api/citys/${id}`)
        .then(res => {
            dispatch({
                type: DELETE_CITYS,
                payload: id
            })
        }).catch(err => console.log(err))
}


/**
 * Делает POST запрос и добавляет новый город в базу данных с именем name. Полученные данные передает в payload
 * @param id
 * @returns {function(*): void}
 */

export const addCity = (name) => (dispatch) => {
    axios.post(`/api/citys/`, name).then(res => {
        dispatch({
            type: ADD_CITY,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}
/**
 * Делает PUT запрос на обновление данных о городе с id на имя name
 * @param id
 * @param name
 * @returns {function(*): void}
 */
export const updateCity = (id,  name) => (dispatch) => {
    const value = {name, id}
    axios.put(`/api/citys/${id}/`, value).then(res => {
        dispatch({
            type: UPDATE_CITY,
            payload: value
        })
    }).catch(err => {console.log(err)})
}