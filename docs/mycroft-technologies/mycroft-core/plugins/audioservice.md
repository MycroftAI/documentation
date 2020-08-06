---
Description: Audioservice Backend  plugins handles playing and queuing audio files.
---
# Audioservice Backend plugin

An audio service adds an interface to a media player allowing Mycroft to play new types of media files or on remote devices.

## AudioBackend
The audioservice creator needs implement a class derived from `AudioBackend` found in `mycroft.audio.service`. This class implements all basic commands and will be called by mycroft. For complete specification see the [docstrings](https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/audio/services/__init__.py) for the class.

Apart from all the play / pause / etc. commands it's there are a couple of important methods to mention.

The `supported_uris()` method this is used to deterine if the service backend can handle the given uri-type (https://, file://, etc). A basic implementation will return an iterable with uri types: `('file', 'http', 'https')`

The playlist handling methods `clear_list()` and `add_list()`, of which the first removes all items from the current list and the second _appends_ a list of uri's to the list.

### RemoteAudioBackend

If the audio backend that's implemented plays media on another device than the one Mycroft is running on this base class should be used. it's mainly used to sort generic playback queries defaulting to a local audio backend unless otherwise specified.

## Instantiation

An audioservice can instanciate a number of backend objects so an instanciation function called `load_service()` needs to exist in the module. It will be called with the mycroft audio configuration and a connection to the messagebus. The method should return an tuple with audio backends included in the file.

The basic layout of a plugin will be something like

```python
from mycroft.audio.service import AudioBackend

class MyAudioBackend(AudioBackend)
    #lots of implementation here
    [...]


def load_service(config, bus):
    return (MyAudioBackend(config, bus), )
```

The `load_service()` function can also be used to scan the local network for things like chromecasts and create an audioservice backend for each found device.

### Entry point

To make the audioservice detectable as an Audioserice backend plugin, the package needs to provide an entry point under the `mycroft.plugin.audioservice` namespace.

```python
setup([...],
      entry_points = {'mycroft.plugin.audioservice': 'example_audiobackend = my_audiobackend'}
      )
```

Where `example_audiobackend` is is the audio service module name for the plugin, my_audiobackend will be the audioservice module containing the `load_service()`function.

Note that this differs a fair bit from the TTS and STT which points to a single class.
