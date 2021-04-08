import React, {Component, Fragment} from 'react'
import {connect} from "react-redux";
import Header from "../Header";
import Reservation from "./Reservation";


class Profile extends Component {

    render() {

        return (
            <Fragment>
                <Header/>
                <Reservation/>
            </Fragment>
        )
    }
}


export default Profile