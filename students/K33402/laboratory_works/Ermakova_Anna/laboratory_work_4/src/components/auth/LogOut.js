import React, {Component, Fragment} from 'react';
import {connect} from 'react-redux'
import {logout} from '../../redux/auth/authActions'
import {Redirect} from "react-router-dom";


class LogOut extends Component {

    componentDidMount() {
        this.props.logout()
    }

    render() {
        if (!this.props.userLoad) {
            return <Redirect to='/'/>
        }
        return (
            <div>
                LogOut
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        userLoad: state.auth.userLoad,
    }
}
export default connect(mapStateToProps, {logout})(LogOut)