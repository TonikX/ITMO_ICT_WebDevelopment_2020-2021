import {GET_CITYS, DELETE_CITYS, ADD_CITY} from "../actions/types.js"


const initialState = {
    citys: []
}

export default function (state = initialState, action){
    switch (action.type){
        case GET_CITYS:
            return{
                ...state,
                citys: action.payload
            }
        case DELETE_CITYS:
            return {
                ...state,
                citys: state.citys.filter(citys => citys.id !==action.payload)
            }
        case ADD_CITY:
            return {
                ...state,
                citys: [...state.citys, action.payload]
            }
        default:
            return state;
    }
}