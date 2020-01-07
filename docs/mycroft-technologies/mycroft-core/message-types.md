---
description: >-
  Messages are used to communicate information between Mycroft services and
  other components. This list of Message types outlines their meaning, expected
  JSON data, standard producer and consumer.
---

# Message Types

Each Message type listed contains a description outlining it's meaning or purpose. Where relevant, the Message type will also list the specific JSON data packets expected to be emitted with that Message, and the most common producers and consumers of the Message.

See the [MessageBus documentation](message-bus.md) for further information on this service and examples of using Messages.

## General

### speak

Request to speak utterance

**Data:**

```JSON
{
    "utterance": <words to be spoken>,
    "lang": <language code, e.g. en-us>
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('speak',
                   self.handler_speak)

def handler_speak(self, message):
    # code to excecute when speak message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('speak',
                              {"utterance": <words to be spoken>,
                               "lang": <language code, e.g. en-us>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'speak' '{ "utterance": <words to be spoken>, "lang": <language code, e.g. en-us>}'
```
{% endtab %}
{% endtabs %}

### mycroft.internet.connected

Internet connection is now available (only generated on initial connection)

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.internet.connected',
                   self.handler_mycroft_internet_connected)

def handler_mycroft_internet_connected(self, message):
    # code to excecute when mycroft.internet.connected message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.internet.connected'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.internet.connected'
```
{% endtab %}
{% endtabs %}

### mycroft.ready

Sent by start-up sequence when everything is ready for user interaction

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/padatious_service.py
      </td>
      <td style="text-align:left">
        Pairing Skill
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.ready',
                   self.handler_mycroft_ready)

def handler_mycroft_ready(self, message):
    # code to excecute when mycroft.ready message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.ready'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.ready'
```
{% endtab %}
{% endtabs %}

### mycroft.stop

Stop command (e.g. button pressed)

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.stop',
                   self.handler_mycroft_stop)

def handler_mycroft_stop(self, message):
    # code to excecute when mycroft.stop message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.stop'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.stop'
```
{% endtab %}
{% endtabs %}

### mycroft.not.paired

Start the pairing process when this event is emitted.

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        Pairing Skill
Weather Skill
Wolfram Alpha Skill
      </td>
      <td style="text-align:left">
        Pairing Skill
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.not.paired',
                   self.handler_mycroft_not_paired)

def handler_mycroft_not_paired(self, message):
    # code to excecute when mycroft.not.paired message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.not.paired'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.not.paired'
```
{% endtab %}
{% endtabs %}

### mycroft.paired

Pairing has completed

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        Pairing Skill
      </td>
      <td style="text-align:left">
        skills/skill_manager.py
enclosure/mark1/__init__.py
enclosure/generic/__init__.py
client/speech/__main__.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.paired',
                   self.handler_mycroft_paired)

def handler_mycroft_paired(self, message):
    # code to excecute when mycroft.paired message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.paired'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.paired'
```
{% endtab %}
{% endtabs %}

### mycroft.awoken

Has come out of sleep mode

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.awoken',
                   self.handler_mycroft_awoken)

def handler_mycroft_awoken(self, message):
    # code to excecute when mycroft.awoken message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.awoken'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.awoken'
```
{% endtab %}
{% endtabs %}

### mycroft.debug.log

log level can be:
   "CRITICAL"
   "ERROR"
   "WARNING"
   "INFO"
   "DEBUG"
These correspond to the Python logging object.

The "bus" parameter allows turning the logging of all bus messages on/off.

**Data:**

```JSON
{
   "level" : <log level>,
   "bus": <True/False>
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.debug.log',
                   self.handler_mycroft_debug_log)

def handler_mycroft_debug_log(self, message):
    # code to excecute when mycroft.debug.log message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.debug.log',
                              {
   "level" : <log level>,
   "bus": <True/False>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.debug.log' '{   "level" : <log level>,   "bus": <True/False>}'
```
{% endtab %}
{% endtabs %}

### complete_intent_failure

Intent processing failed

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('complete_intent_failure',
                   self.handler_complete_intent_failure)

def handler_complete_intent_failure(self, message):
    # code to excecute when complete_intent_failure message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('complete_intent_failure'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'complete_intent_failure'
```
{% endtab %}
{% endtabs %}

### configuration.updated

Notification to services that the configuration has changed and needs reloaded

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('configuration.updated',
                   self.handler_configuration_updated)

def handler_configuration_updated(self, message):
    # code to excecute when configuration.updated message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('configuration.updated'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'configuration.updated'
```
{% endtab %}
{% endtabs %}

## Recognizer

### recognizer_loop:wakeword

Wakeword was heard

**Data:**

```JSON
{
    "utterance": <wakeword heard>,
    "session": <session ID>,
}

```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:wakeword',
                   self.handler_wakeword)

