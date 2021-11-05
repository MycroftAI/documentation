---
description: >-
  Now that your Mycroft Device is Paired with home.mycroft.ai, you may begin
  issuing commands. Try these to get started.
---

# Basic Commands

You issue a command to Mycroft by Speaking the **Wake Word** (e.g. "Hey Mycroft"), awaiting acknowledgement from Mycroft, and then Speaking the command itself (aka the **utterance**).

When you issue a command, you _intend_ for Mycroft to react in a certain way. Your **utterance** contains an **Intent**. Mycroft uses natural language processing to compare the words in your **utterance** to expected phrases or keywords as supplied by the installed **Skills**. When Mycroft determines that there is a _match_ between your **utterance** and a specific expectation (the phrases/keywords), the **Skill** that supplied the matching expectation is notified so that it can respond to your command.

Mycroft comes with a collection of **Skills** installed by default. Each **Skill** supplies a set of **Intents**, and each **Intent** has a set of expected phrases or keywords. Each of the default **Skills** is introduced below with a brief description, followed by a sampling of expected **utterances** (usually grouped by **Intent**). Additional **Skills** may be added to your Mycroft Device; please see [Installing New Skills](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/installing-new-skills).

Have fun exploring natural language processing by trying these commands with variations to the wording and phrasing.

## The Default **Skills**

### Alarm

Manages a collection of alarms. Weekly repetition is supported.

**Set an alarm**

> Hey Mycroft, wake me in two hours \
> Hey Mycroft, wake me up at 10:23pm \
> Hey Mycroft, set an alarm for two hours \
> Hey Mycroft, set an alarm for 3pm \
> Hey Mycroft, add an alarm for Monday at 8:20 \
> Hey Mycroft, create alarms for every weekday at 6 \
> Hey Mycroft, start a repeating alarm for Fridays at 9:30pm \
> Hey Mycroft, set an alarm _<- - - - - Mycroft will ask WHEN_

**Snooze the active alarm**

> Hey Mycroft, snooze _<- - - - - Defaults to 9 minutes_ \
> Hey Mycroft, snooze for 15 minutes \
> Hey Mycroft, give me 2 more hours

**Delete/stop/cancel/dismiss/remove**

> Hey Mycroft, stop the alarm \
> Hey Mycroft, delete the Tuesday alarm for 9 \
> Hey Mycroft, remove all alarms

**Query alarms**

> Hey Mycroft, when is the next alarm? \
> Hey Mycroft, what are the alarms for today?

**Change alarm sound**

> Hey Mycroft, change the sound of the alarm

### Audio Record

Captures audio to a file that can be played back. The file can be deleted.

**Record**

Duration is 60-seconds unless overridden. The new duration value is used until it is overridden.

> Hey Mycroft, record \
> Hey Mycroft, record audio \
> Hey Mycroft, start recording \
> Hey Mycroft, record me for 6 seconds

**Playback**

> Hey Mycroft, play record \
> Hey Mycroft, play back the audio \
> Hey Mycroft, playback recording

**Delete the file**

> Hey Mycroft, delete audio \
> Hey Mycroft, erase recording \
> Hey Mycroft, record clear

### Configuration

Interacts with the Device configuration both locally and at home.mycroft.ai.

**Query the registered name of this Mycroft Device**

> Hey Mycroft, what is your name?

**Query the registered location of this Mycroft Device**

> Hey Mycroft, where are you? \
> Hey Mycroft, tell me your state

**Query which listener is being used to detect the Wake Word**

> Hey Mycroft, tell me the wake word listener \
> Hey Mycroft, what is the listener?

**Command Mycroft to update the configuration both locally and at home.mycroft.ai**

> Hey Mycroft, configuration update\
> Hey Mycroft, update config

**For developers: Select which listener to use**

> Hey Mycroft, set the listener to precise\
> Hey Mycroft, set the listener to default

**For developers: Enable or disable the development version of Precise listener**

> Hey Mycroft, enable the precise dev model \
> Hey Mycroft, disable the new precise model

### Date & Time

Mycroft answers inquiries about Dates (specific dates, relative dates, holidays, leap year, weekends, etc.) and Time (future or current, local or other location).  Mycroft's response to a Date inquiry attempts to supply the 'missing information' and selectively includes: day-of-week, the calendar date, and the quantity of days from now. When answering inquiries about Time, Mycroft may optionally take advantage of the display on the enclosure.

