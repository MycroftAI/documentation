---
post_title: 'Language support in Mycroft - Spanish'
layout: page
published: false
---
# Language support in Mycroft - Spanish - Español

- [Language support in Mycroft - Spanish - français](#language-support-in-mycroft---Spanish---francais)
  * [Change the **Wake Word** to Spanish](#change-the-wake-word-to-Spanish)
    + [Download and install the Spanish dictionary](#download-and-install-the-Spanish-dictionary)
    + [Download and install acoustic model](#download-and-install-acoustic-model)
    + [Download and install Spanish language model](#download-and-install-Spanish-language-model)
    + [Verify the installed files](#verify-the-installed-files)
    + [Install language in Mycroft directories](#install-language-in-mycroft-directories)
    + [Choosing a Spanish **Wake Word**](#choosing-a-Spanish-wake-word)
    + [Configure Mycroft to use Spanish language and the chosen **Wake Word**](#configure-mycroft-to-use-Spanish-language-and-the-chosen-wake-word)
  * [Select and configure a Speech to Text (STT) engine with Spanish support](#select-and-configure-a-speech-to-text-stt-engine-with-Spanish-support)
  * [Select and configure a Text to Speech (TTS) engine with Spanish support](#select-and-configure-a-text-to-speech-tts-engine-with-Spanish-support)
  * [Configure Mycroft source code to handle Spanish](#configure-mycroft-source-code-to-handle-Spanish)
  * [Getting involved](#getting-involved)

Hola! Puedes hablar español? Follow these steps to change Mycroft's language to Spanish (BCP 47: `es`).

If you speak Spanish and wish to enable Spanish language support for Mycroft, this is possible. However, this requires some technical knowledge such as:

* moving and copying files in a Linux shell
* downloading and unzipping large files
* editing Python source code files

If you need further assistance, please join us in the [Languages channel on Mycroft Chat](*https://chat.mycroft.ai/community/channels/languages).

## Change the **Wake Word** to Spanish

Mycroft uses PocketSphinx as the **Wake Word** engine. The default **Wake Word** in English is `Hey Mycroft`.

To change the **Wake Word** to Spanish, we need to download the generic Spanish dictionary and the Spanish acoustic model, trained with the latest `sphinxtrain`.

First, we create a directory for the `pocketsphinx` files:

`mkdir -p /usr/local/share/pocketsphinx/model/es/es`

### Download and install the Spanish dictionary

Next, we download the Spanish dictionary_ [es.dict](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/es.dict/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/es.dict/download -O es.dict`

Then, we install the dictionary into the directory we created.

`cp es.dict /usr/local/share/pocketsphinx/model/es/es`

### Download and install acoustic model

Next, we download the _acoustic model_ [cmusphinx-es-5.2.tar.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/cmusphinx-es-5.2.tar.gz/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/cmusphinx-es-5.2.tar.gz/download -O cmusphinx-es-5.2.tar.gz`

We then  unpack the gzipped file into a temporary directory.

`tar -xzf cmusphinx-es-5.2.tar.gz`

Then we copy it to the PocketSphinx directory

```bash
cd cmusphinx-es-5.2.tar.gz
cp * /usr/local/share/pocketsphinx/model/es/es
cd ..
```

### Download and install Spanish language model

Next, we download the _Spanish language model_ [es-20k.lm.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/es-20k.lm.gz/download) from the CMUSphinx project on SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/es-20k.lm.gz/download -O es-20k.lm.gz`

We then  unpack the gzipped file into a temporary directory.

`gzip -d es-20k.lm.gz

Then we move it to the PocketSphinx directory

`mv es-20k.lm.gz /usr/local/share/pocketsphinx/model/es/es`

### Verify the installed files

Check that the following files exist:

* `/usr/local/share/pocketsphinx/model/es`
* `/usr/local/share/pocketsphinx/model/es/es.dict`
* `/usr/local/share/pocketsphinx/model/es/es-small.lm`
* `/usr/local/share/pocketsphinx/model/es/es`
* `/usr/local/share/pocketsphinx/model/es/es/feat.params`
* `/usr/local/share/pocketsphinx/model/es/es/mdef`
* `/usr/local/share/pocketsphinx/model/es/es/means`
* `/usr/local/share/pocketsphinx/model/es/es/mixture_weights`
* `/usr/local/share/pocketsphinx/model/es/es/noisedict`
* `/usr/local/share/pocketsphinx/model/es/es/README`
* `/usr/local/share/pocketsphinx/model/es/es/sendump`
* `/usr/local/share/pocketsphinx/model/es/es/transition_matrices`
* `/usr/local/share/pocketsphinx/model/es/es/variances`

### Install language in Mycroft directories

Now that we have installed the PocketSphinx files for Spanish, we need to install Spanish in the Mycroft directories.

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

Create a new directory here for Spanish, and then symlink it to the `pocketsphinx` directory.

```bash
mkdir es
ln -s /usr/local/share/pocketsphinx/model/es/es es/hmm
cp /usr/local/share/pocketsphinx/model/es/es.dict es/es.dict
```
_NOTE: The last `cp` command could be replaced by the `ln` command if you wish to save disk space. However, it is normal to add words to the `es.dict`, and copying means the original file is unchanged, and you are working with a copy._

You must have the following directories, files and symbolic links:

* `_your_base_dir_/mycroft/client/speech/recognizer/model/es`
* `_your_base_dir_mycroft/client/speech/recognizer/model/es/hmm`
* `_your_base_dir_mycroft/client/speech/recognizer/model/es/es.dict`
* `_your_base_dir_mycroft/client/speech/recognizer/model/es/es.lm`

### Choosing a Spanish **Wake Word**

Choose a **Wake Word** or Wake Phrase in Spanish, and then verify that it is in the `cmusphinx-voxforge-es.dic` file of the language model. Experience shows that the best choice is a single word with three or more phonemes.

For example, check  if the 'salutations' word exists:

`egrep '^salutations ' es.dict`

`salutations ss aa ll uu tt aa ss yy on`

If your chosen **Wake Word** or phrase is not in the `cmusphinx-voxforge-es.dic` file, either choose a different **Wake Word**, or edit the `cmusphinx-voxforge-es.dic` file to add it.

### Configure Mycroft to use Spanish language and the chosen **Wake Word**

First, locate your `mycroft.conf` configuration file. On Mycroft for Linux, this is stored at:

`_your_base_dir_mycroft/mycroft/configuration/mycroft.conf`

Edit the configuration file with following changes:

```json

    {
      "lang": "es",

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

## Select and configure a Speech to Text (STT) engine with Spanish support

If the Speech to Text engine you are using already supports Spanish, you don't need to do anything.

As an alternative, you can use PocketSphinx, running on your local machine. To use PocketSphinx as your STT engine, add the following to your `mycroft.conf` file:

```json
    "listener": {
       "producer": "pocketsphinx",
       "grammar": "lm"
       }
```

## Select and configure a Text to Speech (TTS) engine with Spanish support

Next, select and configure a Text to Speech engine that supports Spanish. For example, `espeak` has several Spanish voices.

To configure your TTS engine, add the following to your `mycroft.conf` file:

```json
    "tts": {
      "module": "espeak",
      "espeak": {
        "lang": "es",
        "voice": "m1"
      }
    }
```

## Configure Mycroft source code to handle Spanish

There are some source code changes required to handle a language change, and they require manual modification to the source code, as they have not yet been pulled into `mycroft-core`.

* [Changes to `listener.py` and `pocketsphinx_audio_consumer.py`](https://github.com/MycroftAI/mycroft-core/pull/656)

## Getting involved

If you would like to get involved with foreign language translations for Mycroft, we'd love to hear from you. Please join us in the [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)
