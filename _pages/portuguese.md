---
ID: 33667
post_title: >
  Language support in Mycroft –
  Portuguese
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/language-support/portuguese/
published: true
post_date: 2017-12-23 20:20:09
---
# Language support in Mycroft - Portuguese - Português

_NOTE: These instructions apply to Mycroft for Linux only; we don't currently have instructions for changing the language on Picroft, but changing the language in Picroft should work in a similar way - why not give it a try and let us know how you go?. If you'd like to help us out with that, jump into the [~languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages) and let us know._

- [Language support in Mycroft - Portuguese - Português](#language-support-in-mycroft---portuguese---portugues)
  * [Change the **Wake Word** to Portuguese](#change-the-wake-word-to-portuguese)
    + [Download and install Portuguese acoustic model](#download-and-install-acoustic-model)
    + [Install language in Mycroft directories](#install-language-in-mycroft-directories)
    + [Verify installed files](#verify-installed-files)
    + [Choosing a Portuguese **Wake Word**](#choosing-a-italian-wake-word)
    + [Configure Mycroft to use Portuguese language and the chosen **Wake Word**](#configure-mycroft-to-use-portuguese-language-and-the-chosen-wake-word)
  * [Select and configure a Speech to Text (STT) engine with Portuguese support](#select-and-configure-a-speech-to-text-stt-engine-with-italian-support)
  * [Select and configure a Text to Speech (TTS) engine with Portuguese support](#select-and-configure-a-text-to-speech-tts-engine-with-italian-support)
  * [Translating core dialog](#translating-core-dialog)
  * [Configure Mycroft to use Portuguese](#configure-mycroft-source-code-to-use-portuguese)
  * [Language parsing](#language-parsing)
  * [Translating Skills](#translating-skills)
  * [Getting involved](#getting-involved)

Olá, falas Português? Follow these steps to change Mycroft's language to Portuguese (BCP 47:`pt`).

If you speak Portuguese and wish to enable Portuguese language support for
Mycroft, this is possible. However, this requires some technical knowledge such as:

* moving and copying files in a Linux shell
* downloading and unzipping large files
* editing configuration files

If you need further assistance, please join us in the [Languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages).

## Change the **Wake Word** to Portuguese

Mycroft uses PocketSphinx as the **Wake Word** engine. The default **Wake Word** in English is `Hey Mycroft`.

The **Wake Word** engine takes a language parameter. If you can spell your
**Wake Word** with english phonemes nothing special must be done.

You can find English phonemes for words with [The CMU Pronouncing
Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict). Try to pick english
 sounds that spell your Portuguese word. 

First, locate your `mycroft.conf` configuration file. On Mycroft for Linux,
the configuration files exists in several places and is loaded by this order

    default, remote (mycroft.ai), system, user
	
[More information about the mycroft.conf file](https://mycroft.ai/documentation/mycroft-conf/)

You should use remote settings, or edit the user configuration file located at:

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

If you want to use a Portuguese **Wake Word** with Portuguese phonemes we need to
download a Portuguese dictionary and a Portuguese acoustic model, trained with
 the latest `sphinxtrain`. The following steps are optional, you only need
 them if you want to use Portuguese phonemes.


### Download and install Portuguese acoustic model

No official model currently exists, but you can get an acoustic model from
[FalaBrasil](http://laps.ufpa.br/falabrasil/downloads.php)

Download the _acoustic model_ 

@TODO downloads link, site is currently down

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

There is no tool to easily get the Portuguese phonemes for words. You could
choose a **Wake Word** in Portuguese, and then verify that it
is in the `pt-br.dic` file of the language model. This file is not needed for
**Wake Word** spotting, you can get it from [FalaBrasil]() @TODO link

If your chosen **Wake Word** or phrase is not in the `pt-br.dict` file, you
can try looking for similar words and pick the phonemes manually.

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

The standard Mycroft STT should support most languages by default.

* list of languages supported by [google](https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti)

* list of languages supported by [ibm_bluemix](https://www.ibm.com/watson/developercloud/speech-to-text/api/v1/#sessionless_methods)

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

## Translating core dialog

The default Mycroft dialog files may need translation. For Portuguese this is already implemented.

You can find these files at

`mycroft_root_dir/res/txt/pt-pt`

You may need to copy the `pt-pt` folder into a `pt-br` folder

Check that the following files exist:

* `/mycroft_core/mycroft/res/text/pt-br/checking for updates.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/i am awake.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/i didn't catch that.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/checking for updates.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/not connected to the internet.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/reset to factory defaults.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/skills updated.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/sorry i couldn't install default skills.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/ssh disabled.dialog`
* `/mycroft_core/mycroft/res/text/pt-br/ssh enabled.dialog`

## Configure Mycroft to use Portuguese

Finally, to change Mycroft to Portuguese, you should use remote settings or edit
the user configuration file located at

`~/.mycroft/mycroft.conf`

```json
    lang": "pt-br",
```

## Language Parsing

There a few pieces of code needed to fully support a new language. These
include extracting numbers from text, sentence normalization and date time
extraction.

For Portuguese these have [already been implemented](https://github.com/MycroftAI/mycroft-core/pull/1049) and you do not need to worry about it.

## Translating Skills

Language support is implemented individually per **Skill**.

The **Skills** have a folder structure like this:

```
    dialog/en-us/speak.dialog
    vocab/en-us/sentence.intent
    vocab/en-us/word.entity
    vocab/en-us/keyword.voc
    regex/en-us/regex.rx
```

Will need to create a new language folder, `pt-br` in the `dialog`, `vocab` and `regex` directories, then translate all the files for the **Skill** to work in Portugues. Once you do this, please ensure you submit a PR in the Skill Repo on GitHub, so that the **Skill** author can merge the PR - and everyone benefits from your work. 

_NOTE: once you change a **Skill** folder you will no longer get automatic updates of that **Skill**

## Other things to consider with language translation in Mycroft

Some **Skills** may generate speech at runtime. Language support for these **Skills** is non-trivial and will require editing of code in Python. 

Some **Skills** expect English input, like WolframAlpha. These **Skills** will not work correctly with other languages. 

Some **Skills** use number and date-time processing, such as the Reminder and Alarm **Skills**. These **Skills** will not work correctly unless language parsing code has been implemented for the language. 

Some **Skills**, like the News Skill, play audio streams in English. You will need to find alternative audio streams in your language. 

You can also try to use [auto_translatable skills](https://github.com/JarbasAl/auto_translatable_skills). This is community contributed by community member @JarbasAI,  and not officially supported by Mycroft.

## Getting involved

If you would like to get involved with foreign language translations for Mycroft, we'd love to hear from you. Please join us in the [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)