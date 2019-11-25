# Shorteners  
When I got this challenge, I was fixated on this part of the problem-- how to actually shorten the secrets. I came up with a few different solutions, as outlined below.   
*Note: all of the emoji strategies are using an alphabet of 29 emojis as defined in alphabet.py*
## Strategy 1 - Generate Key with Hash of Emoji Sequence (emojiHash):  
This strategy has the advantage of returning a relatively short emoji sequence which is mostly random (Will explain further in steps), will never face collisions, and is still relatively secure (depending on desired token string length). On top of these advantages, this approach allows us to convert from emoji sequence to Private-Key **without the need of a database.**  
The key this generates is formatted as such (Hyphens are only present for illustrative purposes and will not be found in real output):
🦔-🐈-🦅🐈🦆🐳🦊
* 🦔 (0) - The first element is a sequential index as represented in base28. The reason this isn't base29 (using the entire alphabet) is to because the 29th character in our alphabet is reserved as a sentinel value. The purpose of starting our sequence with an index is to guarantee that we won't face any collisions (which could be a real problem if we want to keep our sequences short-but-secure). 
* 🐈 (28) - This is the aforementioned sentinel value. This connotes the end of the index portion, and the start of the random sequence.  
*Note: It would also be possible to design this such that we read the sections from right-to-left without a sentinel value. The advantage of this approach would be that we would have access to the full base29 alphabet for our index, and we'd be able to save a character in the final output. The disadvantage is that we'd be committing to a fixed-width random portion*
* 🦅🐈🦆🐳🦊 (7, 28, 12, 16, 2) - This is the randomly generated portion of the emoji key, in full base29. 

### Step 1: 
Generate emoji sequence. Index is obtained from the database, and the sequence is created by a random number generator. The output of this is the same as the sequence which we will return to the user  
```
Input: index = 0, random_chars = 5
Output: 🦔🐈🦅🐈🦆🐳🦊
```
### Step 2: 
Take the output from Step 1, and add [pepper](https://en.wikipedia.org/wiki/Pepper_(cryptography)) to the sequence to ensure that only our service will be able to convert from emoji-to-key. We generate a 32-byte hash of the output and that serves as our private key!   
*Note: We could use a [salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) instead of pepper. The disadvantage being that a database would be required to make the conversion from sequence to key.*  
```
Input: sequence = 🦔🐈🦅🐈🦆🐳🦊, pepper = supersecretpepper
Function: sha256('🦔🐈🦅🐈🦆🐳🦊supersecretpepper')
Output: 0x 921e99d4292ba24fcb31e4f9233a9d2c93d48c3d0c4572692cd58c49c5934d47
```  
## Strategy 2 - Pure Sequential:  
This strategy is to take the as-short-as-possible goal to the extreme. Simply encode the index in base29, and that's your sequence! The first 29 generated sequences will only require one emoji to represent. The following 841 sequences will only require two, the next 24000 only three. This strategy is identical to Strategy 1, except the sentinel value and randomly generated portions of the sequence generation steps are skipped. 