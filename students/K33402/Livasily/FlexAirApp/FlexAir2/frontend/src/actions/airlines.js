
import {GET_AIRLANES, DELETE_AIRLANES, ADD_AIRLANES, GET_ERRORS} from "./types";

import axios from "axios";


export const getAirplanes = () => dispatch => {

    axios.get('/airline/').then(res => {
        dispatch({
            type: GET_AIRLANES,
            payload: res.data
        })
    }).catch(err => console.log(err))
}

export const deleteAirplanes = (id) => dispatch => {

    axios.delete(`/airline/${id}/`).then(res => {
        dispatch({
            type: DELETE_AIRLANES,
            payload: id
        })
    }).catch(err => console.log(err))
}

export const addAirplanes = (airline) => dispatch => {

    axios.post(`/airline/`, airline).then(res => {
        dispatch({
            type: ADD_AIRLANES,
            payload: res.data
        })
    }).catch(err => {console.log(err.response.data)
        // const errors = {
        //     msg: err.response.data,
        //     status: err.response.status
        // }
        // dispatch({
        //     type: GET_ERRORS,
        //     payload: errors
        // })
    })
}