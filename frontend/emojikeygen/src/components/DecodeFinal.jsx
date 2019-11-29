import React, { Component } from 'react';

class DecodeFinal extends Component{
	render(){
		return(
			<h1 className="ui centered">This emojikey belongs to {this.props.values.name}!</h1>
		)
	}
}

export default DecodeFinal;
