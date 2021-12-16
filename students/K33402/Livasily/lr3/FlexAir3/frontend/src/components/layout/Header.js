import React, {Component} from "react";
import {Link, Redirect} from "react-router-dom";
import {connect} from "react-redux"
import PropTypes from "prop-types"
import {logoutUser} from '../../actions/auth'

export class Header extends Component {
    static propTypes = {
        auth: PropTypes.object.isRequired,
        logoutUser: PropTypes.func.isRequired
    }

    render() {
        let {isAuthenticated, user} = this.props.auth
        const authLinks = (
            <ul className="navbar-nav mr-auto">
                <Link className="navbar-brand" to={"/city"}>City</Link>
                <span className={"navbar-text mr-3"}>
                    <strong>
                        { user ? `Welcome ${user.username}`: "" }
                    </strong>
                </span>
                <li className={"nav-item"}>
                    <button onClick={this.props.logoutUser} className={"nav-link btn "}>Logout</button>
                </li>
            </ul>
        );

        const guestLinks = (
            <ul className="navbar-nav mr-auto">
                <li className={"nav-item"}>
                    <Link to={"/register"} className={"nav-link"}>Register</Link>
                </li>
                <li className={"nav-item"}>
                    <Link to={"/login"} className={"nav-link"}>Login</Link>
                </li>
            </ul>
        )
        return (
            <nav className="navbar navbar-expand-lg navbar-light bg-light">

                <a className="navbar-brand" href="/">Airlines</a>


                <button className="navbar-toggler" type="button" data-toggle="collapse"
                        data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    { isAuthenticated ? authLinks:guestLinks}
                    {/*<ul className="navbar-nav mr-auto">*/}
                    {/*    <li className="nav-item active">*/}
                    {/*        <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>*/}
                    {/*    </li>*/}
                    {/*    <li className="nav-item">*/}
                    {/*        <a className="nav-link" href="#">Link</a>*/}
                    {/*    </li>*/}
                    {/*    <li className="nav-item dropdown">*/}
                    {/*        <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"*/}
                    {/*           data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">*/}
                    {/*            Dropdown*/}
                    {/*        </a>*/}
                    {/*        <div className="dropdown-menu" aria-labelledby="navbarDropdown">*/}
                    {/*            <a className="dropdown-item" href="#">Action</a>*/}
                    {/*            <a className="dropdown-item" href="#">Another action</a>*/}
                    {/*            <div className="dropdown-divider"></div>*/}
                    {/*            <a className="dropdown-item" href="#">Something else here</a>*/}
                    {/*        </div>*/}
                    {/*    </li>*/}
                    {/*    <li className="nav-item">*/}
                    {/*        <a className="nav-link disabled" href="#">Disabled</a>*/}
                    {/*    </li>*/}
                    {/*</ul>*/}
                    {/*<form className="form-inline my-2 my-lg-0">*/}
                    {/*    <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>*/}
                    {/*        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>*/}
                    {/*</form>*/}
                </div>
            </nav>
        )
    }
}

const mapStateToProps = state => ({
    auth: state.auth
})

export default connect(mapStateToProps, {logoutUser})(Header)