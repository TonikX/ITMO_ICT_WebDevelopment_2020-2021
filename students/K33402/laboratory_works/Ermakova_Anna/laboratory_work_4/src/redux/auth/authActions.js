import {
    LOGIN_USER,
    LOGOUT_USER,
    INVALID_TOKEN,
    REGISTER_USER,
    LOAD_USER,
    AUTH_ERROR,
    GET_ERRORS,
    NOT_REGISTER_USER,
} from "./types";
import axios from "axios";


const URL = "http://127.0.0.1:9000"


export const login = (username, password) => dispatch => {
    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }
    const body = JSON.stringify({username, password})

    axios.post(URL + '/auth/token/login/', body, config)
        .then(res => {
            dispatch({
                type: LOGIN_USER,
                payload: res.data
            })
        }).catch(err => console.log(err));
}

export const logout = () => (dispatch, getState) => {
    axios.post(URL + '/auth/token/logout/', null, tokenConfig(getState)).then(res => {
        dispatch({
            type: LOGOUT_USER,
        })
    }).catch(err => {
        dispatch({
            type: INVALID_TOKEN,
        })
    })
}

export const register = (username, password) => dispatch => {
    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }
    const body = JSON.stringify({username, password})

    axios.post(URL + '/auth/users/', body, config).then(res => {
        dispatch({
            type: REGISTER_USER,
            payload: res.data
        })
    }).catch(err => console.log(err))

}
export const notRegister = () => dispatch => {

    dispatch({
        type: NOT_REGISTER_USER,
    })
}
export const tokenConfig = getState => {
    const token = getState().auth.token;
    const config = {
        headers: {
            "Content-Type": "application/json"
        }
    }
    if (token) {
        config.headers["Authorization"] = `Token ${token["auth_token"]}`
    }
    return config
}

export const loadUser = () => (dispatch, getState) => {
    axios.get(URL + '/auth/users/me/', tokenConfig(getState)).then(res => {
        dispatch({
            type: LOAD_USER,
            payload: res.data
        })
    }).catch(err => console.log(err))
}