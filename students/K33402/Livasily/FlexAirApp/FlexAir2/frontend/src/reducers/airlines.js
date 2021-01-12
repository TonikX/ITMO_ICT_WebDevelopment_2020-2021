import { GET_AIRLINE } from '../actions/types.js'


const initialState = {
    airlines: []
}

export default function (state = initialState, action){
    switch (action.type){
        case GET_AIRLINE:{
            return{
                ...state,
                airlines: action.payload
            };
        }
        default:
            return state;
    }
}