def handler_wakeword(self, message):
    # code to excecute when recognizer_loop:wakeword message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('recognizer_loop:wakeword',
                              {"utterance": <wakeword heard>,
                               "session": <session ID>,}
))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:wakeword' '{ "utterance": <wakeword heard>, "session": <session ID>,}'
```
{% endtab %}
{% endtabs %}

### recognizer_loop:record_begin

Recording has started

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:record_begin',
                   self.handler_record_begin)

def handler_record_begin(self, message):
    # code to excecute when recognizer_loop:record_begin message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('recognizer_loop:record_begin'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:record_begin'
```
{% endtab %}
{% endtabs %}

### recognizer_loop:record_end

Recording has ended

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:record_end',
                   self.handler_record_end)

def handler_record_end(self, message):
    # code to excecute when recognizer_loop:record_end message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('recognizer_loop:record_end'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:record_end'
```
{% endtab %}
{% endtabs %}

### recognizer_loop:utterance

STT has detected the given text or text was injected as an utterance via the CLI.

**Data:**

```JSON
{
    "utterances": [text],
    "lang": self.stt.lang,
    "session": session_id
}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        client/speech/__main__.py
client/speech/listener.py
client/text/text_client.py
skills/__main__.py
      </td>
      <td style="text-align:left">
        client/text/text_client.py
messagebus/client/client.py
skills/intent_service.py

      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:utterance',
                   self.handler_utterance)

def handler_utterance(self, message):
    # code to excecute when recognizer_loop:utterance message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('recognizer_loop:utterance',
                              {"utterances": [text],
                               "lang": self.stt.lang,
                               "session": session_id}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:utterance' '{ "utterances": [text], "lang": self.stt.lang, "session": session_id}'
```
{% endtab %}
{% endtabs %}

### recognizer_loop:audio_output_start

Text output (TTS) has begun

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:audio_output_start',
                   self.handler_audio_output_start)

def handler_audio_output_start(self, message):
    # code to excecute when recognizer_loop:audio_output_start message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('recognizer_loop:audio_output_start'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:audio_output_start'
```
{% endtab %}
{% endtabs %}

### recognizer_loop:audio_output_end

Text output (TTS) has ended

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:audio_output_end',
                   self.handler_audio_output_end)

def handler_audio_output_end(self, message):
    # code to excecute when recognizer_loop:audio_output_end message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('recognizer_loop:audio_output_end'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:audio_output_end'
```
{% endtab %}
{% endtabs %}

### recognizer_loop:sleep

Go into "sleep" mode.  Everything except "Hey Mycroft, wake up" will be ignored.

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:sleep',
                   self.handler_sleep)

def handler_sleep(self, message):
    # code to excecute when recognizer_loop:sleep message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('recognizer_loop:sleep'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:sleep'
```
{% endtab %}
{% endtabs %}

### recognizer_loop:wake_up

Come out of "sleep" mode.

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:wake_up',
                   self.handler_wake_up)

def handler_wake_up(self, message):
    # code to excecute when recognizer_loop:wake_up message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('recognizer_loop:wake_up'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:wake_up'
```
{% endtab %}
{% endtabs %}

## Enclosure

### enclosure.notify.no_internet

Detetected a connection error during STT

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('enclosure.notify.no_internet',
                   self.handler_enclosure_notify_no_internet)

def handler_enclosure_notify_no_internet(self, message):
    # code to excecute when enclosure.notify.no_internet message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('enclosure.notify.no_internet'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'enclosure.notify.no_internet'
```
{% endtab %}
{% endtabs %}

### enclosure.mouth.viseme_list

start: timestamp for audio starts (unix epoch)
END_TIME: time in seconds from "start" until the end of the viseme
CODE can be
0 = shape for sounds like 'y' or 'aa'
1 = shape for sounds like 'aw'
2 = shape for sounds like 'uh' or 'r'
3 = shape for sounds like 'th' or 'sh'
4 = neutral shape for no sound
5 = shape for sounds like 'f' or 'v'
6 = shape for sounds like 'oy' or 'ao'

**Data:**

```JSON
{
  "start": timestamp,
  "visemes": [[CODE,END_TIME],...]
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('enclosure.mouth.viseme_list',
                   self.handler_enclosure_mouth_viseme_list)

def handler_enclosure_mouth_viseme_list(self, message):
    # code to excecute when enclosure.mouth.viseme_list message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('enclosure.mouth.viseme_list',
                              {
  "start": timestamp,
  "visemes": [[CODE,END_TIME],...]}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'enclosure.mouth.viseme_list' '{  "start": timestamp,  "visemes": [[CODE,END_TIME],...]}'
```
{% endtab %}
{% endtabs %}

### mycroft.eyes.default

Change eyes to default color

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-mark-1
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.eyes.default',
                   self.handler_mycroft_eyes_default)

def handler_mycroft_eyes_default(self, message):
    # code to excecute when mycroft.eyes.default message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.eyes.default'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.eyes.default'
