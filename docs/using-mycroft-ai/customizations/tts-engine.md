---
description: >-
  Text-To-Speech (TTS) is the process of synthesizing audio from text. Mycroft
  uses our own TTS engines by default, however we also support a range of third
  party services.
---

# Text-To-Speech

Mycroft has two open source TTS engines.

Mimic 1 is a fast, light-weight engine based on [Carnegie Mellon University's FLITE software](http://cmuflite.org/). Whilst the original Mimic may sound more robotic, it is able to be synthesized on your device.

{% page-ref page="../../mycroft-technologies/mimic-overview/README.md" %}

[Mimic 2](https://github.com/MycroftAI/mimic2#mimic2) is an implementation of Tacotron speech synthesis. It is a fork of [Keith Ito's project](https://github.com/keithito/tacotron) with additional tooling and code enhancements. Mimic 2 provides a much more natural sounding voice, however requires significant processing power to do so and is therefore cloud-based.

## Default Engine

The engine that will be used depends on the voice selected in your [Device Settings at Home.mycroft.ai](https://home.mycroft.ai/devices).

Currently:
- British Male is Mimic 1
- American Female is Mimic 1
- American Male is Mimic 2
- Google Voice uses the Google Translate TTS API.

As Mimic 1 voices can be synthesized on device, the British Male voice will be used anytime the device cannot reach your preferred TTS service. This allows Mycroft to continue to speak even if it is not connected to a network.



## ESpeak

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"tts": {
  "module": "espeak",
  "espeak": {
    "lang": "english-us",
    "voice": "m1"
  }
}
```

## Mary TTS

The multilingual open-source MARY text-to-speech platform. MaryTTS is a client-server system written in pure Java, so it runs on many platforms.

### Server Setup
The latest installation instructions can be found on the [MaryTTS Github repository](https://github.com/marytts/marytts).

### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
  "tts": {
    "marytts": {
      "url": "http://YOUR_SERVER:PORT_NUMBER"
    },
    "module": "marytts"
  }
```

## FA TTS

Produced by [Mivoq](https://www.mivoq.it/), it is based off Mary TTS.

### Server Setup
The latest installation instructions can be found on the [Mivoq FA TTS Github repository](https://github.com/mivoq/fatts).

### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
  "tts": {
    "fatts": {
      "url": "http://YOUR_SERVER:PORT_NUMBER"
    },
    "module": "fatts"
  }
```

## Google TTS

Google Translate's text-to-speech API.

### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config set tts.module "google"
```

## IBM Watson

### Account Setup
Create an account at [IBM.com/cloud](https://www.ibm.com/cloud/watson-text-to-speech).
You can find a list of available voices at [Languages and Voices](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices#neuralVoices). For example, "en-US_MichaelV3Voice". Please note that IBM keeps a log of all requests in the lite plan unless you turn it explicitly.


### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"tts": {
  "module": "watson",
  "watson": {
    "voice":"PREFERRED_VOICE",
    "api_key": "YOUR_API_KEY",
    "username": "YOUR_USERNAME", # Not needed if api_key is set
    "password": "YOUR_PASSWORD"  # Not needed if api_key is set
  }
}
```

## Microsoft Azure

### Account Setup
Create a [Microsoft Azure account](https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/) and get a server access token.

### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"tts": {
  "module": "bing",
  "bing": {
    "api_key": "YOUR_API_KEY",
    "format": "riff-16khz-16bit-mono-pcm",
    "gender": "Male"
  }
}
```

## Responsive Voice

Lifelike human digital voices from [ResponsiveVoice.org](https://responsivevoice.org).

### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"tts": {
  "module": "responsive_voice",
  "responsive_voice": {
    "gender": "male",
    "pitch": "0.5",
    "rate": "0.5",
    "vol": "1"
  }
}
```

## SpdSay

A common high-level interface to speech synthesis from [Free(B)Soft](https://freebsoft.org/speechd).

### Software Setup

Install the `speech-dispatcher` package using your systems package manager. For example: `sudo apt-get install speech-dispatcher`

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config set tts.module "spdsay"
```

## Yandex SpeechKit

Speech services from Yandex, one of the largest cloud platforms in Russia.

### Account Setup

1. Register an account at Yandex.
2. Create billing account: https://cloud.yandex.com/docs/billing/quickstart/#create_billing_account
   You can activate a free trial period in the console.
3. Create first "folder" in cloud.
4. Create service account for you Mycroft instance with role editor: https://cloud.yandex.com/docs/iam/operations/sa/create
5. Create API key for service account: https://cloud.yandex.com/docs/iam/operations/api-key/create

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"tts": {
  "module": "yandex",
  "yandex": {
    "lang": "en-US",
    "api_key": "YOUR_API_KEY",
    "voice": "oksana", #optional
    "emotion": "good" #optional
  }
}
```
