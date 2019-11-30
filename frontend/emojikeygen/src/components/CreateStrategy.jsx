// UserDetails.jsx
import React, { Component } from 'react';
import { Form, Button } from 'semantic-ui-react';

class CreateStrategy extends Component{

    submit = (e) => {
        e.preventDefault()
        this.props.setStrategy(e.target.value)
        this.props.setStep('createname')
    }

    render(){
        return(
            <Form >
                <h1 className="ui centered">Which shortening strategy would you like to employ?</h1>
                <Button value='emojihash' onClick={this.submit}>EmojiHash</Button>
                <Button value='shortseq' onClick={this.submit}>ShortSeq</Button>
                <Button value='dracula' onClick={this.submit}>🧛</Button>
                <div className="ui centered">
                    <h3>EmojiHash: Longer, more secure keys (E.g. 🦊🐍🐈🐈🐘🦃🦆🐫)<br/>
                    ShortSeq: Shorter, but easier to remember keys (E.g. 🦊🐈🐍)<br/>
                    🧛: Markov chain generated sentence based on Bram Stoker's Dracula
                    </h3>
                </div>
            </Form>
        )
    }
}

export default CreateStrategy;
