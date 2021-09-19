import React, {Component, Fragment} from 'react';
import styles from "./styles.scss"
import {Link} from 'react-router-dom';
import {connect} from 'react-redux'
import {login} from '../../redux/auth/authActions'
import {Redirect} from "react-router-dom";


class Login extends Component {
    state = {
        username: '',
        password: ''
    }

    onChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    onSubmit = e => {
        e.preventDefault();
        console.log(this.state.username)
        this.props.login(this.state.username, this.state.password)
    };

    render() {
        const {username, password} = this.state
        if (this.props.userLoading) {
            return <Redirect to='/'/>
        }
        return (
            <form onSubmit={this.onSubmit} className={styles.auth}>
                <h1>Login</h1>
                <div className={styles.Container}>
                    <div className="mb-3 row">
                        <label htmlFor="inputPassword" className="col-sm-2 col-form-label">Login</label>
                        <div className="col-sm-10">
                            <input type="text" name="username" value={username} onChange={this.onChange}
                                   className="form-control" id="inputLogin"/>
                        </div>
                    </div>
                    <div className="mb-3 row">
                        <label htmlFor="inputPassword" className="col-sm-2 col-form-label">Password</label>
                        <div className="col-sm-10">
                            <input type="password" name="password" value={password} onChange={this.onChange}
                                   className="form-control" id="inputPassword"/>
                        </div>
                    </div>
                    <div className={styles.Bth}>
                        <Link className="nav-link" to={"/register"}>create account</Link>
                        <button type="submit" className="btn btn-outline-primary">Log in</button>
                    </div>
                </div>
            </form>
        )
    }
}

const mapStateToProps = state => {
    console.log(state)
    return {
        userLoading: state.auth.userLoading,
    }
};

export default connect(mapStateToProps, {login})(Login)