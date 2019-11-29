// UserDetails.jsx
import React, { Component } from 'react';
import { Form, Button } from 'semantic-ui-react';
import config from '../config';

class DecodeSequence extends Component{

	submit = (e) => {
		if(!this.props.values.emojikey){
			alert('You must enter an emoji sequence!')
			return
		}
		e.preventDefault()
		fetch(`${config.API_URL}/emojikey/${this.props.values.emojikey}`)
			.then(resp => resp.json())
			.then(respJson => {
				if(!respJson.name){
					alert(`Please try again! The server returned this error: ${JSON.stringify(respJson)}`)
					return
				}
				this.props.setName(respJson.name)
			})
			.then(_ => {this.props.setStep('decodefinal')})
	}

	render(){
		const { values } = this.props;
		return(
			<Form >
				<h1 className="ui centered">What is the emoji sequence you want to decode?</h1>
				<Form.Field>
					<label>Sequence: </label>
					<input
					placeholder='🦔🦈🐈🐶🐔🐧🦊🦉'
					onChange={this.props.handleChange('emojikey')}
					defaultValue={values.name}
					/>
				</Form.Field>
				<Button onClick={this.submit}>Submit</Button>
			</Form>
		)
	}
}

export default DecodeSequence;