```
{% endtab %}
{% endtabs %}

## Microphone Behavior

### mycroft.mic.listen

Begin recording for STT processing

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.mic.listen',
                   self.handler_mycroft_mic_listen)

def handler_mycroft_mic_listen(self, message):
    # code to excecute when mycroft.mic.listen message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.mic.listen'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.mic.listen'
```
{% endtab %}
{% endtabs %}

### mycroft.mic.mute

Turn off the mic (no wakeword or STT processing)

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        Pairing Skill
      </td>
      <td style="text-align:left">
        client/speech/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.mic.mute',
                   self.handler_mycroft_mic_mute)

def handler_mycroft_mic_mute(self, message):
    # code to excecute when mycroft.mic.mute message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.mic.mute'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.mic.mute'
```
{% endtab %}
{% endtabs %}

### mycroft.mic.unmute

Turn on the mic (enable wakeword and STT processing)

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        Pairing Skill
      </td>
      <td style="text-align:left">
        client/speech/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.mic.unmute',
                   self.handler_mycroft_mic_unmute)

def handler_mycroft_mic_unmute(self, message):
    # code to excecute when mycroft.mic.unmute message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.mic.unmute'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.mic.unmute'
```
{% endtab %}
{% endtabs %}

## Audio Playback

### mycroft.audio.service.play

Start playback of tracklist

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/audioservice.py / playback-control
      </td>
      <td style="text-align:left">
        audio/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.play',
                   self.handler_mycroft_audio_service_play)

def handler_mycroft_audio_service_play(self, message):
    # code to excecute when mycroft.audio.service.play message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.play'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.play'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.stop

Stop playback

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/audioservice.py / playback-control
      </td>
      <td style="text-align:left">
        audio/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.stop',
                   self.handler_mycroft_audio_service_stop)

def handler_mycroft_audio_service_stop(self, message):
    # code to excecute when mycroft.audio.service.stop message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.stop'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.stop'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.pause

Pause playback (if supported)

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/audioservice.py / playback-control
      </td>
      <td style="text-align:left">
        audio/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.pause',
                   self.handler_mycroft_audio_service_pause)

def handler_mycroft_audio_service_pause(self, message):
    # code to excecute when mycroft.audio.service.pause message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.pause'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.pause'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.resume

Resume playback (if supported by backend)

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/audioservice.py / playback-control
      </td>
      <td style="text-align:left">
        audio/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.resume',
                   self.handler_mycroft_audio_service_resume)

def handler_mycroft_audio_service_resume(self, message):
    # code to excecute when mycroft.audio.service.resume message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.resume'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.resume'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.next

Skip to next track

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/audioservice.py / playback-control
      </td>
      <td style="text-align:left">
        audio/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.next',
                   self.handler_mycroft_audio_service_next)

def handler_mycroft_audio_service_next(self, message):
    # code to excecute when mycroft.audio.service.next message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.next'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.next'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.prev

Skip to previous track

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/audioservice.py / playback-control
      </td>
      <td style="text-align:left">
        audio/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.prev',
                   self.handler_mycroft_audio_service_prev)

def handler_mycroft_audio_service_prev(self, message):
    # code to excecute when mycroft.audio.service.prev message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.prev'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.prev'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.track_info

Request track info from audio service

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/audioservice.py / playback-control
      </td>
      <td style="text-align:left">
        audio/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.track_info',
                   self.handler_mycroft_audio_service_track_info)

def handler_mycroft_audio_service_track_info(self, message):
    # code to excecute when mycroft.audio.service.track_info message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.track_info'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.track_info'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.track_info_reply

Reply to track info request

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        audio/main.py
      </td>
      <td style="text-align:left">
        skills/audioservice.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.track_info_reply',
                   self.handler_mycroft_audio_service_track_info_reply)

def handler_mycroft_audio_service_track_info_reply(self, message):
    # code to excecute when mycroft.audio.service.track_info_reply message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.track_info_reply'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.track_info_reply'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.list_backends

Returns list of available backends.

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/audioservice.py
      </td>
      <td style="text-align:left">
        audio/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.audio.service.list_backends',
                   self.handler_mycroft_audio_service_list_backends)

def handler_mycroft_audio_service_list_backends(self, message):
    # code to excecute when mycroft.audio.service.list_backends message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.audio.service.list_backends'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.list_backends'
```
{% endtab %}
{% endtabs %}

## Volume Control

### mycroft.volume.increase

Enclosure Volume up

**Data:**

```JSON
{"play_sound": True}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        client/enclosure/__init__.py
      </td>
      <td style="text-align:left">
        Volume Skill
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.increase',
                   self.handler_mycroft_volume_increase)

def handler_mycroft_volume_increase(self, message):
    # code to excecute when mycroft.volume.increase message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.increase',
                              {"play_sound": True}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.increase' '{"play_sound": True}'
