---
description: >-
  Now that your Mycroft Device is Paired with home.mycroft.ai, you may begin
  issuing commands. Try these to get started.  
---
# Basic Commands

You issue a command to Mycroft by Speaking the **Wake Word** (e.g. "Hey Mycroft"), awaiting aknowledgement from Mycroft, and then Speaking the command itself (aka the **utterance**). 

When you issue a command, you *intend* for Mycroft to react in a certain way.  Your **utterance** contains an **Intent**.  Mycroft uses natural language processing to compare the words in your **utterance** to expected phrases or keywords as supplied by the installed **Skills**.  When Mycroft determines that there is a *match* between your **utterance** and a specific expectation (the phrases/keywords), the **Skill** that supplied the matching expectation is notified so that it can respond to your command.

Mycroft comes with a collection of **Skills** installed by default.  Each **Skill** supplies a set of **Intents**, and each **Intent** has a set of expected phrases or keywords.  Each of the default **Skills** is introduced below with a brief description, followed by a sampling of expected **utterances** (usually grouped by **Intent**). Additional **Skills** may be added to your Mycroft Device; please see [Installing New Skills](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/installing-new-skills).  

Have fun exploring natural language processing by trying these commands with variations to the wording and phrasing. 

## The Default **Skills**
### Alarm
Manages a collection of alarms.  Weekly repetition is supported.
##### Set an alarm
> Hey Mycroft, wake me in two hours <br>
> Hey Mycroft, wake me up at 10:23pm <br>
> Hey Mycroft, set an alarm for two hours <br>
> Hey Mycroft, set an alarm for 3pm <br>
> Hey Mycroft, add an alarm for Monday at 8:20 <br>
> Hey Mycroft, create alarms for every weekday at 6 <br>
> Hey Mycroft, start a repeating alarm for Fridays at 9:30pm <br>
> Hey Mycroft, set an alarm *<- - - - - Mycroft will ask WHEN*
##### Snooze the active alarm
> Hey Mycroft, snooze *<- - - - - Defaults to 9 minutes* <br> 
> Hey Mycroft, snooze for 15 minutes <br>
> Hey Mycroft, give me 2 more hours
##### Delete/stop/cancel/dismiss/remove 
> Hey Mycroft, stop the alarm <br>
> Hey Mycroft, delete the Tuesday alarm for 9 <br>
> Hey Mycroft, remove all alarms
##### Query alarms
> Hey Mycroft, when is the next alarm? <br>
> Hey Mycroft, what are the alarms for today?
##### Change alarm sound
> Hey Mycroft, change the sound of the alarm

### Audio Record
Captures audio to a file that can be played back. The file can be deleted.
##### Record 
Duration is 60-seconds unless overridden. New duration value is used until it is overridden.
> Hey Mycroft, record <br>
> Hey Mycroft, record audio <br>
> Hey Mycroft, start recording <br>
> Hey Mycroft, record me for 6 seconds
##### Playback 
> Hey Mycroft, play record <br>
> Hey Mycroft, play back the audio <br>
> Hey Mycroft, playback recording
##### Delete the file
> Hey Mycroft, delete audio <br>
> Hey Mycroft, erase recording <br>
> Hey Mycroft, record clear

### Configuration
Interacts with the Device configuration both locally and at home.mycroft.ai.
##### Query the registered **name** of this Mycroft Device
> Hey Mycroft, what is your name?
##### Query the registered location of this Mycroft Device
> Hey Mycroft, where are you? <br>
> Hey Mycroft, tell me your state
##### Query which listener is being used to detect the Wake Word
> Hey Mycroft, tell me the wake word listener <br>
> Hey Mycroft, what is the listener?
##### Command Mycroft to update the configuation both locally and at home.mycroft.ai	
> Hey Mycroft, configuration update<br>
> Hey Mycroft, update config
##### For developers: Select which listener to use
> Hey Mycroft, set the listener to precise<br>
> Hey Mycroft, set the listener to default
##### For developers: Enable or disable the development version of Precise listener
> Hey Mycroft, enable the precise dev model <br>
> Hey Mycroft, disable the new precise model

