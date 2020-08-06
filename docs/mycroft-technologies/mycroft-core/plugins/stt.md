---
Description: STT plugins handles converting Speech to Text
---
# Speech To Text plugin

All Mycroft Speech to Text plugins need to provide a class derived from the STT base class in `mycroft.stt`

When the `__init__()` method of the base class is run the config for it will be loaded, and available through `self.config` Mycroft's selected language will also be available through `self.lang`

So for example

```json
  "stt": {
    "module": "example_stt"
    "example_stt": {
      "server": "https://my_server.com",
      "samplerate": 16000
    }
  }
```

will load the the `"example_stt"` structure from the `"stt"` section and provide that in `self.config`.

### execute()

The STT plugin class needs to define the execute() method taking audio as an argument with lang as an optional parameter (currently not used in core.

The audio argument is an [AudioData](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#audiodataframe_data-bytes-sample_rate-int-sample_width-int---audiodata) object.

The bare minimum STT class will look something like

```python

class MySTT(STT):
    def execute(audio, language=None):
        # Handle audio data and return transcribed text
        [...]
        return text
```

### STT base class

The stt system has a couple of base classes specified,

#### `STT`

The base STT, this handles the audio in "batch mode" taking a complete sentence in the audio, and from it generates speech.

#### `StreamingSTT`

A more advanced STT class for streaming data to the STT. This will recieve chunks of audio data as they become available and streaming them to an STT engine.

The plugin author needs to implement the `create_streaming_thread()` method creating a thread for handling data sent through `self.queue`. The thread this method creates should be based on the [StreamThread class](https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/stt/__init__.py#L325) and `handle_audio_data()` method needs to be implemented.

### Entry point

To make the class detectable as an STT plugin, the package needs to provide an entry point under the `mycroft.plugin.stt` namespace.

```python
setup([...],
      entry_points = {'mycroft.plugin.stt': 'example_stt = my_stt:mySTT'}
      )
```

Where `example_stt` is is the STT module name for the plugin, my_stt is the python module and mySTT is the class in the module to return.