```
{% endtab %}
{% endtabs %}

### mycroft.volume.decrease

Enclosure Volume down

**Data:**

```JSON
{"play_sound": True}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        client/enclosure/__init__.py
      </td>
      <td style="text-align:left">
        Volume Skill
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.decrease',
                   self.handler_mycroft_volume_decrease)

def handler_mycroft_volume_decrease(self, message):
    # code to excecute when mycroft.volume.decrease message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.decrease',
                              {"play_sound": True}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.decrease' '{"play_sound": True}'
```
{% endtab %}
{% endtabs %}

### mycroft.volume.mute

Enclosure Volume muted

**Data:**

```JSON
{"speak_message": True}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skill-naptime
      </td>
      <td style="text-align:left">
        Volume Skill
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.mute',
                   self.handler_mycroft_volume_mute)

def handler_mycroft_volume_mute(self, message):
    # code to excecute when mycroft.volume.mute message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.mute',
                              {"speak_message": True}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.mute' '{"speak_message": True}'
```
{% endtab %}
{% endtabs %}

### mycroft.volume.unmute

Enclosure Volume unmuted

**Data:**

```JSON
{"speak_message": True}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skill-naptime
      </td>
      <td style="text-align:left">
        Volume Skill
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.unmute',
                   self.handler_mycroft_volume_unmute)

def handler_mycroft_volume_unmute(self, message):
    # code to excecute when mycroft.volume.unmute message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.unmute',
                              {"speak_message": True}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.unmute' '{"speak_message": True}'
```
{% endtab %}
{% endtabs %}

### mycroft.volume.set

Set enclosure volume (0.0 = no output, 1.0 = loudest possible)

**Data:**

```JSON
{"percent": float}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        Volume Skill
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.set',
                   self.handler_mycroft_volume_set)

def handler_mycroft_volume_set(self, message):
    # code to excecute when mycroft.volume.set message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.set',
                              {"percent": float}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.set' '{"percent": float}'
```
{% endtab %}
{% endtabs %}

### mycroft.volume.get

Request volume level

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.get',
                   self.handler_mycroft_volume_get)

def handler_mycroft_volume_get(self, message):
    # code to excecute when mycroft.volume.get message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.get'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.get'
```
{% endtab %}
{% endtabs %}

### mycroft.volume.get.response



**Data:**

```JSON
{
    "percent": <volume percentage>,
    "muted": <true/false>
}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        Enclosure (skill-mark-2)
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.get.response',
                   self.handler_mycroft_volume_get_response)

def handler_mycroft_volume_get_response(self, message):
    # code to excecute when mycroft.volume.get.response message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.get.response',
                              {"percent": <volume percentage>,
                               "muted": <true/false>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.get.response' '{ "percent": <volume percentage>, "muted": <true/false>}'
```
{% endtab %}
{% endtabs %}

### mycroft.volume.duck

Reduce the volume level temporarilly

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        Enclosure (skill-mark-2)
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.duck',
                   self.handler_mycroft_volume_duck)

def handler_mycroft_volume_duck(self, message):
    # code to excecute when mycroft.volume.duck message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.duck'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.duck'
```
{% endtab %}
{% endtabs %}

### mycroft.volume.unduck

Restore the volume level

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        Enclosure (skill-mark-2)
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.volume.unduck',
                   self.handler_mycroft_volume_unduck)

def handler_mycroft_volume_unduck(self, message):
    # code to excecute when mycroft.volume.unduck message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.volume.unduck'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.volume.unduck'
```
{% endtab %}
{% endtabs %}

## Mycroft Skill Core

### mycroft.skill.handler.start



**Data:**

```JSON
{handler: class/function name}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skill.handler.start',
                   self.handler_mycroft_skill_handler_start)

def handler_mycroft_skill_handler_start(self, message):
    # code to excecute when mycroft.skill.handler.start message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skill.handler.start',
                              {handler: class/function name}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skill.handler.start' '{handler: class/function name}'
```
{% endtab %}
{% endtabs %}

### mycroft.skill.handler.complete



**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skill.handler.complete',
                   self.handler_mycroft_skill_handler_complete)

def handler_mycroft_skill_handler_complete(self, message):
    # code to excecute when mycroft.skill.handler.complete message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skill.handler.complete'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skill.handler.complete'
```
{% endtab %}
{% endtabs %}

### mycroft.skill.enable_intent

Enable disabled intent

**Data:**

```JSON
{"intent_name": "name"}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft/skills/core.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skill.enable_intent',
                   self.handler_mycroft_skill_enable_intent)

def handler_mycroft_skill_enable_intent(self, message):
    # code to excecute when mycroft.skill.enable_intent message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skill.enable_intent',
                              {"intent_name": "name"}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skill.enable_intent' '{"intent_name": "name"}'