### Hello World
Hello World is a well-documented **Skill** that serves as a starting point for code development.  Pleasantries with Mycroft are used as examples.
> Hey Mycroft, greetings <br>
> Hey Mycroft, hello world
> 
> Hey Mycroft, thank you
> 
> Hey Mycroft, how are you doing? <br>
> Hey Mycroft, how was your day?

### IP
Query the SSID or the IP Address (aka the network address) of the Mycroft Device.
##### Query the IP address
> Hey Mycroft, what is your IP address? <br>
> Hey Mycroft, tell me your network address <br>
> Hey Mycroft, what network are you connected to?
##### Query the SSID
> Hey Mycroft, what SSID are you on? <br>
> Hey Mycroft, what wifi network are you using? <br>
> Hey Mycroft, what network are you connected to?

### Jokes
Mycroft uses pyjokes as the source of jokes to tell.
> Hey Mycroft, tell me a joke <br>
> Hey Mycroft, make me laugh <br>	
> Hey Mycroft, brighten my day with a Chuck Norris joke <br>
> Hey Mycroft, tell me a non-offensive joke <br>

### Naptime
While 'napping' Mycroft will ignore utterances other than "Wake up".
##### Begin nap
> Hey Mycroft, go to sleep <br>
> Hey Mycroft, nap time
##### End nap
> Hey Mycroft, wake up

### NPR News
Plays the RSS audio feed for the requested station.  If no station is specified or if the request is unknown, a default station is selected based on Device location. Stations include: ABC (Australia), AP, BBC, CBC, DLF, Ekot, FOX, GPB, NPR, PBS, RDP, RNE, TSF, OE3, VRT, WDR, YLE.
##### Play the news
> Hey Mycroft, what's the news? <br>
> Hey Mycroft, play the BBC news <br>
> Hey Mycroft, what are the headlines?
##### Restart the broadcast
> Hey Mycroft, start over <br>
> Hey Mycroft, restart news
##### Stop playing the news
> Hey Mycroft, stop

### Personal
Ask about the "birth" and parentage of Mycroft, and get a taste of the community fostering this open source artificial intelligence.
> Hey Mycroft, who are you? <br>
> Hey Mycroft, when were you created? <br>
> Hey Mycroft, what are you? <br>
> Hey Mycroft, where were you born? <br>
> Hey Mycroft, who made you? <br>
> Hey Mycroft, do you even rhyme? <br>
> Hey Mycroft, do you dream?

### Playback Control
Common commands for controlling a music service.
##### Pause the music
> Hey Mycroft, pause <br>
> Hey Mycroft, pause the song
##### Resume the paused music
> Hey Mycroft, resume song <br>
> Hey Mycroft, resume play
##### Next track
> Hey Mycroft, next track
##### Previous track
> Hey Mycroft, previous track
##### Play
User provides a genre/artist/title/playlist/service.  Depending on the music service, a dialog may be initiated.
> Hey Mycroft, play my summer playlist <br>
> Hey Mycroft, play Pandora <br>
> Hey Mycroft, play something by hermitude <br>
> Hey Mycroft, play uptown funk on youtube

### Reminder
Manages a collection of reminders.  A Reminder is similar to an Alarm but instead of a beep Mycroft speaks the User specified words.
##### Set a reminder
> Hey Mycroft, remind me to **turn off the oven** in **5 minutes** <br>
> Hey Mycroft, add a reminder to **let the dog out** at **3pm** <br>
> Hey Mycroft, remind me to **take out the trash** *<- - - Mycroft will ask WHEN*<br>
> Hey Mycroft, remind me at **5pm** *<- - - - - - - - - Mycroft will ask FOR WHAT* <br>
> Hey Mycroft, set a reminder for me *<- - - Mycroft will ask WHEN and FOR WHAT* <br>
> Hey Mycroft, remind me of something
##### Snooze the active reminder
> Hey Mycroft, snooze the reminder <br>
> Hey Mycroft, remind me later 
##### Cancel the active reminder
> Hey Mycroft, okay, stop the reminder
##### Get reminders for a specific day
> Hey Mycroft, what are my reminders for today? <br>
> Hey Mycroft, do I have any reminders tomorrow?
##### Get next reminder
> Hey Mycroft, what is my next reminder?
##### Delete all reminders for a specific day 
> Hey Mycroft, cancel today's reminders <br>
> Hey Mycroft, cancel all reminders for tomorrow
##### Delete all reminders
> Hey Mycroft, delete all reminders

