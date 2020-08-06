---
description: >-
Mycroft plugins allows developers to create and distribute new features for 
some of mycroft's main systems.
---

## Mycroft plugins

The plugins extend Mycroft, adding support for new Speech engines, software to play media files, etc.. The idea is that the community shall be able to build and publish plugins extending Mycroft and adding support for new things without the need to bundle the code inside Mycroft-core. This gives the creator freedom to make updates in their own pace without needing to wait for a Mycroft core developer to verify their code contribution (and then wait for the next release).

### Pluggable systems

The plugins are normal pip-installable python modules specifying specially named "entry points". The entry points are a python packaging mechanism for creating common api's and making them discoverable. For more info see the [Python Packaging Guide](https://packaging.python.org/guides/creating-and-discovering-plugins/)

Mycroft supports plugins for

- [Speech to Text (STT)](stt.md)
- [Text to Speech (TTS)](tts.md)
- [Audioservice backends](audioservice.md)

Entry point types
 - TTS Plugin: `mycroft.plugin.tts`
 - STT Plugin: `mycroft.plugin.stt`
 - Audioservice Plugin `mycroft.plugin.audioservice`

### Plugin setup.py

A pip installable package always contain a setup.py file with install instructions, this will not be described in detail on this page but python-packaging has a [great guide](https://python-packaging.readthedocs.io/en/latest/).

To make a plugin discoverable an `entry_point` must be added to the setup call in setup.py

```python
entry_ponts={'entrypoint type': 'my_plugin_name' = 'my_module.myPluginClass'
```
`my_plugin_name` will be the module identifier that can be used in the configuration to reference a plugin, and that will refer to the class (or module) specified by the string to the right of the equal sign. In the example above it will refer to the `myPluginClass` in the module `my_module`

A complete setup.py example:

```python
#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'example_plug = mycroft_example_plugin:ExamplePlugin'
setup(
    name='mycroft-example-plugin',
    version='1',
    description='A tts plugin for mycroft',
    author='Mike Roft',
    author_email='mike@email.com',
    packages=['mycroft_example_plugin'],
    keywords='mycroft plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
```

This will add a tts module called *example_plug* which will refer to a TTS class called `ExamplePlugin` in the module `mycroft_example_plugin`.

In the config this will be selected by setting the tts module to `example_plug`.

```json
  "tts": {
    "module": "example_plug"
  }
```

A complete example plugin re-implementing google TTS can be found [here](https://github.com/forslund/mycroft-tts-plugin-gtts) and a template for creating the setup.py can be found [here](https://gist.github.com/forslund/8e51cba0ffd4e671dfc188e4e33fdbd7).