```
{% endtab %}
{% endtabs %}

### mycroft.skill.disable_intent

Disable intent

**Data:**

```JSON
{"intent_name": "name"}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft/skills/core.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skill.disable_intent',
                   self.handler_mycroft_skill_disable_intent)

def handler_mycroft_skill_disable_intent(self, message):
    # code to excecute when mycroft.skill.disable_intent message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skill.disable_intent',
                              {"intent_name": "name"}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skill.disable_intent' '{"intent_name": "name"}'
```
{% endtab %}
{% endtabs %}

### mycroft.skills.loaded

A Skill has been loaded

**Data:**

```JSON
{
    "id": <skill ID>,
    "name": <skill name>,
    "folder": <skill directory>,
    "modified": <modified time>
}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        skills/main.py
      </td>
      <td style="text-align:left">
        mycroft/skills/intent_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skills.loaded',
                   self.handler_mycroft_skills_loaded)

def handler_mycroft_skills_loaded(self, message):
    # code to excecute when mycroft.skills.loaded message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skills.loaded',
                              {"id": <skill ID>,
                               "name": <skill name>,
                               "folder": <skill directory>,
                               "modified": <modified time>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skills.loaded' '{ "id": <skill ID>, "name": <skill name>, "folder": <skill directory>, "modified": <modified time>}'
```
{% endtab %}
{% endtabs %}

### mycroft.skills.loading_failure

A Skill has failed to load

**Data:**

```JSON
{
    "id": <skill ID>,
    "folder": <skill directory>
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skills.loading_failure',
                   self.handler_mycroft_skills_loading_failure)

def handler_mycroft_skills_loading_failure(self, message):
    # code to excecute when mycroft.skills.loading_failure message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skills.loading_failure',
                              {"id": <skill ID>,
                               "folder": <skill directory>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skills.loading_failure' '{ "id": <skill ID>, "folder": <skill directory>}'
```
{% endtab %}
{% endtabs %}

### mycroft.skills.shutdown

A Skill has shutdown

**Data:**

```JSON
{
    "id": <skill ID>,
    "folder": <skill directory>
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skills.shutdown',
                   self.handler_mycroft_skills_shutdown)

def handler_mycroft_skills_shutdown(self, message):
    # code to excecute when mycroft.skills.shutdown message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skills.shutdown',
                              {"id": <skill ID>,
                               "folder": <skill directory>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skills.shutdown' '{ "id": <skill ID>, "folder": <skill directory>}'
```
{% endtab %}
{% endtabs %}

### mycroft.skills.initialized

Upon startup, all skills have been loaded

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        mycroft/skills/skill_manager.py
      </td>
      <td style="text-align:left">
        mycroft/skills/padatious_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skills.initialized',
                   self.handler_mycroft_skills_initialized)

def handler_mycroft_skills_initialized(self, message):
    # code to excecute when mycroft.skills.initialized message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skills.initialized'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skills.initialized'
```
{% endtab %}
{% endtabs %}

### mycroft.skills.list

List of loaded skills (response to 'skillmanager.list')

**Data:**

```JSON
{"skills": [<list of skill IDs>] }
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skills.list',
                   self.handler_mycroft_skills_list)

def handler_mycroft_skills_list(self, message):
    # code to excecute when mycroft.skills.list message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skills.list',
                              {"skills": [<list of skill IDs>] }))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skills.list' '{"skills": [<list of skill IDs>] }'
```
{% endtab %}
{% endtabs %}

### mycroft.skills.settings.update

Pull new skill settings from the server

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        Configuration Skill
      </td>
      <td style="text-align:left">
        mycroft/skills/settings.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('mycroft.skills.settings.update',
                   self.handler_mycroft_skills_settings_update)

def handler_mycroft_skills_settings_update(self, message):
    # code to excecute when mycroft.skills.settings.update message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('mycroft.skills.settings.update'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skills.settings.update'
```
{% endtab %}
{% endtabs %}

## Mycroft Skill Manager (MSM)

### msm.updating

MSM install has begun

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.updating',
                   self.handler_msm_updating)

def handler_msm_updating(self, message):
    # code to excecute when msm.updating message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.updating'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.updating'
```
{% endtab %}
{% endtabs %}

### msm.installing

MSM update has begun

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.installing',
                   self.handler_msm_installing)

def handler_msm_installing(self, message):
    # code to excecute when msm.installing message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.installing'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.installing'
```
{% endtab %}
{% endtabs %}

### msm.install.succeeded

MSM install succeeded for given skill

**Data:**

```JSON
{ "skill" : <skill name> }
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.install.succeeded',
                   self.handler_msm_install_succeeded)

def handler_msm_install_succeeded(self, message):
    # code to excecute when msm.install.succeeded message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.install.succeeded',
                              { "skill" : <skill name> }))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.install.succeeded' '{ "skill" : <skill name> }'
