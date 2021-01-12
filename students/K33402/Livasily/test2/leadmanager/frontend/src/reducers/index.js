import {combineReducers} from "redux";
import LEADS from './leads'
import auth from "./auth"

export default combineReducers({
    LEADS,
    auth
});