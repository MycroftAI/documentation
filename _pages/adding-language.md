---
ID: 32452
post_title: Adding a new language to Mycroft
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/language-support/adding-language/
published: true
post_date: 2017-12-03 06:53:37
---
# Adding a new language to Mycroft

_NOTE: This documentation is a work in progress and is not yet complete_

The Mycroft software suite has many elements. Adding language support for Mycroft means that each of those elements has to support the new language. This page walks you what has to be done for each of the elements. This is currently a significant undertaking; it is complex and will require some development and Linux system administration knowledge. 

* Wake Word: When you Speak 'Hey Mycroft, do something', you are invoking a **Wake Word**. To change your **Wake Word** to another language, you need to install libraries for that language, and configure your **Wake Word** so that it has phonemes available in the library. 
* Speech to Text: Mycroft is designed to be modular, so you can choose which Speech to Text engine you use. You need to find and configure a Speech to Text engine for your language. 
* Text to Speech: Again, Mycroft is designed to be modula, so you can choosen which Text to Speech engine you use. You need to find and configure a Text to Speech engine for your language. 
* Skills: To support a language, a Skill must have `vocab` and `dialog` entries for that language. 

See additional documentation for these languages: 

* [French](https://mycroft.ai/documentation/language-support/french/)
* [German](https://mycroft.ai/documentation/language-support/german/)
* [Spanish](https://mycroft.ai/documentation/language-support/spanish/)
* [Italian](https://mycroft.ai/documentation/language-support/italian/)
* [Portuguese](https://mycroft.ai/documentation/language-support/portuguese/)

## Wake Word

To change the **Wake Word**, you will need to install libraries for [PocketSphinx](https://cmusphinx.github.io/wiki/download/), then ensure that the foreign language dictionary contains phonemes for the **Wake Word** you want to use. 

## Speech to text (STT)

Speech to text (STT) is the part of Mycroft that translates spoken words into text. That text is then used by intent parsers, and then by **Skills**.

In order to support a new language, a Speech to Text engine (STT engine) must be available.

STT engines are made available by different vendors, and they each have different licenses and usage restrictions.

_NOTE: As of late 2017, Mycroft.AI is working with Mozilla Voice to build an open source STT engine for multiple languages. This development will occur over 2018_

* [List of languages supported by Google STT](https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti)
* [List of languages supported by IBM Watson Bluemix](https://www.ibm.com/watson/developercloud/speech-to-text/api/v1/#sessionless_methods)
* [List of languages supported by Wit.AI](https://wit.ai/faq)

_NOTE: PocketSphinx is not currently supported on Mycroft_

Once you've found an STT engine for your language, you will need to configure Mycroft to use it. This is done through the [mycroft.conf](https://mycroft.ai/documentation/mycroft-conf/) file. 

## Text to Speech

In order to support a new language, a Text to Speech (TTS) engine must be available.

TTS engines are made available by different vendors, and they each have different licenses and usage restrictions.

Once you've found an TTS engine for your language, you will need to configure Mycroft to use it. This is done through the [mycroft.conf](https://mycroft.ai/documentation/mycroft-conf/) file. 

## Skills

In order to support a new language, individual **Skills** must support that language too. 

[See here for more information on how Skills are structured](https://mycroft.ai/documentation/skills/introduction-developing-skills/#structure-of-the-skill-repo) - **Skills** have different `vocab` and `dialog` for each language they support.