import React, {Component, Fragment} from 'react'
import styles from "./styles.scss"
import Header from "../Header";
import {addComments} from "../../redux/feedBack/feedBackActions"
import {connect} from "react-redux"
class Comments extends Component {
    state ={
        text: '',
        rating: 10
    }
    onChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    onSubmit = e =>{
        e.preventDefault();
        this.props.addComments(this.state.rating, this.state.text, this.props.comments[0].hotel.id, this.props.user.id)
    }

    render() {
        const {text, rating} = this.state
        return (<Fragment>
                <br/>
                <div>
                    <ol className="list-group list-group-numbered">
                        {this.props.comments.map(com => (
                            <li key ={com.id}className="list-group-item d-flex justify-content-between align-items-start">
                                <div className="ms-2 me-auto">
                                    <div className="fw-bold">  {com.author.username}</div>
                                    {com.text}
                                </div>
                                {/*<span className="badge bg-primary rounded-pill">del</span>*/}
                            </li>
                        ))}
                    </ol>
                </div>
                <form onSubmit={this.onSubmit} className={styles.Comments}>
                    <textarea name={"text"} value={text} onChange={this.onChange}></textarea>
                    <select name="rating" onChange={this.onChange} value={rating} className={styles.Select}>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                    <button type={"submit"} className="btn btn-primary">Добавить комметарий</button>
                </form>
            </Fragment>


        )
    }
}
const mapStateToProps =state=> {
    return{
        user: state.auth.userData,

    }
}

export default connect(mapStateToProps, {addComments})(Comments)