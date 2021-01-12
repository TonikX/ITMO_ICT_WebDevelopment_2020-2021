import axios from "axios";


import {USER_LOADING, USER_LOADED, AUTH_ERROR, LOGIN_SUCCESS, LOGOUT_SUCCESS, REGISTER_SUCCESS} from './types'

//CHEK TOKEN &LOAD USER
export const loadUser = () => (dispatch, getState) =>{
    dispatch({type: USER_LOADED})

    axios.get('/api/auth/user',  tokenConfig(getState)).then(res => {
        dispatch({
            type: USER_LOADED,
            payload: res.data
        })
    }).catch(err => console.log(err))
}

//LOGIN USEr
export const login = (username, password) => dispatch =>{

    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }

    const body = JSON.stringify({username, password})

    console.log(body)
    axios.post('/api/auth/login', body, config).then(res => {
        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}

// LOGOUT_USER

export const logoutUser = () => (dispatch, getState) =>{

    const token = getState().auth.token

    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }
    //IF token, add too header config
    if(token){
        config.headers['Authorization'] = `Token ${token}`
    }

    axios.post('/api/auth/logout/', null, tokenConfig(getState)).then(res => {
        dispatch({
            type: LOGOUT_SUCCESS,
        })
    }).catch(err => console.log(err))
}


//setup config with token - helper function
export const tokenConfig = getState =>{
    const token = getState().auth.token;

    const config = {
        headers: {
            "Content-Type": "application/json"
        }
    }

    if(token){
        config.headers["Authorization"] = `Token ${token}`
    }


    return config
}

//REGISTER USER
export const register = ({username, password, email}) => dispatch => {

    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }

    const body = JSON.stringify({username, email, password})

    axios.post('/api/auth/register', body, config).then(res => {
        dispatch({
            type: REGISTER_SUCCESS,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}

