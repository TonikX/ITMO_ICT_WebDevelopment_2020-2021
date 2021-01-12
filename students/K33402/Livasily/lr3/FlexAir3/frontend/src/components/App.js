import React, {Component, Fragment} from 'react'
import ReactDOM from 'react-dom'
import {HashRouter as Router, Route, Switch, Redirect } from "react-router-dom";

import {Provider} from 'react-redux'


import store from '../store'
import {loadUser} from "../actions/auth";

import Dashboard from "./airline/Dashboard";
import DashboardCitys from "./citys/DashboardCitys";
import Header from "./layout/Header";
import Register from "./accounts/Register";
import Login from "./accounts/Login";
import PrivateRoute from "./common/PrivateRoute";

class App extends Component {

    componentDidMount() {
        store.dispatch(loadUser())
    }

    render() {
        return (
            <Provider store={store}>
                <Router>
                    <Fragment>
                        <Header/>
                        <div className={"container"}>
                            <Switch>
                                <PrivateRoute exact path={"/"} component={Dashboard}/>
                                <Route exact path={"/city"} component={DashboardCitys}/>
                                <Route exact path={"/register"} component={Register}/>
                                <Route exact path={"/login"} component={Login}/>
                            </Switch>
                        </div>
                    </Fragment>
                </Router>
            </Provider>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'))