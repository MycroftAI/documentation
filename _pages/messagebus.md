---
ID:
post_title: Message Bus
author: Kathy Reid
layout: page
published: false
---


## Introduction to the Message Bus

### What is a Message Bus?

A Message Bus is mechanism for independent systems to communicate with each other using a set of _messages_ for common commands or notifiers. In the Mycroft ecosystem, the Messagebus is a websocket and the messages are contain a message type with an optional JSON data packet.  Some messages trigger actions and have side effects; some are simple notifiers of actions that either have occurred or are about to occur.  The messagebus connects the mycroft-core processes and the skills, and can also be joined by outside systems such as the CLI.

The common _messages_ are listed below. Messages can be sent from the _producers_ listed below and acted upon by [Skills](https://mycroft.ai/documentation/skills) or other _consumers_ within mycroft-core.  The producers and consumers list below is not definitive and some messages might be generated or handled by other processes or advanced skills.

The base [MycroftSkill API](http://mycroft-core.readthedocs.io/en/stable/) handles most of the message bus usage automatically.  For example, the 'mycroft.stop' message is caught by the skill framework, invoking an overridden MycroftSkills.stop() method within a Skill.  Similarly, the MycroftSkill.speak() and MycroftSkill.speak_dialog() methods generate 'speak' messages to be conveyed to the TTS and audio systems.

You will really only need to know about the Mycroft Messagebus if you are developing advanced or complex Skills.  The MycroftSkill.add_event() method allows you to attach a handler which will be triggered when the message is seen on the bus.

_NOTE: We can only currently assist you in writing Skills in Python, so if you choose to write Skills in another programming language, we may not be able to provide assistance - but we don't want to stop you doing awesome things!_

## Mycroft Messagebus messages

| message type                                                                     | data                                                                         | Emitted By (Producer)                   | Handled By (Consumer)                                | Meaning                                                                                    |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------|
| `speak` |```{"utterance": "words to be spoken", "lang": "en-us"}```                                                                              |                                                                          |                              |Request to speak utterance                                                                                                              |
| `mycroft.internet.connected`                                                       |                                                                              |                              |                                              | Internet connection is now available (only generated on initial connection)                |
| `mycroft.stop`                                                                     |                                                                              |                              |                                              | Stop command (e.g. button pressed)                                                         |
| `mycroft.paired`                                                                   |                                                                              |                              |                                              | Pairing has completed                                                                      |
| `open`                                                                             |                                                                              | messagebus\client\ws.py      |                                              | System UI is ready                                                                         |
| `complete_intent_failure`                                                          |                                                                              |                              |                                              | Intent processing failed                                                                   |
| `recognizer_loop:sleep`                                                            |                                                                              |                              |                                              | Go into 'sleep' mode.  Everything except "Hey Mycroft, wake up" will be ignored.           |
| `recognizer_loop:wake_up`                                                          |                                                                              |                              |                                              | Come out of 'sleep' mode.                                                                  |
| `mycroft.awoken`                                                                   |                                                                              |                              |                                              | Has come out of sleep mode                                                                 |
| `recognizer_loop:wakeword`	| `{"utterance": "wakeword heard", "session": session_id}`                                                                                | client/speech/main.py                                                        |                              | Wake Word was heard                                                                                                                       |
| `recognizer_loop:record_begin`                                                     |                                                                              | client/speech/main.py        |                                              | Recording has started                                                                                             |
| `recognizer_loop:record_end`                                                       |                                                                              | client/speech/main.py        |                                              | Recording has ended                                                                                                 |
| `recognizer_loop:utterance`|`{"utterances": [text], "lang": self.stt.lang, "session": session_id}`                                                                              | client/speech/main.py   |                                                     |                                                                                                                        |
| `recognizer_loop:audio_output_start`                                               |                                                                              | audio/speech.py              |                                              | Text output (TTS) has begun                                                                |
| `recognizer_loop:audio_output_end`                                                 |                                                                              | audio/speech.py              |                                              | Text output (TTS) has ended                                                                |
| `enclosure.notify.no_internet`                                                     |                                                                              | audio/speech.py              |                                              | Detetected a connection error during STT                                                   |
| `mycroft.mic.mute`                                                                 |                                                                              |                              | client/speech/main.py                        | Turn off the mic (no wakeword or STT processing)                                           |
| `mycroft.mic.unmute`                                                               |                                                                              |                              | client/speech/main.py                        | Turn on the mic (enable wakeword and STT processing)                                       |
| `mycroft.mic.listen`                                                               |                                                                              |                              |                                              | Begin recording for STT processing                                                                                                                                                   |
| `mycroft.audio.service.play`                                                       |                                                                              | skills/audioservice.py       | audio/main.py                                | Start playback of tracklist                                                                |
| `mycroft.audio.service.stop`                                                       |                                                                              | skills/audioservice.py       | audio/main.py                                | Stop playback                                                                              |
| `mycroft.audio.service.pause`                                                      |                                                                              | skills/audioservice.py       | audio/main.py                                | Pause playback (if supported)                                                              |
| `mycroft.audio.service.resume`                                                     |                                                                              | skills/audioservice.py       | audio/main.py                                | Resume playback (if supported by backend)                                                  |
| `mycroft.audio.service.track_info`                                                 |                                                                              | skills/audioservice.py       | audio/main.py                                | Request track info from audio service                                                      |
| `mycroft.audio.service.track_info_reply`                                           |                                                                              | audio/main.py                | skills/audioservice.py                       | Reply to track info request                                                                |
| `mycroft.audio.service.next`                                                       |                                                                              | skills/audioservice.py       | audio/main.py                                | Skip to next track                                                                         |
| `mycroft.audio.service.prev`                                                       |                                                                              | skills/audioservice.py       | audio/main.py                                | Skip to previous track                                                                     |                                            |                                                                                            |
| `mycroft.volume.increase`                                                          | `{"play_sound": true}`                                                         | client/enclosure/__init__.py | Volume Skill                                 | Enclosure Volume up                                                                        |
| `mycroft.volume.decrease`                                                          | `{"play_sound": true}`                                                         | client/enclosure/__init__.py | Volume Skill                                 | Enclosure Volume down                                                                      |
| `mycroft.volume.mute`                                                              | `{"speak_message": true}`                                                      |                              | Volume Skill                                 | Enclosure Volume muted                                                                     |
| `mycroft.volume.unmute`                                                            | `{"speak_message": true}`                                                      |                              | Volume Skill                                 | Enclosure Volume unmuted                                                                                                                |                                                                                            |
| `mycroft.skill.handler.start`                                                      | `{"handler": class/function name}`                                               |                              |                                              |                                                                                            |
| `mycroft.skill.handler.complete`                                                   |                                                                              |                              |                                              |                                                                                            |
| `mycroft.skill.disable_intent`                                                     | `{"intent_name": "name"}`                                                      |                              | mycroft/skills/core.py                       | Disable intent                                                                             |
| `mycroft.skill.enable_intent`                                                      | `{"intent_name": "name"}`                                                      |                              | mycroft/skills/core.py                       | Enable disabled intent                                                                     |
| `mycroft.skills.loaded`                                                            | `{"id": SKILL ID, "name": SKILL NAME, "folder": FOLDER, "modified": MODIFIED}` | skills/main.py               | mycroft/skills/intent_service.py             | A skill has been loaded                                                                    |
| `mycroft.skills.loading_failure`                                                   | `{"id": SKILL ID, "folder": SKILL FOLDER}`                                     | skills/main.py               |                                              |                                                                                            |
| `mycroft.skills.shutdown`                                                          | `{"id": SKILL ID, "folder": SKILL FOLDER}`                                     | skills/main.py               |                                              |                                                                                            |
| `mycroft.skills.list`                                                              | `{"skills": [...] }`                                                           | skills/main.py               |                                              | List of loaded skills (response to 'skillmanager.list')                                    |
| `mycroft.skills.initialized`                                                       |                                                                              | mycroft/skills/main.py       |                                              | Upon startup, all skills have been loaded                                                  |
| `mycroft.skills.settings.update`  |                                                 |                                                                            Configuration Skill          | mycroft/skills/settings.py   |                Pull new skill settings from the server                                                                                                                                                |
| `msm.updating`                                                                     |                                                                              | msm.sh                       | skills/main.py                               | MSM install has begun                                                                      |
| `msm.installing`                                                                   |                                                                              | msm.sh                       | skills/main.py                               | MSM update has begun                                                                       |
| `msm.install.succeeded`                                                            | `{ "skill" : name }`                                                           | msm.sh                       | skills/main.py                               | MSM install succeeded for given skill                                                      |
| `msm.install.failed`                                                               | `{ "skill" : name, "error" : code }`                                           | msm.sh                       | skills/main.py                               | MSM install failed for given skill                                                         |
| `msm.installed`                                                                    |                                                                              | msm.sh                       | skills/main.py                               | MSM install is complete                                                                    |
| `msm.updated`                                                                      |                                                                              | msm.sh                       | skills/main.py                               | MSM update is complete                                                                     |
| `msm.removing`                                                                     |                                                                              | msm.sh                       | skills/main.py                               | MSM remove has begun                                                                       |
| `msm.remove.succeeded`                                                             | `{ "skill" : name }`                                                           | msm.sh                       | skills/main.py                               | MSM remove succeeded for given skill                                                       |
| `msm.remove.failed`                                                                | `{ "skill" : name, "error" : code }`                                           | msm.sh                       | skills/main.py                               | MSM remove failed for given skill                                                          |
| `msm.removed`                                                                      |                                                                              | msm.sh                       | skills/main.py                               | MSM remove is complete                                                                     |                                                                                          |
| `skillmanager.update`                                                              |                                                                              |                              | skills/main.py                               | Request immediate update of all skills                                                     |
| `skillmanager.list`                                                                |                                                                              | CLI (client/text/main.py)    | skills/main.py                               | Request a response with 'mycroft.skills.list'                                                                                                                                           
| **System administrative actions**                                                    |                                                                              |                              |                                                                                                                                          |
| `system.wifi.setup` / `mycroft.wifi.start`                                           |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Kick off a a wifi-setup session                                                            |
| `system.wifi.reset` / `mycroft.wifi.reset`                                           |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Clear the saved wifi settings                                                              |
| `system.ntp.sync`                                                                  |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Force the system clock to synchronize with NTP servers                                     |
| `system.ssh.enable` / `mycroft.enable.ssh`                                           |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Configure system to allow SSH connections                                                  |
| `system.ssh.disable` / `mycroft.disable.ssh`                                         |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Configure system to block SSH connections                                                  |
| `system.reboot`                                                                    |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Force a Linux reboot                                                                       |
| `system.shutdown`                                                                  |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Force a Linux shutdown                                                                     |
| `system.update`                                                                    |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py |  Force an `apt-get update` on `mycroft-mark-1` or `mycroft-picroft` package (as appropriate) |



## Guidelines for Mycroft Messagebus usage

Private messages can be placed on the messagebus following these naming conventions:
`subsystem.message` or `skill.skillname.message`

* * Messages MUST use verbs for requests - such as;
  - `mic.mute`
  - `mic.unmute`
  - `skill.mycrofttimer.cancel.all`

* Messages MUST use the future tense for pre-action notifications - such as;
  - `mic.muting`
  - `mic.unmuting`

* Messages MUST use the past tense for post-action notifications - such as;
  - `mic.muted`
  - `mic.unmuted`
  - `skill.mycrofttimer.expired`


## Command line invocation syntax:

```bash
python -m mycroft.messagebus.send xxx.yyy.zzz
```

or

```bash
python -m mycroft.messagebus.send xxx.yyy.zzz '{"name": "value"}'
```

## Connecting message handlers within a MycroftSkill

```python
...
def initialize(self):
    self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
    self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)
                           
def handle_listener_started(self, message):
    # code to excecute when active listening begins...

def handle_listener_ended(self, message):
    # code to excecute when active listening begins...
...
```

## Generating messages within a MycroftSkill

```python
...
def some_method(self):
    self.emitter.emit(Message("recognizer_loop:utterance",
                            {'utterances': ["inject a user utterance"],
                                'lang': 'en-us'}))
...
```

## Connecting to the Mycroft Messagebus in Python

Here is an example Python script to connect to the `messagebus`:

```python
#! /usr/bin/env python

import sys
from websocket import create_connection
uri = 'ws://' + sys.argv[1] + ':8181/core'
ws = create_connection(uri)
print "Sending " + sys.argv[2] + " to " + uri + "..."
if len(sys.argv) >= 4:
    data = sys.argv[3]
else:
    data = "{}"

message = '{"type": "' + sys.argv[2] + '", "data": ' + data +'}'
result = ws.send(message)
print "Receiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()
```

Unfortunately, we cannot provide support or examples for other languages.

If you have further questions, then the best place to ask them is our [Community Forum](https://community.mycroft.ai) or in the [~dev Channel](https://chat.mycroft.ai/community/channels/dev) on Mycroft Chat.
