import {
    LOGIN_USER,
    LOGOUT_USER,
    INVALID_TOKEN,
    REGISTER_USER,
    LOAD_USER, AUTH_ERROR, NOT_REGISTER_USER
} from "./types";


const initialState = {
    token: localStorage.getItem('token'),
    isAuthenticated: null,
    userLoading: null,
    userLoad: null,
    registered: null,
    userData: null
}

export const authReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOGIN_USER: {
            return {
                ...state,
                token: action.payload,
                userLoading: true,
                isAuthenticated: true
            }
        }
        case REGISTER_USER: {
            return {
                ...state,
                registered: true,
            }
        }
        case NOT_REGISTER_USER: {
            return {
                ...state,
                registered: false,
            }
        }
        case LOAD_USER: {
            return {
                ...state,
                userLoad: true,
                userLoading: false,
                userData: action.payload
            }
        }
        case LOGOUT_USER:
        case INVALID_TOKEN:
        case AUTH_ERROR:
        {
            return {
                ...state,
                isAuthenticated: null,
                userLoading: null,
                userLoad: false,
                somethink: null,
                token: null
            }
        }
        default:
            return state
    }
}