import React, {Component, Fragment} from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import {getAirlines, deleteAirlines} from "../../actions/airlines";

class Airline extends Component{
    static propTypes = {
        airlines: PropTypes.array.isRequired
    }
    componentDidMount() {
        this.props.getAirlines();
    }

    render(){
        return (
            <Fragment>
                <h2>Airlines</h2>
                <table className={"table table-striped"}>
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Owner</th>
                        <th/>
                    </tr>
                    </thead>
                    <tbody>
                    {this.props.airlines.map(airline => (
                        <tr key={airline.id}>
                            <td>{airline.id}</td>
                            <td>{airline.name}</td>
                            <td>{airline.owner}</td>
                            <td><button onClick={this.props.deleteAirlines.bind(this, airline.id)} className={"btn btn-danger btn-sm"}>Delete</button></td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    airlines: state.airlines.airlines
})

export default connect(mapStateToProps, {getAirlines, deleteAirlines})(Airline)