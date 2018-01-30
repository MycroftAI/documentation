---
ID: 32440
post_title: Skills
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/documentation/skills/
published: true
post_date: 2017-12-02 22:35:25
---
# Mycroft Skills

- [Mycroft Skills](#mycroft-skills)
  * [Overview](#overview)
  * [Core Skills](#core-skills)
  * [Community Developed Skills](#community-developed-skills)
    + [Community Developed Skills status meaning](#community-developed-skills-status-meaning)
    + [Skills looking for feedback and testing](#skills-looking-for-feedback-and-testing)

## Overview

**Skills** provide Mycroft with functionality. **Skills** are what allow Mycroft to tell you the weather in your location, display the time in another timezone, play you a song or tell you a Chuck Norris joke.

Mycroft determines what **Skill** should handle an **Utterance** by using an **intent parser** like Adapt(http://mycroft.ai/documentation/adapt/) or [Padatious](http://mycroft.ai/documentation/padatious/) to identify the **intent** of the user. For instance, if the **intent parser** determines that the user is asking about the *weather*, then Mycroft will pass the **intent data** to the *Weather Skill*.

Mycroft comes with several **Skills** built in. These are called *core skills*. It is easy to add more **Skills** to Mycroft.

**Skills** are developed both by Mycroft.AI staff, as well as our Developer Community. Management of **Skills** - comprising activities such as code review, skill planning and Skill security - has been delegated to the **Skills Management Team**. The **Skills Management Team** is made up of both Mycroft.AI staff and experienced members of the Developer Community, ensuring that Mycroft's product development remains firmly focussed on community needs.

If you want to develop new **Skills** for Mycroft, you will need to know the Python programming language, as all Skills are developed in Python.

## Core Skills

The table below shows the core **Skills** installed with Mycroft by default, and how to trigger them.

|      Skill Name                                                                                                      | Description<br>"handled phrases"                                              |
| ---------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------|
|[AIML Fallback](https://github.com/forslund/fallback-aiml#readme)                                                     | AIML skill by JarbasAI                                                        |
|[Alarm](https://github.com/MycroftAI/skill-alarm#readme)                                                              | Alarm                                                                         |
|[Audio Record](https://github.com/MycroftAI/skill-audio-record#readme)                                                | Record and Play Audio<br>```"record"```                                       |
|[Configuration](https://github.com/mycroftai/skill-configuration#readme)                                              | Update Mycroft configuration<br>```"configuration update"```                  |
|[Date Time](https://github.com/MycroftAI/skill-date-time#readme)                                                      | Tell the date or time<br> ```"what time is it"```                             |
|[Desktop Launcher](https://github.com/MycroftAI/skill-desktop-launcher#readme)                                        | Open Applications on Desktop<br>```"open firefox"```                          |
|[DuckDuckGo](https://github.com/MycroftAI/fallback-duckduckgo#readme)                                                 | Query DuckDuckGo for general questions<br> ```"what is frankenstein"```       |
|[Hello World](https://github.com/mycroftai/skill-hello-world#readme)                                                  | Hello world and Mycroft manners<br> ```"how are you"```                       |
|[IP](https://github.com/MycroftAI/skill-ip#readme)                                                                    | Check the device's IP Address<br> ```"what is your ip address"```             |
|[Joke](https://github.com/MycroftAI/skill-joke#readme)                                                                | Tell jokes<br> ```"tell me a joke"```                                         |
|[Installer](https://github.com/mycroftai/skill-installer#readme)                                                      | Install skills<br> ```"install daily meditation"```<br>```"uninstall skill"```|
|[Mark-1 Demo](https://github.com/MycroftAI/skill-mark1-demo#readme)                                                   | Demonstration of Mark 1                                                       |
|[Media](https://github.com/MycroftAI/skill-media#readme)                                                              | Multimedia Control<br>```"play", "pause", "next track"```                     |
|[Naptime](https://github.com/mycroftai/skill-naptime#readme)                                                          | Put Mycroft to sleep<br>```"go to sleep"```                                   |
|[NPR News](https://github.com/MycroftAI/skill-npr-news#readme)                                                        | Listen to the news from NPR<br>```"news"```<br>```"stop news"```              |
|[Pairing](https://github.com/mycroftai/skill-pairing#readme)                                                          | Pair Mycroft with home.mycroft.ai<br>```"pair my device"```                   |
|[Personal](https://github.com/MycroftAI/skill-personal#readme)                                                        | Learn about Mycroft<br>```"what are you"```                                   |
|[Playback Control](https://github.com/mycroftai/skill-playback-control#readme)                                        | Control audio subsystem<br>```"play"```                                       |
|[Release Test](https://github.com/MycroftAI/skill-release-test)                                                       | Test Mycroft release<br>```"release test"```                                  |
|[Reminder](https://github.com/MycroftAI/skill-reminder#readme)                                                        | Reminders <br>```"remind me to turn off the oven in 5 minutes"```             |
|[Speak](https://github.com/MycroftAI/skill-speak#readme)                                                              | Repeat anything<br>```"say open source AI"```                                 |
|[Singing](https://github.com/MycroftAI/skill-singing#readme)                                                          | Sing some Songs<br>```"sing a song"```                                        |
|[Stock](https://github.com/MycroftAI/skill-stock#readme)                                                              | Stock prices<br>```"stock price of Google"```                                 |
|[Stop](https://github.com/mycroftai/skill-stop#readme)                                                                | Stop running skills<br>```"stop"```                                           |
|[Support](https://github.com/MycroftAI/skill-support#readme)                                                          | Gather support inormation<br>```"create a support ticket"```                  |    
|[Version Checker](https://github.com/MycroftAI/skill-version-checker#readme)                                          | Find the version of mycroft-core<br>```"check version"```                     |
|[Volume](https://github.com/mycroftai/skill-volume#readme)                                                            | Increases or Decreases/Mutes Volume<br>```"reduce volume"```                  |
|[Weather](https://github.com/MycroftAI/skill-weather#readme)                                                          | Current Weather and Forecasts<br>```"what is the weather"```                  |
|[Wiki](https://github.com/MycroftAI/skill-wiki#readme)                                                                | Wikipedia queries<br>```"tell me about AI"```                                 |
|[Platform Patch](https://github.com/MycroftAI/skill-platform-patch#readme)                                            | Patching for official platforms<br>```"platform patch"```                     |

## Community Developed Skills

The table of **Skills** below have all been contributed by the Developer Community. Some of them are experimental, so a *Status* has been included so you know how mature the **Skill** is.

### Community Developed Skills status meaning

* GOOD - good working order  
* WIP -  still being developed and not ready for general use (for reference/collaboration)  
* UNKNOWN - untested (by Mycroft)  
* BROKEN - Broken, but good for ideas!

| Status  | Skill Name                                                                                         | Description<br>```"phrase to trigger"```    |
| ------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------|
| UNKNOWN | [amarok-media-player-skill](https://github.com/AIIX/amarok-player-skill#readme)                    | Player controls for the Amarok Media Player<br>```"amarok play/stop/next/previous music"``` |
| UNKNOWN | [angry-beanie-podcast-player](https://github.com/purserj/mycroft-angrybeanie#readme)               | Skill for querying and playing Angry Beanie Podcasts<br />```"Get Angry Beanie shows"``` |
| GOOD    | [autogui-skill](https://github.com/eClarity/skill-autogui)                                         | Manipulate your mouse and keyboard with Mycroft                                                  |
| UNKNOWN | [audio-control-plasma](https://github.com/AIIX/audio-control-plasma#readme)                        | Audio control for Plasma Desktop<br>```"increase volume to maximum", "decrease microphone to minimum volume"```         |
| GOOD    | [basichelp](https://github.com/btotharye/mycroft-skill-basichelp#readme)                           | Get basic mycroft questions and help answered<br>```"where is the documentation", "how do I install from source"```         |
| UNKNOWN | [bioinformatics](https://github.com/TicklishGiraffe/mycroft_genomics)                              | Adds Bio-Linux Commands to Mycroft   |  
| UNKNOWN | [bitcoin](https://github.com/chrison999/mycroft-skill-bitcoin-enhanced)                            | Check the price of bitcoin                                                               |  
| WIP     | [bitcoin-price](https://github.com/dmp1ce/mycroft-bitcoinprice-skill)                              | Checks the price of bitcoin                             |
| WIP     | [brain-skill](https://github.com/skeledrew/brain-skill)                                            | Chain intents and provide some services                                                 |
| GOOD    | [skill-caffeinewiz](https://github.com/reginaneon/skill-caffeinewiz.git)                           | Provides the caffeine content of various drinks on request.<br>```what's caffeine content of *drink*?```
| WIP     | [skill-calculator](https://github.com/TREE-Edu/calculator-skill)                                   | Provides a conversational based calculator.<br>```Do some math```
| UNKNOWN | [cbc-news-skill](https://github.com/chrison999/mycroft-skill-cbc-news)                             | Fetches CBC News Podcast             |  
| UNKNOWN | [clarifai-image-recognition-skill](https://github.com/AIIX/clarifai-image-recognition-skill#readme)| Image recognition skill based on clarifai<br> ```"search image url [imagelocation]"```   |
| UNKNOWN | [clementine-player-skill](https://github.com/hersche/mycroft-clementine-skill)                     | Controls your clementine-player localy. A fork from amarok-player.   |
| UNKNOWN | [cleverbot-skill](https://github.com/JarbasAI/skill_cleverbot)                                     | cleverbot api fallback skill   |
| GOOD    | [coin-flip-skill](https://github.com/wligtenberg/coin-flip-skill)                                  | Flip a virtual coin   |
| UNKNOWN | [daily-meditation](https://github.com/kfezer/daily_meditation)                                     | Plays your Daily Meditation from the  Meditation Podcast     |
| WIP     | [deepdream_skill](https://github.com/JarbasAI/mycroft-deepdream-skill)                             | Adds Deepdreaming image converstion to Mycroft       |
| UNKNOWN | [diagnostics](https://github.com/the7erm/mycroft-skill-diagnostics)                                | Diagnostic tools (CPU %age, free space, etc)    |
| WIP     | [dice-roll](https://github.com/Friday811/skill-dice)                                               | Rolls dice spoken in RPG notation.                                                       |
| UNKNOWN | [domoticz_skill](https://github.com/matleses/domoticz_skill)                                       | Skill integrating Mycroft with Domoticz    |
| UNKNOWN | [drive_servos](https://github.com/Nold360/mycroft_skill-drive_servos)                              | Control Hacked-Servo-Engines to make your mycroft move around   |
| GOOD    | [easter-eggs](https://github.com/JarbasAI/skill_easter_eggs)                                       | Pop culture references and other easter eggs  |
| UNKNOWN | [earth-orbit-pic-skill](https://github.com/JarbasAI/mycroft---astronomy-picture-of-teh-day)        | Earth orbit picture skill   |
| BROKEN  | [enhanced-bitcoin-skill](https://github.com/chrison999/mycroft-skill-bitcoin-enhanced)             | Enhanced bitcoin skill from api.bitcoinaverage.com        |
| WIP     | [facebook](https://github.com/JarbasAI/mycroft-facebook-skill)                                     | Generates posts for Facebook                  |
| WIP     | [facebook-marketing](https://github.com/ProsperousHeart/mycroft-facebook-marketing)                | Works with Facebook Marketing API                                                        |
| UNKNOWN | [feedback-skill](https://github.com/JarbasAI/mycroft-feedback-skill)                               | Triggers positive feedback intent -> calls feedback method on last active skill          |  
| UNKNOWN | [fox-news-skill](https://github.com/chrison999/mycroft-skill-fox-news)                             | Fetches Fox News Podcast                                                                 |
| UNKNOWN | [Google-calendar](https://github.com/jcasoft/GoogleCalendar-Skill)                                 | Check and add Google Calendar events                                                     |  
| UNKNOWN | [Google-gmail](https://github.com/jcasoft/GoogleGmailSkill)                                        | Get emails from your Gmail Inbox                                                         |  
| UNKNOWN | [Google-image-search](https://github.com/JarbasAI/mycroft-pictureskill)                            | Search Google images for search term and display                                         |
| UNKNOWN | [Google-translate](https://github.com/jcasoft/TranslateSkill)                                      | Translate English phrases into other languages                                           |
| WIP     | [gpio-example](https://github.com/MycroftAI/picroft_example_skill_gpio)                            | Example skill using the GPIO pins on the Raspberry Pi to blink an LED                                         |    
| UNKNOWN | [hue](https://github.com/ChristopherRogers1991/mycroft-hue)                                        | Control your Phillips Hue lights                                                         |  
| GOOD    | [home-assistant](https://github.com/btotharye/mycroft-homeassistant#readme)                        | Control your devices in home-assistant<br>```"turn on office"```                                                      |  
| UNKNOWN | [irsend](https://github.com/ChristopherRogers1991/mycroft-hue)                                     | Control devices via [lirc's](http://www.lirc.org/) [irsend](http://www.lirc.org/html/irsend.html)                                                         |
| UNKNOWN | [jb-podcasts](https://github.com/the7erm/mycroft-skill-jupiter-broadcasting)                       | Play podcasts from Jupiter Broadcasting shows                                            |  
| UNKNOWN | [krunner-search](https://github.com/AIIX/krunner-search-skill#readme)                              | Search local KDE desktop for files, images, recent documents, bookmarks<br>```"search this computer for [any keyword]"```                  |
| UNKNOWN | [kodi-cadair](https://github.com/Cadair/mycroft-kodi)                                              | Kodi playback and search                                                                 |  
| UNKNOWN | [kodi-cbenning](https://github.com/cbenning/kodi-skill)                                            | Control a local or remote Kodi instance                                                  |  
| UNKNOWN | [kodi-k3yb0ardn1nja](https://github.com/k3yb0ardn1nja/mycroft-skill-kodi)                          | Play or pause a Kodi video                                                               |  
| UNKNOWN | [let's-talk-skill](https://github.com/chrison999/mycroft-skill-lets-talk)                          | More salutations |
| UNKNOWN | [lottery-skill](https://github.com/JarbasAI/mycroft---euromillions-skill)                          | Reads Euromillion Lottery Numbers     |
| UNKNOWN | [media-console-control](https://github.com/the7erm/mycroft-skill-simple-media-controls)            | Adds media controls that are mapped to console commands                                  |  
| UNKNOWN | [metal-band-skill](https://github.com/JarbasAI/mycroft---metal-recomend---skill)                   | Recommends a metal band and gives basic information    |
| WIP     | [milight](https://github.com/maxppc/Mycroft-milight-skill)                                         | Lighting control using MiLight                                                           |  
| GOOD    | [mopidy](https://github.com/forslund/mopidy_skill)                                                 | Mopidy-based players for local music, Google Music, and Spotify                          |  
| WIP     | [mopidy-and-bt-lights](https://github.com/swilso793/mycroft_third_party_skills)                    | Remote control of BT lights and Mopidy music playback                                    |  
| UNKNOWN | [movie-recommendation-skill](https://github.com/JarbasAI/mycroft---movie-recommend-skill)          | Recomends a movie  |
| GOOD    | [mp3-demo](https://github.com/ethanaward/demo_skill)                                               | Simple sample of playing local MP3s                                                      |  
| UNKNOWN | [mpd-control](https://github.com/forslund/mpd_skill)                                               | Controls media players that use the MPD  protocol to play found local music           |  
| UNKNOWN | [mqtt](https://github.com/jamiehoward430/mycroft-mymqtt)                                           | Control IoT devices (home automation) using MQTT protocol     |  
| UNKNOWN | [mute-skill](https://github.com/JarbasAI/mycroft---mute-skill)                                     | Mutes Mycroft until re-enabled |
| UNKNOWN | [nasa-picture-of-the-day](https://github.com/JarbasAI/mycroft---astronomy-picture-of-teh-day)      | Nasa picture of the day from the NASA API |
| UNKNOWN | [near-earth-orbit-skill](https://github.com/JarbasAI/mycroft---near-earth-object-tracker)          | Near Earth orbit alert skill via the NASA API   |
| GOOD    | [number-generator-skill](https://github.com/angry-frog/number-generator-skill)                     | Randomly generate a number between 1-100 <br>```Pick a number``` |
| WIP     | [objective-skill](https://github.com/JarbasAI/service_objectives)                                  | skills can now register objectives almost the same has an intent would be registered with ObjectiveBuilder class              |
| WIP     | [openhab-skill](https://github.com/openhab/openhab-mycroft)                                        | This skill adds Openhab support to Mycroft |
| UNKNOWN | [pandora-skill](https://github.com/ethanaward/pianobar-skill)                                      | Adds Pandora to mycroft via Pianobar  |
| UNKNOWN | [photolocation-skill](https://github.com/JarbasAI/mycroft-photolocation-skill)                     | Searches Wikimedia for photos of location  |
| GOOD    | [ping-skill](https://github.com/nogre/ping-skill)                                                  | Pings websites and responds with latency time       |  
| UNKNOWN | [plasma-activities-skill](https://github.com/AIIX/plasma-activities-skill#readme)                  | This skill integrates Plasma 5 Activities with Mycroft<br>```"show activities / switch activity [name]"```|
| UNKNOWN | [plasma-sendsms-skill](https://github.com/AIIX/plasma-sendsms-skill#readme)                        | Send SMS through KDE Plasma<br>```"send a sms"```     |
| UNKNOWN | [plasma-user-control-skill](https://github.com/AIIX/plasma-user-control-skill#readme)              | This skills adds Plasma User control to Mycroft, allowing switch user, logout, and lock screen<br>```"switch user/logout/lock screen"```  |
| UNKNOWN | [poetry-skill](https://github.com/JarbasAI/mycroft-poetry-skill)                                   | Reads poetry based on Hidden Markov Models     |
| UNKNOWN | [proxy-scrape-skill](https://github.com/JarbasAI/mycroft--proxy-scrapping---skill)                 | Scrape proxies from the internet    |
| UNKNOWN | [pushbullet](https://github.com/jcasoft/PushbulletSkill)                                           | Send messsages and photos using Pushbullet                                                  |  
| UNKNOWN | [pushetta-skill](https://github.com/marksev1/Mycroft-Pushetta-skill)                               | Adds push notifications|
| UNKNOWN | [quodlibet](https://github.com/kfarwell/mycroft-skill-quodlibet)                                   | Control Quod Libet music playback                                                        |  
| UNKNOWN | [random-quote-skill](https://github.com/JarbasAI/mycroft---quotes---skill)                         | Adds random quotes,random facts about numbers, and your time left to live          |
| UNKNOWN | [ratp-timetables](https://github.com/ldubost/mycroft-skills)                                       | Access schedules for the RATP Network of trains and buses in Paris                       |  
| WIP     | [read-article-skill](https://github.com/JarbasAI/mycroft-articles-skill)                           | Scrapes text from online articles and reads them to you.   |
| UNKNOWN | [rss-skill](https://github.com/forslund/rss_skill)                                                 | Fetches from RSS feed   |
| WIP     | [sentiment-analysis-skill](https://github.com/JarbasAI/service_sentiment_analisys)                 | Sentiment analysis              |
| WIP     | [slack-skill](https://github.com/guilhembn/Mycroft-Slack-skill)                                    | Integrate Mycroft with Slack<br>```Send <my message> on Slack``` |
| UNKNOWN | [spaceflight-schedule](https://github.com/praxeo/mycroft_spaceflightnow_skill)                     | Check when the next space flight launch is                                               |
| GOOD    | [skill-radio-rne](https://github.com/ReK2Fernandez/skill-radio-rne)                                | Spanish news radio Radio Nacional de Espa?a RNE. |
| GOOD    | [skill-the-cows-lists])https://github.com/CarstenAgerskov/skill-the-cows-lists)                    | Integration with Remember the Milk<br>```"Hey Mycroft, add milk to my grocery list"``` |
| UNKNOWN | [spacelaunch-skill](https://github.com/marksev1/Mycroft-SpaceLaunch-Skill)                         | Check when the next space launch is                                               |
| UNKNOWN | [speedtest](https://github.com/ChristopherRogers1991/mycroft-speedtest)                            | Run a speedtest                                               |
| UNKNOWN | [sunspot-skill](https://github.com/BoatrightTBC/sunspots)                                          | Answers questions on daily sunspots |
| UNKNOWN | [sun-skill](https://github.com/marksev1/Mycroft-SunSkill)                                          | Responds with sunrise and set times          |  
| UNKNOWN | [system-skill](https://github.com/CloneMMDDCVII/systemSkill-Mycroft-core-Skill-)                   | Adds system controls like shutdown and reboot   |
| UNKNOWN | [take_picture](https://github.com/Nold360/mycroft_skill-take_picture)                              | Take Pictures using the Raspberry Pi Camera          |  
| UNKNOWN | [traffic-skill](https://github.com/BongoEADGC6/mycroft-traffic)                                    | Gets the commute time from Google distance matrix api         |  
| GOOD    | [twitter-skill](https://github.com/btotharye/mycroft-twitter-skill#readme)                         | Control twitter with Mycroft<br>```"How many Twitter followers do I have"```                                                                                                         |
| UNKNOWN | [unsplash-wallpaper-plasma-skill](https://github.com/AIIX/unsplash-wallpaper-plasma-skill#readme)  | Change KDE Desktop wallpaper by category type from unsplash<br>```"change wallpaper type [natureabstractany]"``` |
| WIP     | [wallpaper-skill](https://github.com/JarbasAI/mycroft---wallpaper---skill)                         | Downloads wallpapers from reddit and changes randomly         |
| UNKNOWN | [wemo-skill](https://github.com/martymulligan/skill-wemo)                                          | Control Wemo devices with mycroft                                                   |
| WIP     | [wifi-management-skill](https://github.com/JarbasAI/mycroft-wifi-skill)                            | Various options for interacting with WiFi        |
| GOOD    | [wink-smart-home](https://github.com/MycroftAI/skill-wink-iot)                                     | Interact with lights via a Wink-hub                                                      |  
| UNKNOWN | [wiki-fact-scraper-skill](https://github.com/JarbasAI/mycroft---knowledge-skill/)                  | Scrapes for random facts from wikipedia and stores locally    |
| UNKNOWN | [youtube](https://github.com/augustnmonteiro/mycroft-youtube)                                      | Search and listen to a Youtube video                                                        |  


### Skills looking for feedback and testing

The following Skills are in active development, and Community Developers would appreciate help with testing and feedback.

* [Pomodoro Skill](https://github.com/erabti/mycroft-pomodoro-skill): This **Skill** provides functionality for time management using the [Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) technique.
