---
description: A configuration file that contains the device and service settings.
---

# mycroft.conf

{% hint style="info" %}
See a [list of all variables available within `mycroft.conf`](https://github.com/MycroftAI/mycroft-core/blob/master/mycroft/configuration/mycroft.conf)
{% endhint %}

## What is `mycroft.conf`?

`mycroft.conf` is a [JSON](https://www.json.org)-formatted file that is saved locally on your Mycroft Device, such as Picroft or Mark 1. The `mycroft.conf` file contains information about the Device itself, like what type of Device and Enclosure it is, as well as information about user preferences. If you haven't specified preferences, then `mycroft.conf` will contain some default values. Your Device, and Skills installed on your Device, use `mycroft.conf` to provide additional functionality.

## Where are the `mycroft.conf` files stored?

The `mycroft.conf` files are stored in four possible locations:

1. Default - mycroft-core/mycroft/configuration/mycroft.conf
2. Remote (from Home.Mycroft.ai) - /var/tmp/mycroft\_web\_cache.json
3. System - /etc/mycroft/mycroft.conf
4. User - $HOME/.mycroft/mycroft.conf

Mycroft implements an order of precedence; settings defined at a User level override those at a System level. If the file does not exist, Mycroft moves to the following level.

## A look at the inside of `mycroft.conf`

Here is an example System level `mycroft.conf` from a Mark 1 Device:

```
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

## `mycroft_web_cache.json`

`mycroft_web_cache.json` is is a [JSON](https://www.json.org)-formatted file that is saved locally on your Mycroft Device, such as Picroft or Mark 1. `mycroft_web_cache.json` is a cached copy of the settings on your [home.mycroft.ai](https://home.mycroft.ai) account, such as your _Location_ (which determines _Time Zone_), which _Voice_ you have selected and your preference for _Measurements_ such as temperature and distance.

Both of these files are regularly used in troubleshooting, so it's useful to know what information they hold, and where they are stored on your Device.

### Where is the `mycroft_web_cache.json` file stored?

This file is stored at:

`/var/tmp/mycroft_web_cache.json`

on the Device.

### How is `mycroft_web_cache.json` updated?

When you update settings at [home.mycroft.ai](https://home.mycroft.ai), your Device will periodically pull them down. In normal circumstances any change should be reflected on the device within 1-2 minutes. You can also instruct your device to pull down the latest configuration, by saying:

> Hey Mycroft, update configuration

Mycroft will respond in one of two ways:

* If your configuration was out of date, and has been pulled down again, Mycroft will respond:

> Configuration updated

* If your configuration was the same on your device as on home.mycroft.ai, Mycroft will respond:

> Your device has been configured

### Reading values directly from `mycroft_web_cache.json`

To see the city location value:

`jq ".location.city" < /var/tmp/mycroft_web_cache.json`

To see the latitude and longitude coordinates of your location:

`jq ".location.coordinate" < /var/tmp/mycroft_web_cache.json`

To see the timezone setting:

`jq ".location.timezone" < /var/tmp/mycroft_web_cache.json`

To see the listener setting:

`jq ".listener" < /var/tmp/mycroft_web_cache.json`

To see the Speech to Text (STT) settings:

`jq ".stt" < /var/tmp/mycroft_web_cache.json`

To see the Text to Speech (TTS) settings:

`jq ".tts" < /var/tmp/mycroft_web_cache.json`

### A look at the inside of `mycroft_web_cache.json`

Here is an example `mycroft_web_cache.json`.\
_NOTE: Your settings will be different._

```javascript
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
