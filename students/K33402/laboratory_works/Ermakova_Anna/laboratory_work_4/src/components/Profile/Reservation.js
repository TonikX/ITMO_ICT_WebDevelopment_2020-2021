import React, {Component, Fragment} from 'react'
import {connect} from "react-redux";
import {getBooking, delBooking} from "../../redux/booking/bookingActions"


class Reservation extends Component {
    componentDidMount() {
        this.props.getBooking(this.props.user.id)
    }

    render() {
        if(this.props.bookingLoaded){
            return (
                <Fragment>
                    {this.props.booking.map(booking=>(
                        <div key={booking.id} className="card">
                            <h5 className="card-header">{booking.room.hotel.name}</h5>
                            <div className="card-body">
                                <h5 className="card-title">{booking.room.hotel.address}</h5>
                                <p className="card-text">
                                    Заселение {booking.CheckIn.split('T').join(' ').split(':00Z').join('')}
                                    <br/>
                                    Выселение {booking.CheckOut.split('T').join(' ').split(':00Z').join('')}
                                </p>
                                <button onClick={this.props.delBooking.bind(this, booking.id)} className="btn btn-primary">Отменить</button>
                            </div>
                        </div>
                    ))}
                </Fragment>
            )
        }
        else{
            return(
                <Fragment>
                Loading
            </Fragment>)

        }
    }
}
const mapStateToProps = state=>{
    return{
        user: state.auth.userData,
        booking: state.bookings.booking,
        bookingLoaded: state.bookings.bookingLoaded,
    }
}
export default connect(mapStateToProps, {getBooking, delBooking})(Reservation)