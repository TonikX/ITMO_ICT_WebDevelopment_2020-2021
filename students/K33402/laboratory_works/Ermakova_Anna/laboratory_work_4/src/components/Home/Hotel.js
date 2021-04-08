import React, {Component, Fragment} from 'react'
import {connect} from "react-redux";
import {getRooms} from "../../redux/rooms/roomsActions"
import Header from "../Header";
import Room from "./Room";

class Hotel extends Component {
    componentDidMount() {
        this.props.getRooms(this.props.match.params.id)
    }
    render() {
        if (this.props.roomsLoaded) {
            return (
                <Fragment>
                    <Header/>
                    {this.props.rooms.map(room => (
                        <div key={room.id} className="card">
                            <div className="card-header">
                                Комната {room.num_room}
                            </div>
                            <div className="card-body">
                                <Room roomId={room.num_room}/>
                            </div>
                        </div>
                    ))}
                </Fragment>
            )
        } else {
            return <div>Loading</div>
        }

    }
}

const mapStateToPtops = state => {
    return {
        rooms: state.rooms.rooms,
        roomsLoaded: state.rooms.roomsLoaded
    }
}

export default connect(mapStateToPtops, {getRooms})(Hotel)