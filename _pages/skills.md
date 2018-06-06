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

Mycroft determines what **Skill** should handle an **Utterance** by using an **intent parser** like <a href="https://mycroft.ai/documentation/adapt/">Adapt</a> or [Padatious](http://mycroft.ai/documentation/padatious/) to identify the **intent** of the user. For instance, if the **intent parser** determines that the user is asking about the *weather*, then Mycroft will pass the **intent data** to the *Weather Skill*.

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

| Status  | Skill Name                                                                                         | Installation<br>`"phrase to install the Skill"`| Description<br>```"phrase to trigger"```    |
| ------- | -------------------------------------------------------------------------------------------------- | -----------------------------------------------|---------------------------------------------|
| UNKNOWN | [amarok-media-player-skill](https://github.com/AIIX/amarok-player-skill#readme)                    | `"install amarok player skill"`                |Player controls for the Amarok Media Player<br>```"amarok play/stop/next/previous music"``` |
| UNKNOWN | [angry-beanie-podcast-player](https://github.com/purserj/mycroft-angrybeanie#readme)               | `"install mycroft angry beanie"`               |Skill for querying and playing Angry Beanie Podcasts<br />```"Get Angry Beanie shows"``` |
| GOOD    | [autogui-skill](https://github.com/eClarity/skill-autogui)                                         | `"install skill auto G U I"`                   |Manipulate your mouse and keyboard with Mycroft                                                  |
| UNKNOWN | [audio-control-plasma](https://github.com/AIIX/audio-control-plasma#readme)                        | `"install audio control plasma"`               |Audio control for Plasma Desktop<br>```"increase volume to maximum", "decrease microphone to minimum volume"```         |
| GOOD    | [australian-news](https://github.com/KathyReid/skill-australian-news)                              | `"install australian news"`                    |Mycroft Skill for playing the live news feed from the Australian Broadcasting Network (http://www.abc.net.au). <br>```"play the australian news"``` |
| GOOD    | [basichelp](https://github.com/btotharye/mycroft-skill-basichelp#readme)                           | `"install basic help skill"`                   |Get basic Mycroft questions and help answered<br>```"where is the documentation", "how do I install from source"```         |
| GOOD    | [better-jokes](https://github.com/tjoen/skill-better-jokes)                                        | `"install better jokes"`                       |Don't know who Chuck Norris is? Better jokes Skill.<br>```"be funny"```  |
| UNKNOWN | [bioinformatics](https://github.com/TicklishGiraffe/mycroft_genomics)                              | `"install bioinformatics skill"`               |Adds Bio-Linux Commands to Mycroft   |  
| UNKNOWN | [bitcoin](https://github.com/chrison999/mycroft-skill-bitcoin-enhanced)                            | `"install bitcoin"`                            |Check the price of bitcoin                                                               |  
| WIP     | [bitcoin-price](https://github.com/dmp1ce/mycroft-bitcoinprice-skill)                              | `"install bitcoin price"`                      |Checks the price of bitcoin                             |
| WIP     | [brain-skill](https://github.com/skeledrew/brain-skill)                                            | `"install brain skill"`                        |Chain intents and provide some services                                                 |
| GOOD    | [skill-caffeinewiz](https://github.com/reginaneon/skill-caffeinewiz)                               | `"install caffeine"`                           |Provides the caffeine content of various drinks on request.<br>```what's caffeine content of *drink*?```
| WIP     | [calculator-skill](https://github.com/TREE-Edu/calculator-skill)                                   | `"install calculator"`                         |Provides a conversational based calculator<br>```Do some math```
| UNKNOWN | [cbc-news-skill](https://github.com/chrison999/mycroft-skill-cbc-news)                             | `"install C B C news"`                         |Fetches CBC News Podcast<br>```Play CBC News```             |  
| UNKNOWN | [clarifai-image-recognition-skill](https://github.com/AIIX/clarifai-image-recognition-skill#readme)| `"install image recognition"`                  |Image recognition skill based on clarifai<br> ```"search image url [imagelocation]"```   |
| UNKNOWN | [clementine-player-skill](https://github.com/hersche/mycroft-clementine-skill)                     | `"install clementine"`                         |Controls your clementine-player localy. A fork from amarok-player.   |
| UNKNOWN | [skill-cryptoskill](https://github.com/Gobbenobber/skill-CryptoSkill/)                             | `"install crypto skill"`                       |This skill utilizes the CoinMarketCap API found on https://api.coinmarketcap.com to deliver cryptocurrency-related functionality for Mycroft. |
| GOOD    | [coin-flip-skill](https://github.com/wligtenberg/coin-flip-skill)                                  | `"install coin flip"`                          |Flip a virtual coin   |
| UNKNOWN | [daily-meditation](https://github.com/kfezer/daily_meditation)                                     | `"install daily meditation"`                   |Plays your Daily Meditation from the  Meditation Podcast     |
| GOOD    | [deutschlandfunk-skill](https://github.com/ofosos/deutschlandfunk-skill/)                          | `"install funk"`                               |Play Deutschlandfunk streams and query schedule |
| UNKNOWN | [diagnostics](https://github.com/the7erm/mycroft-skill-diagnostics)                                | `"install diagnostics"`                        |Diagnostic tools (CPU %age, free space, etc)    |
| WIP     | [dice-roll](https://github.com/Friday811/skill-dice)                                               | `"install dice"`                               |Rolls dice spoken in RPG notation.                                                       |
| UNKNOWN | [domoticz_skill](https://github.com/matleses/domoticz_skill)                                       | `"install domoticz"`                           |Skill integrating Mycroft with Domoticz    |
| UNKNOWN | [drive_servos](https://github.com/Nold360/mycroft_skill-drive_servos)                              | `"install drive servos"`                       |Control Hacked-Servo-Engines to make your mycroft move around   |
| GOOD    | [easter-eggs](https://github.com/JarbasAI/skill_easter_eggs)                                       | `"install easter eggs"`                        |Pop culture references and other easter eggs  |
| BROKEN  | [enhanced-bitcoin-skill](https://github.com/chrison999/mycroft-skill-bitcoin-enhanced)             | `"install bitcoin enhanced"`                   |Enhanced bitcoin skill from api.bitcoinaverage.com        |
| UNKNOWN | [esp8266-skill](https://github.com/Dark5ide/esp8266-skill/)                                        | `"install E S P 8 2 6 6"`                      |Communicate with an ESP8266 in the context of home automation.|
| WIP     | [facebook](https://github.com/JarbasAI/mycroft-facebook-skill)                                     | `"install facebook"`                           |Generates posts for Facebook                  |
| WIP     | [facebook-marketing](https://github.com/ProsperousHeart/mycroft-facebook-marketing)                | `"install facebook marketing"`                 |Works with Facebook Marketing API                                                        |
| GOOD    | [federal-closings](https://github.com/mason88/skill-federal-closings)                              | `"install federal closings"`                   |Federal Closings Skill<br>```"are there federal closings"``` |
| UNKNOWN | [flight-gear-copilot](https://github.com/merspieler/flight-gear-copilot/)                          | `"install copilot"`                            |Copilot for FlightGear
| UNKNOWN | [fox-news-skill](https://github.com/chrison999/mycroft-skill-fox-news)                             | `"install fox news"`                           |Fetches Fox News Podcast                                                                 |
| UNKNOWN | [Google-calendar](https://github.com/jcasoft/GoogleCalendar-Skill)                                 | `"install google calendar skill"`              |Check and add Google Calendar events                                                     |  
| UNKNOWN | [Google-gmail](https://github.com/jcasoft/GoogleGmailSkill)                                        | `"install gmail-skill"`                        |Get emails from your Gmail Inbox                                                         |  
| UNKNOWN | [Google-translate](https://github.com/jcasoft/TranslateSkill)                                      | `"install google translate skill"`             |Translate English phrases into other languages                                           |
| WIP     | [gpio-example](https://github.com/MycroftAI/picroft_example_skill_gpio)                            | `"install gpio"`                               |Example skill using the GPIO pins on the Raspberry Pi to blink an LED                                         |    
| UNKNOWN | [hue](https://github.com/ChristopherRogers1991/mycroft-hue)                                        | `"install hue"`                                |Control your Phillips Hue lights                                                         |  
| GOOD    | [home-assistant](https://github.com/btotharye/mycroft-homeassistant#readme)                        | `"install home assistant"`                     |Control your devices in home-assistant<br>```"turn on office"```                                                      |  
| GOOD    | [inspirational-quotes](https://github.com/oliveralonzo/skill-inspirational-quotes)                 | `"install inspirational quotes"`               |Skill for Mycroft to provide an inspirational quote |
| GOOD    | [irc-skill](https://github.com/merspieler/irc-skill)                                               | `"install I R C skill"`                        |Mycroft skill that lets you use IRC via voice commands                                   |
| UNKNOWN | [irsend](https://github.com/ChristopherRogers1991/mycroft-hue)                                     | `"install I R send"`                           |Control devices via [lirc's](http://www.lirc.org/) [irsend](http://www.lirc.org/html/irsend.html)                                                         |
| GOOD    | [jarbas-parrot](https://github.com/JarbasAl/skill-parrot)                                          | `"install parrot"`                             |Talks back to the user like a parrot |
| UNKNOWN | [jb-podcasts](https://github.com/the7erm/mycroft-skill-jupiter-broadcasting)                       | `"install J B podcasts`"                       |Play podcasts from Jupiter Broadcasting shows                                            |  
| GOOD    | [jrwarwick-jira-agent-skill](https://github.com/jrwarwick/jrwarwick-jira-agent-skill)              | `"install yeerah agent skill"`                 |MycroftAI Skill: Atlassian JIRA issue inquiry and creation  |
| GOOD    | [kde-kate-control](https://github.com/AIIX/kde-kate-control)                                       | `"install kate control"`                       |This skill enables an user to control the Kate client on the Desktop.  |
| UNKNOWN | [krunner-search](https://github.com/AIIX/krunner-search-skill#readme)                              | `"install K runner search"` (returns Error 121)|Search local KDE desktop for files, images, recent documents, bookmarks<br>```"search this computer for [any keyword]"```                  |
| UNKNOWN | [kodi-cadair](https://github.com/Cadair/mycroft-kodi)                                              | `"install cadair kodi"`                        |Kodi playback and search                                                                 |  
| UNKNOWN | [kodi-cbenning](https://github.com/cbenning/kodi-skill)                                            | `"install C benning kodi"`                     |Control a local or remote Kodi instance                                                  |  
| UNKNOWN | [kodi-k3yb0ardn1nja](https://github.com/k3yb0ardn1nja/mycroft-skill-kodi)                          | `"install K 3 Y B 0 A R D N 1 N J A kodi"`     |Play or pause a Kodi video                                                               |  
| UNKNOWN | [let's-talk-skill](https://github.com/chrison999/mycroft-skill-lets-talk)                          | `"install lets talk"`                          |More salutations |
| UNKNOWN | [media-console-control](https://github.com/the7erm/mycroft-skill-simple-media-controls)            | `"install media console control"`              |Adds media controls that are mapped to console commands                                  |  
| WIP     | [milight](https://github.com/maxppc/Mycroft-milight-skill)                                         | `"install milight"`                            |Lighting control using MiLight                                                           |  
| GOOD    | [mopidy](https://github.com/forslund/mopidy_skill)                                                 | `"install mopidy"`                             |Mopidy-based players for local music, Google Music, and Spotify                          |  
| WIP     | [mopidy-and-bt-lights](https://github.com/swilso793/mycroft_third_party_skills)                    | `"install mopidy and B T lights"`              |Remote control of BT lights and Mopidy music playback                                    |  
| UNKNOWN | [skill-mosquito-speak](https://github.com/CarstenAgerskov/skill-mosquito-speak)                    | `"install mosquito speak"`                     |Allow Mycroft to notify you on events, by speaking text received on a mqtt bus.|
| GOOD    | [mp3-demo](https://github.com/ethanaward/demo_skill)                                               | `"install demo skill"`                         |Simple sample of playing local MP3s                                                      |  
| UNKNOWN | [mpd-control](https://github.com/forslund/mpd_skill)                                               | `"install mycroft M P D skill"`                |Controls media players that use the MPD  protocol to play found local music           |  
| UNKNOWN | [mqtt](https://github.com/jamiehoward430/mycroft-mymqtt)                                           | --                                             |Control IoT devices (home automation) using MQTT protocol     |  
| GOOD    | [number-generator-skill](https://github.com/angry-frog/number-generator-skill)                     | `"install number generator"`                   |Randomly generate a number between 1-100 <br>```Pick a number``` |
| WIP     | [openhab-skill](https://github.com/openhab/openhab-mycroft)                                        | `"install openhab"`                            |This skill adds Openhab support to Mycroft |
| UNKNOWN | [pandora-skill](https://github.com/ethanaward/pianobar-skill)                                      | `"install pandora skill"`                      |Adds Pandora to mycroft via Pianobar  |
| GOOD    | [ping-skill](https://github.com/nogre/ping-skill)                                                  | `"install ping"`                               |Pings websites and responds with latency time       |  
| UNKNOWN | [plasma-activities-skill](https://github.com/AIIX/plasma-activities-skill#readme)                  | `"install plasma activities"`                  |This skill integrates Plasma 5 Activities with Mycroft<br>```"show activities / switch activity [name]"```|
| UNKNOWN | [plasma-sendsms-skill](https://github.com/AIIX/plasma-sendsms-skill#readme)                        | `"install plasma send S M S"`                  |Send SMS through KDE Plasma<br>```"send a sms"```     |
| UNKNOWN | [plasma-user-control-skill](https://github.com/AIIX/plasma-user-control-skill#readme)              | `"install plasma user control"`                |This skills adds Plasma User control to Mycroft, allowing switch user, logout, and lock screen<br>```"switch user/logout/lock screen"```  |
| UNKNOWN | [podcast-skill](https://github.com/JamesPoole/podcast-skill)                                       | `"install podcast skill"`                      |Select your favourite podcasts in the home.mycroft.ai settings and listen to episodes from those podcasts. You can also check with Mycroft if there are any new episodes available from your chosen podcasts|
| UNKNOWN | [proxy-scrape-skill](https://github.com/JarbasAI/mycroft--proxy-scrapping---skill)                 | --                                             |Scrape proxies from the internet    |
| UNKNOWN | [pushbullet](https://github.com/jcasoft/PushbulletSkill)                                           | `"install push bullet"`                        |Send messsages and photos using Pushbullet                                                  |  
| UNKNOWN | [pushetta-skill](https://github.com/marksev1/Mycroft-Pushetta-skill)                               | `"install pushetta"`                           |Adds push notifications|
| UNKNOWN | [quodlibet](https://github.com/kfarwell/mycroft-skill-quodlibet)                                   | `"install quod"`                               |Control Quod Libet music playback                                                        |  
| UNKNOWN | [ratp-timetables](https://github.com/ldubost/mycroft-skills)                                       | `"install R A T P timetables"`                 |Access schedules for the RATP Network of trains and buses in Paris                       |  
| GOOD    | [skill-repeat-recent](https://github.com/MatthewScholefield/skill-repeat-recent)                   | `"install repeat recent"`                      |Repeat what you or Mycroft just said<br>```"Repeat what you just said"``` |
| UNKNOWN | [rss-skill](https://github.com/forslund/rss_skill)                                                 | --                                             |Fetches from RSS feed   |
| GOOD    | [developer-silly-name-maker](https://github.com/RHackrid/deviloper-silly-name-maker/)              | `"install silly name"`                         |Returns a user's silly name by prompting the user for a favorite color and lucky number. |
| WIP     | [slack-skill](https://github.com/guilhembn/Mycroft-Slack-skill)                                    | `"install slack"`                              |Integrate Mycroft with Slack<br>```Send <my message> on Slack``` |
| UNKNOWN | [spaceflight-schedule](https://github.com/praxeo/mycroft_spaceflightnow_skill)                     | `"install space flight schedule"`              |Check when the next space flight launch is                                               |
| GOOD    | [skill-radio-rne](https://github.com/ReK2Fernandez/skill-radio-rne)                                | `"install radio R N E skill"`                  |Spanish news radio Radio Nacional de Espa?a RNE. |
| GOOD    | [skill-the-cows-lists](https://github.com/CarstenAgerskov/skill-the-cows-lists)                    | `"install skill the cows"`                     |Integration with Remember the Milk<br>```"Hey Mycroft, add milk to my grocery list"``` |
| UNKNOWN | [spacelaunch-skill](https://github.com/marksev1/Mycroft-SpaceLaunch-Skill)                         | `"install space launch"`                       |Check when the next space launch is                                               |
| GOOD    | [spotify-skill](https://github.com/forslund/spotify-skill)                                         | `"install spotify"`                            |Mycroft Skill to control spotify using the Spotify Connect API  |
| UNKNOWN | [speedtest](https://github.com/ChristopherRogers1991/mycroft-speedtest)                            | `"install speed test"`                         |Run a speedtest                                               |
| GOOD    | [subsonic-media](https://github.com/ejstacey/skill-subsonic-media)                                 | `"install subsonic"`                           |Subsonic media player skill<br>```"Play Nine Inch Nails"``` |
| UNKNOWN | [sunspot-skill](https://github.com/BoatrightTBC/sunspots)                                          | `"install sunspots"`                           |Answers questions on daily sunspots |
| UNKNOWN | [sun-skill](https://github.com/marksev1/Mycroft-SunSkill)                                          | --                                             |Responds with sunrise and set times          |  
| UNKNOWN | [system-skill](https://github.com/CloneMMDDCVII/systemSkill-Mycroft-core-Skill-)                   | `"install system skill"`                       |Adds system controls like shutdown and reboot   |
| UNKNOWN | [take_picture](https://github.com/Nold360/mycroft_skill-take_picture)                              | `"install take picture"`                       |Take Pictures using the Raspberry Pi Camera          |  
| UNKNOWN | [traffic-skill](https://github.com/BongoEADGC6/mycroft-traffic)                                    | `"install traffic"`                            |Gets the commute time from Google distance matrix api         |  
| GOOD    | [twitter-skill](https://github.com/btotharye/mycroft-twitter-skill#readme)                         | `"install twitter skill"`                      |Control twitter with Mycroft<br>```"How many Twitter followers do I have"```                                                                                     
| GOOD    | [translate-skill](https://github.com/jcasoft/translate-skill#readme)                               | `"install translate skill"`                      |Translate phrases into other languages<br>```"Translate good morning into Japanese"```                                                                                   |
| UNKNOWN | [unsplash-wallpaper-plasma-skill](https://github.com/AIIX/unsplash-wallpaper-plasma-skill#readme)  | `"install unsplash"`                           |Change KDE Desktop wallpaper by category type from unsplash<br>```"change wallpaper type [natureabstractany]"``` |
| WIP     | [wallpaper-skill](https://github.com/JarbasAI/mycroft---wallpaper---skill)                         | `"install wallpaper"`                          |Downloads wallpapers from reddit and changes randomly         |
| UNKNOWN | [wemo-skill](https://github.com/martymulligan/skill-wemo)                                          | `"install wemo"`                               |Control Wemo devices with mycroft                                                   |
| GOOD    | [whats-nearby](https://github.com/AIIX/whats-nearby)                                               | `"install whats nearby"`                       |Nearby places and location Skill for Mycroft on Plasma<br>```"search for nearby hotels"``` |
| GOOD    | [wink-smart-home](https://github.com/MycroftAI/skill-wink-iot)                                     | `"install wink I O T"`                         |Interact with lights via a Wink-hub                                                      |  
| UNKNOWN | [youtube](https://github.com/augustnmonteiro/mycroft-youtube)                                      | `"install youtube"`                            |Search and listen to a Youtube video                                                        |  


### Skills looking for feedback and testing

The following Skills are in active development, and Community Developers would appreciate help with testing and feedback.

* [Pomodoro Skill](https://github.com/erabti/mycroft-pomodoro-skill): This **Skill** provides functionality for time management using the [Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) technique.