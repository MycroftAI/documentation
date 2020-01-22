---
description: >-
  Speech-To-Text (STT) is the process of converting audio of spoken words into
  strings of text. Mycroft supports a range of Speech-To-Text engines.
---

# Speech-To-Text Engines

Many users want to use a specific STT engine rather than the default. Like most of Mycroft's technology stack, this too can be customized.

## Default Engine

For a voice assistant like Mycroft, speech recognition must be performed very quickly and with a high degree of accuracy. For this reason, Mycroft by default uses Google's STT engine.

In order to provide an additional layer of privacy for our users, we proxy all STT requests through Mycroft's servers. This prevents Google's service from profiling Mycroft users or connecting voice recordings to their identities. Only the voice recording is sent to Google, no other identifying information is included in the request. Therefore Google's STT service does not know if an individual person is making thousands of requests, or if thousands of people are making a small number of requests each.

By supporting Mozilla's DeepSpeech project we are aiming to provide a competitive open source alternative. The accuracy of DeepSpeech is not yet sufficient to provide a quality experience for Mycroft users. However we will be switching to DeepSpeech by default as soon as we have achieved an acceptable level of accuracy.

The following are some of the available STT options. Each provides details on how to get setup, and how to configure Mycroft.

## Mozilla DeepSpeech

Mycroft has been supporting Mozilla's efforts to build DeepSpeech, an open Speech-to-Text technology. It is a fully open source STT engine, based on Baidu’s Deep Speech architecture and implemented with Google’s TensorFlow framework. Being open source means that if you have the hardware, it can be run within your own network providing additional privacy and control for you and your family.

