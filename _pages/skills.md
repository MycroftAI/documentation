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

## Overview

**Skills** provide Mycroft with functionality. **Skills** are what allow Mycroft to tell you the weather in your location, display the time in another timezone, play you a song or tell you a Chuck Norris joke.

Mycroft determines what **Skill** should handle an **Utterance** by using an **intent parser** like Adapt(http://mycroft.ai/documentation/adapt/) or [Padatious](http://mycroft.ai/documentation/padatious/) to identify the **intent** of the user. For instance, if the **intent parser** determines that the user is asking about the *weather*, then Mycroft will pass the **intent data** to the *Weather Skill*.

Mycroft comes with several **Skills** built in. These are called *core skills*. It is easy to add more **Skills** to Mycroft.

**Skills** are developed both by Mycroft.AI staff, as well as our Developer Community. Management of **Skills** - comprising activities such as code review, skill planning and Skill security - has been delegated to the **Skills Management Team**. The **Skills Management Team** is made up of both Mycroft.AI staff and experienced members of the Developer Community, ensuring that Mycroft's product development remains firmly focussed on community needs.

If you want to develop new **Skills** for Mycroft, you will need to know the Python programming language, as all Skills are developed in Python.

## Core Skills

The table below shows the core **Skills** installed with Mycroft by default, and how to trigger them.

|      Skill Name                                              |                Description<br>"handled phrases"                      |                                           
| -------------------------------------------------------------| ---------------------------------------------------------------------|
|[AIML Fallback](https://github.com/forslund/fallback-aiml#readme)|          AIML skill by JarbasAI                                   |
|[Alarm](https://github.com/MycroftAI/skill-alarm#readme)             |          Alarm                                                       |
|[Audio Record](https://github.com/MycroftAI/skill-audio-record#readme)|         Record and Play Audio<br>```"record"```                       |
|[Configuration](https://github.com/mycroftai/skill-configuration#readme)|       Update Mycroft configuration<br>```"configuration update"```  |
|[Date Time](https://github.com/MycroftAI/skill-date-time#readme)     |          Tell the date or time<br> ```"what time is it"```             |
|[Desktop Launcher](https://github.com/MycroftAI/skill-desktop-launcher#readme)| Open Applications on Desktop<br>```"open firefox"```          |
|[DuckDuckGo](https://github.com/MycroftAI/fallback-duckduckgo#readme)| Query DuckDuckGo for general questions<br> ```"what is frankenstein"```|
|[Hello World](https://github.com/mycroftai/skill-hello-world#readme) | Hello world and Mycroft manners<br> ```"how are you"```                |
|[IP](https://github.com/MycroftAI/skill-ip#readme)                   | Check the device's IP Address<br> ```"what is your ip address"```      |
|[Joke](https://github.com/MycroftAI/skill-joke#readme)               | Tell jokes<br> ```"tell me a joke"```                                  |
|[Installer](https://github.com/mycroftai/skill-installer#readme)     | Install skills<br> ```"install daily meditation"```<br>```"uninstall skill"```                                                                                                                             |
|[Mark-1 Demo](https://github.com/MycroftAI/skill-mark1-demo#readme)  | Demonstration of Mark 1                                              |
|[Media](https://github.com/MycroftAI/skill-media#readme)             | Multimedia Control<br>```"play", "pause", "next track"```            |
|[Naptime](https://github.com/mycroftai/skill-naptime#readme)         | Put Mycroft to sleep<br>```"go to sleep"```                          |
|[NPR News](https://github.com/MycroftAI/skill-npr-news#readme)       | Listen to the news from NPR<br>```"news"```<br>```"stop news"```     |
|[Pairing](https://github.com/mycroftai/skill-pairing#readme)         | Pair Mycroft with home.mycroft.ai<br>```"pair my device"```          |
|[Personal](https://github.com/MycroftAI/skill-personal#readme)       | Learn about Mycroft<br>```"what are you"```                          |
|[Playback Control](https://github.com/mycroftai/skill-playback-control#readme)| Control audio subsystem<br>```"play"```                     |
|[Reminder](https://github.com/MycroftAI/skill-reminder#readme)       | Reminders to do something<br>```"remind me to turn off the oven in 5 minutes"```                                                                                                                           |
|[Speak](https://github.com/MycroftAI/skill-speak#readme)             | Repeat anything<br>```"say open source AI"```                        |
|[Singing](https://github.com/MycroftAI/skill-singing#readme)         | Sing some Songs<br>```"sing a song"```                               |
|[Stock](https://github.com/MycroftAI/skill-stock#readme)             | Stock prices<br>```"stock price of google"```                        |
|[Stop](https://github.com/mycroftai/skill-stop#readme)               | Stop running skills<br>```"stop"```                                  |
|[Version Checker](https://github.com/MycroftAI/skill-version-checker#readme)| Find the version of mycroft-core<br>```"check version"```     |
|[Volume](https://github.com/mycroftai/skill-volume#readme)           | Increases or Decreases/Mutes Volume<br>```"reduce volume"```         |
|[Weather](https://github.com/MycroftAI/skill-weather#readme)         | Current Weather and Forecasts<br>```"what is the weather"```         |
|[Wiki](https://github.com/MycroftAI/skill-wiki#readme)               | Wikipedia queries<br>```"tell me about AI"```                        |
|[Platform Patch](https://github.com/MycroftAI/skill-platform-patch#readme)| Patching for official platforms<br>```"platform patch"```       |

## Community Developed Skills

The table of **Skills** below have all been contributed by the Developer Community. Some of them are experimental, so a *Status* has been included so you know how mature the **Skill** is.

### Community Developed Skills status meaning

:heavy_check_mark: good working order  
:construction:     still being developed and not ready for general use (for reference/collaboration)  
:question:         untested (by us)  
:skull:            Broken, but good for ideas!

| Status              | Skill Name                                                     | Description<br>```"phrase to trigger"```    |
| ------------------- | -------------------------------------------------------------- | --------------------------------------------|
| :question:          | [amarok-media-player-skill](https://github.com/AIIX/amarok-player-skill#readme)               | Player controls for the Amarok Media Player<br>```"amarok play/stop/next/previous music"``` |
| :question:          | [angry-beanie-podcast-player](https://github.com/purserj/mycroft-angrybeanie#readme)         | Skill for querying and playing Angry Beanie Podcasts<br />```"Get Angry Beanie shows"``` |
| :heavy_check_mark:  | [autogui-skill](https://github.com/eClarity/skill-autogui)                      | Manipulate your mouse and keyboard with Mycroft                                                  |
| :question:          | [audio-control-plasma](https://github.com/AIIX/audio-control-plasma#readme)| Audio control for Plasma Desktop<br>```"increase volume to maximum", "decrease microphone to minimum volume"```         |
| :heavy_check_mark:  | [basichelp](https://github.com/btotharye/mycroft-skill-basichelp#readme)| Get basic mycroft questions and help answered<br>```"where is the documentation", "how do I install from source"```         |
| :question:          | [bioinformatics](https://github.com/TicklishGiraffe/mycroft_genomics)               | Adds Bio-Linux Commands to Mycroft   |  
| :question:          | [bitcoin](https://github.com/chrison999/mycroft-skill-bitcoin-enhanced)                            | Check the price of bitcoin                                                               |  
| :construction:      | [bitcoin-price](https://github.com/dmp1ce/mycroft-bitcoinprice-skill)                |  Checks the price of bitcoin                             |
| :construction:      | [brain-skill](https://github.com/skeledrew/brain-skill)                          |  Chain intents and provide some services                                                 |
| :construction:      | [skill-calculator](https://github.com/TREE-Edu/calculator-skill)| Provides a conversational based calculator.<br>```Do some math```
| :question:          | [cbc-news-skill](https://github.com/chrison999/mycroft-skill-cbc-news)        | Fetches CBC News Podcast             |  
| :question:          | [clarifai-image-recognition-skill](https://github.com/AIIX/clarifai-image-recognition-skill#readme)      | Image recognition skill based on clarifai<br> ```"search image url [imagelocation]"```   |
| :question:          | [clementine-player-skill](https://github.com/hersche/mycroft-clementine-skill)  | Controls your clementine-player localy. A fork from amarok-player.   |
| :question:          | [cleverbot-skill](https://github.com/JarbasAI/skill_cleverbot)        | cleverbot api fallback skill   |
| :heavy_check_mark:  | [coin-flip-skill](https://github.com/wligtenberg/coin-flip-skill)        | Flip a virtual coin   |
| :question:          | [daily-meditation](https://github.com/kfezer/daily_meditation)          |Plays your Daily Meditation from the  Meditation Podcast     |
| :construction:      | [deepdream_skill](https://github.com/JarbasAI/mycroft-deepdream-skill)                  | Adds Deepdreaming image converstion to Mycroft       |
| :question:          | [diagnostics](https://github.com/the7erm/mycroft-skill-diagnostics)                    | Diagnostic tools (CPU %age, free space, etc)    |
| :construction:      | [dice-roll](https://github.com/Friday811/skill-dice)                             | Rolls dice spoken in RPG notation.                                                       |
| :question:          | [domoticz_skill](https://github.com/matleses/domoticz_skill)                    | Skill integrating Mycroft with Domoticz    |
| :question:          | [drive_servos](https://github.com/Nold360/mycroft_skill-drive_servos)                  | Control Hacked-Servo-Engines to make your mycroft move around   |
| :heavy_check_mark:  | [easter-eggs](https://github.com/JarbasAI/skill_easter_eggs)                    | Pop culture references and other easter eggs  |
| :question:          | [earth-orbit-pic-skill](https://github.com/JarbasAI/mycroft---astronomy-picture-of-teh-day)      | Earth orbit picture skill   |
| :skull:             | [enhanced-bitcoin-skill](https://github.com/chrison999/mycroft-skill-bitcoin-enhanced)  | Enhanced bitcoin skill from api.bitcoinaverage.com        |
| :construction:      | [facebook](https://github.com/JarbasAI/mycroft-facebook-skill)                          | Generates posts for Facebook                  |
| :construction:      | [facebook-marketing](https://github.com/ProsperousHeart/mycroft-facebook-marketing)      | Works with Facebook Marketing API                                                        |
| :question:          | [feedback-skill](https://github.com/JarbasAI/mycroft-feedback-skill)                    | triggers positive feedback intent -> calls feedback method on last active skill          |  
| :question:          | [fox-news-skill](https://github.com/chrison999/mycroft-skill-fox-news)                    | Fetches Fox News Podcast                                                                 |
| :question:          | [google-calendar](https://github.com/jcasoft/GoogleCalendar-Skill)            | Check and add google calendar events                                                     |  
| :question:          | [google-gmail](https://github.com/jcasoft/GoogleGmailSkill)                  | Get emails from your Gmail Inbox                                                         |  
| :question:          | [google-image-search](https://github.com/JarbasAI/mycroft-pictureskill)    | Search google images for search term and display                                         |
| :question:          | [google-translate](https://github.com/jcasoft/TranslateSkill)          | Translate English phrases into other languages                                           |
| :construction:      | [gpio-example](https://github.com/MycroftAI/picroft_example_skill_gpio)                            | Example skill using the GPIO pins on the Raspberry Pi to blink an LED                                         |    
| :question:          | [hue](https://github.com/ChristopherRogers1991/mycroft-hue)                                    | Control your Phillips Hue lights                                                         |  
| :heavy_check_mark:  | [home-assistant](https://github.com/btotharye/mycroft-homeassistant#readme)| Control your devices in home-assistant<br>```"turn on office"```                                                      |  
| :question:          | [irsend](https://github.com/ChristopherRogers1991/mycroft-hue)                              | Control devices via [lirc's](http://www.lirc.org/) [irsend](http://www.lirc.org/html/irsend.html)                                                         |
| :question:          | [jb-podcasts](../../wiki/SKILL-Jupiter-Broadcasting-Podcasts)  | Play podcasts from Jupiter Broadcasting shows                                            |  
| :question:          | [krunner-search](https://github.com/AIIX/krunner-search-skill#readme) | Search local KDE desktop for files, images, recent documents, bookmarks<br>```"search this computer for [any keyword]"```                  |
| :question:          | [kodi-cadair](../../wiki/SKILL-cadair-kodi)                    | Kodi playback and search                                                                 |  
| :question:          | [kodi-cbenning](../../wiki/SKILL-cbenning-kodi)                | Control a local or remote Kodi instance                                                  |  
| :question:          | [kodi-k3yb0ardn1nja](../../wiki/SKILL-kodi-k3yb0ardn1nja)      | Play or pause a Kodi video                                                               |  
| :question:          | [let's-talk-skill](../../wiki/SKILL-lets-talk)                 | More salutations |
| :question:          | [lottery-skill](../../wiki/SKILL-lottery)                      | Reads Euromillion Lottery Numbers     |
| :question:          | [media-console-control](../../wiki/SKILL-media-console-control)| Adds media controls that are mapped to console commands                                  |  
| :question:          | [metal-band-skill](../../wiki/SKILL-metal-band)                | Recommends a metal band and gives basic information    |
| :construction:      | [milight](../../wiki/SKILL-milight)                            | Lighting control using MiLight                                                           |  
| :question:          | [mopidy](../../wiki/SKILL-mopidy)                              | Mopidy-based players for local music, Google Music, and Spotify                          |  
| :construction:      | [mopidy-and-bt-lights](../../wiki/SKILL-mopidy-and-bt-lights)  | Remote control of BT lights and Mopidy music playback                                    |  
| :question:          | [mopidy-media-player](../../wiki/SKILL-Mopidy-Media-Players)   | Mopidy-based players for local MP3 library, Spotify and a Swedish radio station's stream |
| :question:          | [movie-recommendation-skill](../../wiki/SKILL-movie-recomentation)                        | Recomends a movie  |
| :heavy_check_mark:  | [mp3-demo](../../wiki/SKILL-mp3-demo)                          | Simple sample of playing local MP3s                                                      |  
| :question:          | [mpd-control](../../wiki/SKILL-mpd-control)                    | Controls media players that use the MPD  protocol to play found local music           |  
| :question:          | [mqtt](../../wiki/SKILL-mqtt)                        | Control IoT devices (home automation) using MQTT protocol     |  
| :question:          | [mute-skill](../../wiki/SKILL-mute)            | Mutes Mycroft until re-enabled |
| :question:          | [nasa-picture-of-the-day](../../wiki/SKILL-nasa-pic-of-the-day)                    | Nasa picture of the day from the NASA API |
| :question:          | [near-earth-orbit-skill](../../wiki/SKILL-near-earth-orbit)                    | Near Earth orbit alert skill via the NASA API   |
| :construction:	  | [objective-skill](../../wiki/SKILL-objective)                  | skills can now register objectives almost the same has an intent would be registered with ObjectiveBuilder class              |
| :construction:	  |	[openhab-skill](../../wiki/SKILL-Openhab)					| This skill adds Openhab support to Mycroft |
| :question:          | [pandora-skill](../../wiki/SKILL-pandora)                   | Adds Pandora to mycroft via Pianobar  |
| :question:          | [photolocation-skill](../../wiki/SKILL-photolocation)          | Searches wikimedia for photos of location  |
| :question:          | [pickup-line-skill](../../wiki/SKILL-pickup-line)  | Responds with random nerdy pick-up lines          |
| :heavy_check_mark:          | [ping-skill](../../wiki/SKILL-ping)  | Pings websites and responds with latency time       |  
| :question:          | [plasma-activities-skill](https://github.com/AIIX/plasma-activities-skill#readme)  | This skill integrates Plasma 5 Activities with Mycroft<br>```"show activities / switch activity [name]"```|
| :question:          | [plasma-sendsms-skill](https://github.com/AIIX/plasma-sendsms-skill#readme)         |Send SMS through KDE Plasma<br>```"send a sms"```     |
| :question:          | [plasma-user-control-skill](https://github.com/AIIX/plasma-user-control-skill#readme) | This skills adds Plasma User control to Mycroft, allowing switch user, logout, and lock screen<br>```"switch user/logout/lock screen"```  |
| :question:          | [poetry-skill](../../wiki/SKILL-poetry)                      | Reads poetry based on Hidden Markov Models     |
| :question:          | [proxy-scrape-skill](../../wiki/SKILL-proxy-scrape)          | Scrape proxies from the internet    |
| :question:          | [pushbullet](../../wiki/SKILL-pushbullet)                      | Send messsages and photos using Pushbullet                                                  |  
| :question:          | [pushetta-skill](../../wiki/SKILL-pushetta)                    | Adds push notifications|
| :question:          | [quodlibet](../../wiki/SKILL-quodlibet)                        | Control Quod Libet music playback                                                        |  
| :question:          | [random-quote-skill](../../wiki/SKILL-random-quote)            | Adds random quotes,random facts about numbers, and your time left to live          |
| :question:          | [ratp-timetables](../../wiki/SKILL-ratp-timetables)            | Access schedules for the RATP Network of trains and buses in Paris                       |  
| :construction:      | [read-article-skill](../../wiki/SKILL-read-article)            | Scrapes text from online articles and reads them to you.   |
| :question:          | [rss-skill](../../wiki/SKILL-rss)            | Fetches from RSS feed   |
| :construction:      | [sentiment-analysis-skill](../../wiki/SKILL-sentiment-analysis)  | Sentiment analysis              |
| :question:          | [spaceflight-schedule](../../wiki/SKILL-spaceflight-schedule)  | Check when the next space flight launch is                                               |
| :heavy_check_mark:  | [skill-radio-rne](../..wiki/SKILL-radio-rne)       | Spanish news radio Radio Nacional de Espa?a RNE. |
| :question:          | [spacelaunch-skill](../../wiki/SKILL-spacelaunch)  | Check when the next space launch is                                               |
| :question:          | [speedtest](../../wiki/SKILL-speedtest)  | Run a speedtest                                               |
| :question:          | [slack-skill](../../wiki/SKILL-slack)                          | Allows to post and listen to Slack messages.  |
| :question:          | [sunspot-skill](../../wiki/SKILL-sunspot-skill)                    | Answers questions on daily sunspots |
| :question:          | [sun-skill](../../wiki/SKILL-sun)  | Responds with sunrise and set times          |  
| :question:          |[system-skill](../../wiki/SKILL-system)               | Adds system controls like shutdown and reboot   |
| :question:          | [take_picture](../../wiki/SKILL-take-picture)  | Take Pictures using the Raspberry Pi Camera          |  
| :question:          | [traffic-skill](../../wiki/SKILL-traffic)  | Gets the commute time from Google distance matrix api         |  
| :heavy_check_mark:  | [twitter-skill](https://github.com/btotharye/mycroft-twitter-skill#readme)| Control twitter with mycroft<br>```"How many twitter followers do I have"```                                                                                                         |
| :question:          | [unsplash-wallpaper-plasma-skill](https://github.com/AIIX/unsplash-wallpaper-plasma-skill#readme)  | Change KDE Desktop wallpaper by category type from unsplash<br>```"change wallpaper type [natureabstractany]"``` |
| :construction:      | [wallpaper-skill](../../wiki/SKILL-wallpaper)  | Downloads wallpapers from reddit and changes randomly         |
| :question:  	      | [wemo-skill](../../wiki/SKILL-wemo)              | Control Wemo devices with mycroft                                                   |
| :construction:      | [wifi-management-skill](../../wiki/SKILL-wifi-management)  | Various options for interacting with WiFi        |
| :construction:      | [wink-smart-home](../../wiki/SKILL-wink)                       | Interact with lights via a Wink-hub                                                      |  
| :question:          | [wiki-fact-scraper-skill](../../wiki/SKILL-wiki-fact-scraper)                        | Scrapes for random facts from wikipedia and stores locally    |
| :question:  | [youtube](../../wiki/SKILL-youtube)                            | Search and listen to a youtube video                                                        |  
| :question:  | [release-test](../../wiki/SKILL-release-test)                            | test mycroft release                                                        |  
| :heavy_check_mark:  | [skill-caffeinewiz](https://github.com/reginaneon/skill-caffeinewiz.git)| Provides the caffeine content of various drinks on request.<br>```what's caffeine content of *drink*?```
