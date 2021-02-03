---
description: >-
  Mycroft stores file in various locations which can be changed by the user using some environment variables
---

# XDG Base directory specification

Mycroft follows the [Freedesktop XDG Base directory specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).
This means that files and folders aren't stored to a single directory, but split out to several directories depending on their function.
It also means that although there are default locations, they can be modified by the user using environment variables if they so desire.

By default the directories used are:

- `$XDG_CONFIG_HOME/mycroft` for configuration
- `$XDG_DATA_HOME/mycroft` for persistent data storage
- `$XDG_CACHE_HOME/mycroft` for non-essential data

These variables can be set to anything the user desires and Mycroft will automatically change where it's stores it's data and configuration.
Previously Mycroft used to store everything under `$HOME/.mycroft` which can be replicated quite easily if so desired:

```bash
export XDG_CONFIG_HOME=$HOME/.mycroft
export XDG_DATA_HOME=$HOME/.mycroft
export XDG_CACHE_HOME=$HOME/.mycroft
```

If the above mentioned variables don't exist, which will be the case for the majority of people, Mycroft will use the following default values:

- `$HOME/.config/mycroft` for configuration
- `$HOME/.local/share/mycroft` for persistent data storage
- `$HOME/.cache/mycroft` for non-essential data

These default values are used in the Mycroft documentation, but can as mentioned be changed to the XDG variables.
