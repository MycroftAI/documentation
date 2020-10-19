# Wake Word Plugins

All Mycroft Wake Word Plugins need to provide a class derived from the HotWordEngine base class in `mycroft.client.speech.hotword_factory`

When the `__init__()` method of the base class is run the config for that module will be loaded and available through `self.config`. Mycroft's selected language will also be available through `self.lang`.

For example, the following [Mycroft configuration](../../../using-mycroft-ai/customizations/config-manager.md):

```javascript
{
  "listener": {
    "wake_word": "my wake word",
  },
  "hotwords": {
    "my wake word": {
      "module": "example_wake_word_plugin",
      "custom_attribute": "some value"
    }
  }
}
```

will load the `"my wake word"` structure from the `"hotwords"` section using the `"example_wake_word_plugin"` . The defined `custom_attribute` will then be available within my plugin on `self.config`

### found\_wake\_word\(\)

Each Wake Word plugin must define the `found_wake_word()` method taking one argument:

* `frame_data` - this is the audio data that needs to be checked for a wake word. You can process audio here or return a result previously handled in the `update()` method.

### update\(\)

The `update()` method is optional and takes one argument:

* `chunk` - live audio chunks allowing for streaming predictions. Results must be returned in the `found_wake_word()` method.

### stop\(\)

The `stop()` method is optional and takes no arguments. It should be used to perform any actions needed to shut down the hot word engine. This may include things such as unloading data or to shutdown external processes.

## Entry point

To make the class detectable as a Wake Word plugin, the package needs to provide an entry point under the `mycroft.plugin.wake_word` namespace.

```python
setup([...],
      entry_points = {'mycroft.plugin.wake_word': 'example_wake_word_plugin = my_example_ww:myWakeWordEngine'}
      )
```

Where: 

* `example_wake_word_plugin` is the Wake Word module name for the plugin
* `my_example_ww` is the Python module; and
* `myWakeWordEngine` is the class in the module to return

