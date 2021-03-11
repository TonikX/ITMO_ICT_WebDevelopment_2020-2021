import axios from "axios";

import {GET_LEADS, DELETE_LEADS, ADD_LEADS} from "./types";
import  {tokenConfig} from "./auth";

export const getLeads = () => (dispatch, getState) => {
    axios.get('api/leads/',
        tokenConfig(getState)).then(res => {
        dispatch({
            type: GET_LEADS,
            payload: res.data
        })
    }).catch(err => console.log(err))
}

export const deleteLead = id => (dispatch, getState) => {
    axios.delete(`api/leads/${id}/`, tokenConfig(getState)).then(res => {
        dispatch({
            type: DELETE_LEADS,
            payload: id
        })
    }).catch(err => console.log(err))
}

export const addLead = (lead) => (dispatch, getState) => {
    axios.post(`api/leads/`, lead, tokenConfig(getState)).then(res => {
        dispatch({
            type: ADD_LEADS,
            payload: res.data
        })
    }).catch(err => console.log(err))
}