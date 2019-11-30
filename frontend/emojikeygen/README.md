# Emojikeygen API  

This is the frontend of the emojikeygen project. 

## Instructions to run locally  
The frontend working is dependent on the API being live. To start the API locally, please consult the API's [README.md](../../emojikeygen/README.md)  
- Run `npm install`
- Run `npm start`
- That's it! The frontend should now be live and accessible on port 3000  

(note: If you're not running this locally, you'll want to alter config.js to point to wherever you're hosting the backend)
## Details  
The way this is structured, is that we have a base component called `MainForm` which manages state. `MainForm` starts by loading `CreateDecodeToggle`, which allows the user to decide between the distinct 'create' and 'decode' flows.   
![](https://i.imgur.com/3ehtyD3.png)
### Create Flow: 
#### CreateStrategy: 
CreateStrategy is the first component to be loaded in the create flow. This allows the user to choose how they want to shorten their key.  
![](https://i.imgur.com/GheRtfq.png)  
  
#### CreateName: 
CreateName is the component where the user enters their name, and it will alert() the user with an error if they do not enter a name. CreateName also submits the name to the emojikeygen API, and checks the result for errors. If there is an API error, the user is free to try again as well.
![](https://i.imgur.com/0svtMUI.png)  
  
#### CreateFinal:
This is the final step in the create flow. Here we just return the generated emoji sequence to the user.   
![](https://i.imgur.com/r2kfFiE.png)

### Decode Flow: 
#### DecodeSequence:
Similar to CreateName, here the user enters their sequence and it's sent to the server where the name associated with the sequence is looked up.  
![](https://i.imgur.com/8xX9lIu.png)

#### DecodeFinal:
This is the final step in the create flow. Here we just return sequence's user name to the user.   
![](https://i.imgur.com/4ILwv2s.png)

