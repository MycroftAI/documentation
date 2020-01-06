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

{% tabs %}
{% tab title="Description" %}
Request to speak utterance
{% endtab %}

{% tab title="Data" %}
```
{"utterance": "words to be spoken", "lang": "en-us"}
```
{% endtab %}
{% endtabs %}

### mycroft.internet.connected

{% tabs %}
{% tab title="Description" %}
Internet connection is now available (only generated on initial connection)
{% endtab %}
{% endtabs %}

### mycroft.ready

{% tabs %}
{% tab title="Description" %}
Sent by start-up sequence when everything is ready for user interaction
{% endtab %}

{% tab title="Producer" %}
`skills/padatious_service.py`
{% endtab %}

{% tab title="Consumer" %}
Pairing Skill
{% endtab %}
{% endtabs %}

### mycroft.stop

{% tabs %}
{% tab title="Description" %}
Stop command (e.g. button pressed)
{% endtab %}
{% endtabs %}

### mycroft.not.paired

{% tabs %}
{% tab title="Description" %}
Start the pairing process when this event is emitted.
{% endtab %}

{% tab title="Producer" %}
Pairing Skill
Weather Skill
Wolfram Alpha Skill
{% endtab %}

{% tab title="Consumer" %}
Pairing Skill
{% endtab %}
{% endtabs %}

### mycroft.paired

{% tabs %}
{% tab title="Description" %}
Pairing has completed
{% endtab %}

{% tab title="Producer" %}
Pairing Skill
{% endtab %}

{% tab title="Consumer" %}
```
skills/skill_manager.py
enclosure/mark1/__init__.py
enclosure/generic/__init__.py
client/speech/__main__.py
```
{% endtab %}
{% endtabs %}

### mycroft.awoken

{% tabs %}
{% tab title="Description" %}
Has come out of sleep mode
{% endtab %}
{% endtabs %}

### mycroft.debug.log

{% tabs %}
{% tab title="Description" %}
Log `level` can be:
- CRITICAL
- ERROR
- WARNING
- INFO
- DEBUG

These correspond to the Python logging object.

The `bus` parameter allows turning the logging of all bus messages on/off.
{% endtab %}

{% tab title="Data" %}
```
{
   ""level"" : <log level>,
   ""bus"": <True/False>
}
```
{% endtab %}
{% endtabs %}

### mycroft.eyes.default

{% tabs %}
{% tab title="Description" %}
Change eyes to default color
{% endtab %}

{% tab title="Consumer" %}
mycroft-mark-1
{% endtab %}
{% endtabs %}

### complete_intent_failure

{% tabs %}
{% tab title="Description" %}
Intent processing failed
{% endtab %}
{% endtabs %}

### configuration.updated

{% tabs %}
{% tab title="Description" %}
Notification to services that the configuration has changed and needs reloaded
{% endtab %}
{% endtabs %}

## Recognizer

### recognizer_loop:wakeword

{% tabs %}
{% tab title="Description" %}
Wakeword was heard
{% endtab %}

{% tab title="Data" %}
```
{
    "utterance": <wakeword heard>,
    "session": <session ID>,
}
```
{% endtab %}

{% tab title="Producer" %}
`client/speech/main.py`
{% endtab %}
{% endtabs %}

### recognizer_loop:record_begin

{% tabs %}
{% tab title="Description" %}
Recording has started
{% endtab %}

{% tab title="Producer" %}
`client/speech/main.py`
{% endtab %}
{% endtabs %}

### recognizer_loop:record_end

{% tabs %}
{% tab title="Description" %}
Recording has ended
{% endtab %}

{% tab title="Producer" %}
`client/speech/main.py`
{% endtab %}
{% endtabs %}

### recognizer_loop:utterance

{% tabs %}
{% tab title="Description" %}
STT has detected the given text or text was injected as an utterance via the CLI.
{% endtab %}

{% tab title="Data" %}
```
{
    "utterances": [text],
    "lang": self.stt.lang,
    "session": session_id
}
```
{% endtab %}

