import "./actions/types";
import {GET_TODO_LIST} from "./actions/types";

// import {GET_TODO_LIST, ADD_TODO, DELETE_TODO, TOGGLE_TODO} from  "./actions/types";
const initialState = {
    todos: []
}

export default function (state = initialState, action){
    switch (action.type){
        case GET_TODO_LIST:
            return{
                ...state,
                todos: action.payload
            };
        default:
            return state
    }
}