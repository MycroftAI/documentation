---
ID: 42297
post_title: Mycroft in other languages
author: Kathy Reid
post_excerpt: >
  Learn about foreign language support in
  Mycroft, and how to approach configuring
  Mycroft to support other languages.
layout: page
permalink: >
  http://mycroft.ai/documentation/languages/
published: true
post_date: 2019-06-10 10:59:07
---
# Mycroft in other languages

In order to support other languages, several components have to be in place in the end to end [Mycroft Voice Stack](https://mycroft.ai/voice-stack-introduction/). Adding language support for Mycroft means that each of those components has to support the new language. This page walks you what has to be done for each of the elements. 

At present English is the only officially supported language. Using a language other than English will require at least some editing via the commandline, and likely general troubleshooting. If you are not familiar with Mycroft's configuration files, please see our [dedicated documentation for `mycroft.conf`](https://mycroft.ai/documentation/mycroft-conf/). 

Adding support for a new language is a significant undertaking. It is complex and will require some development and Linux system administration knowledge.

## Overview
For Mycroft to be usable in a language we need to look at six components.
1. [Language setting](#1-language-setting): To inform each of the following components which language we are using, we must set our overall language setting.
2. [Wake Word](#2-wake-word): When you Speak 'Hey Mycroft, do something', you are invoking a Wake Word. To change your Wake Word to another language, you need to change the Wake Word phrase that is used.
3. [Speech to Text](#3-speech-to-text-stt): Mycroft is designed to be modular, so you can choose which Speech to Text engine you use. You need to find and configure a Speech to Text engine for your language.
4. [Text to Speech](#4-text-to-speech-tts): Again, Mycroft is designed to be modular, so you can choosen which Text to Speech engine you use. You need to find and configure a Text to Speech engine for your language.
5. [Skills](#5-skills): To support a language, a Skill must have `vocab` and `dialog` entries for that language.
6. [Mycroft Core](#6-mycroft-core-lingua-franca-library): To support a new language, `mycroft-core` needs to have supporting files added to the [Lingua Franca library](https://github.com/MycroftAI/lingua-franca).

## 1. Language setting
Your primary language is set within your `mycroft.conf` file. Setting this at the user level `~/.mycroft/mycroft.conf` file might look like:
```json
{
  "max_allowed_core_version": 19.2,
  "lang": "it-it"
}
```
_Please note that all configuration changes must result in a valid JSON file. If a change to your config does not seem to be working or you are unsure, please check the contents of your `mycroft.conf` file with one of the many JSON validators available online. A single misplaced comma can cause hours of frustration._

## 2. Wake Word
Changing your wake word is not necessary, however may be desirable in order to wake the device with a phrase that is more appropriate or relevant in your language. By default, Mycroft will continue to be awoken by the phrase _"Hey Mycroft"_.

[See our documentation on changing your Wake Word, and select a Wake Word that suits your language](https://mycroft.ai/documentation/home-mycroft-ai-pairing/#changing-your-wake-word).

## 3. Speech to Text (STT)

Speech to text (STT) is the part of Mycroft that translates spoken words into text. That text is then used by intent parsers, and then by Skills.

### Available STT engines
In order to support a new language, a Speech to Text engine (STT engine) must be available.

STT engines are made available by different vendors, and they each have different licenses and usage restrictions.

* [List of languages supported by Google STT](https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti)
* [List of languages supported by IBM Watson Bluemix](https://www.ibm.com/watson/developercloud/speech-to-text/api/v1/#sessionless_methods)
* [List of languages supported by Wit.AI](https://wit.ai/faq)

Once you've found an STT engine for your language, you will need to configure Mycroft to use it. This is done through the [mycroft.conf](https://mycroft.ai/documentation/mycroft-conf/) file.

##### What if there isn't an STT engine available for my language?

Unfortunately, STT engines aren't available for every language in the world.

We recommend that you request your language at [Mozilla's Common Voice project](https://voice.mozilla.org/en/languages).

### Setting your STT engine

Locate your `mycroft.conf` file, and open it for editing on the Linux command line, using a tool like `vi` or `nano`.

```json
{
  “stt”: {
  “module”: “google_cloud”,    <- this should be set to the name of your STT provider (ie "google_cloud", "wit" etc)
  “google_cloud”: {            <- this should be set to the name of your STT provider (ie "google_cloud", "wit" etc)
    “lang”: “hi-in”,           <- the IETF BCP-47 language code for your language (shown is Hindi as spoken in India)
    “credential”: {            <- some STT engines require credentials - check the documentation for the STT engine
      “json”: {
      }
    }
  }
}
```
To obtain the google_cloud credential json data, you must first have a Google API Console project.
You make a Google API Console project like this:
* Select or create a GCP project - [link](https://console.cloud.google.com/cloud-resource-manager)
* Make sure that billing is enabled for your project - [link](https://cloud.google.com/billing/docs/how-to/modify-project)
* Enable the Cloud Text-to-Speech API - [link](https://console.cloud.google.com/apis/dashboard)
* Set up authentication:
  - Go to the Create service account key page in the GCP Console - [link](https://console.cloud.google.com/apis/credentials/serviceaccountkey)
  - From the Service account drop-down list, select New service account.
  - Enter a name into the Service account name field.
  - Don't select a value from the Role drop-down list. No role is required to access this service.
  - Click Create. A note appears, warning that this service account has no role.
  - Click Create without role. A JSON file that contains your key downloads to your computer.

Remember to activate the API -  [link](https://console.developers.google.com/apis/library/speech.googleapis.com?)

the JSON configuration should look like this:

```JSON
"stt": {
  "module": "google_cloud",
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
  }
},
```

The STT options you can select from are;

* `"mycroft"`
* `"google"`
* `"google_cloud"`
* `"wit"`
* `"ibm"`
* `"kaldi"`
* `"bing"`
* `"govivace"`
* `"houndify"`
* `"deepspeech_server"`
* `"mycroft_deepspeech"`


## 4. Text to Speech (TTS)

In order to support a new language, a Text to Speech (TTS) engine must be available.

### Available TTS engines
TTS engines are made available by different vendors, and they each have different licenses and usage restrictions.

* [List of languages supported by eSpeak TTS](http://espeak.sourceforge.net/)
* [List of languages supported by Google Cloud TTS](https://cloud.google.com/text-to-speech/docs/voices)
* [List of languages supported by MaryTTS](http://mary.dfki.de/)
* [List of languages supported by BingTTS](https://docs.microsoft.com/en-us/azure/cognitive-services/speech/api-reference-rest/s)

Once you've found an TTS engine for your language, you will need to configure Mycroft to use it. This is done through the [mycroft.conf](https://mycroft.ai/documentation/mycroft-conf/) file.

##### What if there isn't an TTS engine available for my language?

Unfortunately, TTS engines aren't available for every language in the world.

If you would like to build a TTS for your language, then we recommend you check out [Mimic Recording Studio](https://mycroft.ai/documentation/mimic-recording-studio/). Mimic Recording Studio facilitates the recording of phrases based on a _corpus_, and the recordings can be used to train a voice with the `mimic2` TTS software.

### Setting your TTS engine

Locate your `mycroft.conf` file, and open it for editing on the Linux command line, using a tool like `vi` or `nano`.

```json
  "tts": {
    "module": "google",
    "google": {
      "lang": "hi"
    }
  }
```

The TTS options you can select from are;

* `"mimic"`
* `"mimic2"`
* `"google"`
* `"marytts"`
* `"fatts"`
* `"espeak"`
* `"spdsay"`
* `"watson"`
* `"bing"`
* `"responsive_voice"`


## 5. Skills

In order to support a new language, individual Skills must support that language too. Mycroft Skills are already structured to cater for new languages. Within the Skill's directory, you will see subdirectories called `dialog`, `vocab` or `locale`. Within these directories is a directory for each of the languages the Skill supports, named after the BCP-47 language code for the language - such as `en-us` for American English and `pt-br` for Brazilian Portuguese.

To have a Skill support another language, the easiest way is to contribute to translating `dialog` and `vocab` files on the [Mycroft Translate](https://translate.mycroft.ai) platform. When significant progress has been made on a language in Mycroft Translate, the translations are automatically added to Skills.

You can modify the individual `dialog` and `vocab` files for a Skill on your own device if you need to. Each Skill is in it's own directory on your device at `/opt/mycroft/skills/`.

## 6. Mycroft Core - Lingua Franca library

In addition to the above, `mycroft-core` also requires localization, in particular to extract dates and numbers.

[For more information, have a look at the `lang` directory within `mycroft/util` in `mycroft-core`](https://github.com/MycroftAI/mycroft-core/tree/dev/mycroft/util/lang). This is also maintained as a stand-alone repository called [Lingua Franca](https://github.com/MycroftAI/lingua-franca).

Some common files for each language are:

* `parse_LANG.py` - this file parses large numbers, extracts dates and times in formats specific to the language, and handles definite articles such as 'a, an' etc.

* `format_LANG.py` - this file formats cardinal and ordinal numbers, and helps to handle pronunciation of complex phrases involving decimals and fractions. Depending on the language, this file will also help format days of the week and other complex date and time phrasing.

As of mid-2019, the languages supported by `mycroft-core` are:

* German (`de`)
* French (`fr`)
* Hungarian (`hu`)
* Italian (`it`)
* Portuguese (`pt`)
* Swedish (`sv`)

There is also active progress being made on:
* Danish (`da`)
* Dutch (`nl`)
* Spanish (`es`)

Contributions to this utility are warmly welcomed.

## Example configuration
Putting these six components together allows us to use Mycroft in another language. A simple `mycroft.conf` file for Italian users might look like:
```json
{
  "lang": "it-it",
  "stt": {
    "module": "mycroft",
    "mycroft": {
      "lang": "it-it"
    }
  },
  "tts": {
    "module": "google",
    "google": {
      "lang": "it"
    }
  }
}
```
This configuration will set the:
* overall system language
* Spech to Text (STT) engine
* Text to Speech (TTS) engine

This configuration has not changed the Wake Word, so the device will continue responding to "Hey Mycroft".

## Further languages support

You're welcome to post questions and queries to the [Languages topic on the Mycroft Forum](https://community.mycroft.ai/c/languages) or join our [Languages chatroom at Mycroft Chat](https://chat.mycroft.ai/community/channels/languages) to connect with others from around the world.

We also have a number of [language-specific channels in Chat](https://mycroft.ai/contribute/#translate-to-new-languages).