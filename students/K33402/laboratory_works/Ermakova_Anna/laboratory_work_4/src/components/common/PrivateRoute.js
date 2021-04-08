import React from 'react';
import {Route, Redirect} from 'react-router-dom'
import {connect} from 'react-redux'
import {loadUser, notRegister} from '../../redux/auth/authActions'

const PrivateRoute = (auth) => (
    <Route
        render={props => {
            if(!auth.isAuthenticated && !auth.userLoading){
                auth.notRegister()
                return <Redirect to={"./login"}/>
            }else if ((!auth.isAuthenticated || auth.userLoading) && !auth.userLoad){
                auth.loadUser();
                return <h2>Loadin...</h2>
            }
            else if(auth.userLoad){
                return <Redirect to={"./home"}/>
            }
        }
        }
    />
)
const mapStateToProps = state => {
    return {
        isAuthenticated: state.auth.isAuthenticated,
        userLoading: state.auth.userLoading,
        userLoad: state.auth.userLoad,
    }
}


export default connect(mapStateToProps, {loadUser, notRegister})(PrivateRoute)