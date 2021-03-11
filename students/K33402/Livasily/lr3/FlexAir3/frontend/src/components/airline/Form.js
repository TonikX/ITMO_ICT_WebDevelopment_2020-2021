import React, {Component, Fragment} from "react";
import ReactDOM from 'react-dom'
import {connect} from 'react-redux'
import PropTypes from 'prop-types'
import { addAirplanes } from "../../actions/airlines";

export class Form extends Component {
    state = {
        name: '',
    }

    static propTypes = {
        addAirplanes: PropTypes.func.isRequired
    }

    onChange = e => this.setState({ [e.target.name]:
        e.target.value });

    onSubmit = e =>{
        e.preventDefault();
        const {name} = this.state
        const airline = { name }
        this.props.addAirplanes(airline)
    }
    render() {
        const {name} = this.state
        return (
            <div className={"card card-body mt-4 mb-4"}>
                <h2>Add Airline</h2>
                <form onSubmit={this.onSubmit}>
                    <div className={"form-group"}>
                        <label>Name</label>
                        <input
                            className={"form-control"}
                            type={"text"}
                            name={"name"}
                            onChange={this.onChange}
                            value={name}
                        />
                    </div>
                    <div className={"form-group"}>
                        <button type={"submit"} className={"btn btn-primary"}>
                            Submit
                        </button>
                    </div>
                </form>
            </div>
        )
    }
}


export default connect(null, {addAirplanes})(Form)