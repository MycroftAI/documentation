---
description: >-
  Messages are used to communicate information between Mycroft services and
  other components. This list of Message types outlines the details and provides
  sample code for each.
---

# Message Types

Each Message type listed contains a description outlining it's meaning or purpose. Where relevant, the Message type will also list the specific JSON data packets expected to be emitted with that Message, and the most common producers and consumers of the Message.

See the [MessageBus documentation](message-bus.md) for further information on this service and examples of using Messages.

## General

### speak

Request to speak utterance

**Data:**

```javascript
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
    self.bus.emit(Message('speak',
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

Internet connection is now available \(only generated on initial connection\)

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
    self.bus.emit(Message('mycroft.internet.connected'))
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

| Producer | Consumer |
| :--- | :--- |
| `skills/padatious_service.py` | Pairing Skill |

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
    self.bus.emit(Message('mycroft.ready'))
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

Stop command \(e.g. button pressed\)

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
    self.bus.emit(Message('mycroft.stop'))
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

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p>Pairing Skill</p>
        <p>Weather Skill</p>
        <p>Wolfram Alpha Skill</p>
      </th>
      <th style="text-align:left">Pairing Skill</th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.not.paired'))
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

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">Pairing Skill</th>
      <th style="text-align:left">
        <p><code>skills/skill_manager.py</code>
        </p>
        <p><code>enclosure/mark1/__init__.py</code>
        </p>
        <p><code>enclosure/generic/__init__.py</code>
        </p>
        <p><code>client/speech/__main__.py</code>
        </p>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.paired'))
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
    self.bus.emit(Message('mycroft.awoken'))
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

log level can be: "CRITICAL" "ERROR" "WARNING" "INFO" "DEBUG" These correspond to the Python logging object.

The "bus" parameter allows turning the logging of all bus messages on/off.

**Data:**

```javascript
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
    self.bus.emit(Message('mycroft.debug.log',
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

### complete\_intent\_failure

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
    self.bus.emit(Message('complete_intent_failure'))
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
    self.bus.emit(Message('configuration.updated'))
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

### recognizer\_loop:wakeword

Wakeword was heard

**Data:**

```javascript
{
    "utterance": <wakeword heard>,
    "session": <session ID>,
}
```

| Producer | Consumer |
| :--- | :--- |
| `client/speech/main.py` |  |

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
    self.bus.emit(Message('recognizer_loop:wakeword',
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

### recognizer\_loop:record\_begin

Recording has started

| Producer | Consumer |
| :--- | :--- |
| `client/speech/main.py` |  |

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
    self.bus.emit(Message('recognizer_loop:record_begin'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:record_begin'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:record\_end

Recording has ended

| Producer | Consumer |
| :--- | :--- |
| `client/speech/main.py` |  |

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
    self.bus.emit(Message('recognizer_loop:record_end'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:record_end'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:utterance

STT has detected the given text or text was injected as an utterance via the CLI.

**Data:**

```javascript
{
    "utterances": [text],
    "lang": self.stt.lang,
    "session": session_id
}
```

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>client/speech/__main__.py</code>
        </p>
        <p><code>client/speech/listener.py</code>
        </p>
        <p><code>client/text/text_client.py</code>
        </p>
        <p><code>skills/__main__.py</code>
        </p>
      </th>
      <th style="text-align:left">
        <p><code>client/text/text_client.py</code>
        </p>
        <p><code>messagebus/client/client.py</code>
        </p>
        <p><code>skills/intent_service.py</code>
        </p>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('recognizer_loop:utterance',
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

### recognizer\_loop:audio\_output\_start

Text output \(TTS\) has begun

| Producer | Consumer |
| :--- | :--- |
| `audio/speech.py` |  |

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
    self.bus.emit(Message('recognizer_loop:audio_output_start'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:audio_output_start'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:audio\_output\_end

Text output \(TTS\) has ended

| Producer | Consumer |
| :--- | :--- |
| `audio/speech.py` |  |

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
    self.bus.emit(Message('recognizer_loop:audio_output_end'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:audio_output_end'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:sleep

Go into "sleep" mode. Everything except "Hey Mycroft, wake up" will be ignored.

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
    self.bus.emit(Message('recognizer_loop:sleep'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'recognizer_loop:sleep'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:wake\_up

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
    self.bus.emit(Message('recognizer_loop:wake_up'))
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

### enclosure.notify.no\_internet

Detetected a connection error during STT

| Producer | Consumer |
| :--- | :--- |
| `audio/speech.py` |  |

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
    self.bus.emit(Message('enclosure.notify.no_internet'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'enclosure.notify.no_internet'
```
{% endtab %}
{% endtabs %}

### enclosure.mouth.viseme\_list

start: timestamp for audio starts \(unix epoch\) END\_TIME: time in seconds from "start" until the end of the viseme CODE can be 0 = shape for sounds like 'y' or 'aa' 1 = shape for sounds like 'aw' 2 = shape for sounds like 'uh' or 'r' 3 = shape for sounds like 'th' or 'sh' 4 = neutral shape for no sound 5 = shape for sounds like 'f' or 'v' 6 = shape for sounds like 'oy' or 'ao'

**Data:**

```javascript
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
    self.bus.emit(Message('enclosure.mouth.viseme_list',
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

| Producer | Consumer |
| :--- | :--- |
|  | mycroft-mark-1 |

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
    self.bus.emit(Message('mycroft.eyes.default'))
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
    self.bus.emit(Message('mycroft.mic.listen'))
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

Turn off the mic \(no wakeword or STT processing\)

| Producer | Consumer |
| :--- | :--- |
| Pairing Skill | `client/speech/main.py` |

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
    self.bus.emit(Message('mycroft.mic.mute'))
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

Turn on the mic \(enable wakeword and STT processing\)

| Producer | Consumer |
| :--- | :--- |
| Pairing Skill | `client/speech/main.py` |

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
    self.bus.emit(Message('mycroft.mic.unmute'))
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

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.audio.service.play'))
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

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.audio.service.stop'))
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

Pause playback \(if supported\)

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.audio.service.pause'))
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

Resume playback \(if supported by backend\)

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.audio.service.resume'))
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

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.audio.service.next'))
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

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.audio.service.prev'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.prev'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.track\_info

Request track info from audio service

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>{% tabs %}
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
    self.bus.emit(Message('mycroft.audio.service.track_info'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.track_info'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.track\_info\_reply

Reply to track info request

| Producer | Consumer |
| :--- | :--- |
| `audio/main.py` | `skills/audioservice.py` |

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
    self.bus.emit(Message('mycroft.audio.service.track_info_reply'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.audio.service.track_info_reply'
```
{% endtab %}
{% endtabs %}

### mycroft.audio.service.list\_backends

Returns list of available backends.

| Producer | Consumer |
| :--- | :--- |
| `skills/audioservice.py` | `audio/main.py` |

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
    self.bus.emit(Message('mycroft.audio.service.list_backends'))
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

```javascript
{"play_sound": True}
```

| Producer | Consumer |
| :--- | :--- |
| `client/enclosure/__init__.py` | Volume Skill |

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
    self.bus.emit(Message('mycroft.volume.increase',
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

```javascript
{"play_sound": True}
```

| Producer | Consumer |
| :--- | :--- |
| `client/enclosure/__init__.py` | Volume Skill |

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
    self.bus.emit(Message('mycroft.volume.decrease',
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

```javascript
{"speak_message": True}
```

| Producer | Consumer |
| :--- | :--- |
| skill-naptime | Volume Skill |

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
    self.bus.emit(Message('mycroft.volume.mute',
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

```javascript
{"speak_message": True}
```

| Producer | Consumer |
| :--- | :--- |
| skill-naptime | Volume Skill |

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
    self.bus.emit(Message('mycroft.volume.unmute',
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

Set enclosure volume \(0.0 = no output, 1.0 = loudest possible\)

**Data:**

```javascript
{"percent": float}
```

| Producer | Consumer |
| :--- | :--- |
|  | Volume Skill |

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
    self.bus.emit(Message('mycroft.volume.set',
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
    self.bus.emit(Message('mycroft.volume.get'))
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

```javascript
{
    "percent": <volume percentage>,
    "muted": <true/false>
}
```

| Producer | Consumer |
| :--- | :--- |
|  | Enclosure \(skill-mark-2\) |

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
    self.bus.emit(Message('mycroft.volume.get.response',
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

| Producer | Consumer |
| :--- | :--- |
|  | Enclosure \(skill-mark-2\) |

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
    self.bus.emit(Message('mycroft.volume.duck'))
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

| Producer | Consumer |
| :--- | :--- |
|  | Enclosure \(skill-mark-2\) |

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
    self.bus.emit(Message('mycroft.volume.unduck'))
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

```javascript
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
    self.bus.emit(Message('mycroft.skill.handler.start',
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
    self.bus.emit(Message('mycroft.skill.handler.complete'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skill.handler.complete'
```
{% endtab %}
{% endtabs %}

### mycroft.skill.enable\_intent

Enable disabled intent

**Data:**

```javascript
{"intent_name": "name"}
```

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft/skills/core.py` |

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
    self.bus.emit(Message('mycroft.skill.enable_intent',
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

### mycroft.skill.disable\_intent

Disable intent

**Data:**

```javascript
{"intent_name": "name"}
```

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft/skills/core.py` |

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
    self.bus.emit(Message('mycroft.skill.disable_intent',
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

```javascript
{
    "id": <skill ID>,
    "name": <skill name>,
    "path": <skill directory>,
    "modified": <modified time>
}
```

| Producer | Consumer |
| :--- | :--- |
| `skills/main.py` | `mycroft/skills/intent_service.py` |

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
    self.bus.emit(Message('mycroft.skills.loaded',
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

### mycroft.skills.loading\_failure

A Skill has failed to load

**Data:**

```javascript
{
    "id": <skill ID>,
    "folder": <skill directory>
}
```

| Producer | Consumer |
| :--- | :--- |
| `skills/main.py` |  |

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
    self.bus.emit(Message('mycroft.skills.loading_failure',
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

```javascript
{
    "id": <skill ID>,
    "folder": <skill directory>
}
```

| Producer | Consumer |
| :--- | :--- |
| `skills/main.py` |  |

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
    self.bus.emit(Message('mycroft.skills.shutdown',
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

| Producer | Consumer |
| :--- | :--- |
| `mycroft/skills/skill_manager.py` | `mycroft/skills/padatious_service.py` |

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
    self.bus.emit(Message('mycroft.skills.initialized'))
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

List of loaded skills \(response to 'skillmanager.list'\)

**Data:**

```javascript
{"skills": [<list of skill IDs>] }
```

| Producer | Consumer |
| :--- | :--- |
| `skills/main.py` |  |

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
    self.bus.emit(Message('mycroft.skills.list',
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

| Producer | Consumer |
| :--- | :--- |
| Configuration Skill | `mycroft/skills/settings.py` |

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
    self.bus.emit(Message('mycroft.skills.settings.update'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'mycroft.skills.settings.update'
```
{% endtab %}
{% endtabs %}

## Mycroft Skill Manager \(MSM\)

### msm.updating

MSM install has begun

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.updating'))
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

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.installing'))
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

```javascript
{ "skill" : <skill name> }
```

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.install.succeeded',
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

```javascript
{
    "skill" : <skill name>,
    "error": <error code>
}
```

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.install.failed',
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

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.installed'))
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

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.updated'))
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

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.removing'))
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

```javascript
{ "skill" : <skill name> }
```

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.remove.succeeded',
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

```javascript
{
    "skill" : <skill name>,
    "error": <error code>
}
```

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.remove.failed',
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

| Producer | Consumer |
| :--- | :--- |
| `msm.sh` | `skills/main.py` |

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
    self.bus.emit(Message('msm.removed'))
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

Deactivate a skill. Activate by typing ":deactivate " in the CLI

**Data:**

```javascript
{'skill': <skill directory name>}
```

| Producer | Consumer |
| :--- | :--- |
| CLI \(`client/text/main.py`\) | `skills/skill_manager.py` |

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
    self.bus.emit(Message('skillmanager.deactivate',
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

List installed skills. Activate by typing ":list" in the CLI

| Producer | Consumer |
| :--- | :--- |
| CLI \(`client/text/main.py`\) | `skills/skill_manager.py` |

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
    self.bus.emit(Message('skillmanager.list'))
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

| Producer | Consumer |
| :--- | :--- |
|  | `skills/main.py` |

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
    self.bus.emit(Message('skillmanager.update'))
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

| Producer | Consumer |
| :--- | :--- |
| `messagebus\client\ws.py` |  |

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
    self.bus.emit(Message('open'))
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

| Producer | Consumer |
| :--- | :--- |
| `messagebus\client\ws.py` |  |

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
    self.bus.emit(Message('close'))
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

| Producer | Consumer |
| :--- | :--- |
| `messagebus\client\ws.py` |  |

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
    self.bus.emit(Message('reconnecting'))
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

### system.wifi.setup

Kick off a a wifi-setup session

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft-wifi-setup: mycroft_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.wifi.setup',
                   self.handler_system_wifi_setup)

def handler_system_wifi_setup(self, message):
    # code to excecute when system.wifi.setup message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.wifi.setup'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.wifi.setup'
```
{% endtab %}
{% endtabs %}

### system.wifi.reset

Clear the saved wifi settings

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft-wifi-setup: mycroft_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.wifi.reset',
                   self.handler_system_wifi_reset)

def handler_system_wifi_reset(self, message):
    # code to excecute when system.wifi.reset message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.wifi.reset'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.wifi.reset'
```
{% endtab %}
{% endtabs %}

### system.ntp.sync

Force the system clock to synchronize with NTP servers

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft-wifi-setup: mycroft_admin_service.py` |

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
    self.bus.emit(Message('system.ntp.sync'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.ntp.sync'
```
{% endtab %}
{% endtabs %}

### system.ssh.enable

Configure system to allow SSH connections

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft-wifi-setup: mycroft_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.ssh.enable',
                   self.handler_system_ssh_enable)

def handler_system_ssh_enable(self, message):
    # code to excecute when system.ssh.enable message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.ssh.enable'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.ssh.enable'
```
{% endtab %}
{% endtabs %}

### system.ssh.disable

Configure system to block SSH connections

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft-wifi-setup: mycroft_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in MycroftSkill" %}
```python
...
def initialize(self):
    self.add_event('system.ssh.disable',
                   self.handler_system_ssh_disable)

def handler_system_ssh_disable(self, message):
    # code to excecute when system.ssh.disable message detected...
...
```
{% endtab %}

{% tab title="Generating Message from MycroftSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.ssh.disable'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'system.ssh.disable'
```
{% endtab %}
{% endtabs %}

### system.reboot

Force a Linux reboot

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft-wifi-setup: mycroft_admin_service.py` |

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
    self.bus.emit(Message('system.reboot'))
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

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft-wifi-setup: mycroft_admin_service.py` |

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
    self.bus.emit(Message('system.shutdown'))
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

Force an apt-get update on 'mycroft-mark-1' or 'mycroft-picroft' package \(as appropriate\)

| Producer | Consumer |
| :--- | :--- |
|  | `mycroft-wifi-setup: mycroft_admin_service.py` |

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
    self.bus.emit(Message('system.update'))
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

```javascript
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
    self.bus.emit(Message('play:query',
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

There are three responses to a `play:query`. These are not intended to be consumed directly by a Skill, see the methods available in the CommonPlaySkill Class.

#### Confirm Search

The initial response confirms that a search is being attempted. It also extends the Skill timeout while it looks for a match.

**Data:**

```javascript
{
  "phrase": search_phrase,
  "skill_id": self.skill_id,
  "searching": True
}
```

#### Search Result

Emitted if a result is found. Responses from the Play services must be received within 1 second to be included.

**Data:**

```javascript
{
    "phrase": phrase,
    "skill_id":  self.skill_id,
    "callback_data": data,
    "service_name": self.spoken_name,
    "conf": confidence
}
```

* `phrase` - the phrase that was queried for this response
* `id` - uniquely identifies the skill, normally the Skill's `self.skill_id`
* `callback_data` - optional data structure to return in `play:start`
* `service_name` - the name of the service returning the highest confidence in a speakable format
* `conf` - the confidence it can handle the request, between 0.0 and 1.0

Confidence guidelines:

* 1.0 = exact command match, e.g. "play npr news"
* &gt;0.9 = multi-key match for database entry, e.g. "play madonna's lucky star" or "play artist madona" \(matches "artist" and "madonna"\). For each additional key over 2, add 0.1 to the confidence, so "play madonna's lucky star on spotify" would be 0.91 for three keywords
* &gt;0.8 = single-key match for database title entry, e.g. "play lucky star"
* &gt;0.7 = single-key match for database artist or group, e.g. "play madonna"
* &gt;0.6 = single-key match for database genre or category, e.g. "play reggae"
* &gt;0.5 = generic match, e.g. "play some music" or "play a movie"

#### Search Failed

No suitable result was found.

**Data:**

```javascript
{
  "phrase": search_phrase,
  "skill_id": self.skill_id,
  "searching": False
}
```

### play:start

* skill\_id -- the unique ID of the skill that is being invoked
* phrase -- the original phrase user said, e.g. "some thing" from utterance "play some thing"
* callback\_data -- \(optional\) data the skill can use to start playback

**Data:**

```javascript
{
    "skill_id": <skill_id>,
     "phrase": phrase,
     "callback_data": optional_data
}
```

## Common Query System

### question:query

**Data:**

```javascript
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
    self.bus.emit(Message('question:query',
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

* skill\_id -- the unique ID of the skill that is being invoked
* phrase -- the original phrase user said, e.g. "some thing" from utterance "how tall was abraham lincoln"
* conf -- confidence level of answers validity
* callback\_data -- \(optional\) data the skill can use for any additional actions \(such as image url or similar\)
* searching -- true if more time is needed to complete the search, otherwise false

**Data:**

```javascript
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
    self.bus.emit(Message('question:query.response',
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

* skill\_id -- the unique ID of the skill that is being invoked
* phrase -- the original phrase user said, e.g. "some thing" from utterance "how tall was abraham lincoln"
* callback\_data -- \(optional\) data the skill can use to take additional actions

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
    self.bus.emit(Message('question:action'))
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

### private.mycroftai.has\_alarm

Count of running alarms \(0 == no alarms\)

**Data:**

```javascript
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
    self.bus.emit(Message('private.mycroftai.has_alarm',
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

### skill.namespace.\*

e.g. "skill.mycroft.noftify.alarm\_changed" or "skill.jaguar.notify.car\_stopped"

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
    self.bus.emit(Message('skill.namespace.*'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'skill.namespace.*'
```
{% endtab %}
{% endtabs %}

### private.github\_username.\*

for private \(not intended to be used by anyone else\)

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
    self.bus.emit(Message('private.github_username.*'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m mycroft.messagebus.send 'private.github_username.*'
```
{% endtab %}
{% endtabs %}

