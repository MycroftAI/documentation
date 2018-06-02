---
ID: 37508
post_title: 'Training Deep Speech: How you can help'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/training-deep-speech-how-you-can-help/
published: true
post_date: 2018-05-07 10:00:15
---
<span style="font-weight: 400;">Last month we released <a href="https://mycroft.ai/blog/deepspeech-update/" target="_blank" rel="noopener">DeepSpeech support for Mycroft</a>.  Many have now tried it and been, well, underwhelmed by the performance.  Was this a colossal failure?</span>
<h1><span style="font-weight: 400;">Welcome to the Evolution</span></h1>
<span style="font-weight: 400;">Short answer:  Nope, this isn’t a failure at all.  DeepSpeech is behaving exactly as we expected.</span>

<span style="font-weight: 400;">The data that Mozilla has used to train DeepSpeech so far is largely from individuals reading text on their computer.  A bit also came from speakers at conferences. In both cases, the person in the recordings is very careful to speak plainly and directly into a microphone.  So DeepSpeech learned to understand speech, but only </span><i><span style="font-weight: 400;">clear</span></i><span style="font-weight: 400;"> speech like it was trained on.  No slurred words or yelling from across the room.</span>

<span style="font-weight: 400;">Like many interesting problems, the first pass isn’t perfect.  But without it there would never be a second, third or fourth pass.</span>
<h1><span style="font-weight: 400;">Machine Learning Loops</span></h1>
<span style="font-weight: 400;">The exciting thing about this step is that we have created a machine learning loop.  We took an imperfect dataset, trained on it to produce a model, and now we are using this model to create more data to place in a better dataset.</span>

<span style="font-weight: 400;">In the next few weeks, you will see a new tagger at Home for validating the voice data we have collected.  This will create an invaluable </span><i><span style="font-weight: 400;">real-world</span></i><span style="font-weight: 400;"> voice dataset to include in the training.  The Mycroft Open Voice Dataset. Mozilla will be granted access to it to complete this machine learning loop.</span>

<span style="font-weight: 400;">Wash.  Rinse. Repeat.  Every time this cycle completes things will be a little bit better.</span>
<h1><span style="font-weight: 400;">Let Your Voice be Heard!</span></h1>
<span style="font-weight: 400;">The voices in the dataset are exclusively from those who have chosen to Opt-In.  At Mycroft we will never use your data without your explicit permission. So far over 2,500 of you have chosen to join us in this effort, and we can’t thank you enough for your trust and contributions.</span>

<span style="font-weight: 400;">But there is a secret… by contributing to this dataset you are literally training the technology to recognize </span><i><span style="font-weight: 400;">your</span></i><span style="font-weight: 400;"> voice.  Eventually the tech will evolve to work for virtually everyone, but initially, it will be slightly biased to recognize the voice and pronunciation variants of those in the training data.</span>

<span style="font-weight: 400;">If you want to participate, go to Home and check </span><a href="https://home.mycroft.ai/#/setting/basic" target="_blank" rel="noopener"><span style="font-weight: 400;">Opt-In under your settings</span></a><span style="font-weight: 400;">.  Joining is easy, and changing your mind later is just as easy.  Working together -- Mycroft and Mozilla on the technology, you and the Mycroft community on the data -- we are creating the foundation of an open </span><i><span style="font-weight: 400;">AI for Everyone</span></i><span style="font-weight: 400;">!</span>