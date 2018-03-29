---
ID: 36814
post_title: DeepSpeech in Mycroft
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/deepspeech-update/
published: true
post_date: 2018-03-28 23:42:00
---
Lots has been quietly happening over the last few months around DeepSpeech. Today I'll share what's coming out now and what to expect in the coming weeks and months.
<h1>Mycroft and Mozilla</h1>
For the last 9 months or so, Mycroft has been working with the <a href="https://research.mozilla.org/machine-learning/">Mozilla DeepSpeech team</a>. Their new open-source speech to text (STT) engine was shiny with promise and looking for use cases.  Mycroft had started the <a href="https://openstt.org/">OpenSTT</a> initiative to identify and/or build a strong and open STT technology.  The pair looked like a natural match, so we got to know each other.

Back in <a href="https://mycroft.ai/blog/mycroft-speech-to-text-and-balance/">January</a> we announced our intention to make DeepSpeech the default engine for Mycroft.  This is one of the first widespread uses of DeepSpeech and pushes both teams.
<h1>First Steps</h1>
For several months core Mycroft developers have been experimenting with DeepSpeech as a <a href="https://github.com/MycroftAI/mycroft-core/pull/1370">local Mycroft STT engine</a>.  This has been a really exciting option and shows the promise of the Mycroft architecture -- allowing a personal assistant that keeps things between the two of you.

However, the current state of the art DeepSpeech system requires a powerful GPU to run at the kind of speed you want for a personal assistant. While it  <em>can</em> run on a slower GPU or even directly on a basic CPU, those configurations will be much slower than needed for a personal assistant. In one example it took 15 seconds to transcribe 5 seconds of audio on a reasonably modern CPU.  That is painfully slow.

On top of this, the setup of DeepSpeech on your own computer or on a server you personally control isn't super simple.  Even for an experienced developer it takes hours to get things downloaded, installed and configured.
<h1>Road to Mass Adoption</h1>
Given the challenges above, we decided to put in extra effort to make this easy for everyone to use.  We've created a shared pool of GPU equipped machines that can run DeepSpeech as a service for Mycroft users.  This provides a really easy on-ramp for everyone. No extra hardware or difficult configuration required.

This also puts the burden of keeping up with the latest developments in DeepSpeech on us. Several foundational changes to DeepSpeech are coming down the pike -- things like streaming transcription.  These advances will require starting from scratch on the server setup. Like any emerging technology, keeping up with changes will be a challenge.
<h1>Trying Thing Out</h1>
As of the mycroft-core 18.2.3 release, you can configure the STT module to use DeepSpeech. This is intended for developers initially while we shake out any glitches on the system. Details can be found on the <a href="https://github.com/MycroftAI/mycroft-core/pull/1503">mycroft-core PR</a>.

If the above is all Greek to you, that's OK. In a few weeks we will add a button to the <a href="https://home.mycroft.ai/#/setting/advanced">Home Settings page</a> that will let you easily switch to DeepSpeech.
<h1>Just Getting Started</h1>
This may appear to be the end of things, but it really is just the beginning.  Like any machine learning system, the quality of the result is directly tied to how well the training data represents the use case.

If you used Google's voice recognition technology when it first came out, remember how error-prone it was initially.  Using Android to acquire <a href="https://venturebeat.com/2015/08/11/google-details-how-it-cut-google-voice-transcription-error-rates-by-50/">voicemails for millions of people</a> they were able to rapidly create a huge and varied training data set.  This led to the outstanding system they have today.
<h1>We need your help!</h1>
The Mycroft system is perfect for doing the same thing for DeepSpeech that cellphones did for Google. Currently DeepSpeech is trained on people reading texts or delivering public speeches. These speakers were careful to speak clearly and directly into the microphone. As a result, DeepSpeech of today works best on clear pronunciations.

What Mycroft and those who volunteer to assist will be providing is <em>real world</em> audio.   Hundreds of "What'sDaWeatha like?" utterances in different accents and from different ages and types of voices will provide the kind of data it takes to build DeepSpeech into what we need for a personal assistant.

Please join us by choosing to <a href="https://home.mycroft.ai/#/setting/basic">Opt In to the Open Dataset</a>. We promise to respect your data and privacy -- and we are working hard to <a href="http://www.dailymail.co.uk/sciencetech/article-5553573/Facebook-never-sell-information-says-Mark-Zuckerberg-2009.html">guarantee this is more than just an empty promise</a>.

Thank you for supporting Mycroft and for joining us in building better technology for everyone!