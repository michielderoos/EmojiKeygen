// MainForm.jsx
import React, { Component } from 'react';
import CreateDecodeToggle from './CreateDecodeToggle';
import CreateName from './CreateName';
import CreateStrategy from './CreateStrategy';
import CreateFinal from './CreateFinal'
import DecodeSequence from './DecodeSequence'
import DecodeFinal from './DecodeFinal'

class MainForm extends Component {
	state = {
		step: 'start',
		name: '',
		strategy: '',
		emojikey: '',
	}

	setStep = (newStep) => { this.setState({ step : newStep }) }
	setStrategy = (newStrategy) => { this.setState({ strategy: newStrategy }) }
	setEmojikey = (newEmojikey) => { this.setState({ emojikey: newEmojikey }) }
	setName = (newName) => { this.setState({ name: newName }) }
	handleChange = input => event => { this.setState({ [input] : event.target.value }) }

	render(){
		const {step, name, strategy, emojikey } = this.state;
		const values = { name, strategy, emojikey };
		switch(step) {
		// Start step. Choose whether to create a new sequence, or find out who owns an existing one
		default:
			return <CreateDecodeToggle 
					setStep={this.setStep} 
					values={values}
					/>

		// Key creation steps
		case 'createstrategy':
			return <CreateStrategy 
					setStep={this.setStep} 
					setStrategy = {this.setStrategy}
					values={values}
					/>
		case 'createname':
			return <CreateName 
					setStep={this.setStep} 
					handleChange = {this.handleChange}
					setEmojikey = {this.setEmojikey}
					values={values}
					/>
		case 'createfinal':
			return <CreateFinal 
					values={values}
					/>

		// Sequence lookup steps
		case 'decodesequence':
			return <DecodeSequence 
				setStep={this.setStep} 
				handleChange = {this.handleChange}
				setName = {this.setName}
				values={values}
				/>
		case 'decodefinal':
				return <DecodeFinal 
					values={values}
					/>
		
		}
	}
}

export default MainForm;
