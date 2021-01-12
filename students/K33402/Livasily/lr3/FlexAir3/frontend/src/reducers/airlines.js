import {GET_AIRLINES, DELETE_AIRLINES,ADD_AIRLANES, DELETE_AIRLANES} from "../actions/types.js"

const initialState = {
    airlines: []
}

export default function (state = initialState, action){
    switch (action.type){
        case GET_AIRLINES:
            return{
                ...state,
                airlines: action.payload
            }
        case DELETE_AIRLANES:
            return {
                ...state,
                airlines: state.airlines.filter(airline => airline.id !==action.payload)
            }
        case ADD_AIRLANES:
            return {
                ...state,
                airlines: [...state.airlines, action.payload]
            }
        default:
            return state;
    }
}