```
{% endtab %}
{% endtabs %}

### msm.install.failed

MSM install failed for given skill

**Data:**

```JSON
{
    "skill" : <skill name>,
    "error": <error code>
}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.install.failed',
                   self.handler_msm_install_failed)

def handler_msm_install_failed(self, message):
    # code to excecute when msm.install.failed message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.install.failed',
                              {"skill" : <skill name>,
                               "error": <error code>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.install.failed' '{ "skill" : <skill name>, "error": <error code>}'
```
{% endtab %}
{% endtabs %}

### msm.installed

MSM install is complete

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.installed',
                   self.handler_msm_installed)

def handler_msm_installed(self, message):
    # code to excecute when msm.installed message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.installed'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.installed'
```
{% endtab %}
{% endtabs %}

### msm.updated

MSM update is complete

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.updated',
                   self.handler_msm_updated)

def handler_msm_updated(self, message):
    # code to excecute when msm.updated message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.updated'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.updated'
```
{% endtab %}
{% endtabs %}

### msm.removing

MSM remove has begun

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.removing',
                   self.handler_msm_removing)

def handler_msm_removing(self, message):
    # code to excecute when msm.removing message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.removing'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.removing'
```
{% endtab %}
{% endtabs %}

### msm.remove.succeeded

MSM remove succeeded for given skill

**Data:**

```JSON
{ "skill" : <skill name> }
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.remove.succeeded',
                   self.handler_msm_remove_succeeded)

def handler_msm_remove_succeeded(self, message):
    # code to excecute when msm.remove.succeeded message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.remove.succeeded',
                              { "skill" : <skill name> }))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.remove.succeeded' '{ "skill" : <skill name> }'
```
{% endtab %}
{% endtabs %}

### msm.remove.failed

MSM remove failed for given skill

**Data:**

```JSON
{
    "skill" : <skill name>,
    "error": <error code>
}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.remove.failed',
                   self.handler_msm_remove_failed)

def handler_msm_remove_failed(self, message):
    # code to excecute when msm.remove.failed message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.remove.failed',
                              {"skill" : <skill name>,
                               "error": <error code>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.remove.failed' '{ "skill" : <skill name>, "error": <error code>}'
```
{% endtab %}
{% endtabs %}

### msm.removed

MSM remove is complete

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        msm.sh
      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('msm.removed',
                   self.handler_msm_removed)

def handler_msm_removed(self, message):
    # code to excecute when msm.removed message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('msm.removed'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'msm.removed'
```
{% endtab %}
{% endtabs %}

## Skill Manager

### skillmanager.deactivate

Deactivate a skill.  Activate by typing ":deactivate <skill>" in the CLI

**Data:**

```JSON
{'skill': <skill directory name>}
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        CLI (client/text/main.py)
      </td>
      <td style="text-align:left">
        skills/skill_manager.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('skillmanager.deactivate',
                   self.handler_skillmanager_deactivate)

def handler_skillmanager_deactivate(self, message):
    # code to excecute when skillmanager.deactivate message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('skillmanager.deactivate',
                              {'skill': <skill directory name>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'skillmanager.deactivate' '{'skill': <skill directory name>}'
```
{% endtab %}
{% endtabs %}

### skillmanager.list

List installed skills.  Activate by typing ":list" in the CLI

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        CLI (client/text/main.py)
      </td>
      <td style="text-align:left">
        skills/skill_manager.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('skillmanager.list',
                   self.handler_skillmanager_list)

def handler_skillmanager_list(self, message):
    # code to excecute when skillmanager.list message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('skillmanager.list'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'skillmanager.list'
```
{% endtab %}
{% endtabs %}

### skillmanager.update

Request immediate update of all skills

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        skills/main.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('skillmanager.update',
                   self.handler_skillmanager_update)

def handler_skillmanager_update(self, message):
    # code to excecute when skillmanager.update message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('skillmanager.update'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'skillmanager.update'
```
{% endtab %}
{% endtabs %}

## Messagebus Connection

### open

websocket connection has closed

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('open',
                   self.handler_open)

def handler_open(self, message):
    # code to excecute when open message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('open'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'open'
```
{% endtab %}
{% endtabs %}

### close

websocket connection was lost, reconnecting

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('close',
                   self.handler_close)

def handler_close(self, message):
    # code to excecute when close message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('close'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'close'
```
{% endtab %}
{% endtabs %}

### reconnecting

websocket connection has opened

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('reconnecting',
                   self.handler_reconnecting)

def handler_reconnecting(self, message):
    # code to excecute when reconnecting message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('reconnecting'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'reconnecting'
```
{% endtab %}
{% endtabs %}

## System Administrative Actions

### system.wifi.setup / mycroft.wifi.start

Kick off a a wifi-setup session

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-wifi-setup: mycroft_admin_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.wifi.setup / mycroft.wifi.start',
                   self.handler_system_wifi_setup / mycroft_wifi_start)

