import axios from 'axios';

import { GET_AIRLINE} from "./types";



export const getAirlines = () => {
    axios.get('/FlexAir/Airport/list/')
        .then(res => {
        dispatch({
            type: GET_AIRLINE,
            airline: res.data
        })
    }).catch(err => console.log(err))
}