{% tab title="Producer" %}
```
client/speech/__main__.py
client/speech/listener.py
client/text/text_client.py
skills/__main__.py
```
{% endtab %}

{% tab title="Consumer" %}
```
client/text/text_client.py
messagebus/client/client.py
skills/intent_service.py
```
{% endtab %}
{% endtabs %}

### recognizer_loop:audio_output_start

{% tabs %}
{% tab title="Description" %}
Text output (TTS) has started
{% endtab %}

{% tab title="Producer" %}
`audio/speech.py`
{% endtab %}
{% endtabs %}

### recognizer_loop:audio_output_end

{% tabs %}
{% tab title="Description" %}
Text output (TTS) has ended
{% endtab %}

{% tab title="Producer" %}
`audio/speech.py`
{% endtab %}
{% endtabs %}

### recognizer_loop:sleep

{% tabs %}
{% tab title="Description" %}
Go into "sleep" mode.  Everything except "Hey Mycroft, wake up" will be ignored.
{% endtab %}
{% endtabs %}

### recognizer_loop:wake_up

{% tabs %}
{% tab title="Description" %}
Come out of "sleep" mode.
{% endtab %}
{% endtabs %}

## Microphone Behavior

### mycroft.mic.listen

{% tabs %}
{% tab title="Description" %}
Begin recording for STT processing
{% endtab %}
{% endtabs %}

### mycroft.mic.mute

{% tabs %}
{% tab title="Description" %}
Turn off the mic (no wakeword or STT processing)
{% endtab %}

{% tab title="Producer" %}
Pairing Skill
{% endtab %}

{% tab title="Consumer" %}
`client/speech/main.py`
{% endtab %}
{% endtabs %}

### mycroft.mic.unmute

{% tabs %}
{% tab title="Description" %}
Turn on the mic (enable wakeword and STT processing)
{% endtab %}

{% tab title="Producer" %}
Pairing Skill
{% endtab %}

{% tab title="Consumer" %}
`client/speech/main.py`
{% endtab %}
{% endtabs %}

## Audio Playback

### mycroft.audio.service.play

{% tabs %}
{% tab title="Description" %}
Start playback of tracklist
{% endtab %}

{% tab title="Producer" %}
`skills/audioservice.py`
playback-control
{% endtab %}

{% tab title="Consumer" %}
`audio/main.py`
{% endtab %}
{% endtabs %}

### mycroft.audio.service.stop

{% tabs %}
{% tab title="Description" %}
Stop playback
{% endtab %}

{% tab title="Producer" %}
`skills/audioservice.py`
playback-control
{% endtab %}

{% tab title="Consumer" %}
`audio/main.py`
{% endtab %}
{% endtabs %}

### mycroft.audio.service.pause

{% tabs %}
{% tab title="Description" %}
Pause playback (if supported)
{% endtab %}

{% tab title="Producer" %}
`skills/audioservice.py`
playback-control
{% endtab %}

{% tab title="Consumer" %}
`audio/main.py`
{% endtab %}
{% endtabs %}

### mycroft.audio.service.resume

{% tabs %}
{% tab title="Description" %}
Resume playback (if supported)
{% endtab %}

{% tab title="Producer" %}
`skills/audioservice.py`
playback-control
{% endtab %}

{% tab title="Consumer" %}
`audio/main.py`
{% endtab %}
{% endtabs %}

### mycroft.audio.service.next

{% tabs %}
{% tab title="Description" %}
Skip to next track
{% endtab %}

{% tab title="Producer" %}
`skills/audioservice.py`
playback-control
{% endtab %}

{% tab title="Consumer" %}
`audio/main.py`
{% endtab %}
{% endtabs %}

### mycroft.audio.service.prev

{% tabs %}
{% tab title="Description" %}
Skip to previous track
{% endtab %}

{% tab title="Producer" %}
`skills/audioservice.py`
playback-control
{% endtab %}

