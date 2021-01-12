import {combineReducers} from "redux";
import airlines from "./airlines";
import auth from "./auth";
import citys from "./citys";

export default combineReducers({
    airlines,
    auth,
    citys
})