import React, {Component, Fragment} from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import {getCitys, deleteCity} from "../../actions/citys";

class City extends Component{
    static propTypes = {
        citys: PropTypes.array.isRequired
    }
    componentDidMount() {
        this.props.getCitys();
    }

    render(){
        return (
            <Fragment>
                <h2>Airlines</h2>
                <table className={"table table-striped"}>
                    <thead>
                    <tr>
                        <th>Name</th>
                        <th/>
                    </tr>
                    </thead>
                    <tbody>
                    {this.props.citys.map(city => (
                        <tr key={city.name}>
                            <td>{city.name}</td>
                            <td><button onClick={this.props.deleteCity.bind(this, city.name)} className={"btn btn-danger btn-sm"}>Delete</button></td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    citys: state.citys.citys
})

export default connect(mapStateToProps, {getCitys, deleteCity})(City)