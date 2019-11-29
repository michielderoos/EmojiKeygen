# Emojikeygen API  

This is the API portion of the emojikeygen project. 

## Instructions to run locally  
  
- Install requirements (`pip3 install -r requirements.txt`) from the root directory
- Run `python app.py` from the root directory
- That's it! The backend should now be live on port 5000

## Details  
The API is broken up into a few different components as detailed below
### Config: 
config.py is a basic config file which comes equipped out of the box with settings that allow you to run the API locally with no modification. Their functions are as follows:  
```
SQLALCHEMY_DATABASE_URI - URI for database where we're storing names and keys. By default (for demo purposes) this is set to a new local sqlite database, in prod you'll want to change this to whatever DBMS you choose  

PEPPER - This is the pepper we add to strings before using a hashing function to build a key. **This should be changed before use**  

DATABASE_ENCRYPTION_KEY - We encrypt private keys before storing them, and this is the key we use. **This should be changed before use**  

DEFAULT_RANDOM_SEQUENCE_LENGTH - This is how many emojis we generate for the emojihash strategy
```
 
### Shorteners: 
Emojikeygen supports multiple strategies to create sequence/key pairs  
See [shorteners/README.md](shorteners/README.md) for more detail on these.