#### Query current time (in location)

> Hey Mycroft, the time now please\
> Hey Mycroft, what time is it in Paris?

#### Query future time (in location)

> Hey Mycroft, what time will it be in 2 hours?\
> Hey Mycroft, tell me the time 6 hours from now in Paris?

#### On some enclosures: Display the time (in location)

> Hey Mycroft, display the time\
> Hey Mycroft, display the time in Paris

#### Query a holiday

> Hey Mycroft, when is Labor Day?\
> Hey  Mycroft, what day is Christmas in 2025?

#### Query next leap year

> Hey Mycroft, when is the next leap year?

#### Query a specific date

> Hey Mycroft, when in July 1st?

#### Query a relative date

> Hey Mycroft, what is today's date?\
> Hey Mycroft, what is today?\
> Hey Mycroft, when is next Tuesday?\
> Hey Mycroft, what is 6 days from now?\
> Hey Mycroft, when in next Friday?

#### Query weekend dates

> Hey Mycroft, what was last weekend?\
> Hey Mycroft, what were the days last weekend?\
> Hey Mycroft, what are the dates this weekend?\
> Hey Mycroft, what are the days for next weekend?

### Hello World

Hello World is a well-documented **Skill** that serves as a starting point for code development. Pleasantries with Mycroft are used as examples.

> Hey Mycroft, greetings \
> Hey Mycroft, hello world
>
> Hey Mycroft, thank you
>
> Hey Mycroft, how are you doing? \
> Hey Mycroft, how was your day?

### IP

Query the SSID or the IP Address (aka the network address) of the Mycroft Device.

**Query the IP address**

> Hey Mycroft, what is your IP address? \
> Hey Mycroft, tell me your network address \
> Hey Mycroft, what network are you connected to?

**Query the SSID**

> Hey Mycroft, what SSID are you on? \
> Hey Mycroft, what wifi network are you using? \
> Hey Mycroft, what network are you connected to?

### Jokes

Mycroft uses pyjokes as the source of jokes to tell.

> Hey Mycroft, tell me a joke \
> Hey Mycroft, make me laugh \
> Hey Mycroft, brighten my day with a Chuck Norris joke \
> Hey Mycroft, tell me a non-offensive joke&#x20;

### Naptime

While 'napping' Mycroft will ignore utterances other than "Wake up".

**Begin nap**

> Hey Mycroft, go to sleep \
> Hey Mycroft, nap time

**End nap**

> Hey Mycroft, wake up

### NPR News

Plays the RSS audio feed for the requested station. If no station is specified or if the request is unknown, a default station is selected based on Device location. Stations include: ABC (Australia), AP, BBC, CBC, DLF, Ekot, FOX, GPB, NPR, PBS, RDP, RNE, TSF, OE3, VRT, WDR, YLE.

**Play the news**

> Hey Mycroft, what's the news? \
> Hey Mycroft, play the BBC news \
> Hey Mycroft, what are the headlines?

**Restart the broadcast**

> Hey Mycroft, start over \
> Hey Mycroft, restart news

**Stop playing the news**

> Hey Mycroft, stop

### Personal

Ask about the "birth" and parentage of Mycroft, and get a taste of the community fostering this open source artificial intelligence.

> Hey Mycroft, who are you? \
> Hey Mycroft, when were you created? \
> Hey Mycroft, what are you? \
> Hey Mycroft, where were you born? \
> Hey Mycroft, who made you? \
> Hey Mycroft, do you even rhyme? \
> Hey Mycroft, do you dream?

### Playback Control

Common commands for controlling a music service.

**Pause the music**

> Hey Mycroft, pause \
> Hey Mycroft, pause the song

**Resume the paused music**

> Hey Mycroft, resume song \
> Hey Mycroft, resume play

**Next track**

> Hey Mycroft, next track

**Previous track**

> Hey Mycroft, previous track

**Play**

User provides a genre/artist/title/playlist/service. Depending on the music service, a dialog may be initiated.

> Hey Mycroft, play my summer playlist \
> Hey Mycroft, play Pandora \
> Hey Mycroft, play something by hermitude \
> Hey Mycroft, play uptown funk on youtube

### Reminder

Manages a collection of reminders. A Reminder is similar to an Alarm but instead of a beep Mycroft speaks the User specified words.

**Set a reminder**

