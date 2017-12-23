---
ID: 33667
post_title: Language support in Mycroft – Portuguese
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/language-support/portuguese/
published: true
post_date: 2017-12-23 20:20:09
---
# Language support in Mycroft - Portuguese - Português

@TODO this should work exactly the same in picroft?
_NOTE: These instructions apply to Mycroft for Linux only; we don't currently have instructions for changing the language on Picroft. If you'd like to help us out with that, jump into the [~languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages) and let us know._

- [Language support in Mycroft - Portuguese - Português](#language-support-in-mycroft---portuguese---portugues)
  * [Change the **Wake Word** to Portuguese](#change-the-wake-word-to-portuguese)
    + [Download and install Portuguese acoustic model](#download-and-install-acoustic-model)
    + [Install language in Mycroft directories](#install-language-in-mycroft-directories)
    + [Verify installed files](#verify-installed-files)
    + [Choosing a Portuguese **Wake Word**](#choosing-a-italian-wake-word)
    + [Configure Mycroft to use Portuguese language and the chosen **Wake Word**](#configure-mycroft-to-use-portuguese-language-and-the-chosen-wake-word)
  * [Select and configure a Speech to Text (STT) engine with Portuguese support](#select-and-configure-a-speech-to-text-stt-engine-with-italian-support)
  * [Select and configure a Text to Speech (TTS) engine with Portuguese support](#select-and-configure-a-text-to-speech-tts-engine-with-italian-support)
  * [Configure Mycroft to use Portuguese](#configure-mycroft-source-code-to-use-portuguese)
  * [Language parsing](#language-parsing)
  * [Translating Skills](#translating-skills)
  * [Getting involved](#getting-involved)

Olá, falas Português? Follow these steps to change Mycroft's language to Portuguese (BCP 47:`pt`).

If you speak Portuguese and wish to enable Portuguese language support for
Mycroft, this is possible. However, this requires some technical knowledge such as:

* moving and copying files in a Linux shell
* downloading and unzipping large files
* editing Python source code files

If you need further assistance, please join us in the [Languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages).

## Change the **Wake Word** to Portuguese

Mycroft uses PocketSphinx as the **Wake Word** engine. The default **Wake Word** in English is `Hey Mycroft`.

The wake word engine takes a language parameter, if you can spell your
wakeword with english phonemes nothing special must be done

You can find english phonemes for words with [The CMU Pronouncing
Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict), try to pick english
 sounds that spell your Portuguese word

First, locate your `mycroft.conf` configuration file. On Mycroft for Linux,
the configuration files exists in several places and is loaded by this order

    default, remote (mycroft.ai), system, user

You should use remote settings or edit the user configuration file located at

`~/.mycroft/mycroft.conf`

```json
    {
    // Hotword configurations
      "hotwords": {
        "hey jarbas": {
            "module": "pocketsphinx",
            "phonemes": "HH EY . JH AA R B AA SH ",
            "threshold": 1e-60,
            "lang": "en-us"
            },
        "hey mycroft": {
            "module": "pocketsphinx",
            "phonemes": "HH EY . M AY K R AO F T",
            "threshold": 1e-90,
            "lang": "en-us"
            }
        },

      "listener": {
        "wake_word": "hey jarbas",
        ...
        },
    }
```

If you want to use a Portuguese Wake Word with Portuguese phonemes we need to
download a Portuguese dictionary and a Portuguese acoustic model, trained with
 the latest `sphinxtrain`. The following steps are optional, you only need
 them if you want to use portuguese phonemes


### Download and install Portuguese acoustic model

No official model currently exists, but you can get an acoustic model from
[FalaBrasil](http://laps.ufpa.br/falabrasil/downloads.php)

Download the _acoustic model_ @TODO downloads link, site is currently down

`wget link -O file`


### Install language in Mycroft directories

Now that we have downloaded the PocketSphinx files for Portuguese, we need to install Portuguese in the Mycroft directories.

First, [SSH into your device](https://mycroft.ai/documentation/mark-1/#connecting-to-the-mark-1-via-ssh).

Navigate to the Mycroft language model directory.

For instance, on `mycroft-core` for Linux, navigate to

`/mycroft-core/mycroft/client/speech/recognizer/model`

You should see the following files in this directory:

```bash
$ ls -las
total 24
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 .
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 ..
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 en-us
```

_NOTE: Note that there is only one model folder - `en-us` for American English_

Create a new directory here for Portuguese, and then copy the downloaded files

@TODO bash usage example

### Verify the installed files

Check that the following files exist:

* `/mycroft_core/mycroft/client/speech/recognizer/model/pt-br/hmm/feat.params`
* `/mycroft_core/mycroft/client/speech/recognizer/model/pt-br/hmm/mdef`
* `/mycroft_core/mycroft/client/speech/recognizer/model/pt-br/hmm/means`
* `/mycroft_core/mycroft/client/speech/recognizer/model/pt-br/hmm/mixture_weights`
* `/mycroft_core/mycroft/client/speech/recognizer/model/pt-br/hmm/noisedict`
* `/mycroft_core/mycroft/client/speech/recognizer/model/pt-br/hmm/sendump`
* `/mycroft_core/mycroft/client/speech/recognizer/model/pt-br/hmm/transition_matrices`
* `/mycroft_core/mycroft/client/speech/recognizer/model/pt-br/hmm/variances`


### Choosing a Portuguese **Wake Word**

There is no tool to easily get the portuguese phonemes for words, you could
choose a **Wake Word** or Wake Phrase in Portuguese, and then verify that it
is in the `pt-br.dic` file of the language model. This file is not needed for
wake word spotting, you can get it from [FalaBrasil]() @TODO link

If your chosen **Wake Word** or phrase is not in the `pt-br.dict` file, you
can try looking for similar words and pick the phonemes manually

### Configure Mycroft to use Portuguese language and the chosen **Wake Word**

You should use remote settings or edit the user configuration file located at

`~/.mycroft/mycroft.conf`

Edit the configuration file and add the new portuguese wake word:

```json
    {
    // Hotword configurations
      "hotwords": {
        "oi jarbas": {
            "module": "pocketsphinx",
            "phonemes": "o ii . zm a rm b a s",
            "threshold": 1e-60,
            "lang": "pt-br"
            },
        "hey mycroft": {
            "module": "pocketsphinx",
            "phonemes": "HH EY . M AY K R AO F T",
            "threshold": 1e-90,
            "lang": "en-us"
            }
        },

      "listener": {
        "wake_word": "oi jarbas",
        ...
        },
    }
```

## Select and configure a Speech to Text (STT) engine with Portuguese support

If the Speech to Text engine you are using already supports Portuguese, you
don't need to do anything.

The standard Mycroft STT should support most languages by default

list of languages supported by [google](https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti)

list of languages supported by [ibm_bluemix](https://www.ibm.com/watson/developercloud/speech-to-text/api/v1/#sessionless_methods)

@TODO list of languages for all officially supported engines

## Select and configure a Text to Speech (TTS) engine with Portuguese support

Next, select and configure a Text to Speech engine that supports Portuguese.

To configure your TTS engine, you should use remote settings or edit the user
configuration file located at

`~/.mycroft/mycroft.conf`

Espeak should support [most languages](http://espeak.sourceforge.net/languages.html)

```json
    "tts": {
      "module": "espeak",
      "espeak": {
        "lang": "pt",
        "voice": "m1"
      }
    }
```

@TODO list of languages for all officially supported engines like in this [post](https://jarbasai.github.io//tts_comparison/)

## Configure Mycroft to use Portuguese

Finally change mycroft to Portuguese, you should use remote settings or edit
the user configuration file located at

`~/.mycroft/mycroft.conf`

```json
    lang": "pt-br",
```

## Language Parsing

There a few pieces of code needed to fully support a new language, these
include extracting numbers from text, sentence normalization and date time
extraction

for portuguese these have [already been implemented](https://github.com/MycroftAI/mycroft-core/pull/1049) and you do not need to
worry about it


## Translating Skills

Language support is implemented individually per skill

The skills have a folder structure like this:

    dialog/en-us/speak.dialog
    vocab/en-us/sentence.intent
    vocab/en-us/keyword.voc
    regex/en-us/regex.rx

Just create the new language folder `pt-br` and translate all the files,
please submit a PR in the skill repo so everyone benefits

_NOTE: once you change a skill folder you will no longer get automatic updates

Some skills, may generate speech at runtime, these need you to edit the code and language support is non trivial

Some skills need english input, like WolframAlpha, these will not trigger correctly

Skills like the reminder and alarm skill may not work correctly for languages
that did not implement the previous step

Finally some skills, like the News skill, play english audio and you must find an alternative


## Getting involved

If you would like to get involved with foreign language translations for Mycroft, we'd love to hear from you. Please join us in the [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)
