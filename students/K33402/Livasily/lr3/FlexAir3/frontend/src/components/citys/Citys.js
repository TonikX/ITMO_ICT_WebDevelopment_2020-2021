import React, {Component, Fragment} from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import {getCitys, deleteCity, updateCity} from "../../actions/citys";

class City extends Component{

    static propTypes = {
        citys: PropTypes.array.isRequired
    }
    state = {
        newName: [],
    }
    componentDidMount() {
        this.props.getCitys();
    }

    onChange = e => {
        this.state.newName[e.target.name] = e.target.value
        this.setState(
        {
            [e.target.name]:
            e.target.value
        });}

    render(){
        const newName = this.state
        return (
            <Fragment>
                <h2>Citys</h2>
                <table className={"table table-striped"}>
                    <thead>
                    <tr>
                        <th>id</th>
                        <th>Name</th>
                        <th/>
                        <th/>
                        <th/>
                    </tr>
                    </thead>
                    <tbody>
                    {this.props.citys.map(city => (
                        <tr key={city.id}>
                            <td>{city.id}</td>
                            <td>{city.name}</td>
                            <td><button onClick={this.props.deleteCity.bind(this, city.id)} className={"btn btn-danger btn-sm"}>Delete</button></td>
                            <td><input  onChange={this.onChange} type="next" name={"newName"+city.id} value={newName[city.id]}/></td>
                            <td><button onClick={this.props.updateCity.bind(this, city.id, this.state.newName["newName"+city.id])} className={"btn btn-danger btn-sm"}>update</button></td>
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

export default connect(mapStateToProps, {getCitys, deleteCity, updateCity})(City)