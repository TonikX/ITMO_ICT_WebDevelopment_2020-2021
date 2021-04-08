import {
    GET_COMMENTS,
    ADD_COMMENTS
} from "./types";
import axios from "axios";


const URL = "http://127.0.0.1:8000"


export const getFeetBack = (id) => dispatch => {

    axios.get(URL + `/api/comments/?hotel=${id}`)
        .then(res => {
            dispatch({
                type: GET_COMMENTS,
                payload: res.data
            })
        }).catch(err => console.log(err));
}

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
