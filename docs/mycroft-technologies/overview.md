---
description: A broad overview of the technology that makes up Mycroft AI.
---

# Technology Overview

Mycroft is the name of a suite of software and hardware tools that use [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) and [machine learning](https://en.wikipedia.org/wiki/Machine_learning) to provide an open source voice assistant.

{% embed url="https://www.youtube.com/watch?v=m4L0QfzUeEI" caption="Our vision for Mycroft" %}

## Mycroft components

Mycroft is modular. Some components can be easily 'swapped out' for others:

* Wake Word detection
* Speech to Text \(STT\)
* Intent parser

### Wake Word detection

A Wake Word is a phrase you use to tell Mycroft you're about to issue a command. By default, this is `Hey Mycroft`, but you can configure your own **Wake Word** in your [Mycroft Home](https://home.mycroft.ai) account.

There are two technologies that Mycroft.AI currently uses for **Wake Word** detection:

* [PocketSphinx](https://github.com/cmusphinx/pocketsphinx): PocketSphinx is part of the broader [CMUSphinx package](https://cmusphinx.github.io/), developed by [Carnegie Mellon University](https://www.cmu.edu). PocketSphinx is a lightweight speech recognition engine, specifically tuned for handheld and mobile devices.

Because PocketSphinx is trained on English speech, your **Wake Word** currently needs to be an English word, like `Hello Mike`, `Hi there Mickey` or `Hey Mike`. Wake Words in other languages, like Spanish, French or German, won't work as well.

* [Precise](https://mycroft.ai/documentation/precise): Unlike PocketSphinx, which is based on Speech to Text technology, Precise is a neural network that is trained on audio data. It doesn't matter what _words_ you want to use for your **Wake Word**. Instead, you train it on _sounds_. The downside is that Precise needs to be trained on your chosen **Wake Word**. Precise has been the default **Wake Word** Listener for each Mycroft Device since mid-March 2018. Prior to this date, PocketSphinx was the default.

### Speech to Text \(STT\)

Speech to Text \(STT\) software is used to take spoken words, and turn them into text phrases that can then be acted on.

We are working with Mozilla to build [DeepSpeech](https://github.com/mozilla/DeepSpeech). A fully open source STT engine, based on Baidu’s Deep Speech architecture and implemented with Google’s [TensorFlow](https://www.tensorflow.org/) framework.

DeepSpeech is not yet ready for production use and Mycroft currently uses [Google STT](https://cloud.google.com/speech/) as the default STT engine.

Mycroft also supports other STT engines that can be configured using the [Configuration Manager](../using-mycroft-ai/customizations/config-manager.md):

* [IBM Watson Speech to Text](https://www.ibm.com/watson/services/speech-to-text/) \(username and password required\)
* [wit.ai Speech to Text](https://wit.ai/blog/2014/02/12/speech-api) \(wit.ai API key required\)

### Intent parser

An **intent parser** is software which identifies what the user's _intent_ is based on their speech. An **intent parser** usually takes the output of a Speech to Text \(STT\) engine as an input.

For example, Julie Speaks the following to Mycroft: `Hey Mycroft, tell me about the weather`

Julie's _intent_ is to find out about the weather \(probably in her current location\).

An **intent parser** can then match the _intent_ with a suitable **Skill** to handle the _intent_.

* [Adapt intent parser](https://github.com/MycroftAI/adapt): Adapt is the default intent parser for all Mycroft platforms. Adapt was developed by Mycroft and is available under an open source license.
* [Padatious](https://github.com/MycroftAI/padatious): Padatious is a neural network based intent parser. Padatious is currently under active development by Mycroft and is available under an open source license. It is likely that some Mycroft platforms will switch to using Padatious in the future instead of Adapt.

### Text to Speech

Text to Speech \(TTS\) software takes written text, such as text files on a computer, and uses a _voice_ to _speak_ the text. Text to Speech can have different voices, depending on the TTS engine used.

* [Mimic](https://github.com/MycroftAI/mimic): Mycroft's default text to speech \(TTS\) engine, based on CMU's Flite \(Festival Lite\)

In your home.mycroft.ai account, you can select several other TTS engines if you don't wish to use Mimic.

* [eSpeak](http://espeak.sourceforge.net/): you need to choose which [voice](http://espeak.sourceforge.net/voices.html) to use
* [MaryTTS](http://mary.dfki.de/): you need to choose which voice to use
* [Google TTS](https://play.google.com/store/apps/details?id=com.google.android.tts): you need to choose which voice to use
* FATTS: you need to choose which voice to use

### Middleware

The Mycroft middleware has two components:

* [Mycroft Core](https://github.com/MycroftAI/mycroft-core): this code, written in Python, is the core software that provides the 'glue' between other modules. Mycroft Core is available under an open source license.
* [Mycroft Home and Mycroft API](https://home.mycroft.ai): this is the platform where data on **Users** and **Devices** is held. This platform provides abstraction services, such as storing API keys that are used to access third-party services to provide **Skill** functionality. The code for this platform is not publicly available.

### Mycroft Skills

[Mycroft Skills](https://github.com/MycroftAI/mycroft-skills) are like 'add-ons' or 'plugins' that provide additional functionality. **Skills** can be developed by Mycroft Developers, or by Community Developers, and vary in their functionality and maturity.

[Mycroft Skills Management \(msm\)](https://github.com/MycroftAI/msm) is a set of helper scripts that assist in the installation and management of **Skills**.

### Devices and Enclosures

Mycroft is designed to run on many different platforms - called **Devices**, with different hardware, called **Enclosures**.

* **Mark 1** - a software image of Mycroft designed to be installed on the Mycroft Mark 1 - a reference hardware device
* **Picroft** - a software image of Mycroft designed to be installed on Raspberry Pi 3
* **Android** - a software image of Mycroft designed to be installed on Android devices

