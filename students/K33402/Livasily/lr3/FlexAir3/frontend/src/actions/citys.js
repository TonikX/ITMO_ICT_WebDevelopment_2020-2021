import axios from "axios";
import {GET_CITYS, DELETE_CITYS, ADD_CITY, UPDATE_CITY} from "./types";

export const getCitys = () => (dispatch) =>{
    console.log('getCitys')
    axios.get('/api/citys/')
        .then(res => {
            console.log('res')
            console.log(res.data)
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

export const addCity = (id) => (dispatch) => {
    axios.post(`/api/citys/`, id).then(res => {
        dispatch({
            type: ADD_CITY,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}

export const updateCity = (id,  name) => (dispatch) => {
    const value = {name, id}
    axios.put(`/api/citys/${id}/`, value).then(res => {
        dispatch({
            type: UPDATE_CITY,
            payload: value
        })
    }).catch(err => {console.log(err)})
}