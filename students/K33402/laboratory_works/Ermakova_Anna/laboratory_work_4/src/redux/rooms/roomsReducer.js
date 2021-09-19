import {
    GET_ROOMS
} from "./types";


const initialState = {
    rooms: null,
    roomsLoaded: false
}

export const roomsReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ROOMS: {
            return {
                ...state,
                rooms: action.payload,
                roomsLoaded: true
            }
        }
        default:
            return state
    }
}