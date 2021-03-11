import {GET_CITYS, DELETE_CITYS, ADD_CITY, UPDATE_CITY} from "../actions/types.js"


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
                citys: state.citys.filter(citys => citys.id !== action.payload)
            }
        case ADD_CITY:
            return {
                ...state,
                citys: [...state.citys, action.payload]
            }
        case UPDATE_CITY:
            for(let i = 0; i<state.citys.length; i++){
                if(state.citys[i].id === action.payload.id && state.citys[i].name !== action.payload.name){
                    state.citys[i].name = action.payload.name
                }
            }
            return {
                ...state,
                citys: [...state.citys]
            }
        default:
            return state;
    }
}

//state.citys.filter(citys => citys.id === action.payload.id && citys.name !== action.payload.name)