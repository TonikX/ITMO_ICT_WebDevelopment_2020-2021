import React, {Component, Fragment} from 'react'
import {connect} from "react-redux";
import {getHotels} from "../../redux/hotels/hotelsActions"

import {Link} from "react-router-dom";


import styles from "./styles.scss"
class MainContainer extends Component {
    componentDidMount() {
        this.props.getHotels()
    }
    render() {
        if (this.props.hotelsLoaded) {
            return (
                <Fragment>
                    {this.props.hotels.map(hotel => (
                        <div key={hotel.id}className="card">
                            <div className="card-header">
                                {hotel.name}
                            </div>
                            <div className="card-body">
                                {/*<h5 className="card-title">Special title treatment</h5>*/}
                                <p className="card-text">{hotel.address}</p>
                                <div className={styles.BTN}>
                                    <Link className="btn btn-primary"to={'/hotel/'+hotel.id}>Просмотреть</ Link>
                                    <Link className="btn btn-outline-primary"to={'/feedback/'+hotel.id}>Комментарии</ Link>
                                </div>

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
        hotels: state.hotels.hotels,
        hotelsLoaded: state.hotels.hotelsLoaded
    }
}

export default connect(mapStateToPtops, {getHotels})(MainContainer)