---
Description: Audioservice Backend plugins handles playing and queuing audio files.
description: >-
  An Audioservice Backend plugin adds an interface to a media player allowing
  Mycroft to play new types of media files or on remote devices.
---

# Audioservice Plugins

## AudioBackend

Each Audioservice plugin must implement a class derived from `AudioBackend` found in `mycroft.audio.service`. This class implements all basic commands and will be called by Mycroft. For complete specification see the [docstrings](https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/audio/services/__init__.py) for the class.

Apart from the expected commands \(`play`, `pause`, etc\), there are a couple of important methods to mention.

The `supported_uris()` method this is used to determine if the service backend can handle the given uri-type \(https://, file://, etc\). A basic implementation will return an iterable with uri types: `('file', 'http', 'https')`

The playlist handling methods `clear_list()` and `add_list()`, of which the first removes all items from the current list, and the second _appends_ a list of uri's to the list.

### RemoteAudioBackend

If the audio backend that is implemented plays media on another device than the one Mycroft is running on this base class should be used. It is mainly used to sort generic playback queries defaulting to a local audio backend unless otherwise specified.

## Instantiation

An audioservice can instantiate a number of backend objects so an instantiation function called `load_service()` needs to exist in the module. It will be called with the Mycroft audio configuration and a connection to the messagebus. The method should return a tuple with audio backends included in the file.

The `load_service()` function can also be used to scan the local network for things like chromecast and create an audioservice backend for each found device.

The basic layout of an Audioservice Plugin will be:

```python
from mycroft.audio.service import AudioBackend

class MyAudioBackend(AudioBackend)
    #lots of implementation here
    [...]


def load_service(config, bus):
    return (MyAudioBackend(config, bus), )
```

Example Audioservices can be found [here](https://github.com/MycroftAI/mycroft-core/tree/97ff8a4708cb91dd6661091e935c46753f2aa4d9/mycroft/audio/services).

### Entry point

To make the audioservice detectable as an Audioservice Backend Plugin, the package needs to provide an entry point under the `mycroft.plugin.audioservice` namespace.

```python
setup([...],
      entry_points = {'mycroft.plugin.audioservice': 'example_audiobackend = my_audiobackend'}
      )
```

Where `example_audiobackend` is the audio service module name for the plugin, `my_audiobackend` will be the audioservice module containing the `load_service()` function.

Note that this differs a fair bit from the TTS and STT Plugin entry points that point to a single class.