> Hey Mycroft, remind me to **turn off the oven** in **5 minutes** \
> Hey Mycroft, add a reminder to **let the dog out** at **3pm** \
> Hey Mycroft, remind me to **take out the trash** _<- - - Mycroft will ask WHEN_\
> Hey Mycroft, remind me at **5pm** _<- - - - - - - - - Mycroft will ask FOR WHAT_ \
> Hey Mycroft, set a reminder for me _<- - - Mycroft will ask WHEN and FOR WHAT _

**Snooze the active reminder**

> Hey Mycroft, snooze the reminder \
> Hey Mycroft, remind me later

**Cancel the active reminder**

> Hey Mycroft, okay, stop the reminder

**Get reminders for a specific day**

> Hey Mycroft, what are my reminders for today? \
> Hey Mycroft, do I have any reminders tomorrow?

**Get next reminder**

> Hey Mycroft, what is my next reminder?

**Delete all reminders for a specific day**

> Hey Mycroft, cancel today's reminders \
> Hey Mycroft, cancel all reminders for tomorrow

**Delete all reminders**

> Hey Mycroft, delete all reminders

### Singing

Mycroft will speak the lyrics to a random pop music song.

> Hey Mycroft, sing \
> Hey Mycroft, sing me a song

### Speak

Speak a phrase and have Mycroft repeat it.

> Hey Mycroft, speak **Mary had a little lamb** \
> Hey Mycroft, say **yada yada yada** \
> Hey Mycroft, repeat **hey good looking**

### Spelling

Mycroft will spell any word that is understood by the Speech-To-Text system.

> Hey Mycroft, spell **aardvark** \
> Hey Mycroft, what is the spelling of **aardvark**? \
> Hey Mycroft, how do you spell word **aardvark**?

### Stock

This Skill has been disabled.

### Stop

Tell Mycroft to STOP doing whatever it is doing. Should work with all **Skills**.

> Hey Mycroft, stop \
> Hey Mycroft, silence \
> Hey Mycroft, shut up

### Support Helper

