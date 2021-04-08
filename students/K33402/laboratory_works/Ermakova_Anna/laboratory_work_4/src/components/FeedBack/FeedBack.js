import React, {Component, Fragment} from 'react'
import {connect} from "react-redux";
import Header from "../Header";
import {getFeetBack} from "../../redux/feedBack/feedBackActions"
import Comments from "./Comments";

class FeedBack extends Component {
    componentDidMount() {
        this.props.getFeetBack(this.props.match.params.id)
    }

    render() {
        if(this.props.commentsLoaded){
            return (
                <div>
                    <Header/>
                    <Comments comments={this.props.comments}/>
                </div>
            )
        }else{
            return <Fragment>Loading...</Fragment>
        }

    }
}
const mapeStateToProps = state=> {
    return {
        comments: state.comments.comments,
        commentsLoaded: state.comments.commentsLoaded,

    }
}

export default connect(mapeStateToProps, {getFeetBack} )(FeedBack)