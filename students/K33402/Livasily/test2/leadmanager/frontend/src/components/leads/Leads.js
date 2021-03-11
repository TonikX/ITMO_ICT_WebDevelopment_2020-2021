import React, {Component, Fragment} from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux'
import {getLeads, deleteLead} from "../../actions/leads";

export class Leads extends Component {
    static propTypes = {
        leads: PropTypes.array.isRequired
    }

    componentDidMount() {


        this.props.getLeads();

    }

    render() {
        return (
            <Fragment>
                <h1>Leads</h1>
                <table className="table table-striped">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Message</th>
                        <th/>
                    </tr>
                    </thead>
                    <tbody>
                    {this.props.leads.map(lead => (
                        <tr key={lead.id}>
                            <td>{lead.id}</td>
                            <td>{lead.name}</td>
                            <td>{lead.email}</td>
                            <td>{lead.message}</td>
                            <td>
                                <button onClick={this.props.deleteLead.bind(this, lead.id)} className={"btn btn-danger btn-sm"}>Delete</button>
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
    leads: state.LEADS.leads
})


export default connect(mapStateToProps, {getLeads, deleteLead})
(Leads)