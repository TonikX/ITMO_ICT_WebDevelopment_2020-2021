import React, {Component, Fragment} from 'react'
import ReactDOM from 'react-dom'
import Form from "./Form";
import Airline from "./Airline";

class Dashboard extends Component{
    render(){
        return (
            <Fragment>
                <Form/>
                <Airline/>
            </Fragment>

        )
    }
}

export default Dashboard