def handler_system_wifi_setup / mycroft_wifi_start(self, message):
    # code to excecute when system.wifi.setup / mycroft.wifi.start message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('system.wifi.setup / mycroft.wifi.start'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.wifi.setup / mycroft.wifi.start'
```
{% endtab %}
{% endtabs %}

### system.wifi.reset / mycroft.wifi.reset

Clear the saved wifi settings

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-wifi-setup: mycroft_admin_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.wifi.reset / mycroft.wifi.reset',
                   self.handler_system_wifi_reset / mycroft_wifi_reset)

def handler_system_wifi_reset / mycroft_wifi_reset(self, message):
    # code to excecute when system.wifi.reset / mycroft.wifi.reset message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('system.wifi.reset / mycroft.wifi.reset'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.wifi.reset / mycroft.wifi.reset'
```
{% endtab %}
{% endtabs %}

### system.ntp.sync

Force the system clock to synchronize with NTP servers

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-wifi-setup: mycroft_admin_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.ntp.sync',
                   self.handler_system_ntp_sync)

def handler_system_ntp_sync(self, message):
    # code to excecute when system.ntp.sync message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('system.ntp.sync'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.ntp.sync'
```
{% endtab %}
{% endtabs %}

### system.ssh.enable / mycroft.enable.ssh

Configure system to allow SSH connections

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-wifi-setup: mycroft_admin_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.ssh.enable / mycroft.enable.ssh',
                   self.handler_system_ssh_enable / mycroft_enable_ssh)

def handler_system_ssh_enable / mycroft_enable_ssh(self, message):
    # code to excecute when system.ssh.enable / mycroft.enable.ssh message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('system.ssh.enable / mycroft.enable.ssh'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.ssh.enable / mycroft.enable.ssh'
```
{% endtab %}
{% endtabs %}

### system.ssh.disable / mycroft.disable.ssh

Configure system to block SSH connections

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-wifi-setup: mycroft_admin_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.ssh.disable / mycroft.disable.ssh',
                   self.handler_system_ssh_disable / mycroft_disable_ssh)

def handler_system_ssh_disable / mycroft_disable_ssh(self, message):
    # code to excecute when system.ssh.disable / mycroft.disable.ssh message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('system.ssh.disable / mycroft.disable.ssh'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.ssh.disable / mycroft.disable.ssh'
```
{% endtab %}
{% endtabs %}

### system.reboot

Force a Linux reboot

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-wifi-setup: mycroft_admin_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.reboot',
                   self.handler_system_reboot)

def handler_system_reboot(self, message):
    # code to excecute when system.reboot message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('system.reboot'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.reboot'
```
{% endtab %}
{% endtabs %}

### system.shutdown

Force a Linux shutdown

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-wifi-setup: mycroft_admin_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.shutdown',
                   self.handler_system_shutdown)

def handler_system_shutdown(self, message):
    # code to excecute when system.shutdown message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('system.shutdown'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.shutdown'
```
{% endtab %}
{% endtabs %}

### system.update

 Force an apt-get update on 'mycroft-mark-1' or 'mycroft-picroft' package (as appropriate)

<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">

      </td>
      <td style="text-align:left">
        mycroft-wifi-setup: mycroft_admin_service.py
      </td>
    </tr>
  </tbody>
</table>

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.update',
                   self.handler_system_update)

def handler_system_update(self, message):
    # code to excecute when system.update message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('system.update'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.update'
```
{% endtab %}
{% endtabs %}

## Common Play System

### play:query



**Data:**

```JSON
{ "phrase": <something to be played> }
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('play:query',
                   self.handler_query)

def handler_query(self, message):
    # code to excecute when play:query message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('play:query',
                              { "phrase": <something to be played> }))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'play:query' '{ "phrase": <something to be played> }'
```
{% endtab %}
{% endtabs %}

### play:query.response

phrase -- the phrase this response is regarding
id -- uniquely identifies the skill, so normally the skill's self.skill_id
conf -- the confidence it can handle the request, between 0.0 and 1.0
     Confidence guidelines:
          1.0 = exact command match, e.g. "play npr news"
        >0.9 = multi-key match for database entry, e.g. "play madonna's lucky star" or
                   "play artist madona"  (matches "artist" and "madonna").
                   For each additional key over 2, add 0.1 to the confidence, so
                   "play madonna's lucky star on spotify" would be 0.91 for three keywords
        >0.8 = single-key match for database title entry, e.g. "play lucky star"
        >0.7 = single-key match for database artist or group, e.g. "play madonna"
        >0.6 = single-key match for database genre or category, e.g. "play reggae"
        >0.5 = generic match, e.g. "play some music" or "play a movie"
callback_data -- optional data structure to return in play:start

NOTE: Must be received within 1 second.  If longer is needed, see the "searching" response below.

**Data:**

