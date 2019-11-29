// UserDetails.jsx
import React, { Component } from 'react';
import { Form, Button } from 'semantic-ui-react';

class CreateDecodeToggle extends Component{

	continueToCreate = (e) => {
		e.preventDefault()
		this.props.setStep('createstrategy')
	}

	continueToDecode = (e) => {
		e.preventDefault()
		this.props.setStep('decodesequence')
	}

	render(){
		const { values } = this.props;
		return(
			<Form >
				<h1 className="ui centered">Would you like to Create or Decode?</h1>
				<Button onClick={this.continueToCreate}>Create Sequence</Button>
				<Button onClick={this.continueToDecode}>Decode Sequence</Button>
			</Form>
		)
	}
}

export default CreateDecodeToggle;