Captures troubleshooting information from the Mycroft Device and stores it on the [0x0.st](https://0x0.st) storage service. This information is useful for your own debugging and for communicating with Support. A link to the information is emailed to the address registered at home.mycroft.ai.

> Hey Mycroft, contact support \
> Hey Mycroft, create a support ticket \
> Hey Mycroft, troubleshoot my device \
> Hey Mycroft, create a troubleshoot request&#x20;

### Timer

Manages a collection of timers. Timers are requested with a duration expressed in hours, minutes, and/or seconds. A timer may optionally be given a name. The name is useful in queries, subsequent commands, and for display purposes. All timers beep.

* If you wish to command a specific expiration time (e.g. 'at 3:05pm'), please use either an Alarm or a Reminder. \

* Timers have a duration of less than 24-hours.  When a Timer is requested with a duration greater than 24-hours, an Alarm is set instead. \

* Mycroft refers to a timer by it's original duration and the optional User supplied name.\

* When there is more than one timer with the same duration, Mycroft may include an ordinal (e.g. the second timer for 5-minutes).\

* The User may refer to an individual timer by its name or by the ordinal of its position in the list of timers (e.g. the third timer).

**Start a timer**

> Hey Mycroft, I need a timer named **turkey** for **15 minutes** \
> Hey Mycroft, start a **10-minute** timer called **time to go** \
> Hey Mycroft, set a timer to **take out the trash** _<- - - Mycroft will ask for the DURATION_ \
> Hey Mycroft, ping me in 2 hours _<- - - - - - - - - No NAME is associated with this timer_ \
> Hey Mycroft, Start a timer _<- - - - - - - - Mycroft will ask for the DURATION but not a NAME_ \
> Hey Mycroft, Begin timer

**Query a timer**

> Hey Mycroft, how's my **turkey** timer? \
> Hey Mycroft, how much time is left?

**Cancel the beeping timer**

> Hey Mycroft, cancel the timer

**Cancel a timer in the list of timers**

> Hey Mycroft, cancel the first timer \
> Hey Mycroft, delete the fourth timer \
> Hey Mycroft, remove the **potatoes** timer \
> Hey Mycroft, kill the **turkey** timer

**Cancel all timers**

When no timers are beeping, this command removes all timers from the list. If any timers are beeping, this command stops all of the beeping timers.&#x20;

> Hey Mycroft, cancel all timers \
> Hey Mycroft, delete all timers

**Mute timer**

Muting stops the beep but leaves the timer in the list so that expired timers can be displayed.&#x20;

> Hey Mycroft, mute the timer \
> Hey Mycroft, silence the timer

### Version Checker

Check the version of the software. If an update exists, Mycroft will ask if the User wishes to update. To keep up-to-date, Mycroft automatically performs these checks on a daily basis.

**Query the Mycroft software version (mycroft-core)**

> Hey Mycroft, check version \
> Hey Mycroft, what is code?

**Query the platform (e.g. Picroft, Mark 1) build version**

> Hey Mycroft, find platform version \
> Hey Mycroft, what is platform build?

### Volume

Manages Mycroft's volume level.

**Query volume level**

> Hey Mycroft, what is the volume? \
> Hey Mycroft, how loud?

**Set volume to a numeric level (0 to 10)**

In a tribute to Spinal Tap, a level of '11' is accepted (equivalent to level 10).&#x20;

> Hey Mycroft, increase volume to 8 \
> Hey Mycroft, set sound to NORMAL _<- - - Keyword options: NORMAL=6, QUIET=3, LOUD=9_

**Set volume to a percentage (0 to 100%)**

> Hey Mycroft, set audio to 75 percent \
> Hey Mycroft, decrease volume to 50 percent

**Set to maximum volume**

> Hey Mycroft, crank it all the way up \
> Hey Mycroft, set audio to max

**Increase volume by one numeric level**

> Hey Mycroft, raise the sound\
> Hey Mycroft, make it higher\
> Hey Mycroft, louder

**Decrease volume by one numeric level**

> Hey Mycroft, lower the sound\
> Hey Mycroft, make it quieter\
> Hey Mycroft, softer

**Mute**

> Hey Mycroft, mute the volume \
> Hey Mycroft, silence the audio

**Unmute**

> Hey Mycroft, unmute the speaker \
> Hey Mycroft, restore the sound

### Weather

An interface to OpenWeatherMap.org that supports an extensive set of queries.

> Hey Mycroft, what is the weather? \
> Hey Mycroft, what is the forecast tomorrow? \
> Hey Mycroft, what is the weather going to be like Tuesday? \
> Hey Mycroft, what is the weather in Houston? \
> Hey Mycroft, when will it rain next? \
> Hey Mycroft, how windy is it? \
> Hey Mycroft, what's the humidity? \
> Hey Mycroft, is it going to snow? \
> Hey Mycroft, what's the temperature?

### Wiki

Interfaces to Wikipedia.org

**Query Wikipedia**

> Hey Mycroft, what does Wikipedia say about chocolate? \
> Hey Mycroft, tell me about artificial intelligence \
> Hey Mycroft, search Grace Hopper

**Ask Wikipedia for more details on same subject**

> Hey Mycroft, tell me more \
> Hey Mycroft, please continue

**Let Wikipedia select the subject**

> Hey Mycroft, teach me something \
> Hey Mycroft, tell me a random thing

## The Fallback Handlers

Mycroft has two _fallback_ handlers for the situation where the natural language processing fails to match a specific **Intent** and **Skill**; one for queries and one for unknowns.

By default, Mycroft has access to two general purpose search engines: Duck Duck Go and Wolfram Alpha. When the **utterance** is a query, Mycroft sends it to all of these Common Query search engines simultaneously. The first engine to reply successfully is the search engine selected by Mycroft to reply to the User.

If no search engine provides a successful answer to the query, or if the **utterance** was not a query, then Mycroft activates the Unknown Handler that responds with a variety of phrases explaining that Mycroft cannot handle the **utterance**.

### Common Query

Sent to all _fallback_ Common Query search engines.

> Hey Mycroft, what is Frankenstein? \
> Hey Mycroft, who is Kathryn Johnson? \
> Hey Mycroft, how high is Mount Everest? \
> Hey Mycroft, how many inches in a meter?

### Subsequent Commands to a Common Query

A Common Query search engine may optionally support subsequent commands (e.g. "send me details") that are processed if that search engine handled the initial query.

#### Subsequent commands for Wolfram Alpha:

**Have more details of last query emailed to User**

> Hey Mycroft, send me details on that \
> Hey Mycroft, email sources to me

## More information on Skills

For more information on Skills, please see the [Skills section](http://mycroft.ai/documentation/skills/)
