import {
    GET_ROOMS
} from "./types";
import axios from "axios";


const URL = "http://127.0.0.1:8000"


export const getRooms = (id) => dispatch => {

    axios.get(URL + `/api/roomSet/?hotel=${id}`)
        .then(res => {
            dispatch({
                type: GET_ROOMS,
                payload: res.data
            })
        }).catch(err => console.log(err));
}
