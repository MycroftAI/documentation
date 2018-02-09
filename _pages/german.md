---
ID: 33364
post_title: Language support in Mycroft – German
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/language-support/german/
published: true
post_date: 2017-12-03 04:41:11
---
# Language support in Mycroft - German - Deutsch

_NOTE: These instructions apply to Mycroft for Linux only; we don't currently have instructions for changing the language on Picroft. If you'd like to help us out with that, jump into the [~languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages) and let us know._

- [Language support in Mycroft - German - français](#language-support-in-mycroft---german---francais)
  * [Change the **Wake Word** to German](#change-the-wake-word-to-german)
    + [Download and install the German dictionary](#download-and-install-the-german-dictionary)
    + [Download and install acoustic model](#download-and-install-acoustic-model)
    + [Download and install German language model](#download-and-install-german-language-model)
    + [Verify the installed files](#verify-the-installed-files)
    + [Install language in Mycroft directories](#install-language-in-mycroft-directories)
    + [Choosing a German **Wake Word**](#choosing-a-german-wake-word)
    + [Configure Mycroft to use German language and the chosen **Wake Word**](#configure-mycroft-to-use-german-language-and-the-chosen-wake-word)
  * [Select and configure a Speech to Text (STT) engine with German support](#select-and-configure-a-speech-to-text-stt-engine-with-german-support)
  * [Select and configure a Text to Speech (TTS) engine with German support](#select-and-configure-a-text-to-speech-tts-engine-with-german-support)
  * [Configure Mycroft source code to handle German](#configure-mycroft-source-code-to-handle-german)
  * [Getting involved](#getting-involved)

Guten tag. Sprechen sie Deutsch? Follow these steps to change Mycroft's language to German (BCP 47: `de`).

If you speak German and wish to enable German language support for Mycroft, this is possible. However, this requires some technical knowledge such as:

* moving and copying files in a Linux shell
* downloading and unzipping large files
* editing Python source code files

If you need further assistance, please join us in the [Languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages).

## Change the **Wake Word** to German

Mycroft uses PocketSphinx as the **Wake Word** engine. The default **Wake Word** in English is `Hey Mycroft`.

To change the **Wake Word** to German, we need to download the generic German dictionary and the German acoustic model, trained with the latest `sphinxtrain`.

First, we create a directory for the `pocketsphinx` files:

`sudo mkdir -p /usr/local/share/pocketsphinx/model/de/de`

### Download and install the German dictionary

Next, we download the German dictionary_ [cmusphinx-voxforge-de.dic](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.dic/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.dic/download -O cmusphinx-voxforge-de.dic`

Then, we install the dictionary into the directory we created.

`sudo mv cmusphinx-voxforge-de.dic /usr/local/share/pocketsphinx/model/de/de.dict`

### Download and install acoustic model

Next, we download the _acoustic model_ [cmusphinx-de-ptm-voxforge-5.2.tar.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-de-ptm-voxforge-5.2.tar.gz/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-de-ptm-voxforge-5.2.tar.gz/download -O cmusphinx-de-ptm-voxforge-5.2.tar.gz`

We then  unpack the gzipped file into a temporary directory.

`tar -xf cmusphinx-de-ptm-voxforge-5.2.tar.gz`

Then we copy it to the PocketSphinx directory

```bash
cd cmusphinx-de-ptm-voxforge-5.2
sudo mv * /usr/local/share/pocketsphinx/model/de/de
cd ..
```

### Download and install German language model

Next, we download the _German language model_ [cmusphinx-voxforge-de.lm.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.lm.gz/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.lm.gz/download -O cmusphinx-voxforge-de.lm.gz`

We then  unpack the gzipped file into a temporary directory.

`gzip -d cmusphinx-voxforge-de.lm.gz`

Then we move it to the PocketSphinx directory

`sudo mv cmusphinx-voxforge-de.lm /usr/local/share/pocketsphinx/model/de/de.lm`

### Verify the installed files

Check that the following files exist:

* `/usr/local/share/pocketsphinx/model/de`
* `/usr/local/share/pocketsphinx/model/de/de.dict`
* `/usr/local/share/pocketsphinx/model/de/de.lm`
* `/usr/local/share/pocketsphinx/model/de/de`
* `/usr/local/share/pocketsphinx/model/de/de/feat.params`
* `/usr/local/share/pocketsphinx/model/de/de/mdef`
* `/usr/local/share/pocketsphinx/model/de/de/means`
* `/usr/local/share/pocketsphinx/model/de/de/mixture_weights`
* `/usr/local/share/pocketsphinx/model/de/de/noisedict`
* `/usr/local/share/pocketsphinx/model/de/de/README`
* `/usr/local/share/pocketsphinx/model/de/de/sendump`
* `/usr/local/share/pocketsphinx/model/de/de/transition_matrices`
* `/usr/local/share/pocketsphinx/model/de/de/variances`

### Install language in Mycroft directories

Now that we have installed the PocketSphinx files for German, we need to install German in the Mycroft directories.

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

Create a new directory here for German, and then symlink it to the `pocketsphinx` directory.

```bash
mkdir de
ln -s /usr/local/share/pocketsphinx/model/de/de de/hmm
cp /usr/local/share/pocketsphinx/model/de/de.lm de/de.lm
cp /usr/local/share/pocketsphinx/model/de/de.dict de/de.dict
```
_NOTE: The last `cp` command could be replaced by the `ln` command if you wish to save disk space. However, it is normal to add words to the `de.dict`, and copying means the original file is unchanged, and you are working with a copy._

You must have the following directories, files and symbolic links:

* `_your_base_dir_/mycroft/client/speech/recognizer/model/de`
* `_your_base_dir_mycroft/client/speech/recognizer/model/de/hmm`
* `_your_base_dir_mycroft/client/speech/recognizer/model/de/de.dict`
* `_your_base_dir_mycroft/client/speech/recognizer/model/de/de.lm`

### Choosing a German **Wake Word**

Choose a **Wake Word** or Wake Phrase in German, and then verify that it is in the `cmusphinx-voxforge-de.dic` file of the language model. Experience shows that the best choice is a single word with three or more phonemes.

For example, check  if the 'hallo' word exists:

`egrep '^hallo ' de.dict`

`hallo HH AE L AX UU`

If your chosen **Wake Word** or phrase is not in the `de.dict` file, either choose a different **Wake Word**, or edit the `de.dict` file to add it.

### Configure Mycroft to use German language and the chosen **Wake Word**

First, locate your `mycroft.conf` configuration file. On Mycroft for Linux, this is stored at:

`_your_base_dir_mycroft/mycroft/configuration/mycroft.conf`

Edit the configuration file with following changes:

```json

    {
      "lang": "de",

      "listener": {

        "wake_word": "hallo",
        "phonemes": "HH AE L AX UU",
        "threshold": 1e-10,
        "standup_word": "hallo",
        "standup_phonemes": "HH AE L AX UU",
        "standup_threshold": 1e-10
      }
    }
```

## Select and configure a Speech to Text (STT) engine with German support

If the Speech to Text engine you are using already supports German, you don't need to do anything - this is the case with the default mycroft hosted engine for example.

As an alternative, you can use PocketSphinx, running on your local machine. To use PocketSphinx as your STT engine, add the following to your `mycroft.conf` file:

```json
    "listener": {
       "producer": "pocketsphinx",
       "grammar": "lm"
       }
```

## Select and configure a Text to Speech (TTS) engine with German support

Next, select and configure a Text to Speech engine that supports German. For example, `espeak` has several German voices.

To configure your TTS engine, add the following to your `mycroft.conf` file:

```json
    "tts": {
      "module": "espeak",
      "espeak": {
        "lang": "de",
        "voice": "m1"
      }
    }
```

## Configure Mycroft source code to handle German

There are some source code changes required to handle a language change, and they require manual modification to the source code, as they have not yet been pulled into `mycroft-core`.

* [Changes to `listener.py` and `pocketsphinx_audio_consumer.py`](https://github.com/MycroftAI/mycroft-core/pull/656)

## Getting involved

If you would like to get involved with foreign language translations for Mycroft, we'd love to hear from you. Please join us in the [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)
