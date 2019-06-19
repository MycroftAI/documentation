---
ID: 48212
post_title: 'The State of i18n &#8211; The Internationalization of Mycroft'
author: Kris Gesling
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/the-state-of-i18n-the-internationalization-of-mycroft/
published: true
post_date: 2019-06-19 10:00:20
---
Mycroft has always aimed to be the AI voice assistant for everyone. We believe that everyone has digital rights and these must include equality of access and privacy, regardless of what language you speak.

This month, we hit a new milestone in that quest. One thousand multilingual Community Members have contributed over 100,000 translations to Mycroft across almost 50 languages!

This is exciting progress, and we know there are already Community Members actively using Mycroft in many of these languages. In response, we wanted to take the time to give a rundown of where all that progress is going, and the steps we have ahead of us in the journey to make Mycroft more linguistically accessible to users everywhere.
<h2>How do I use Mycroft in my language?</h2>
First, the bad news. At the moment, we only officially support Mycroft in English, but that doesn’t mean you can’t try it out. Using Mycroft in other languages is still experimental, requires editing configuration files, and most likely some troubleshooting efforts. Whilst we can’t support everyone going through this process, we want to make it as easy as possible for those who have the time and patience to give it a go. Here’s a brief walkthrough of the four components you’ll adjust to use Mycroft in another language.
<h3>Speech to Text and Text to Speech</h3>
We continue to collaborate with Mozilla on their DeepSpeech STT engine. The data contributed by our Opt-In users provides valuable real-life samples for their <a href="https://voice.mozilla.org/">CommonVoice</a> dataset. Through this initiative, Mozilla are making excellent progress. There have been over 20,000 individuals that have submitted more than 400,000 samples in 70 different languages. Unfortunately, these services aren’t yet available for public usage.

This means we don’t yet have native support for other languages in Mycroft’s STT and TTS engines. However, this is one of the reasons we intentionally designed Mycroft in a modular way. We don’t think you should be restricted to using what Mycroft can provide, and thankfully there are a number of existing services available from the likes of Bing, eSpeak, Google, IBM, Mary, and Wit AI.

For more details on these and how to use them with Mycroft, check out our more detailed <a href="https://mycroft.ai/documentation/languages/">Languages documentation</a>.
<h3>Skills</h3>
Thanks to our amazing Community from around the globe, our <a href="https://translate.mycroft.ai/">Translate platform</a> has been facilitating the translation of Skills in almost 50 different languages. More than half of the Skills in the Marketplace have been translated into Dutch, French, German, Italian, Spanish, and Swedish, with a number of other languages catching up quickly.

There has been incredible progress made here, but there’s a lot more we can do. We know the process of managing Skill and translation submissions can be improved, and there are plenty of ways we can improve the platform itself. If you speak more than one language and want to contribute, sign up at <a href="https://translate.mycroft.ai/">https://translate.mycroft.ai/</a> to start translating!
<h3>Mycroft Core</h3>
The final piece needed for complete support is the language parsing and formatting tools available in Mycroft Core known as <a href="https://github.com/MycroftAI/lingua-franca">Lingua Franca</a>. This library is what allows Mycroft to both understand and respond with naturally expressed dates, numbers and times. As an example, if you want an alarm for next Friday, Lingua Franca can determine what date that refers to. Or if we want to respond that a movie is showing on the 25th, that makes much more sense to a human as “next Tuesday”.

There are a lot of incredibly helpful functions provided through this library, and because they relate to the semantics and syntax of language, they differ greatly between languages.

Again, thanks to the incredible contributions of the Community, these are currently available for French, German, Hungarian, Italian, Portuguese, and Swedish. There is also active progress being made on Danish, Dutch, and Spanish.
<h2>How can I help?</h2>
<h3>Translate Skills</h3>
As you can probably tell, we think pretty highly of our Community and everything they do. If you speak multiple languages and are keen to help out, please sign up to <a href="https://translate.mycroft.ai/">Mycroft Translate</a> if you haven’t already.
<h3>Contribute Code</h3>
If you are also a developer, take a look at <a href="https://github.com/MycroftAI/lingua-franca">Lingua Franca</a> and consider adding support for your own language. Definitely come chat with the Community in the <a href="https://chat.mycroft.ai/community/channels/languages">Languages channel on Chat</a> too.
<h3>Nominate to join our new Mycroft Internationalization (i18n) Team</h3>
Finally, if you want to help us take Mycroft to the world, consider nominating yourself to join our newest Community Team.

There are 7.5 billion people on our planet, and only 400 million speak English as a first language. How can we continue developing Mycroft as a technology, a project, and a community, to reach the other 7 billion?

The Mycroft Internationalization (i18n) Team will help us answer this question by providing strategic guidance and oversight of the internationalization of Mycroft AI. This includes the moderation of <a href="https://translate.mycroft.ai/">Mycroft Translate</a>, as well as informing the continued development of <a href="https://github.com/MycroftAI/lingua-franca">Lingua Franca</a>, our text parsing and formatting library, and <a href="https://mycroft.ai/initiatives/">other Mycroft technologies</a> to better meet the needs of our global Community.
<h4>Requirements</h4>
Nominating members must:
<ul>
 	<li>Be fluent in at least one language other than English</li>
 	<li>Commit to meeting at least monthly by video chat</li>
 	<li>Have a basic understanding of Mycroft</li>
</ul>
All members of the i18n Team are active leaders in our Community, demonstrating their passion for bringing open source voice technologies to the world. They are open and honest in their interactions and value the diversity of skills and experience that our contributors bring.

If this sounds like you, then join a fantastic group of like-minded people from around the world by completing a nomination today. It looks great on your CV or academic service record too!

&nbsp;

[ninja_form id=4]