---
ID: 46396
post_title: >
  Yes, humans listen to smart speaker
  recordings. Can it be done right?
author: Eric Jurgeson
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/yes-humans-listen-to-smart-speaker-recordings-can-it-be-done-right/
published: true
post_date: 2019-04-17 13:00:22
---
On April 11, 2019, stories began making the rounds highlighting that Amazon employs thousands of people worldwide to transcribe users' Alexa queries to help improve the Alexa software. The <a href="https://www.bloomberg.com/news/articles/2019-04-10/is-anyone-listening-to-you-on-alexa-a-global-team-reviews-audio" target="_blank" rel="noopener noreferrer">original Bloomberg article</a> reports “Amazon ... doesn’t explicitly say humans are listening to recordings of some conversations picked up by Alexa. 'We use your requests to Alexa to train our speech recognition and natural language understanding systems,' the company says in a list of frequently asked questions.”

To us at Mycroft, this wasn’t exactly groundbreaking news. Other companies might not make it easily known that the audio from your interactions is key to improving the software and that humans are still needed to evaluate the recordings. We want you to know that is absolutely the case, be it at Amazon, Google, Apple, or even Mycroft. At Mycroft, we give our Community a clear choice whether to have their data stored and used to improve the software or not. Read on to learn more.
<h2>Voice software needs voice data</h2>
Voice technology has come a long way, but isn't past the point of needing humans in the loop. STT like <a href="https://github.com/mozilla/DeepSpeech" target="_blank" rel="noopener noreferrer">Mozilla DeepSpeech</a> is rapidly improving but still not totally accurate. NLP is able to do more and more every day, but doesn’t keep up with context, ambiguity, or multi-part requests like a human could. TTS engines like <a href="https://github.com/MycroftAI/mimic2" target="_blank" rel="noopener noreferrer">Mycroft's Mimic2</a> sound more natural than ever but trip over words at times. These issues need human review to improve. It's fair to presume any voice tech, from full assistants to the speech recognition on your phone, still use humans in the loop.

So if all assistants require some human intervention to improve, what makes Mycroft different? If you use Mycroft, by default you are not sharing your data and Mycroft is not storing it. On other platforms, users must dig around in the settings in order to exclude themselves from training sets or delete their recordings. These options are often buried and obscure.

But as said above, data and human review are needed to improve these technologies, Mycroft included. To bridge that gap, Mycroft offers users the <a href="https://mycroft.ai/blog/privacy-machine-learning-open-data-set-opt-feature/" target="_blank" rel="noopener noreferrer">choice to Opt-In to our datasets</a>. Only once a user has provided explicit permission will their anonymized usage data be shared to Mycroft’s Open Dataset. Then, they can be used to improve our Wake Word spotting, STT, NLP, TTS, and overall software. If an Opted-In user decides to Opt-Out, all their audio files, logs, and other information <span style="background-color: #f6d5d9;">are </span>scrubbed from the datasets.

<a href="https://mycroft.ai/wp-content/uploads/2019/04/MycroftVACUUM_all.png"><img class="alignnone wp-image-46512 size-full" src="https://mycroft.ai/wp-content/uploads/2019/04/MycroftVACUUM_all.png" alt="Mycroft takes voice assistant privacy seriously. Mycroft does not store users recordings unless given explicit permission." width="1200" height="600" /></a>

We think giving our users the choice of whether to have their interactions used for Mycroft’s improvement builds trust in our brand and product. More than 15% of Mycroft’s registered users have raised their hands as contributors to our Open Datasets. Our tagging is done by the Community, and help other projects like Mozilla DeepSpeech.
<h2>Why data - and privacy - are important</h2>
There are caveats, though. Machine learning engines gain accuracy based on how much good data they are trained on. This is why companies like Google and Amazon currently have an upper hand in these technologies. They have massive datasets to train their models on. Additionally, machine learning engines perform especially well on new inputs similar to data they are trained on. As such, an Opted-In user should have their experience greatly improved while helping Mycroft improve overall. In the case of other assistants, a new user's recordings and interactions are fed into the models, improving the experience for themselves from the moment they sign up.

Privacy and user agency is one of the biggest challenges in the tech world. At Mycroft, we lean towards giving users more choice and control. That’s why we only save and use data from those that choose to Opt-In, and are developing other options for privacy-conscious users, like the <a href="https://github.com/MycroftAI/personal-backend" target="_blank" rel="noopener noreferrer">Personal Backend</a>.

We should also note, it is possible for users to <a href="https://www.tomsguide.com/us/how-to-stop-amazon-listen-recordings,news-29851.html" target="_blank" rel="noopener noreferrer">opt-out of Alexa using their recordings</a> for these purposes, and to delete recordings individually. But it still seems, according to Bloomberg's reporting, that Alexa would rather not explicitly tell their users what happens with their recordings. But, they'll still legally cover that option in their Terms of Use.

No one will become the leader in this industry without taking some hits. <a href="https://mycroft.ai/blog/early-stages-of-voice-technology-coupling-privacy-and-user-agency/" target="_blank" rel="noopener noreferrer">We’ve said as much before.</a> But putting privacy first and designing the product around the desires of our Community should help Mycroft along. If you agree, don't forget to share the idea when talking about voice technology.

For another view on the topic, our friends at <a href="https://voicebot.ai/2019/04/12/yes-humans-behind-alexa-and-other-voice-assistants-are-listening-to-some-user-utterances-the-technology-requires-it-to-get-better/" target="_blank" rel="noopener noreferrer">Voicebot AI put together a post</a> and collected examples of both industry insider and consumer sentiment on the news.