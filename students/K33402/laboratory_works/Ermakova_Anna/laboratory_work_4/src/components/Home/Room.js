import React, {Component, Fragment} from 'react'
import {addBooking} from "../../redux/booking/bookingActions"
import {connect} from "react-redux";

class Room extends Component {
    state ={
        dataBegin: '',
        dataEnd: ''
    }
    onChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    onSubmit = e => {
        if ((new Date(this.state.dataBegin) < new Date(this.state.dataEnd))
            && new Date() <= new Date(this.state.dataBegin)
            && !(this.state.dataEnd === this.state.dataBegin === ''))
            this.props.addBooking(this.props.roomId, this.props.user.id, new Date(this.state.dataBegin), new Date(this.state.dataEnd))
        else
            alert("Неккоректные даты")

    }

    render() {
        const {dataBegin,dataEnd} = this.state
        return (
            <Fragment>
                <button type="button" className="btn btn-primary" data-toggle="modal"
                        data-target={"#staticBackdrop" + this.props.roomId}>
                    просмотреть
                </button>
                <div className="modal fade" id={"staticBackdrop" + this.props.roomId} data-backdrop="static"
                     data-keyboard="false"
                     tabIndex="-1"
                     aria-labelledby="staticBackdropLabel" aria-hidden="true">
                    <div className="modal-dialog modal-dialog-centered">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title" id="staticBackdropLabel">Комната {this.props.roomId}</h5>
                                <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div className={"p-3"}>
                                <div className="form-group row">
                                    <label htmlFor="example-date-input" className="col-2 col-form-label">Заезд</label>
                                    <div className="col-10">
                                        <input className="form-control" name="dataBegin"onChange={this.onChange}type="date"
                                               id="example-date-input" value={dataBegin}/>
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="example-date-input" className="col-2 col-form-label">Выезд</label>
                                    <div className="col-10">
                                        <input className="form-control" name="dataEnd" onChange={this.onChange}type="date" value={dataEnd}

                                               id="example-date-input"/>
                                    </div>
                                </div>
                            </div>
                            <form  onSubmit={this.onSubmit} className="modal-footer">
                                <button type="submit" className="btn btn-primary">Зарезервировать</button>
                            </form>
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}
const mapStateToProps = state =>{
    return{
        user: state.auth.userData
    }
}

export default connect(mapStateToProps, {addBooking})(Room)