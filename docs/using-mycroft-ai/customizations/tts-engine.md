---
description: >-
  Text-To-Speech (TTS) is the process of synthesizing audio from text. Mycroft
  uses our own TTS engines by default, however we also support a range of third
  party services.
---

# Text-To-Speech

Mycroft has two open source TTS engines.

Mimic 1 is a fast, light-weight engine based on [Carnegie Mellon University's FLITE software](http://cmuflite.org/). Whilst the original Mimic may sound more robotic, it is able to be synthesized on your device.

{% page-ref page="../../mycroft-technologies/mimic-overview/" %}

[Mimic 2](https://github.com/MycroftAI/mimic2#mimic2) is an implementation of Tacotron speech synthesis. It is a fork of [Keith Ito's project](https://github.com/keithito/tacotron) with additional tooling and code enhancements. Mimic 2 provides a much more natural sounding voice, however requires significant processing power to do so and is therefore cloud-based.

## Default Engine

The engine that will be used depends on the voice selected in your [Device Settings at Home.mycroft.ai](https://home.mycroft.ai/devices).

Currently:

* British Male is Mimic 1
* American Female is Mimic 1
* American Male is Mimic 2
* Google Voice uses the Google Translate TTS API.

As Mimic 1 voices can be synthesized on device, the British Male voice will be used anytime the device cannot reach your preferred TTS service. This allows Mycroft to continue to speak even if it is not connected to a network.

## eSpeak

A multi-lingual software speech synthesizer for Linux and Windows.

[eSpeak](http://espeak.sourceforge.net/) uses a "formant synthesis" method. This allows many languages to be provided in a small size. The speech is clear, and can be used at high speeds, but is not as natural or smooth as larger synthesizers which are based on human speech recordings.

### Mycroft Configuration

First, ensure that the espeak package is installed on your system.

```bash
sudo apt-get install espeak
```

Then, using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:

```javascript
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

```javascript
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

```javascript
  "tts": {
    "fatts": {
      "url": "http://YOUR_SERVER:PORT_NUMBER"
    },
    "module": "fatts"
  }
```

## Amazon Polly

[Amazon Polly's](https://aws.amazon.com/polly/) text-to-speech service.

### Account Setup

[Create an AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) and add the Polly service.

You will need to take note of your private "Access Key ID" and "Secret Access Key".

### Mycroft Configuration

First, check the [list of available voices and languages](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html). Note that Polly does not provide a separate `language` attribute like other TTS options. The language is determined by which voice is chosen.

Then, install the `boto3` python module in the Mycroft virtual environment:

```bash
mycroft-pip install boto3
```

or

```bash
cd ~/mycroft-core
source .venv/bin/activate
pip3 install boto3
deactivate
```

Finally, using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:

```javascript
"tts": {
  "module": "polly",
  "polly": {
    "voice": "Matthew",
    "region": "us-east-1",
    "engine": "standard",
    "access_key_id": "YOUR_ACCESS_KEY_ID",
    "secret_access_key": "YOUR_SECRET_ACCESS_KEY"
  }
}
```

If the `voice`, `region`, and `engine` attributes are ommitted the defaults of `Matthew`, `us-east-1` and `standard` will be used. This is an English \(US\) voice.

## Google TTS

Google Translate's text-to-speech API.

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config set tts.module "google"
```

## IBM Watson

### Account Setup

Create an account at [IBM.com/cloud](https://www.ibm.com/cloud/watson-text-to-speech). Once you add the TTS service to your account, you will receive an API key and unique API url.

You can find a list of available voices at [Languages and Voices](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices#neuralVoices). For example, "en-US\_MichaelV3Voice".

IBM keeps a log of all requests in the lite plan unless you turn it off explicitly by setting "X-Watson-Learning-Opt-Out" to true. We have set Mycroft to Opt-Out by default, so if you want to share data with IBM then you must set this to false.

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:

```javascript
"tts": {
  "module": "watson",
  "watson": {
    "voice":"PREFERRED_VOICE",
    "apikey": "YOUR_API_KEY",
    "url": "YOUR_API_URL",
    "X-Watson-Learning-Opt-Out": "true"
  }
}
```

## Microsoft Azure Cognitive Service

_Note: This is a Community provided TTS plugin and is not controlled by Mycroft AI. Updates for this plugin may not have been reviewed by the Mycroft team. We strongly recommend reviewing any code you intend to install from outside Mycroft's official channels._

_Plugins are currently only available on the `dev` channel of Mycroft. They will be available on all systems in the next minor release. If you're not sure what that means,_ [_sign up to our newsletter_](https://mycroft.ai/newsletters/) _to get notified about the next release._

### Installation

```bash
mycroft-pip install mycroft-tts-plugin-azure
```

### Account Setup

This TTS service requires a subscription to Microsoft Azure and the creation of a Speech resource \([https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview\#create-the-azure-resource](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview#create-the-azure-resource)\) The free plan is more than able to handle domestic usage \(5 million character per month, or 0.5 million with neural TTS voice\)

### Mycroft Configuration

You can choose your voice here in the column "voice name" \([https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support\#text-to-speech](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech)\) Neural voices are much better, but cost more.

```javascript
"tts": {
  "module": "azure",
  "azure": {
    "api_key": "insert_your_key_here",
    "voice": "en-US-JennyNeural", # optional, default "en-US-Guy24kRUS"
    "region": "westus" # optional, if your region is westus
  }
}
```

## Microsoft Bing

### Account Setup

Create a [Microsoft Azure account](https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/) and get a server access token.

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:

```javascript
"tts": {
  "module": "bing",
  "bing": {
    "api_key": "YOUR_API_KEY",
    "format": "riff-16khz-16bit-mono-pcm",
    "gender": "Male"
  }
}
```

## Mozilla TTS

### Server Setup

Instructions for setting up a Mozilla TTS server are [available on the projects wiki](https://github.com/mozilla/TTS/wiki/Build-instructions-for-server).

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:

```javascript
"tts": {
  "module": "mozilla",
  "mozilla": {
    "url": "http://my-mozilla-tts-server/api/tts"
  }
}
```

By default the `url` is set to the localhost: [`http://0.0.0.0:5002/api/tts`](http://0.0.0.0:5002/api/tts) So if you are running the server on the same machine as your Mycroft instance, only the `module` attribute needs to be set. This can also be done with a single command:

```bash
mycroft-config set tts.module mozilla
```

## Responsive Voice

{% hint style="warning" %}
The API for this service may have significantly changed. As such this TTS option may not be available. Contributions to restore the service are warmly welcomed. Please direct any development questions to the [~Dev channel of Mycroft Chat](https://chat.mycroft.ai/community/channels/dev).
{% endhint %}

Lifelike human digital voices from [ResponsiveVoice.org](https://responsivevoice.org).

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:

```javascript
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

A common high-level interface to speech synthesis from [Free\(B\)Soft](https://freebsoft.org/speechd).

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
2. Create billing account: [https://cloud.yandex.com/docs/billing/quickstart/\#create\_billing\_account](https://cloud.yandex.com/docs/billing/quickstart/#create_billing_account)

   You can activate a free trial period in the console.

3. Create first "folder" in cloud.
4. Create service account for you Mycroft instance with role editor: [https://cloud.yandex.com/docs/iam/operations/sa/create](https://cloud.yandex.com/docs/iam/operations/sa/create)
5. Create API key for service account: [https://cloud.yandex.com/docs/iam/operations/api-key/create](https://cloud.yandex.com/docs/iam/operations/api-key/create)

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:

```javascript
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

