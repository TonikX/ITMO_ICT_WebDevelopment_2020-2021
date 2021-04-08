import {
    ADD_RESERVATIONS,
    GET_BOOKING,
    BOOKING_CLOSE,
    DELETE_BOOKING
} from "./types";


const initialState = {
    booking: null,
    bookingLoaded: false,

}

export const bookingReducer = (state = initialState, action) => {
    switch (action.type) {
        case ADD_RESERVATIONS: {
            return {
                ...state,
            }
        }
        case GET_BOOKING: {
            return {
                ...state,
                booking: action.payload,
                bookingLoaded: true
            }
        }
        case DELETE_BOOKING: {
            return {
                ...state,
                booking: state.booking.filter(book => book.id !== action.payload),
            }
        }
        case BOOKING_CLOSE: {
            return {
                ...state,
                booking: [],
                bookingLoaded: false
            }
        }
        default:
            return state
    }
}