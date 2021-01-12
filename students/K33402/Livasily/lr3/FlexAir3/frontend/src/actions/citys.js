import axios from "axios";
import {GET_CITYS, DELETE_CITYS, ADD_CITY} from "./types";

export const getCitys = () => (dispatch) =>{
    axios.get('/api/citys/')
        .then(res => {
            dispatch({
                type: GET_CITYS,
                payload: res.data
            })
        }).catch(err => console.log(err))
}

export const deleteCity = id => (dispatch) =>{
    axios.delete(`/api/citys/${id}`)
        .then(res => {
            dispatch({
                type: DELETE_CITYS,
                payload: id
            })
        }).catch(err => console.log(err))
}

export const addCity = (city) => (dispatch) => {
    axios.post(`/api/citys/`, city).then(res => {
        dispatch({
            type: ADD_CITY,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}