// UserDetails.jsx
import React, { Component } from 'react';
import { Form, Button } from 'semantic-ui-react';

class CreateName extends Component{
	submit = (e) => {
		if(!this.props.values.name){
			alert('You must enter a name!')
			return
		}
		e.preventDefault()
		fetch('http://127.0.0.1:5000/emojikey',
			{
				method: 'POST',
				headers: {'Content-Type': 'application/json'},
				body: JSON.stringify({
					name: this.props.values.name,
					strategy: this.props.values.strategy
				})
			})
			.then(resp => resp.json())
			.then(respJson => {
				if(!respJson.emojikey){
					alert(`Please try again! The server returned this error: ${JSON.stringify(respJson)}`)
				}
				this.props.setEmojikey(respJson.emojikey)
			})
			.then(() => {this.props.setStep('createfinal')})
	}

	render(){
		return(
			<Form >
				<h1 className="ui centered">What is your name?</h1>
				<Form.Field>
					<label>Name</label>
					<input
					placeholder='Name'
					onChange={this.props.handleChange('name')}
					defaultValue={this.props.values.name}
					/>
				</Form.Field>
				<Button onClick={this.submit}>Submit</Button>
			</Form>
		)
	}
}

export default CreateName;