### Server Setup
You can test DeepSpeech using their pre-trained model by following the instructions on the [DeepSpeech Github repository](https://github.com/mozilla/DeepSpeech#project-deepspeech).

To setup a DeepSpeech server that Mycroft can use, try the [deepspeech-server project on PyPI](https://pypi.org/project/deepspeech-server/). Once you have this up and running, we can configure Mycroft to use this server.

### Mycroft Configuration
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

### Community Support

If you are interested in the continued development of the DeepSpeech STT engine, please join our the [DeepSpeech channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/deepspeech-stt).

## Kaldi

[Kaldi](http://kaldi-asr.org/) is described as a toolkit for speech recognition written in C++ and licensed under the Apache License v2.0. It is intended for use by speech recognition researchers.

Kaldi can be run on a Linux cluster or an individual machine, making it another option for those wanting local network speech-to-text.

### Server Setup
First be sure to read the [system requirements in the Kaldi documentation](https://kaldi-asr.org/doc/dependencies.html).

The latest installation instructions can be found on the [Kaldi Github repository](https://github.com/kaldi-asr/kaldi#kaldi-speech-recognition-toolkit).

### Mycroft Configuration
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

## GoVivaci

[GoVivaci](https://www.govivace.com/) is a for-profit company that has a [proprietary STT engine](https://www.govivace.com/products/automatic-speech-recognition-asr/).

### Account Setup
The software is available in both 32 and 64-bit versions for Linux, Windows, and Mac platforms. A minimum of 4GB of RAM and a 2.0GHz processor is recommended. A [UniMRCP server plugin](https://www.unimrcp.org/govivacesr) is also available.

See [their website](https://www.govivace.com/products/automatic-speech-recognition-asr/) for more details.

### Mycroft Configuration
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

## Google Cloud

The standard [Google Cloud Speech-To-Text API](https://cloud.google.com/speech-to-text/).

### Account Setup

A [Google Cloud account](https://cloud.google.com/) with active billing is required. Please carefully consider the [financial cost of using this service](https://cloud.google.com/speech-to-text/pricing).

To obtain the required credential JSON data, you must create a Google API Console project. To do this:

* Select or create a GCP project in the [Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager)
* Make sure that billing is enabled for your project - [see documentation](https://cloud.google.com/billing/docs/how-to/modify-project)
* Enable the Cloud Text-to-Speech API from your [GCP Console](https://console.cloud.google.com/apis/dashboard)
* Set up authentication:
  * Go to the [Create service account key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey) in the GCP Console
  * From the Service account drop-down list, select New service account.
  * Enter a name into the Service account name field.
  * Don't select a value from the Role drop-down list. No role is required to access this service.
  * Click Create. A note appears, warning that this service account has no role.
  * Click Create without role. A JSON file that contains your key downloads to your computer.

Remember to activate the API in the [GCP Console](https://console.developers.google.com/apis/library/speech.googleapis.com?)

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"stt": {
  "google_cloud": {
    "lang": "hi-in",
    "credential": {
      "json": {
        "type": "service_account",
        "project_id": "xxxxxxxxxx",
        "private_key_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "private_key": "-----BEGIN PRIVATE KEY-----nxxxxxxxxxxxxxxxxn-----END PRIVATE KEY-----n",
        "client_email": "xxxx@xxxx.iam.gserviceaccount.com",
        "client_id": "xxxxxxxxxxxxxxxxxxxxx",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/xxxxxx.iam.gserviceaccount.com"
      }
    }
  },
  "module": "google_cloud"
},
```

## Google Cloud Streaming STT

A streaming STT interface for the Google Cloud Speech-To-Text API.

### Account Setup

A [Google Cloud account](https://cloud.google.com/) with active billing is required. Please carefully consider the [financial cost of using this service](https://cloud.google.com/speech-to-text/pricing).

### Mycroft Configuration

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

## Houndify

STT provided by Houndify.

### Account Setup

Create a [Houndify account](https://www.houndify.com/), then:
* Create a New Client from your dashboard
  * Give your client a name and select a platform.
* Enable the "Speech To Text Only" domain for your Client.
* Get the `Client ID` and `Client Key` from your Client Information panel.

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"stt": {
  "houndify": {
    "credential": {
      "client_id": "xxxxx",
      "client_key": "xxxxx"
    }
  },
  "module": "houndify"
}
```

## IBM Watson

Speech-to-text using the IBM Watson cloud.

### Account Setup

Create an account at [IBM.com/cloud](https://www.ibm.com/cloud/watson-speech-to-text).

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"stt": {
  "ibm": {
    "username": "xxxxx",
    "password": "xxxxx"
  },
  "module": "ibm"
}
```

## Microsoft Azure

STT provided by the Microsoft Azure Speech Services. Formerly known as Bing STT.

### Account Setup

Create a [Microsoft Azure account](https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/) and get a server access token.

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"stt": {
  "bing": {
    "credential": {
      "token": "xxxxx"
    }
  },
  "module": "bing"
}
```

## Wit.ai

A natural langauge platform owned by Facebook.

### Account Setup

Create an account at [Wit.ai](https://wit.ai/) then create a new app to get your server access token. See the [Wit.ai documentation](https://wit.ai/docs) for further details.

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"stt": {
  "wit": {
    "credential": {
      "token": "xxxxx"
    }
  },
  "module": "wit"
}
```

## Yandex SpeechKit STT

A natural langauge platform owned by Facebook.

### Account Setup

Create a [Yandex Cloud account](https://cloud.yandex.com/services/speechkit), then:
* [Create a billing account](https://cloud.yandex.com/docs/billing/quickstart/#create_billing_account) - you can activate a free period in the console.
* Create first "folder" in cloud.
* [Create a service account](https://cloud.yandex.com/docs/iam/operations/sa/create) for your Mycroft instance with role editor.
* [Create an API key](https://cloud.yandex.com/docs/iam/operations/api-key/create) for your service account.

See the [Yandex Identity and Access Management documentation](https://cloud.yandex.com/docs/iam/) for further details.

### Mycroft Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `mycroft.conf` file by running:
```bash
mycroft-config edit user
```

To our existing configuration values we will add the following:
```JSON
"stt": {
  "yandex": {
    "lang": "en-US",
    "credential": {
      "api_key": "YOUR_API_KEY"
    }
  },
  "module": "yandex"
}
```