```JSON
{
    "phrase": phrase,
    "skill_id":  self.skill_id,
    "conf": confidence,
    "callback_data": data
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('play:query.response',
                   self.handler_query_response)

def handler_query_response(self, message):
    # code to excecute when play:query.response message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('play:query.response',
                              {"phrase": phrase,
                               "skill_id":  self.skill_id,
                               "conf": confidence,
                               "callback_data": data}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'play:query.response' '{ "phrase": phrase, "skill_id":  self.skill_id, "conf": confidence, "callback_data": data}'
```
{% endtab %}
{% endtabs %}

###

Request a timeout extension while performing a search

**Data:**

```JSON
{
    "phrase": phrase,
    "searching":  true
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('',
                   self.handler_)

def handler_(self, message):
    # code to excecute when  message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('',
                              {"phrase": phrase,
                               "searching":  true}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send '' '{ "phrase": phrase, "searching":  true}'
```
{% endtab %}
{% endtabs %}

### play:start

skill_id -- the unique ID of the skill that is being invoked
phrase -- the original phrase user said, e.g. "some thing" from utterance "play some thing"
callback_data -- (optional) data the skill can use to start playback

**Data:**

```JSON
{
    "skill_id": <skill_id>,
     "phrase": phrase,
     "callback_data": optional_data
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('play:start',
                   self.handler_start)

def handler_start(self, message):
    # code to excecute when play:start message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('play:start',
                              {"skill_id": <skill_id>,
                                "phrase": phrase,
                                "callback_data": optional_data}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'play:start' '{ "skill_id": <skill_id>,  "phrase": phrase,  "callback_data": optional_data}'
```
{% endtab %}
{% endtabs %}

## Common Query System

### question:query



**Data:**

```JSON
{"phrase": "complete question"}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('question:query',
                   self.handler_query)

def handler_query(self, message):
    # code to excecute when question:query message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('question:query',
                              {"phrase": "complete question"}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'question:query' '{"phrase": "complete question"}'
```
{% endtab %}
{% endtabs %}

### question:query.response

skill_id -- the unique ID of the skill that is being invoked
phrase -- the original phrase user said, e.g. "some thing" from utterance "how tall was abraham lincoln"
answer - the returned answer from the skill
conf -- confidence level of answers validity
callback_data -- (optional) data the skill can use for any additional actions (such as image url or similar)
searching -- true if more time is needed to complete the search, otherwise false

**Data:**

```JSON
{
    "phrase": phrase,
    "skill_id": <skill_id>,
    "answer": "answer string",
    "conf": confidence,
    "callback_data": <json data>,
    "searching": true/false
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('question:query.response',
                   self.handler_query_response)

def handler_query_response(self, message):
    # code to excecute when question:query.response message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('question:query.response',
                              {"phrase": phrase,
                               "skill_id": <skill_id>,
                               "answer": "answer string",
                               "conf": confidence,
                               "callback_data": <json data>,
                               "searching": true/false}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'question:query.response' '{ "phrase": phrase, "skill_id": <skill_id>, "answer": "answer string", "conf": confidence, "callback_data": <json data>, "searching": true/false}'
```
{% endtab %}
{% endtabs %}

### question:action

skill_id -- the unique ID of the skill that is being invoked
phrase -- the original phrase user said, e.g. "some thing" from utterance "how tall was abraham lincoln"
callback_data -- (optional) data the skill can use to take additional actions

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('question:action',
                   self.handler_action)

def handler_action(self, message):
    # code to excecute when question:action message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('question:action'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'question:action'
```
{% endtab %}
{% endtabs %}

## Mycroft Alarm Skill

### private.mycroftai.has_alarm

Count of running alarms (0 == no alarms)

**Data:**

```JSON
{"active_alarms": COUNT }
```

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('private.mycroftai.has_alarm',
                   self.handler_private_mycroftai_has_alarm)

def handler_private_mycroftai_has_alarm(self, message):
    # code to excecute when private.mycroftai.has_alarm message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('private.mycroftai.has_alarm',
                              {"active_alarms": COUNT }))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'private.mycroftai.has_alarm' '{"active_alarms": COUNT }'
```
{% endtab %}
{% endtabs %}

## PROPOSED

### skill.namespace.*

e.g. "skill.mycroft.noftify.alarm_changed" or "skill.jaguar.notify.car_stopped"

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('skill.namespace.*',
                   self.handler_skill_namespace_*)

def handler_skill_namespace_*(self, message):
    # code to excecute when skill.namespace.* message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('skill.namespace.*'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'skill.namespace.*'
```
{% endtab %}
{% endtabs %}

### private.github_username.*

for private (not intended to be used by anyone else)

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('private.github_username.*',
                   self.handler_private_github_username_*)

def handler_private_github_username_*(self, message):
    # code to excecute when private.github_username.* message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.emitter.emit(Message('private.github_username.*'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'private.github_username.*'
```
{% endtab %}
{% endtabs %}
