import React, {Component, Fragment} from 'react'
import ReactDOM from 'react-dom'
import City from "./Citys";
import Form from "./Form";

class DashboardCitys extends Component{
    render(){
        return (
            <Fragment>
                <Form />
                <City/>
            </Fragment>

        )
    }
}

export default DashboardCitys