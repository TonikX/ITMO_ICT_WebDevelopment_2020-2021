import {
    GET_HOTELS
} from "./types";


const initialState = {
    hotels: null,
    hotelsLoaded: false
}

export const hotelsReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_HOTELS: {
            return {
                ...state,
                hotels: action.payload,
                hotelsLoaded: true
            }
        }
        default:
            return state
    }
}