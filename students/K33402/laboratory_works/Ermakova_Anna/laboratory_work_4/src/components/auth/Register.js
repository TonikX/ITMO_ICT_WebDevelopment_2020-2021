import React, {Component, Fragment} from 'react';
import {form, button} from 'bootstrap-4-react';
import {Redirect} from "react-router-dom";
import {register} from "../../redux/auth/authActions"
import styles from "./styles.scss"
import {Link} from 'react-router-dom';
import {connect} from "react-redux";

class Register extends Component {
    state = {
        username: '',
        password: '',
        repeatPassword: ''
    }

    onChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    onSubmit = e => {
        e.preventDefault();
       this.props.register(this.state.username, this.state.password)
    };

    render() {
        if(this.props.userLoad || this.props.registered){
            return <Redirect to={'./'}/>
        }
        const {username, password, repeatPassword} = this.state
        return (
            <form onSubmit={this.onSubmit} className={styles.auth}>
                <h1>Register</h1>
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
                    <div className="mb-3 row">
                        <label htmlFor="inputPassword" className="col-sm-2 col-form-label">Repeat</label>
                        <div className="col-sm-10">
                            <input type="password" name="repeatPassword" value={repeatPassword} onChange={this.onChange}
                                   className="form-control" id="inputPasswordRepeat"/>
                        </div>
                    </div>
                    <div className={styles.Bth}>
                        <Link className="nav-link" to={"/login"}>I have account</Link>
                        <button type="submit" className="btn btn-outline-primary">Log up</button>
                    </div>
                </div>
            </form>
        )
    }
}
const mapStateToProps = state =>{
    return{
        userLoad: state.auth.userLoading,
        registered: state.auth.registered

    }
}

export default connect(mapStateToProps, {register})(Register)