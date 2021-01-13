import React, {Component, Fragment} from "react";
import ReactDOM from 'react-dom'
import {connect} from 'react-redux'
import PropTypes from 'prop-types'
import {getAirplanes, deleteAirplanes} from "../../actions/airlines";
import airlines from "../../reducers/airlines";

export class Airline extends Component {

    static propTypes ={
        airlines: PropTypes.array.isRequired,
        getAirplanes: PropTypes.func.isRequired,
        deleteAirplanes: PropTypes.func.isRequired,
    }
    componentDidMount() {
        this.props.getAirplanes()
    }

    render() {
        return (
            <Fragment>
                <h1>Airlines</h1>
                <table className="table table-striped">
                    <thead>
                    <tr>
                        <th>id</th>
                        <th>owner</th>
                        <th>name</th>
                        <th/>
                    </tr>
                    </thead>
                    <tbody>
                    {this.props.airlines.map(airline => (
                        <tr key={airline.id}>
                            <td>{airline.id}</td>
                            <td>{airline.owner}</td>
                            <td>{airline.name}</td>
                            <td>
                                <button onClick={this.props.deleteAirplanes.bind(this, airline.id)} className={"btn btn-danger btn-sm"}>Delete</button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </Fragment>
        )
    }
}
const mapStateToProps = state => (console.log(state),{
    airlines: state.Airlines.airlines
})

export default connect(mapStateToProps, {getAirplanes, deleteAirplanes})(Airline)