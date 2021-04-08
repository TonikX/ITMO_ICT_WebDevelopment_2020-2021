import {
    ADD_RESERVATIONS,
    GET_BOOKING,
    BOOKING_CLOSE,
    DELETE_BOOKING
} from "./types";
import axios from "axios";


const URL = "http://127.0.0.1:8000"


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
export const delBooking = (idBook) => dispatch => {
    axios.delete(URL + `/api/bookingSet/${idBook}`)
        .then(res => {
            dispatch({
                type: DELETE_BOOKING,
                payload: idBook
            })
        }).catch(err => console.log(err));
}

export const getBooking = (userId) => dispatch => {
    axios.get(URL + `/api/booking/?guest=${userId}`)
        .then(res => {
            dispatch({
                type: GET_BOOKING,
                payload: res.data
            })
        }).catch(err => console.log(err));
}
export const closeBooking = () => dispatch => {

    dispatch({
        type: BOOKING_CLOSE,

    })

}
