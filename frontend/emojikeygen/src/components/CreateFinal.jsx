import React, { Component } from 'react';

class create extends Component{
    render(){
        return(
            <h1 className="ui centered">Your emojikey is {this.props.values.emojikey}</h1>
        )
    }
}

export default create;
