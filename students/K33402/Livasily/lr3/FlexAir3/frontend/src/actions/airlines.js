import axios from "axios";
import {tokenConfig} from "./auth";
import {GET_AIRLINES, DELETE_AIRLINES} from "./types";
import {ADD_AIRLANES} from "../../../../../FlexAirApp/FlexAir2/frontend/src/actions/types";

export const getAirlines = () => (dispatch, getState) =>{
    axios.get('/api/airlines/',tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_AIRLINES,
                payload: res.data
            })
        }).catch(err => console.log(err))
}

export const deleteAirlines = id => (dispatch, getState) =>{
    axios.delete(`/api/airlines/${id}`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: DELETE_AIRLINES,
                payload: id
            })
        }).catch(err => console.log(err))
}

export const addAirplanes = (airline) => (dispatch, getState) => {
    axios.post(`/api/airlines/`, airline, tokenConfig(getState)).then(res => {
        dispatch({
            type: ADD_AIRLANES,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}