import React, {Component, Fragment} from 'react'
import {HashRouter as Router, Route, Switch, Redirect} from "react-router-dom";
import PrivateRoute from "./common/PrivateRoute";
import Login from "./auth/Login";
import Register from "./auth/Register";
import LogOut from "./auth/LogOut";
import Home from "./Home/Home";
import Hotel from "./Home/Hotel";
import Profile from "./Profile/Profile";
import FeedBack from "./FeedBack/FeedBack";


class App extends Component {

    render() {
        return (
            <Router>
                <Switch>
                    <PrivateRoute exact path={"/"}/>
                    <Route exact path={"/login"} component={Login}/>
                    <Route exact path={"/register"} component={Register}/>
                    <Route exact path={"/home"} component={Home}/>
                    <Route exact path={"/logout"} component={LogOut}/>
                    <Route exact path={"/hotel/:id"} component={Hotel}/>
                    <Route exact path={"/profile"} component={Profile}/>
                    <Route exact path={"/feedback/:id"} component={FeedBack}/>
                </Switch>
            </Router>
        )
    }
}


export default App