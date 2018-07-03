---
ID:
post_title: Message Bus
author: Kathy Reid
layout: page
published: false
---


## Introduction to the Message Bus

### What is a Message Bus?

A Message Bus is a system which contains a data model, a set of common commands or _messages_ and a way to send and receive _messages_. In the Mycroft ecosystem, the data model is the [Mycroft Skills API] API](http://mycroft-core.readthedocs.io/en/stable/), and the common _messages_ are listed here. Messages are sent using various Python scripts in `mycroft-core` (_producers_) and acted upon by [Skills](https://mycroft.ai/documentation/skills) (_consumers_).

You will really only need to know about the Mycroft Message Bus if you are developing advanced or complex Skills, or attempting to write Skills in languages other than Python.

_NOTE: We can only currently assist you in writing Skills in Python, so if you choose to write Skills in another programming language, we may not be able to provide assistance - but we don't want to stop you doing awesome things!_

## Mycroft Messagebus messages

| message type                                                                     | data                                                                         | Emitted By (Producer)                   | Handled By (Consumer)                                | Meaning                                                                                    |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------|
| `speak` |```"{'utterance': 'words to be spoken','lang': 'en-us''lang': 'en-us'}"```                                                                              |                                                                          |                              |Request to speak utterance                                                                                                              |
| `mycroft.internet.connected`                                                       |                                                                              |                              |                                              | Internet connection is now available (only generated on initial connection)                |
| `mycroft.stop`                                                                     |                                                                              |                              |                                              | Stop command (e.g. button pressed)                                                         |
| `mycroft.paired`                                                                   |                                                                              |                              |                                              | Pairing has completed                                                                      |
| `open`                                                                             |                                                                              | messagebus\client\ws.py      |                                              | System UI is ready                                                                         |
| `complete_intent_failure`                                                          |                                                                              |                              |                                              | Intent processing failed                                                                   |
| `recognizer_loop:sleep`                                                            |                                                                              |                              |                                              | Go into 'sleep' mode.  Everything except "Hey Mycroft, wake up" will be ignored.           |
| `recognizer_loop:wake_up`                                                          |                                                                              |                              |                                              | Come out of 'sleep' mode.                                                                  |
| `mycroft.awoken`                                                                   |                                                                              |                              |                                              | Has come out of sleep mode                                                                 |
| `recognizer_loop:wakeword`	| `"{'utterance': 'wakeword heard','session': session_id,}"`                                                                                | client/speech/main.py                                                        |                              | Wake Word was heard                                                                                                                       |
| `recognizer_loop:record_begin`                                                     |                                                                              | client/speech/main.py        |                                              | Recording has started                                                                                             |
| `recognizer_loop:record_end`                                                       |                                                                              | client/speech/main.py        |                                              | Recording has ended                                                                                                 |
| `recognizer_loop:utterance`|`"{'utterances': [text],'lang': self.stt.lang,'session': session_id}"`                                                                              | client/speech/main.py   |                                                     |                                                                                                                        |
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
| `mycroft.volume.increase`                                                          | `{'play_sound': True}`                                                         | client/enclosure/__init__.py | Volume Skill                                 | Enclosure Volume up                                                                        |
| `mycroft.volume.decrease`                                                          | `{'play_sound': True}`                                                         | client/enclosure/__init__.py | Volume Skill                                 | Enclosure Volume down                                                                      |
| `mycroft.volume.mute`                                                              | `{'speak_message': True}`                                                      |                              | Volume Skill                                 | Enclosure Volume muted                                                                     |
| `mycroft.volume.unmute`                                                            | `{'speak_message': True}`                                                      |                              | Volume Skill                                 | Enclosure Volume unmuted                                                                                                                |                                                                                            |
| `mycroft.skill.handler.start`                                                      | ``{handler: class/function name}``                                               |                              |                                              |                                                                                            |
| `mycroft.skill.handler.complete`                                                   |                                                                              |                              |                                              |                                                                                            |
| `mycroft.skill.disable_intent`                                                     | ```{"intent_name": "name"}```                                                      |                              | mycroft/skills/core.py                       | Disable intent                                                                             |
| `mycroft.skill.enable_intent`                                                      | ```{"intent_name": "name"}```                                                      |                              | mycroft/skills/core.py                       | Enable disabled intent                                                                     |
| `mycroft.skills.loaded`                                                            | ```{"id": SKILL ID, "name": SKILL NAME, "folder": FOLDER, "modified": MODIFIED}``` | skills/main.py               | mycroft/skills/intent_service.py             | A skill has been loaded                                                                    |
| `mycroft.skills.loading_failure`                                                   | ```{"id": SKILL ID, "folder": SKILL FOLDER}```                                     | skills/main.py               |                                              |                                                                                            |
| `mycroft.skills.shutdown`                                                          | ```{"id": SKILL ID, "folder": SKILL FOLDER}```                                     | skills/main.py               |                                              |                                                                                            |
| `mycroft.skills.list`                                                              | ```{"skills": [...] }```                                                           | skills/main.py               |                                              | List of loaded skills (response to 'skillmanager.list')                                    |
| `mycroft.skills.initialized`                                                       |                                                                              | mycroft/skills/main.py       |                                              | Upon startup, all skills have been loaded                                                  |
| `mycroft.skills.settings.update`  |                                                 |                                                                            Configuration Skill          | mycroft/skills/settings.py   |                Pull new skill settings from the server                                                                                                                                                |
| `msm.updating`                                                                     |                                                                              | msm.sh                       | skills/main.py                               | MSM install has begun                                                                      |
| `msm.installing`                                                                   |                                                                              | msm.sh                       | skills/main.py                               | MSM update has begun                                                                       |
| `msm.install.succeeded`                                                            | ```{ "skill" : name }```                                                           | msm.sh                       | skills/main.py                               | MSM install succeeded for given skill                                                      |
| `msm.install.failed`                                                               | ```{ "skill" : name, "error" : code }```                                           | msm.sh                       | skills/main.py                               | MSM install failed for given skill                                                         |
| `msm.installed`                                                                    |                                                                              | msm.sh                       | skills/main.py                               | MSM install is complete                                                                    |
| `msm.updated`                                                                      |                                                                              | msm.sh                       | skills/main.py                               | MSM update is complete                                                                     |
| `msm.removing`                                                                     |                                                                              | msm.sh                       | skills/main.py                               | MSM remove has begun                                                                       |
| `msm.remove.succeeded`                                                             | ```{ "skill" : name }```                                                           | msm.sh                       | skills/main.py                               | MSM remove succeeded for given skill                                                       |
| `msm.remove.failed`                                                                | ```{ "skill" : name, "error" : code }```                                           | msm.sh                       | skills/main.py                               | MSM remove failed for given skill                                                          |
| `msm.removed`                                                                      |                                                                              | msm.sh                       | skills/main.py                               | MSM remove is complete                                                                     |                                                                                          |
| `skillmanager.update`                                                              |                                                                              |                              | skills/main.py                               | Request immediate update of all skills                                                     |
| `skillmanager.list`                                                                |                                                                              | CLI (client/text/main.py)    | skills/main.py                               | Request a response with 'mycroft.skills.list'                                                                                                                                           
| **System administrative actions**                                                    |                                                                              |                              |                                              |                                                                                            |
| `system.wifi.setup` / `mycroft.wifi.start`                                           |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Kick off a a wifi-setup session                                                            |
| `system.wifi.reset` / `mycroft.wifi.reset`                                           |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Clear the saved wifi settings                                                              |
| `system.ntp.sync`                                                                  |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Force the system clock to synchronize with NTP servers                                     |
| `system.ssh.enable` / `mycroft.enable.ssh`                                           |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Configure system to allow SSH connections                                                  |
| `system.ssh.disable / mycroft.disable.ssh`                                         |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Configure system to block SSH connections                                                  |
| `system.reboot`                                                                    |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Force a Linux reboot                                                                       |
| `system.shutdown`                                                                  |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py | Force a Linux shutdown                                                                     |
| `system.update`                                                                    |                                                                              |                              | mycroft-wifi-setup: mycroft_admin_service.py |  Force an `apt-get update` on `mycroft-mark-1` or `mycroft-picroft` package (as appropriate) |



## Guidelines for using the Mycroft Messagebus

* Messages MUST use verbs for requests - such as;
  - `mic.mute`
  - `mic.unmute`

* Messages MUST use the future tense for pre-action notifications - such as;
  - `mic.muting`
  - `mic.unmuting`

* Messages MUST use the past tense for post-action notifications - such as;
  - `mic.muted`
  - `mic.unmuted`

The command line invocation syntax is:

`python -m mycroft.messagebus.send xxx.yyy.zzz`

## Connecting to the Messagebus in Python

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