### Singing
Mycroft will speak the lyrics to a random pop music song.
> Hey Mycroft, sing <br>
> Hey Mycroft, sing me a song

### Speak
Speak a phrase and have Mycroft repeat it.
> Hey Mycroft, speak **Mary had a little lamb** <BR>
> Hey Mycroft, say **yada yada yada** <BR>
> Hey Mycroft, repeat **hey good looking**

### Spelling
Mycroft will spell any word that is understood by the Speech-To-Text system.
> Hey Mycroft, spell **aardvark** <BR>
> Hey Mycroft, what is the spelling of **aardvark**? <BR>
> Hey Mycroft, how do you spell word **aardvark**?

### Stock
This Skill has been disabled.

### Stop
Tell Mycroft to STOP doing whatever it is doing.  Should work with all **Skills**
##### Stop
> Hey Mycroft, stop <BR>
> Hey Mycroft, silence <BR>
> Hey Mycroft, shut up

### Support Helper
Captures troubleshooting information from the Mycroft Device and stores it on the [0x0.st](https://0x0.st) storage service.  This information is useful for your own debugging and for communicating with Support. A link to the information is emailed to the address registered at home.mycroft.ai.
> Hey Mycroft, contact support <br>
> Hey Mycroft, create a support ticket <br>
> Hey Mycroft, troubleshoot my device <br>
> Hey Mycroft, create a troubleshoot request <br>

### Timer
Manages a collection of timers.  Timers are requested with durations expressed in hours, minutes, and/or seconds. A timer may optionally be given a name.  The name is useful in queries, subsequent commands, and for display purposes.  All timers beep.
* If you wish to command a specific expiration time (e.g. 'at 3:05pm'), please use either an Alarm or a Reminder. <br>
* Timers have durations less than 24-hours.  When a Timer is requested with a duration greater than 24-hours, an Alarm is set instead. <br>
* Mycroft refers to a timer by it's original duration and the optional User supplied name.<br>
* When there is more than one timer with the same duration, Mycroft may include an ordinal (e.g. the second timer for 5-minutes).<br>
* The User may refer to an individual timer by its name or by the ordinal of its position in the list of timers (.e.g. the third timer).
##### Start a timer
> Hey Mycroft, I need a timer named **turkey** for **15 minutes** <br>
> Hey Mycroft, start a **10-minute** timer called **time to go** <br>
> Hey Mycroft, set a timer to **take out the trash** *<- - - Mycroft will ask for the DURATION* <br>
> Hey Mycroft, ping me in 2 hours *<- - - - - - - - - No NAME is associated with this timer* <br>
> Hey Mycroft, Start a timer *<- - - - - - - - Mycroft will ask for the DURATION but not a NAME* <br>
> Hey Mycroft, Begin timer
##### Query a timer
> Hey Mycroft, how's my **turkey** timer? <br>
> Hey Mycroft, how much time is left?
##### Cancel the beeping timer
> Hey Mycroft, cancel the timer 
##### Cancel a timer in the list of timers
> Hey Mycroft, cancel the first timer <br>
> Hey Mycroft, delete the fourth timer <br>
> Hey Mycroft, remove the **potatoes** timer <br>
> Hey Mycroft, kill the **turkey** timer
##### Cancel all timers
When no timers are beeping, this command removes all timers from the list.
If any timers are beeping, this command stops all of the beeping timers.
> Hey Mycroft, cancel all timers <br>
> Hey Mycroft, delete all timers
##### Mute timer
Muting stops the beep but leaves the timer in the list so that expired timers can be displayed.
> Hey Mycroft, mute the timer <br>
> Hey Mycroft, silence the timer

### Version Checker
Check the version of the software.  If an update exists, Mycroft will ask if the User wishes to update.  To keep up-to-date, Mycroft automatically performs these checks on a daily basis.
##### Query the Mycroft software version (mycroft-core)
> Hey Mycroft, check version <br>
> Hey Mycroft, what is code?
##### Query the platform (e.g. Picroft, Mark 1) build version
> Hey Mycroft, find platform version <br>
> Hey Mycroft, what is platform build?

### Volume
Manages Mycroft's volume level.
##### Query volume level
> Hey Mycroft, what is the volume? <br>
> Hey Mycroft, how loud?
##### Set volume to a numeric level (0 to 10)
In a tribute to Spinal Tap, a level of '11' is accepted (equivalent to level 10).
> Hey Mycroft, increase volume to 8 <br>
> Hey Mycroft, set sound to NORMAL *<- - - Keyword options: NORMAL=6, QUIET=3, LOUD=9*
##### Set volume to a percentage (0 to 100%)
> Hey Mycroft, set audio to 75 percent <br>
> Hey Mycroft, decrease volume to 50 percent
##### Set to maximum volume
> Hey Mycroft, crank it all the way up <br>
> Hey Mycroft, set audio to max
##### Increase volume by one numeric level
> Hey Mycroft, raise the sound<br>
> Hey Mycroft, make it higher<br>
> Hey Mycroft, louder
##### Decrease volume by one numeric level
> Hey Mycroft, lower the sound<br>
> Hey Mycroft, make it quieter<br>
> Hey Mycroft, softer
##### Mute
> Hey Mycroft, mute the volume <br>
> Hey Mycroft, silence the audio
##### Unmute
> Hey Mycroft, unmute the speaker <br>
> Hey Mycroft, restore the sound

### Weather
An interface to OpenWeatherMap.org that supports an extensive set of queries.
> Hey Mycroft, what is the weather? <br>
> Hey Mycroft, what is the forecast tomorrow? <br>
> Hey Mycroft, what is the weather going to be like Tuesday? <br>
> Hey Mycroft, what is the weather in Houston? <br>
> Hey Mycroft, when will it rain next? <br>
> Hey Mycroft, how windy is it? <br>
> Hey Mycroft, what's the humidity? <br>
> Hey Mycroft, is it going to snow? <br>
> Hey Mycroft, what's the temperature?

### Wiki
Interfaces to Wikipedia.org
##### Query Wikipedia
> Hey Mycroft, what does wikipedia say about chocolate? <br>
> Hey Mycroft, tell me about artificial intelligence <br>
> Hey Mycroft, search Grace Hopper
##### Ask Wikipedia for more details on same subject
> Hey Mycroft, tell me more <br>
> Hey Mycroft, please continue
##### Let Wikipedia select the subject
> Hey Mycroft, teach me something <br>
> Hey Mycroft, tell me a random thing

## The Fallback Handlers
Mycroft has two *fallback* handlers for the situation where the natural language processing fails to match a specific **Intent** and **Skill**; one for queries and one for unknowns.  

By default, Mycroft has access to two general purpose search engines: DuckDuckGo and Wolfram Alpha.  When the **utterance** is a query, Mycroft sends it to all of these Common Query search engines simulataneously. The first engine to reply successfully is the search engine selected by Mycroft to reply to the User.

If no search engine provides a successful answer to the query, or if the **utterance** was not a query, then Mycroft activates the Unknown Handler that responds with a variety of phrases explaining that Mycroft cannot handle the **utterance**.

### Common Query
Sent to all *fallback* Common Query search engines.
> Hey Mycroft, what is Frankenstein? <br>
> Hey Mycroft, who is Kathryn Johnson? <br>
> Hey Mycroft, how high is Mount Everest? <br>
> Hey Mycroft, how many inches in a meter?

### Subsequent Commands to a Common Query
A Common Query search engine may optionally support subsequent commands (e.g. "send me details") that are processed if that search engine handled the initial query.
#### Subsequent commands for Wolfram Alpha
##### Have more details of last query emailed to User
> Hey Mycroft, send me details on that <br>
> Hey Mycroft, email sources to me

## More information on Skills
For more information on Skills, please see the [Skills section](http://mycroft.ai/documentation/skills/)

