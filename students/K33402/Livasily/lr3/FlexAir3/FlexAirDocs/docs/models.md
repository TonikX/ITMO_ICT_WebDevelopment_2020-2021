

## airlines
Делает Get запрос на список Авиакомпаний

    export const getAirlines = () => (dispatch, getState) =>{
        axios.get('/api/airlines/',tokenConfig(getState))
            .then(res => {
                dispatch({
                    type: GET_AIRLINES,
                    payload: res.data
                })
            }).catch(err => console.log(err))
    }

Делает DELETE Запрос на удаление авиакомпании по id

    export const deleteAirlines = id => (dispatch, getState) =>{
        axios.delete(`/api/airlines/${id}`, tokenConfig(getState))
            .then(res => {
                dispatch({
                    type: DELETE_AIRLINES,
                    payload: id
                })
            }).catch(err => console.log(err))
    }

Делает POST Запрос на добавление авиакомпании

    export const addAirplanes = (airline) => (dispatch, getState) => {
        axios.post(`/api/airlines/`, airline, tokenConfig(getState)).then(res => {
            dispatch({
                type: ADD_AIRLANES,
                payload: res.data
            })
        }).catch(err => {console.log(err)})
    }

## Auth
Делает GET запрос на таблицу user

    
    export const loadUser = () => (dispatch, getState) =>{
        dispatch({type: USER_LOADING})
    
        axios.get('/api/auth/user',  tokenConfig(getState)).then(res => {
            dispatch({
                type: USER_LOADED,
                payload: res.data
            })
        }).catch(err => console.log(err))
    }

Делает POST запрос для входа под User с username и password

    export const login = (username, password) => dispatch =>{
    
        const config = {
            headers: {
                "Content-Type": 'application/json'
            }
        }
    
        const body = JSON.stringify({username, password})
    
        axios.post('/api/auth/login', body, config).then(res => {
            dispatch({
                type: LOGIN_SUCCESS,
                payload: res.data
            })
        }).catch(err => {console.log(err)})
    }


Делает POST запрос для выхода

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


Функция делаетPOST запрос для регистрации нового пользователя

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

##types
    GET_AIRLINES = "GET_AIRLANES"
    DELETE_AIRLINES = "DELETE_AIRLANES"
    USER_LOADED = "USER_LOADED"
    USER_LOADING = "USER_LOADING"
    AUTH_ERROR = "AUTH_ERROR"
    LOGIN_SUCCESS = "LOGIN_SUCCESS"
    LOGIN_FAIL = "LOGIN_FAIL"
    LOGOUT_SUCCESS = "LOGOUT_SUCCESS"
    REGISTER_SUCCESS = "REGISTER_SUCCESS"
    REGISTER_FAIL = "REGISTER_FAIL"
    ADD_AIRLANES = "ADD_AIRLANES"
    DELETE_AIRLANES = "DELETE_AIRLANES"
    GET_CITYS  = "GET_CITYS"
    DELETE_CITYS = "DELETE_CITYS"
    ADD_CITY = "ADD_CITY"



