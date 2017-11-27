---
ID: 33222
post_title: 'Language support in Mycroft - French'
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?page_id=33222
published: false
---
# Language support in Mycroft - French - français

- [Language support in Mycroft - French - français](#language-support-in-mycroft---french---francais)
  * [Change the **Wake Word** to French](#change-the-wake-word-to-french)
    + [Download and install the French dictionary](#download-and-install-the-french-dictionary)
    + [Download and install acoustic model](#download-and-install-acoustic-model)
    + [Download and install French language model](#download-and-install-french-language-model)
    + [Verify the installed files](#verify-the-installed-files)
    + [Install language in Mycroft directories](#install-language-in-mycroft-directories)
    + [Choosing a French **Wake Word**](#choosing-a-french-wake-word)
    + [Configure Mycroft to use French language and the chosen **Wake Word**](#configure-mycroft-to-use-french-language-and-the-chosen-wake-word)
  * [Select and configure a Speech to Text (STT) engine with French support](#select-and-configure-a-speech-to-text-stt-engine-with-french-support)
  * [Select and configure a Text to Speech (TTS) engine with French support](#select-and-configure-a-text-to-speech-tts-engine-with-french-support)
  * [Configure Mycroft source code to handle French](#configure-mycroft-source-code-to-handle-french)
  * [Getting involved](#getting-involved)

Bonjour. Parlez-vous français? Follow these steps to change Mycroft's language to French (BCP 47: `fr`).

If you speak French and wish to enable French language support for Mycroft, this is possible. However, this requires some technical knowledge such as:

* moving and copying files in a Linux shell
* downloading and unzipping large files
* editing Python source code files

If you need further assistance, please join us in the [Languages channel on Mycroft Chat](*https://chat.mycroft.ai/community/channels/languages).

## Change the **Wake Word** to French

Mycroft uses PocketSphinx as the **Wake Word** engine. The default **Wake Word** in English is `Hey Mycroft`.

To change the **Wake Word** to French, we need to download the generic French dictionary and the French acoustic model, trained with the latest `sphinxtrain`.

First, we create a directory for the `pocketsphinx` files:

`mkdir -p /usr/local/share/pocketsphinx/model/fr/fr`

### Download and install the French dictionary

Next, we download the _French dictionary_ [fr.dict](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/French/fr.dict/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/French/fr.dict/download -O fr.dict`

Then, we install the dictionary into the directory we created.

`cp fr.dict /usr/local/share/pocketsphinx/model/fr`

### Download and install acoustic model

Next, we download the _acoustic model_ [cmusphinx-fr-ptm-5.2.tar.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/French/cmusphinx-fr-ptm-5.2.tar.gz/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/French/cmusphinx-fr-ptm-5.2.tar.gz/download -O cmusphinx-fr-ptm-5.2.tar.gz`

We then  unpack the gzipped file into a temporary directory.

`tar -xzf cmusphinx-fr-ptm-5.2.tar.gz`

Then we copy it to the PocketSphinx directory

```bash
cd cmusphinx-fr-ptm-5.2
cp * /usr/local/share/pocketsphinx/model/fr/fr
cd ..
```

### Download and install French language model

Next, we download the _French language model_ [fr-small.lm.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/French/fr-small.lm.gz/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/French/fr-small.lm.gz/download -O fr-small.lm.gz`

We then  unpack the gzipped file into a temporary directory.

`gzip -d fr-small.lm.gz

Then we move it to the PocketSphinx directory

`mv fr-small.lm /usr/local/share/pocketsphinx/model/fr`

### Verify the installed files

Check that the following files exist:


* `/usr/local/share/pocketsphinx/model/fr`
* `/usr/local/share/pocketsphinx/model/fr/fr.dict`
* `/usr/local/share/pocketsphinx/model/fr/fr-small.lm`
* `/usr/local/share/pocketsphinx/model/fr/fr`
* `/usr/local/share/pocketsphinx/model/fr/fr/feat.params`
* `/usr/local/share/pocketsphinx/model/fr/fr/mdef`
* `/usr/local/share/pocketsphinx/model/fr/fr/means`
* `/usr/local/share/pocketsphinx/model/fr/fr/mixture_weights`
* `/usr/local/share/pocketsphinx/model/fr/fr/noisedict`
* `/usr/local/share/pocketsphinx/model/fr/fr/README`
* `/usr/local/share/pocketsphinx/model/es/es/sendump`
* `/usr/local/share/pocketsphinx/model/fr/fr/transition_matrices`
* `/usr/local/share/pocketsphinx/model/fr/fr/variances`

### Install language in Mycroft directories

Now that we have installed the PocketSphinx files for French, we need to install French in the Mycroft directories.

First, SSH into your device.
@TODO link here to SSH instructions


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

Create a new directory here for French, and then symlink it to the `pocketsphinx` directory.

```bash
mkdir fr
ln -s /usr/local/share/pocketsphinx/model/fr/fr fr/hmm
cp /usr/local/share/pocketsphinx/model/fr/fr.dict fr/fr.dict
```
_NOTE: The last `cp` command could be replaced by the `ln` command if you wish to save disk space. However, it is normal to add words to the `fr.dict`, and copying means the original file is unchanged, and you are working with a copy._

You must have the following directories, files and symbolic links:

* `_your_base_dir_/mycroft/client/speech/recognizer/model/fr`
* `_your_base_dir_mycroft/client/speech/recognizer/model/fr/hmm`
* `_your_base_dir_mycroft/client/speech/recognizer/model/fr/fr.dict`
* `_your_base_dir_mycroft/client/speech/recognizer/model/fr/fr.lm`

### Choosing a French **Wake Word**

Choose a **Wake Word** or Wake Phrase in French, and then verify that it is in the `fr.dict` file of the language model. Experience shows that the best choice is a single word with three or more phonemes.

For example, check  if the 'salutations' word exists:

`egrep '^salutations ' fr.dict`

`salutations ss aa ll uu tt aa ss yy on`

If your chosen **Wake Word** or phrase is not in the `fr.dict` file, either choose a different **Wake Word**, or edit the `fr.dict` file to add it.

### Configure Mycroft to use French language and the chosen **Wake Word**

First, locate your `mycroft.conf` configuration file. On Mycroft for Linux, this is stored at:

`_your_base_dir_mycroft/mycroft/configuration/mycroft.conf`

Edit the configuration file with following changes:

```json

    {
      "lang": "fr",

      "listener": {

        "wake_word": "salutations",
        "phonemes": "ss aa ll uu tt aa ss yy on",
        "threshold": 1e-10,
        "standup_word": "salutations",
        "standup_phonemes": "ss aa ll uu tt aa ss yy on",
        "standup_threshold": 1e-10
      }
    }
```

## Select and configure a Speech to Text (STT) engine with French support

If the Speech to Text engine you are using already supports French, you don't need to do anything.

As an alternative, you can use PocketSphinx, running on your local machine. To use PocketSphinx as your STT engine, add the following to your `mycroft.conf` file:

```json
    "listener": {
       "producer": "pocketsphinx",
       "grammar": "lm"
       }
```

## Select and configure a Text to Speech (TTS) engine with French support

Next, select and configure a Text to Speech engine that supports French. For example, `espeak` has several French voices.

To configure your TTS engine, add the following to your `mycroft.conf` file:

```json
    "tts": {
      "module": "espeak",
      "espeak": {
        "lang": "fr",
        "voice": "m1"
      }
    }
```

## Configure Mycroft source code to handle French

There are some source code changes required to handle a language change, and they require manual modification to the source code, as they have not yet been pulled into `mycroft-core`.

* [Changes to `listener.py` and `pocketsphinx_audio_consumer.py`](https://github.com/MycroftAI/mycroft-core/pull/656)

## Getting involved

If you would like to get involved with foreign language translations for Mycroft, we'd love to hear from you. Please join us in the [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)
