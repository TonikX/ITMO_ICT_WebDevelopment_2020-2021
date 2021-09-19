import React, {Component, Fragment} from 'react'
import {connect} from "react-redux";
import Header from "../Header";
import MainContainer from "./MainContainer";

class Home extends Component {

    render() {
        return (
            <div>
                <Header/>
                <MainContainer/>
            </div>
        )
    }
}


export default Home