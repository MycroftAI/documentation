---
description: >-
  Text-To-Speech (TTS) is the process of synthesizing audio from text. Mycroft
  uses our own TTS engines by default, however we also support a range of third
  party services.
---

# Text-To-Speech

Mycroft has two open source TTS engines.

Mimic 1 is a fast, light-weight engine based on [Carnegie Mellon University's FLITE software](http://cmuflite.org). Whilst the original Mimic may sound more robotic, it is able to be synthesized on your device.

{% content-ref url="../../mycroft-technologies/mimic-overview/" %}
[mimic-overview](../../mycroft-technologies/mimic-overview/)
{% endcontent-ref %}

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

[eSpeak](http://espeak.sourceforge.net) uses a "formant synthesis" method. This allows many languages to be provided in a small size. The speech is clear, and can be used at high speeds, but is not as natural or smooth as larger synthesizers which are based on human speech recordings.

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

**Added in mycroft-core v21.2.2**

Further customization of espeak voices is available through the following options:

* Amplitude
* Gap
* Capital
* Pitch
* Speed

For more information on these parameters see `espeak --help`

Example Config:

```json
{
  "max_allowed_core_version": 21.2,
  "lang": "de-de",
  "tts": {
    "module": "espeak",
    "espeak": {
      "lang": "german-mbrola-5",
      "voice": "german-mbrola-5",
      "speed": "135",
      "amplitude": "80",
      "pitch": "20"
    }
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

Produced by [Mivoq](https://www.mivoq.it), it is based off Mary TTS.

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

[Create an AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h\_ct\&src=default\&redirect\_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) and add the Polly service.

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

If the `voice`, `region`, and `engine` attributes are ommitted the defaults of `Matthew`, `us-east-1` and `standard` will be used. This is an English (US) voice.

## Google TTS

Google Translate's text-to-speech API.

{% hint style="warning" %}
The Google TTS module uses the gTTS Python package which interfaces with the Google Translate text-to-speech API. This is not intended for commercial or production usage. The service may break at any time, and you are subject to their Terms of Service that can be found at: [https://policies.google.com/terms](https://policies.google.com/terms)
{% endhint %}

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

{% hint style="info" %}
_Note: This is a Community provided TTS plugin and is not controlled by Mycroft AI. Updates for this plugin may not have been reviewed by the Mycroft team. We strongly recommend reviewing any code you intend to install from outside Mycroft's official channels._
{% endhint %}

### Installation

```bash
mycroft-pip install mycroft-tts-plugin-azure
```

### Account Setup

This TTS service requires a subscription to Microsoft Azure and the creation of a Speech resource ([https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview#create-the-azure-resource](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview#create-the-azure-resource)) The free plan is more than able to handle domestic usage (5 million character per month, or 0.5 million with neural TTS voice)

### Mycroft Configuration

You can choose your voice here in the column "voice name" ([https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech)) Neural voices are much better, but cost more.

```javascript
"tts": {
  "module": "azure_tts",
  "azure_tts": {
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

## Coqui TTS

Coqui TTS is an actively maintained fork of the Mozilla TTS project. A Coqui TTS server can be run locally without internet connection.

Pretrained TTS models are available based on open voice datasets (_eg. LJSpeech, LibriTTS, Thorsten-DE, Mai, ..._). The [Coqui release page](https://github.com/coqui-ai/TTS/releases) shows a complete list of available TTS models.

### Server Setup

Coqui TTS is based on Python3 so it's recommended to setup a new virtual environment (_venv_) for the TTS server.

```
mkdir <TTS directory>
cd <TTS directory>
python3 -m venv .
source ./bin/activate
```

Then within that environment install the TTS server.

```
pip install pip --upgrade
pip install tts --upgrade
```

#### Running TTS server

To run the server we need to know two things:

1. Whether we have a CUDA enabled GPU. Synthesizing voice is significantly faster when run on a [CUDA](https://en.wikipedia.org/wiki/CUDA) enabled GPU compared to a CPU.
2. Which TTS model to use.

Running `tts --list_models` within the venv shows the TTS models available in the current release.

Example output:

```
tts_models/en/ek1/tacotron2
tts_models/es/mai/tacotron2-DDC
tts_models/fr/mai/tacotron2-DDC
tts_models/de/thorsten/tacotron2-DCA
...
```

Within the venv we can now start the TTS server by running:

```
tts-server --use_cuda=false/true --model_name *modelNameFromList* 
`
```

Example commands:

* _English:_  `tts-server --use_cuda=true --model_name tts_models/en/ek1/tacotron2`
* _German:_   `tts-server --use_cuda=true --model_name tts_models/de/thorsten/tacotron2-DCA`

By default a Coqui TTS server uses the best vocoder for the selected TTS model. However you can override the default using the `--vocoder_name` parameter when starting your server.

Once the TTS server is running you can test it by opening `http://localhost:5002` in your browser and try synthesizing a test sentence.

### Mycroft Configuration

After your TTS server setup is finished you can [configure Mycroft](tts-engine.md#mycroft-configuration-8) to use it with the same configuration as Mozilla TTS.

## Responsive Voice

{% hint style="info" %}
_Note: This is a Community provided TTS plugin and is not controlled by Mycroft AI. The code in this plugin has not been reviewed by the Mycroft team. We strongly recommend reviewing any code you intend to install from outside Mycroft's official channels._
{% endhint %}

Lifelike human digital voices from [ResponsiveVoice.org](https://responsivevoice.org).

### Installation

```bash
mycroft-pip install ovos-tts-plugin-responsivevoice
```

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:

```bash
mycroft-config edit user
```

See the plugin's Github repository for suggested configurations:

[https://github.com/OpenVoiceOS/ovos-tts-plugin-responsivevoice#configuration](https://github.com/OpenVoiceOS/ovos-tts-plugin-responsivevoice#configuration)

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
2.  Create billing account: [https://cloud.yandex.com/docs/billing/quickstart/#create\_billing\_account](https://cloud.yandex.com/docs/billing/quickstart/#create\_billing\_account)

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
