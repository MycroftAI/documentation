---
ID: 32412
post_title: About Mycroft
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/mycroft-software-hardware/
published: true
post_date: 2017-12-02 22:35:25
---
# About Mycroft

Welcome to Mycroft.

## What is Mycroft?

Mycroft is the name of a suite of software and hardware tools that use [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) and [machine learning](https://en.wikipedia.org/wiki/Machine_learning) to provide an open source voice assistant.

As of late 2017, Mycroft is undergoing heavy development. It is at a level of maturity where developers and hardware hobbyists will be able to use it effectively. However, it is not yet ready for mainstream adoption.

[This video provides a quick overview](https://youtu.be/m4L0QfzUeEI) of our vision for Mycroft.

## Mycroft components

Mycroft is modular. Some components can be easily 'swapped out' for others:

* Wake Word detection
* Speech to Text (STT)
* Intent parser

### Wake Word detection

A Wake Word is a phrase you use to tell Mycroft you're about to issue a command. By default this is `Hey Mycroft`, but you can configure your own **Wake Word** in your [Mycroft Home](https://home.mycroft.ai) account.

There are two technologies that Mycroft.AI currently uses for **Wake Word** detection:

* [PocketSphinx](https://github.com/cmusphinx/pocketsphinx): PocketSphinx is part of the broader [CMUSphinx package](https://cmusphinx.github.io/), developed by [Carnegie Mellon University](https://www.cmu.edu). PocketSphinx is a lightweight speech recognition engine, specifically tuned for handheld and mobile devices. PocketSphinx is currently the default **Wake Word** detection tool on all Mycroft platforms.

Because PocketSphinx is trained on English speech, your **Wake Word** currently needs to be an English word, like `Hello Mike`, `Hi there Mickey` or `Hey Mike`. Wake Words in other languages, like Spanish, French or German, won't work as well. 

* Precise: Unlike PocketSphinx, which is based on Speech to Text technology, Precise is a neural network that is trained on audio data. It doesn't matter what *words* you want to use for your **Wake Word**. Instead, you train it on *sounds*. The downside is that Precise needs to be trained on your chosen **Wake Word**. Precise is currently being developed and tested internally at Mycroft, and is not yet ready for Community Developers to work with.
@TODO: Put link in here to the Precise documentation

### Speech to Text (STT)

Speech to Text (STT) software is used to take spoken words, and turn them into text phrases that can then be acted on.

Mycroft currently uses external Speech to Text software. However, we are aiming to build our own open Speech to Text solution, [OpenSTT](https://openstt.org/), by partnering with other organizations and their projects, such as [Mozilla Voice](https://voice.mozilla.org/).

* [Google STT](https://cloud.google.com/speech/): Google STT is the default STT engine used with Mycroft. In [home.mycroft.ai](https://home.mycroft.ai), you are able to change this default.

Mycroft also supports these other STT engines:

* [IBM Watson Speech to Text](https://www.ibm.com/watson/services/speech-to-text/) (username and password required)
* [wit.ai Speech to Text](https://wit.ai/blog/2014/02/12/speech-api) (wit.ai API key required)

### Intent parser

An **intent parser** is software which identifies what the user's _intent_ is based on their speech. An **intent parser** usually takes the output of a Speech to Text (STT) engine as an input.

For example, Julie Speaks the following to Mycroft:
`Hey Mycroft, tell me about the weather`

Julie's *intent* is to find out about the weather (probably in her current location).

An **intent parser** can then match the *intent* with a suitable **Skill** to handle the *intent*.

* [Adapt intent parser](https://github.com/MycroftAI/adapt): Adapt is the default intent parser for all Mycroft platforms. Adapt was developed by Mycroft and is available under an open source license.

* [Padatious](https://github.com/MycroftAI/padatious): Padatious is a neural network based intent parser. Padatious is currently under active development by Mycroft and is available under an open source license. It is likely that some Mycroft platforms will switch to using Padatious in the future instead of Adapt.

### Text to Speech

Text to Speech (TTS) software takes written text, such as as in text files on a computer, and uses a *voice* to *speak* the text. Text to Speech can have different voices, dependenting on the TTS engine used.

* [Mimic](https://github.com/MycroftAI/mimic): Mycroft's default text to speech (TTS) engine, based on CMU's Flite (Festival Lite)

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

[Mycroft Skills Management (msm)](https://github.com/MycroftAI/msm) is a set of helper scripts that assist in the installation and management of **Skills**.

### Devices and Enclosures

Mycroft is designed to run on many different platforms - called **Devices**, with different hardware, called **Enclosures**.

* **Mark 1** - a software image of Mycroft designed to be installed on the Mycroft Mark 1 - a reference hardware device
* **Picroft** - a software image of Mycroft designed to be installed on Raspberry Pi 3
* **Android** - a software image of Mycroft designed to be installed on Android devices

## Choosing to use Mycroft

### Why would you choose to use Mycroft over alternatives such as Amazon™ Alexa™, Google Assistant™, Microsoft Cortana™ or Apple's Siri™?

Great question!

While alternative tools are readily available, and easy to use, they come with some pretty big downsides.

#### Open source

Mycroft is open source. This means that the code used by Mycroft can be inspected, copied, modified, and contributed back to the Mycroft community for everyone to enjoy.

Tools like Amazon™ Alexa™, Google Assistant™, Microsoft Cortana™ or Apple's Siri™ are _black boxes_. That is, you can't look inside them, and see what they do - or importantly - _how_ they do it. And while they may allow you some flexibility to create new **Skills**, these are usually strictly controlled. Mycroft gives you freedom, flexibility and control over how your want _your_ voice assistant to work. Mycroft is AI for _everyone_.

Mycroft code is licensed under the [Apache 2 open source license](https://en.wikipedia.org/wiki/Apache_License).

#### Respecting your privacy

Mycroft uses _opt-in privacy_. This means we will only record what you say to Mycroft with your explicit permission. Don't want us to record your voice? No problem! If you'd like us to help Mycroft become more accurate, you can opt in to have your voice anonymously recorded.

You're welcome to view our [privacy policy](https://home.mycroft.ai/#/privacy-policy)

#### More hardware, more choices

Mycroft runs on a wide range of software platforms and hardware - meaning that you can run Mycroft on the **Devices** _you_ want. Try Mycroft on a Raspberry Pi, on an Android device - or on your Linux desktop.

#### Lightweight

Mycroft is lightweight, and will run on low-powered hardware, such as the Raspberry Pi 3. So if you're a Hacker, Maker or Hobbyist, it's the perfect platform for low cost experimentation.

#### Community

Mycroft has a vibrant, engaged and helpful community. You can interact with the community via:

* Chat - [https://chat.mycroft.ai](https://chat.mycroft.ai)
* Forum - [https://community.mycroft.ai](https://community.mycroft.ai)
