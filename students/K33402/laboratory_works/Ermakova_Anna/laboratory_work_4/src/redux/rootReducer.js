import {combineReducers} from "redux";
import {authReducer} from "./auth/authReducer";
import {hotelsReducer} from "./hotels/hotelsReducer";
import {roomsReducer} from "./rooms/roomsReducer";
import {bookingReducer} from "./booking/bookingReducer";
import {feedBackReducer} from "./feedBack/feedBackReducer";

export const rootReducer = combineReducers({
    auth: authReducer,
    hotels: hotelsReducer,
    rooms: roomsReducer,
    bookings: bookingReducer,
    comments: feedBackReducer
})