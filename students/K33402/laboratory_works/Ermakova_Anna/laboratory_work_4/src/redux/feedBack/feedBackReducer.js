import {
    ADD_COMMENTS,
    GET_COMMENTS
} from "./types";



const initialState = {
    comments: null,
    commentsLoaded: false
}

export const feedBackReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_COMMENTS: {
            return {
                ...state,
                comments: action.payload,
                commentsLoaded: true
            }
        }
        case ADD_COMMENTS: {
            return {
                ...state,
                comments: [...state.comments, action.payload]
            }
        }
        default:
            return state
    }
}