{% tab title="Consumer" %}
`audio/main.py`
{% endtab %}
{% endtabs %}

### mycroft.audio.service.track_info

{% tabs %}
{% tab title="Description" %}
Request track info from audio service
{% endtab %}

{% tab title="Producer" %}
`skills/audioservice.py`
playback-control
{% endtab %}

{% tab title="Consumer" %}
`audio/main.py`
{% endtab %}
{% endtabs %}

### mycroft.audio.service.track_info_reply

{% tabs %}
{% tab title="Description" %}
Reply to track info request
{% endtab %}

{% tab title="Producer" %}
`audio/main.py`
{% endtab %}

{% tab title="Consumer" %}
`skills/audioservice.py`
{% endtab %}
{% endtabs %}

### mycroft.audio.service.list_backends

{% tabs %}
{% tab title="Description" %}
Returns list of available backends.
{% endtab %}

{% tab title="Producer" %}
`skills/audioservice.py`
playback-control
{% endtab %}

{% tab title="Consumer" %}
`audio/main.py`
{% endtab %}
{% endtabs %}

## Volume Control

### mycroft.volume.increase

{% tabs %}
{% tab title="Description" %}
Enclosure Volume up
{% endtab %}

{% tab title="Data" %}
```
{"play_sound": True}
```
{% endtab %}

{% tab title="Producer" %}
`client/enclosure/__init__.py`
{% endtab %}

{% tab title="Consumer" %}
Volume Skill
{% endtab %}
{% endtabs %}

### mycroft.volume.decrease

{% tabs %}
{% tab title="Description" %}
Enclosure Volume down
{% endtab %}

{% tab title="Data" %}
```
{"play_sound": True}
```
{% endtab %}

{% tab title="Producer" %}
`client/enclosure/__init__.py`
{% endtab %}

{% tab title="Consumer" %}
Volume Skill
{% endtab %}
{% endtabs %}

### mycroft.volume.mute

{% tabs %}
{% tab title="Description" %}
Enclosure Volume muted
{% endtab %}

{% tab title="Data" %}
```
{"speak_message": True}
```
{% endtab %}

{% tab title="Producer" %}
skill-naptime
{% endtab %}

{% tab title="Consumer" %}
Volume Skill
{% endtab %}
{% endtabs %}

### mycroft.volume.unmute

{% tabs %}
{% tab title="Description" %}
Enclosure Volume unmuted
{% endtab %}

{% tab title="Data" %}
```
{"speak_message": True}
```
{% endtab %}

{% tab title="Producer" %}
skill-naptime
{% endtab %}

{% tab title="Consumer" %}
Volume Skill
{% endtab %}
{% endtabs %}

### mycroft.volume.set

{% tabs %}
{% tab title="Description" %}
Set enclosure volume (0.0 = no output, 1.0 = loudest possible)
{% endtab %}

{% tab title="Data" %}
```
{"percent": float}
```
{% endtab %}

{% tab title="Consumer" %}
Volume Skill
{% endtab %}
{% endtabs %}

### mycroft.volume.get

{% tabs %}
{% tab title="Description" %}
Request volume level
{% endtab %}
{% endtabs %}

### mycroft.volume.get.response

{% tabs %}
{% tab title="Description" %}

{% endtab %}

{% tab title="Data" %}
```
{
    "percent": <volume percentage>,
    "muted": <true/false>
}
```
{% endtab %}

{% tab title="Consumer" %}
Enclosure (skill-mark-2)
{% endtab %}
{% endtabs %}

### mycroft.volume.duck

{% tabs %}
{% tab title="Description" %}
Reduce the volume level temporarilly
{% endtab %}

{% tab title="Consumer" %}
Enclosure (skill-mark-2)
{% endtab %}
{% endtabs %}

### mycroft.volume.unduck

{% tabs %}
{% tab title="Description" %}
Restore the volume level
{% endtab %}

{% tab title="Consumer" %}
Enclosure (skill-mark-2)
{% endtab %}
{% endtabs %}
