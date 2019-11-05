---
description: A configuration file that contains the device and service settings.
---

# mycroft.conf

### What is `mycroft.conf`?

`mycroft.conf` is a [JSON](https://www.json.org/)-formatted file that is saved locally on your Mycroft **Device**, such as Picroft or Mark 1. `mycroft-conf` contains information about the **Device** itself, like what type of **Device** and **Enclosure** it is, as well as information about user preferences. If you haven't specified preferences, then `mycroft.conf` will contain some default values. Your **Device**, and **Skills** installed on your **Device**, use `mycroft.conf` to provide additional functionality.

### What is `mycroft_web_cache.json`?

`mycroft_web_cache.json` is is a [JSON](https://www.json.org/)-formatted file that is saved locally on your Mycroft **Device**, such as Picroft or Mark 1. `mycroft_web_cache.json` is a cached copy of the settings on your [home.mycroft.ai](https://home.mycroft.ai) account, such as your _Location_ \(which determines _Time Zone_\), which _Voice_ you have selected and your preference for _Measurements_ such as temperature and distance.

Both of these files are regularly used in troubleshooting, so it's useful to know what information they hold, and where they are stored on your **Device**.

### How are `mycroft.conf` and `mycroft_web_cache.json` updated?

When you update settings at [home.mycroft.ai](https://home.mycroft.ai), your **Device** will periodically pull them down. However, this may not be fast enough to do what you want to do. To refresh your `mycroft.conf` from [home.mycroft.ai](https://home.mycroft.ai), Speak:

> Hey Mycroft, update config

Mycroft will then pull the files down to your **Device**.

### Where is the `mycroft.conf` file stored?

The `mycroft.conf` file is stored in different locations on different **Devices**, including:

* `/etc/mycroft/mycroft.conf`
* `~/.mycroft/mycroft.conf`

Mycroft implements an order of precedence; settings at a User level override those at a System level.

### A look at the inside of `mycroft.conf`

Here is an example System level `mycroft.conf` from a Mark 1 **Device**:

```text
pi@mark_1:/etc/mycroft $ cat mycroft.conf
{
  "enclosure": {
    "platform": "mycroft_mark_1",
    "platform_build": 9,
    "port": "/dev/ttyAMA0",
    "rate": 9600,
    "timeout": 5,
    "update": true,
    "test": false
  },
  "VolumeSkill": {
    "default_level": 6,
    "min_volume": 0,
    "max_volume": 83
  }
}
```

{% hint style="info" %}
See a [list of all variables available within `mycroft.conf`](https://github.com/MycroftAI/mycroft-core/blob/master/mycroft/configuration/mycroft.conf)\`\`
{% endhint %}

### Where is the `mycroft_web_cache.json` file stored?

This file is stored at:

`/var/tmp/mycroft_web_cache.json`

on the **Device**.

### A look at the inside of `mycroft_web_cache.json`

Here is an example `mycroft_web_cache.json`. _NOTE: Your settings will be different._

```text
{
  "date_format": "DMY",
  "tts": {
    "google": {
      "created_at": 1504481866992,
      "updated_at": 1514794901075
    },
    "module": "mimic",
    "fatts": {
      "created_at": 1504481866991,
      "updated_at": 1514794900939
    },
    "mimic": {
      "created_at": 1504481866989,
      "voice": "ap",
      "updated_at": 1514794900809
    },
    "espeak": {
      "created_at": 1504481866987,
      "updated_at": 1514794900679
    },
    "marytts": {
      "created_at": 1504481866986,
      "updated_at": 1514794900548
    }
  },
  "opt_in": true,
  "created_at": 1504481866955,
  "updated_at": 1514794898083,
  "listener": {
    "energy_ratio": 1.5,
    "created_at": 1504481866996,
    "updated_at": 1514794901398,
    "channels": 1,
    "sample_rate": 16000,
    "multiplier": 1,
    "threshold": 1e-90,
    "phonemes": "HH EY . M AY K R AO F T",
    "wake_word": "hey mycroft"
  },
  "time_format": "full",
  "skills": {
    "directory": "~/.mycroft/skills",
    "created_at": 1504481866994,
    "updated_at": 1514794901226,
    "stop_threshold": 2
  },
  "stt": {
    "google": {
      "credential": {
        "created_at": 1504481866970,
        "updated_at": 1514794899383
      },
      "created_at": 1504481866970,
      "updated_at": 1514794898989
    },
    "ibm": {
      "credential": {
        "created_at": 1504481866958,
        "updated_at": 1514794898334
      },
      "created_at": 1504481866958,
      "updated_at": 1514794898218
    },
    "mycroft": {
      "credential": {
        "created_at": 1504481866965,
        "updated_at": 1514794898856
      },
      "created_at": 1504481866965,
      "updated_at": 1514794898469
    },
    "module": "mycroft",
    "wit": {
      "credential": {
        "created_at": 1504481866981,
        "updated_at": 1514794900417
      },
      "created_at": 1504481866981,
      "updated_at": 1514794900031
    },
    "openstt": {
      "credential": {
        "created_at": 1504481866976,
        "updated_at": 1514794899900
      },
      "created_at": 1504481866976,
      "updated_at": 1514794899521
    }
  },
  "location": {
    "coordinate": {
      "latitude": -38.149918,
      "created_at": 1504500674753,
      "updated_at": 1504500674753,
      "longitude": 144.361719
    },
    "city": {
      "created_at": 1504500674710,
      "state": {
        "country": {
          "created_at": 1486125571309,
          "code": "AU",
          "name": "Australia",
          "updated_at": 1486125571309
        },
        "created_at": 1489950675941,
        "code": "VIC",
        "name": "Victoria",
        "updated_at": 1489950675941
      },
      "code": "Newtown",
      "name": "Newtown",
      "updated_at": 1504500674710
    },
    "created_at": 1504500674709,
    "updated_at": 1504500674709,
    "timezone": {
      "code": "Australia/Melbourne",
      "name": "Australian Eastern Standard Time (Victoria)",
      "dst_offset": 3600000,
      "created_at": 1489950676105,
      "updated_at": 1489950676105,
      "offset": 36000000
    }
  },
  "enclosure": {
    "created_at": 1504481866997,
    "rate": 9600,
    "updated_at": 1514794901541,
    "timeout": 5,
    "port": "/dev/ttyAMA0"
  },
  "system_unit": "metric"
}
```

## Advanced Configuration Options

### Changing your Wake Word

The Advanced Settings allow you to change the **Wake Word** that Mycroft responds to using the PocketSphinx listener. You might want to change the **Wake Word** to a phrase that's easier for you to speak, or more culturally appropriate.

First, choose the phrase that you wish to set as your **Wake Word**. For the purposes of this example, we're going to use the phrase:

`yo mike`

instead of

`hey mycroft`

We then need to identify the **phoneme** sounds for this **Wake Word** using the [CMU Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict).

`Y OW . M AY K .`

Remember that the period, or full stop, indicates the end of a word.

#### About Phonemes

Phonemes are basic units of sound. They are a way to represent the different sounds in speech in a standard way. English spelling varies so much that it cannot be used for this purpose. For example, the "j" sound in "juice" is the same as the "g" sound in "giant".

You can see the similarity when these words are written as phonemes:

* `JH UW S .` = juice
* `JH AY AH N T .` = giant

The period, or full stop, indicates the end of the word.

#### Other Settings

Other settings are available to further tune how sensitive the Speech to Text \(STT\) engine is in recognizing the **Wake Word**.

* **Sample rate \(Hz\)**: The rate at which the audio stream is sampled. The default is 16KHz. You shouldn't need to change this, unless the microphone you are using needs a much higher or lower sample rate.
* **Channels**: The audio channel that should be sampled for the **Wake Word**. The default is 1, and you shouldn't have to change this unless your microphone is not operating on audio channel 1.
* **Wake Word**: In plain English text, the Wake Word that Mycroft should listen for.
* **Phonemes**: The **phonemes** corresponding to the **Wake Word**. If your Wake Word phrase is more than one word, remember to include a period \(.\) at the end of each phoneme.
* **Threshold \(scientific notation\)**: The level of sensitivity at which the **Wake Word** should trigger Mycroft to respond. To _increase_ the sensitivity, _reduce_ the Threshold. The Threshold is given in [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation). Use this [handy converter](http://www.easysurf.cc/scintd.htm) to convert between decimal and scientific notation.
* **Threshold multiplier \(float\)**: This multiplier acts on the **Threshold**, and may be an easier way to make adjustments rather than scientific notation.
* **Dynamic Energy Ratio \(float\)**: Dynamic Energy Ratio \(DER\) is one signal feature used in [speech recognition](https://en.wikipedia.org/wiki/Speech_recognition) to identify characteristics of audio, such as whether a person has stopped or started speaking. DER is similar to signal-to-noise-ratio. A high ratio indicates a high difference in signal between speech and no speech, and a low ratio indicates a small difference in signal between speech and no speech.

If Mycroft is being _too sensitive_, reduce this value. If Mycroft _is not being sensitive enough_, increase this value.

#### Adding Wake Word Settings to `mycroft.conf`

For the "Yo Mike" example we started with, an example `~/.mycroft/mycroft.conf` file might look like:

```javascript
{
  "max_allowed_core_version": 19.2,
  "listener": {
    "wake_word": "yo mike",
    "threshold": 1e-18
  },
  "hotwords": {
    "yo mike": {
      "module": "pocketsphinx",
      "phonemes": "Y OW . M AY K ."
    }
  }
}
```

#### Telling Mycroft to pick up the new settings

Mycroft doesn't automatically fetch the new settings. You need to tell Mycroft to fetch the new settings by speaking

> Hey Mycroft, configuration update

Mycroft will then pull the new Settings configuration down.

