---
description: >-
  Mycroft plugins allows developers to create and distribute new features for
  some of Mycroft's main systems.
---

# Plugins

## Mycroft plugins

Plugins extend the functionality of Mycroft without needing to modify the source code of Mycroft-core. They can be used to add support for new speech recognition or synthesis engines, or to provide additional audio backends to play media files.

The intention behind the plugin system is to allow the community to build and publish new functionality, adding support for new services and making Mycroft more easily customizable. The Mycroft Community has grown tremendously over the last few years and Mycroft is being used in many different ways. This gives developers the freedom to make updates at their own pace, without needing to wait for a Mycroft core developer to verify their code contribution \(and then wait for the next release\). It also helps to keep Mycroft-core light and flexible, not requiring everything for every system to be bundled into the one code base.

### Pluggable systems

The plugins are normal pip-installable python modules specifying specially named "entry points". The entry points are a python packaging mechanism for creating common api's and making them discoverable. For more info see the [Python Packaging Guide](https://packaging.python.org/guides/creating-and-discovering-plugins/)

Mycroft supports plugins for:

* [Speech to Text \(STT\)](stt.md)
* [Text to Speech \(TTS\)](tts.md)
* [Audioservice backends](audioservice.md)
* [Wake word engines](wake-word-plugins.md)

These are accessible at through the following entry point types:

* STT Plugin: `mycroft.plugin.stt`
* TTS Plugin: `mycroft.plugin.tts`
* Audioservice Plugin `mycroft.plugin.audioservice`
* Wake Word Plugin `mycroft.plugin.wake_word`

### Plugin setup.py

A pip installable package always contain a `setup.py` file with install instructions, this will not be described in detail on this page but python-packaging has a [great guide](https://python-packaging.readthedocs.io/en/latest/).

To make a plugin discoverable an `entry_point` must be added to the setup call in `setup.py`.

```python
entry_points={'entrypointtype': 'my_plugin_name = my_module.myPluginClass'
```

`my_plugin_name` will be the module identifier that can be used in the Mycroft configuration to reference a plugin. That plugin name will refer to the class \(or module\) specified by the string to the right of the equal sign. In the example above it will refer to the `myPluginClass` in the module `my_module`.

A complete `setup.py` example:

```python
#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'example_plug = mycroft_example_plugin:ExamplePlugin'
setup(
    name='mycroft-example-plugin',
    version='1',
    description='A TTS plugin for mycroft',
    author='Mike Roft',
    author_email='mike@email.com',
    packages=['mycroft_example_plugin'],
    keywords='mycroft plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
```

This will add a TTS module called _example\_plug_ which will refer to a TTS class called `ExamplePlugin` in the module `mycroft_example_plugin`.

In the config this will be selected by setting the tts module to `example_plug`.

```javascript
  "tts": {
    "module": "example_plug"
  }
```

A complete example plugin re-implementing Google TTS can be found [here](https://github.com/forslund/mycroft-tts-plugin-gtts). A template for creating the `setup.py` can be found [here](https://gist.github.com/forslund/8e51cba0ffd4e671dfc188e4e33fdbd7).

