---
Description: TTS plugins handles converting Text to Speech
---
## Creating a Mycroft TTS

All mycroft TTS plugins need to define a class based on the TTS base class from mycroft.tts

```python
from mycroft.tts import TTS

class myTTS(TTS):
    def __init__(self, lang, config):
        super().__init__(lang, config, validator, audio_ext='wav',
                         phonetic_spelling=False, ssml_tags=None)
        # Any specific init code goes here

```

The `super()` call does some setup adding specific options to how mycroft will preprocess the sentence.

- `audio_ext`: filetype of output, possible options 'wav' and 'mp3'
- `phonetec_spelling`, True if Mycroft should preprocess some difficult to pronounce words (ex spotify) or provide the raw text to the tts.
- `ssml_tags`: list of valid SSML tags for the TTS if any, otherwise None
- validator a special class that verifies that the TTS is working in the current configuration.

It also regisers the module's config from the mycroft configuration in `self.config` as well as the current language in `self.lang`

For the following config snippet

```json
  "tts": {
    "module": "example_tts",
    "example_tts": {
      ...
    }
  }
```

Mycroft will register the `"example_tts"` part in the TTS's `self.config`

### `get_tts()`

The `get_tts()` method will be called by Mycroft to generate audio and (optionally) phonemes. This is the main method that the plugin creator needs to implement.

It's called with a `sentence`, a piece of text to turn into audio, and a `wav_file` an path to where Mycroft would like to store the generated audio data.

This method should generate audio data and return a Tuple (path to written data (generally the input argument), phoneme list).

As an example see the [get_tts for mimic2](https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/tts/mimic2_tts.py#L225)

### TTS Validator

To check if the TTS can be used a validator class is needed, this should inherit from `mycroft.tts.TTSValidaor`. It will be called with the TTS class as argument and will store it in `self.tts`.

The following is the bare minimum implementation:

```python
class MyValidator(TTSValidator):
    def get_tts_class(self):
        # Should return a reference to the TTS class it's inteded to validate.

    def validate_lang(self):
        # Raise exception if `self.tts.lang` is not supported.

    def validate_connection(self):
        # Check that the software needed for the TTS is reachable,
        # be it a local executable, python module or remote server and
        # if not available raise an exception.
```

### Entry point

To make the class detectable as an TTS plugin, the package needs to provide an entry point under the `mycroft.plugin.tts` namespace.

```python
setup([...],
      entry_points = {'mycroft.plugin.tts': 'example_tts = my_tts:myTTS'}
      )
```

Where example_tts is is the TTS module name for the plugin, my_tts is the python module and myTTS is the class in the module to return.
