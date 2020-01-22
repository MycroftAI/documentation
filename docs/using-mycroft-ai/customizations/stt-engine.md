---
description: >-
  Speech-To-Text (STT) is the process of converting audio of spoken words into
  strings of text. Mycroft supports a range of Speech-To-Text engines.
---

# Speech-To-Text Engines

Speech-To-Text (STT) is the process of converting audio of spoken words into strings of text. We know that many Mycroft users do not want to use the default STT engine, and like most of Mycroft's technology stack, this too can be customized.

To be useful for a voice assistant like Mycroft, speech recognition must be performed very quickly and with a high degree of accuracy. For this reason, Mycroft by default uses Google's STT engine. In order to provide an additional layer of privacy for our users, we proxy all STT requests through Mycroft's servers. This prevents Google's service from profiling Mycroft users or connecting voice recordings to their identities. Only the voice recording is sent to Google, no other identifying information is included in the request. Therefore Google's STT service does not know if an individual person is making thousands of requests, or if thousands of people are making a small number of requests each.

By supporting Mozilla's DeepSpeech project we are aiming to provide a competitive open source alternative. The accuracy of DeepSpeech is not yet sufficient to provide a quality experience for Mycroft users. However we will be switching to DeepSpeech by default as soon as we have achieved an acceptable level of accuracy.

The following are some of the available STT options. Each provides details on how to get setup, and how to configure Mycroft.

## Self-hosted

### Mozilla DeepSpeech

Mycroft has been supporting Mozilla's efforts to build DeepSpeech, an open Speech-to-Text technology. It is a fully open source STT engine, based on Baidu’s Deep Speech architecture and implemented with Google’s TensorFlow framework. Being open source means that if you have the hardware, it can be run within your own network providing additional privacy and control for you and your family.

#### Server Setup
You can test DeepSpeech using their pre-trained model by following the instructions on the [DeepSpeech Github repository](https://github.com/mozilla/DeepSpeech#project-deepspeech).

To setup a DeepSpeech server that Mycroft can use, try the [deepspeech-server project on PyPI](https://pypi.org/project/deepspeech-server/). Once you have this up and running, we can configure Mycroft to use this server.

#### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
  "stt": {
    "deepspeech_server": {
      "uri": "http://localhost:8080/stt"
    },
    "module": "deepspeech_server"
  }
```

#### Community Support

If you are interested in the continued development of the DeepSpeech STT engine, please join our the [DeepSpeech channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/deepspeech-stt).

### Kaldi

[Kaldi](http://kaldi-asr.org/) is described as a toolkit for speech recognition written in C++ and licensed under the Apache License v2.0. It is intended for use by speech recognition researchers.

Kaldi can be run on a Linux cluster or an individual machine, making it another option for those wanting local network speech-to-text.

#### Server Setup
First be sure to read the [system requirements in the Kaldi documentation](https://kaldi-asr.org/doc/dependencies.html).

The latest installation instructions can be found on the [Kaldi Github repository](https://github.com/kaldi-asr/kaldi#kaldi-speech-recognition-toolkit).

#### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
  "stt": {
    "kaldi": {
      "uri": "http://localhost:8080/client/dynamic/recognize"
    },
    "module": "kaldi"
  }
```

## Cloud-based

### GoVivaci

[GoVivaci](https://www.govivace.com/) is a for-profit company that has a [proprietary STT engine](https://www.govivace.com/products/automatic-speech-recognition-asr/).

#### Account Setup
The software is available in both 32 and 64-bit versions for Linux, Windows, and Mac platforms. A minimum of 4GB of RAM and a 2.0GHz processor is recommended. A [UniMRCP server plugin](https://www.unimrcp.org/govivacesr) is also available.

See [their website](https://www.govivace.com/products/automatic-speech-recognition-asr/) for more details.

#### Mycroft Configuration
Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"stt": {
  "govivace": {
    "uri": "https://services.govivace.com:49149/telephony",
    "credential": {
      "token": "xxxxx"
    }
  },
  "module": "govivaci"
}
```

The credential token will be provided to you by GoVivaci.

### Google Cloud Streaming STT

A streaming STT interface for the Google Cloud Speech-To-Text API.

#### Account Setup

A [Google Cloud account](https://cloud.google.com/) with active billing is required. Please carefully consider the [financial cost of using this service](https://cloud.google.com/speech-to-text/).

#### Mycroft Configuration

Install `google-cloud-speech` in the Mycroft Virtual environment using:
```
mycroft-pip install google-cloud-speech
```

Then, using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"stt": {
  "google_cloud_streaming": {
    "credential": {
      "json": # Paste Google API key JSON here
    }
  },
  "module": "google_cloud_streaming"
}
```
