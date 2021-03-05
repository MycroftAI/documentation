---
Description: TTS plugins handles converting Text to Speech
---

# TTS Plugins

All Mycroft TTS plugins need to define a class based on the TTS base class from mycroft.tts

```python
from mycroft.tts import TTS

class myTTS(TTS):
    def __init__(self, lang, config):
        super().__init__(lang, config, validator, audio_ext='wav',
                         phonetic_spelling=False, ssml_tags=None)
        # Any specific init code goes here
```

The `super()` call does some setup adding specific options to how Mycroft will preprocess the sentence.

* `audio_ext`: filetype of output, possible options 'wav' and 'mp3'.
* `phonetec_spelling`, True if Mycroft should preprocess some difficult to pronounce words \(eg spotify\) or provide the raw text to the TTS.
* `ssml_tags`: list of valid SSML tags for the TTS if any, otherwise None.
* `validator`: a special class that verifies that the TTS is working in the current configuration.

It also registers the module's config from the [Mycroft configuration](../../../using-mycroft-ai/customizations/config-manager.md) in `self.config` as well as the current language in `self.lang`

For the following config snippet

```javascript
  "tts": {
    "module": "example_tts",
    "example_tts": {
      ...
    }
  }
```

Mycroft will register the `"example_tts"` part in the TTS's `self.config`

## `get_tts()`

The `get_tts()` method will be called by Mycroft to generate audio and \(optionally\) phonemes. This is the main method that the plugin creator needs to implement. It is called with:

* `sentence` \(str\): a piece of text to turn into audio.
* `wav_file` \(str\): where the plugin should store the generated audio data.

This method should generate audio data and return a Tuple `(wav_file, visemes)`:

* `wav_file` \(str\): path to written data \(generally the input argument\)
* `visemes` \(list\): viseme list for synthesized audio

As an example see the [`get_tts` method for Mimic2](https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/tts/mimic2_tts.py#L225).

## TTS Validator

To check if the TTS can be used, a validator class is needed. This should inherit from `mycroft.tts.TTSValidaor`. It will be called with the TTS class as argument and will store it in `self.tts`.

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

## Entry point

To make the class detectable as an TTS plugin, the package needs to provide an entry point under the `mycroft.plugin.tts` namespace.

```python
setup([...],
      entry_points = {'mycroft.plugin.tts': 'example_tts = my_tts:myTTS'}
      )
```

Where `example_tts` is is the TTS module name for the plugin, `my_tts` is the Python module and `myTTS` is the class in the module to return.

