---
ID: 39970
post_title: translate
author: Steve Penrod
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/translate/
published: true
post_date: 2018-08-08 14:19:04
---
<h1>Internationalization</h1>
<span style="font-weight: 400;">As the open source world’s voice assistant Mycroft needs to represent everyone.  That means understanding and speaking hundreds of local languages. Each language represents a new challenge and a new opportunity to connect with a population that wants to use this technology in their native language.</span>

<span style="font-weight: 400;">Supporting local languages is important because it facilitates creativity and entrepreneurship in communities that are not necessarily at the heart of the technology revolution.  That means giving people who speak Farsi or Navajo the same access to innovation as people who speak English or Mandarin. The net result is a more level playing field with new opportunities for everyone from students to entrepreneurs.</span>

<span style="font-weight: 400;">We are committed to supporting as many languages as possible, but we are going to need help.  Though our team is from places as diverse as Sweden, Brazil, Czech Republic, we don’t even come close to being able to translate into the hundreds of languages we’d like to support.  We’ve been working on some tools over the past few months to make translation easier and we’re now ready to roll out the first alpha versions.</span>
<h1>Overview</h1>
Supporting a language fully requires several independent but related processes.  The major pieces are the Mycroft Text, Text to Speech (TTS), and Speech to Text (STT).
<h3>1) Text defining the Mycroft interaction</h3>
At the lowest level, the verbal interaction with Mycroft gets converted to text for processing, then back again to be spoken to you.  So the majority of the interaction level is defined with text files.  The most important step in localizing the interaction is translating these text files.

Our localization is managed using an open set of tools called Pootle.  The Mycroft translation suite can be found here:  <a href="https://translate.mycroft.ai">https://translate.mycroft.ai </a> (<em>Coming Soon!</em>)

This tool is the hub for translating all Mycroft Core technology and all the Skills built by both the Mycroft AI team and by the community.  This is a straightforward and generally well understood translation process.
<h3>2) Text to Speech engine</h3>
Unlike most simple apps on a phone or computer, supporting a voice agent requires literally teaching it to talk!  With Mycroft, this happens through machine learning with several steps.  The process is very similar to teaching a child to the relationship between written language and spoken language by reading books out loud to them.

The steps of the process are:
<ul>
 	<li>Build the language "corpus" (list of phrases)
Each language needs around 15,000 phrases:  <a href="https://docs.google.com/spreadsheets/d/1NHLe0C8Ajk-oS22qxe81Ulj50ALCzcVnxmm1JLByiDc">Icelandic</a></li>
 	<li>Read the language corpus out loud.
<em>This requires a sizable portion of the full corpus to begin.  The Mycroft interaction phrases also help build this corpus.</em></li>
 	<li>Train the Mimic voice on the language
<em>Mycroft AI will provide the computing resources and expertise for this</em></li>
 	<li>Publish the trained voice</li>
</ul>
<h3>3) Speech to Text engine</h3>
The last and most difficult piece is teaching the agent to understand human speech.  While the Text to Speech can be done by a single dedicated individual, Speech to Text requires a community.  Recordings of hundreds of voices are needed to make this work well.

The steps of the process are:
<ul>
 	<li>Record transcribed voice utterances
The phrases can be predefined, as is done with Mozilla's <a href="https://voice.mozilla.org/">Common Voice</a>; or recordings can be transcribed and validated after the fact.  Both are valuable.</li>
 	<li>Train DeepSpeech using the recordings and transcriptions</li>
 	<li>Publish a trained Speech to Text model</li>
</ul>
Mycroft is working <a href="https://mycroft.ai/voice-mycroft-ai/">in conjunction with Mozilla</a> to gather and build this technology for each language.
<h1>Join Us</h1>
Contact us at <a href="mailto:translate@mycroft.ai">translate@mycroft.ai</a> for more information on how join in to bring this to your native tongue!

&nbsp;