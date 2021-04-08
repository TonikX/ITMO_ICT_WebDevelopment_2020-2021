import {applyMiddleware, createStore} from "redux";

import {rootReducer} from "./rootReducer";
import thunk from 'redux-thunk';
import {composeWithDevTools} from "redux-devtools-extension";


const middleware = [thunk]
import logger from "redux-logger"


const saveState = (state) => {
    try {
        const serialisedState = JSON.stringify(state);
        window.localStorage.setItem('app_state', serialisedState);
    } catch (err) {
        console.log(err)
    }
};
const loadState = () => {
    try {
        const serialisedState = window.localStorage.getItem('app_state');
        if (!serialisedState) return undefined;
        return JSON.parse(serialisedState);
    } catch (err) {
        return undefined;
    }
};
const oldState = loadState();

const store = createStore(rootReducer,oldState,
    composeWithDevTools(applyMiddleware(...middleware, logger)))

store.subscribe(() => {
    saveState(store.getState());
});

export default store