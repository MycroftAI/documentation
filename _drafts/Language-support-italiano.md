---
post_title: Language support in Mycroft - Italian
layout: page
published: false
---

# Language support in Mycroft - Italian - italiano

- [Language support in Mycroft - Italian - italiano](#language-support-in-mycroft---italian---italiano)
  * [Change the **Wake Word** to Italian](#change-the-wake-word-to-italian)
    + [Download and install the Italian dictionary](#download-and-install-the-italian-dictionary)
    + [Download and install acoustic model](#download-and-install-acoustic-model)
    + [Download and install Italian language model](#download-and-install-italian-language-model)
    + [Verify the installed files](#verify-the-installed-files)
    + [Install language in Mycroft directories](#install-language-in-mycroft-directories)
    + [Choosing a Italian **Wake Word**](#choosing-a-italian-wake-word)
    + [Configure Mycroft to use Italian language and the chosen **Wake Word**](#configure-mycroft-to-use-italian-language-and-the-chosen-wake-word)
  * [Select and configure a Speech to Text (STT) engine with Italian support](#select-and-configure-a-speech-to-text-stt-engine-with-italian-support)
  * [Select and configure a Text to Speech (TTS) engine with Italian support](#select-and-configure-a-text-to-speech-tts-engine-with-italian-support)
  * [Configure Mycroft source code to handle Italian](#configure-mycroft-source-code-to-handle-italian)
  * [Getting involved](#getting-involved)

Ciao. Parli italiano? Follow these steps to change Mycroft's language to Italian (BCP 47: `it`).

If you speak Italian and wish to enable Italian language support for Mycroft, this is possible. However, this requires some technical knowledge such as:

* moving and copying files in a Linux shell
* downloading and unzipping large files
* editing Python source code files

If you need further assistance, please join us in the [Languages channel on Mycroft Chat](*https://chat.mycroft.ai/community/channels/languages).

## Change the **Wake Word** to Italian

Mycroft uses PocketSphinx as the **Wake Word** engine. The default **Wake Word** in English is `Hey Mycroft`.

To change the **Wake Word** to Italian, we need to download the generic Italian dictionary and the Italian acoustic model, trained with the latest `sphinxtrain`.

First, we create a directory for the `pocketsphinx` files:

`mkdir -p /usr/local/share/pocketsphinx/model/it/it`

### Download and install the Italian dictionary

Next, we download the _Italian dictionary_. This file is part of a larger archive, [so we must download the archive first](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Italian/it.tar.gz/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Italian/it.tar.gz/download -O it.tar.gz`

Extract the file `it.dic` from this archive.

Then, we install the dictionary into the directory we created.

`cp it.dic /usr/local/share/pocketsphinx/model/it`

### Download and install acoustic model

Next, we download the _acoustic model_ [cmusphinx-it-5.2.tar.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Italian/cmusphinx-it-5.2.tar.gz/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Italian/cmusphinx-it-5.2.tar.gz/download -O cmusphinx-it-5.2.tar.gz`

We then  unpack the gzipped file into a temporary directory.

`tar -xzf cmusphinx-it-5.2.tar.gz`

Then we copy it to the PocketSphinx directory

```bash
cd cmusphinx-it-5.2.tar.gz
cp * /usr/local/share/pocketsphinx/model/it/it
cd ..
```

### Download and install Italian language model

The _Italian language model_ file is archived within the `cmusphinx-it-5.2.tar.gz` file in the path `/cmusphinx-it-5.2/etc/voxforge_it_sphinx.ml`

Check that this file has been extracted into
`/usr/local/share/pocketsphinx/model/it`

### Verify the installed files

Check that the following files exist:

* `/usr/local/share/pocketsphinx/model/it`
* `/usr/local/share/pocketsphinx/model/it/it.dict`
* `/usr/local/share/pocketsphinx/model/it/it-small.lm`
* `/usr/local/share/pocketsphinx/model/it/it`
* `/usr/local/share/pocketsphinx/model/it/it/feat.params`
* `/usr/local/share/pocketsphinx/model/it/it/mdef`
* `/usr/local/share/pocketsphinx/model/it/it/means`
* `/usr/local/share/pocketsphinx/model/it/it/mixture_weights`
* `/usr/local/share/pocketsphinx/model/it/it/noisedict`
* `/usr/local/share/pocketsphinx/model/it/it/README`
* `/usr/local/share/pocketsphinx/model/it/it/sendump`
* `/usr/local/share/pocketsphinx/model/it/it/transition_matrices`
* `/usr/local/share/pocketsphinx/model/it/it/variances`

### Install language in Mycroft directories

Now that we have installed the PocketSphinx files for Italian, we need to install Italian in the Mycroft directories.

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
kathyreid@kathyreid-N76VZ:~/Dropbox/PHPworkspace/mycroft-core/mycroft/client/speech/recognizer/model$
```

_NOTE: Note that there is only one model folder - `en-us` for American English_

Create a new directory here for Italian, and then symlink it to the `pocketsphinx` directory.

```bash
mkdir it
ln -s /usr/local/share/pocketsphinx/model/it/it it/hmm
cp /usr/local/share/pocketsphinx/model/it/it.dic it/it.dic
```
_NOTE: The last `cp` command could be replaced by the `ln` command if you wish to save disk space. However, it is normal to add words to the `it.dict`, and copying means the original file is unchanged, and you are working with a copy._

You must have the following directories, files and symbolic links:

* `_your_base_dir_/mycroft/client/speech/recognizer/model/it`
* `_your_base_dir_mycroft/client/speech/recognizer/model/it/hmm`
* `_your_base_dir_mycroft/client/speech/recognizer/model/it/it.dict`
* `_your_base_dir_mycroft/client/speech/recognizer/model/it/it.lm`

### Choosing a Italian **Wake Word**

Choose a **Wake Word** or Wake Phrase in Italian, and then verify that it is in the `it.dic` file of the language model.

If your chosen **Wake Word** or phrase is not in the `it.dict` file, either choose a different **Wake Word**, or edit the `it.dict` file to add it.

### Configure Mycroft to use Italian language and the chosen **Wake Word**

First, locate your `mycroft.conf` configuration file. On Mycroft for Linux, this is stored at:

`_your_base_dir_mycroft/mycroft/configuration/mycroft.conf`

Edit the configuration file with following changes:

```json

    {
      "lang": "it",

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

## Select and configure a Speech to Text (STT) engine with Italian support

If the Speech to Text engine you are using already supports Italian, you don't need to do anything.

As an alternative, you can use PocketSphinx, running on your local machine. To use PocketSphinx as your STT engine, add the following to your `mycroft.conf` file:

```json
    "listener": {
       "producer": "pocketsphinx",
       "grammar": "lm"
       }
```

## Select and configure a Text to Speech (TTS) engine with Italian support

Next, select and configure a Text to Speech engine that supports Italian.

To configure your TTS engine, add the following to your `mycroft.conf` file:

```json
    "tts": {
      "module": "espeak",
      "espeak": {
        "lang": "it",
        "voice": "m1"
      }
    }
```

## Configure Mycroft source code to handle Italian

There are some source code changes required to handle a language change, and they require manual modification to the source code, as they have not yet been pulled into `mycroft-core`.

* [Changes to `listener.py` and `pocketsphinx_audio_consumer.py`](https://github.com/MycroftAI/mycroft-core/pull/656)

## Getting involved

If you would like to get involved with foreign language translations for Mycroft, we'd love to hear from you. Please join us in the [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)

@TODO This documentation was based on the French version, but the CMUSphinx file paths are not the same for Italian as they are for French, so I've had to extrapolate a little - there may be some errors in this file.
