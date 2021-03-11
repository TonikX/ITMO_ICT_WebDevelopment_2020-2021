import React, {Component, Fragment} from "react";
import Form from './Form'
import Airline from "./Airlines";

export default function Dashboard(){
    return(
        <Fragment>
            <Form/>
            <Airline/>
        </Fragment>
    )
}