# Intent Service

Mycroft supports both Padatious and Adapt intent handlers. Mycroft Core has an intent service that decides which intent will be triggered by a particular utterance. This is based on the confidence of a

## Intent Confidence

## Order of Priority
1. Active skills attempt to handle using `converse()`  
2. Padatious high match intents (confidence > 0.95)  
3. Adapt intent handlers  
4. Fallbacks:  
  - Padatious near match intents (confidence > 0.8)  
  - General fallbacks  
  - Padatious loose match intents (confidence > 0.5)  
  - Unknown intent handler  
