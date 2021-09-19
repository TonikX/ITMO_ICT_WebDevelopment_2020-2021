import {
GET_HOTELS
} from "./types";
import axios from "axios";


const URL = "http://127.0.0.1:8000"


export const getHotels = (username, password) => dispatch => {

    axios.get(URL + '/api/hotels')
        .then(res => {
            dispatch({
                type: GET_HOTELS,
                payload: res.data
            })
        }).catch(err => console.log(err));
}
