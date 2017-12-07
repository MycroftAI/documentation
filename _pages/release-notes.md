---
ID: 33666
post_title: Release notes
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/release-notes/
published: true
post_date: 2017-12-07 11:39:43
---
# Release notes



## [release/v0.9.7](https://github.com/MycroftAI/mycroft-core/tree/release/v0.9.7)

### Send E-mail #1230

The skills API now includes a `self.send_email()` method allowing the skill to send an e-mail to the user. Practical if the skill wants to send a link to the user or for things such as shopping lists.

### Metrics #1247 
The `DeviceApi` now includes a `metrics` method allowing skills and core to upload information to the Mycroft server should the user allow it. The method is very general purpose and can take any method as long as it can be serialized to json.

Skills developer can easily access this functionality using the `self.report_metric` method in the Skill API.

### Misc
- Added support for Google Cloud API SST, big thanks to @ahayworth for providing this. #1226 
- The AudioService can now add files to currently playing playlist #1197 
- Listening can now be triggered from the messagebus by sending `mycroft.mic.listen` #1244  
- Remove pystache dependency #1235
- Improve lip synch #1242  
- Code cleanup and bugfixes, Many thanks to @gauravMann for cleaning up the usage of mutables as default arguments. 

## [release/v0.9.6](https://github.com/MycroftAI/mycroft-core/tree/release/v0.9.6)

Minor release with a critical Debian packaging fix to v0.9.5 that corrected a mistake creating incorrect ownership of the ```/etc/sudoers``` file.

## [release/v0.9.5](https://github.com/MycroftAI/mycroft-core/tree/release/v0.9.5)

### Precise wake word engine #1199, #1207 

New machine-learning based wake word listener.  This system includes a feedback loop, allowing user-contributed information to be incorporated into the training database, improving the wake-word performance.  This happens when Opt In has been chosen at home.mycroft.ai.

Precise is enabled by changing /etc/mycroft/mycroft.conf to include:
    {"hotwords": {"hey mycroft": {"module": "precise"}}}. 

### API enhancements
* Add MycroftSkill.get_intro_message() method which skills can override when they wish to provide instructions to the user after installation.  (#1211)
* Extend scheduled event mechanism with MycroftSkill.get_event_status(),  MycroftSkill.remove_event() (#1193)

### Utility changes
* Add ```msm list``` command to show already installed skills; and ```msm info <skill>``` command to display info from the README.md in the skill's Github repo.  Thanks @theCalcaholic!  (#1201, #1202, #1203  )
* Add 'all' option for mycroft-stop utility to mirror mycroft-start (#1212)
* Changed mycroft-use utility to autoremove when switching from unstable to stable builds.  (#1213)
* Add 'home' and 'home-test' options to mycroft-use to simplify backend testing.  Also added platform support and extended the 'github' option.  (#1182)

### Misc
* Wakeword validation, defaulting to "Hey Mycroft" when user-entered settings fail.  (#1188)
* Add event scheduler tests (#1189)
* Reduced requirements.txt to only the packages actually used by mycroft-core, removing those only needed for default skills.  (#1192, #1215, #1216)
* Added stop() to the AudioService.  Thanks, @akailash!  (#1194)
* Configuration system fix (#1196)
* Padations 0.3.7, fixing several minor bugs (#1198)
* The remote configuration file was prematurely loaded at import time.  Now it is loaded when the Session is created.  (#1204)