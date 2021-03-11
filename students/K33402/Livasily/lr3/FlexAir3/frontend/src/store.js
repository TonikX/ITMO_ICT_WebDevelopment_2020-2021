import {createStore, applyMiddleware} from "redux";
import {composeWithDevTools} from "redux-devtools-extension";
import thunk from "redux-thunk";
import rootReducers from './reducers'
import logger from "redux-logger"
const initialState = {}

const middleware = [thunk]

const store = createStore(
    rootReducers,
    initialState,
    composeWithDevTools(applyMiddleware(...middleware, logger))
)

export default store