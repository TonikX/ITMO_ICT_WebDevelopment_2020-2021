import React, {Component} from "react";
import {Link, Redirect} from "react-router-dom";
import {connect} from "react-redux";
import {register} from "../../actions/auth"
import PropTypes from 'prop-types'
import {Login} from "./Login";

export class Register extends Component {
    state = {
        username: '',
        email: '',
        password: '',
        password2: ''
    }
    static proptypes ={
        register: PropTypes.func.isRequired,
        isAuthenticated: PropTypes.func.isRequired
    }
    onSubmit = e => {
        e.preventDefault();
        const {username, email, password, password2} = this.state
        if(password!==password2){
            console.log("пароли не совпадают")
        } else{
            const newUser ={
                username,
                email,
                password
            }
            this.props.register(newUser)
        }
        if(this.props.isAuthenticated){
            this.props.history.push('/');
        }
    }

    onChange = e => this.setState({[e.target.name]:e.target.value})


    render() {
        const {username, email, password, password2} = this.state
        return(
            <div className={"col-md-6 m-auto"}>
                <div className={"card card-body mt-5"}>
                    <h2 className={"text-center"}>Register</h2>
                    <form onSubmit={this.onSubmit}>
                        <div className={"form-group"}>
                            <label>Username</label>
                            <input
                                type={"text"}
                                className={"form-control"}
                                name={"username"}
                                onChange={this.onChange}
                                value={username}
                            />
                        </div>
                        <div className={"form-group"}>
                            <label>Email</label>
                            <input
                                type={"text"}
                                className={"form-control"}
                                name={"email"}
                                onChange={this.onChange}
                                value={email}
                            />
                        </div>
                        <div className={"form-group"}>
                            <label>Password</label>
                            <input
                                type={"text"}
                                className={"form-control"}
                                name={"password"}
                                onChange={this.onChange}
                                value={password}
                            />
                        </div>
                        <div className={"form-group"}>
                            <label>Password2</label>
                            <input
                                type={"text"}
                                className={"form-control"}
                                name={"password2"}
                                onChange={this.onChange}
                                value={password2}
                            />
                        </div>
                        <div className={"form-group"}>
                         <button type={"submit"} className={"btn btn-primary"}>
                             Register
                         </button>
                        </div>
                        <p>
                            Already hav an account?
                            <Link to={"/login"}>Login</Link>
                        </p>
                    </form>
                </div>
            </div>
        )
    }
}
const mapStateToProps = state => ({
    isAuthenticated:  state.auth.isAuthenticated
})
export default connect(mapStateToProps, {register})(Register)
