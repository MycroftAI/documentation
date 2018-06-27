---
ID: 39037
post_title: >
  Myzilla! Mycroft at the Mozilla All
  Hands
author: Steve Penrod
post_excerpt: >
  Mycroft attended the 2018 Mozilla All
  Hands in San Francisco to share learning
  and help plan the future of voice
  technology.
layout: post
permalink: >
  https://mycroft.ai/blog/myzilla-mycroft-at-the-mozilla-all-hands/
published: true
post_date: 2018-06-27 10:00:05
---
For the last year, Mycroft and <a href="https://www.mozilla.org" target="_blank" rel="noopener">Mozilla</a> have been building a relationship based on our shared interests. I was invited to join them at their company get together last week and want to share info about the event and what we've been up to this year.
<h1>Mozilla All Hands</h1>
Every six months the entire global Mozilla organization gets together in one physical location to share knowledge via presentations and organized sessions, to plan the next six months, and to let collaborators meet face-to-face. As someone who has worked in remote teams for the past 20 years, I can attest to the value of being in the same space to build camaraderie and rapidly share ideas.

As part of these All Hands, Mozilla also invites a number of "volunteers" from outside the company. These are individuals who aren't paid by Mozilla, but who work closely with the organization. This year, I was included in this group.

The Spring 2018 All Hands was June 11 - 15 in San Francisco. In all, approximately 1200 employees and 70 volunteers attended.
<h1>Overlapping Interests</h1>
There is quite a bit of common ground between what Mycroft and Mozilla are doing. Mycroft has, obviously, been working on voice interaction tech. Additionally, the level of access we have to hardware makes Mycroft a great platform for Internet of Things (IoT) interaction and control. We currently can combine voice with control of equipment like <a href="https://www2.meethue.com/en-au" target="_blank" rel="noopener">Hue lights</a>, IoT hubs like <a href="https://www.wink.com/" target="_blank" rel="noopener">Wink</a>, or larger ecosystems like <a href="https://www.home-assistant.io/" target="_blank" rel="noopener">Home Assistant</a>. Additionally, we are able to work with hardware directly, reacting to<a href="https://www.raspberrypi.org/documentation/usage/gpio/" target="_blank" rel="noopener"> GPIO pins</a> connected to switches and sensors. Plus we are able to communicate on local networks with equipment within the home.

These capabilities overlap with several Mozilla teams...
<h1><a href="https://research.mozilla.org/machine-learning/" target="_blank" rel="noopener">Machine Learning</a> / DeepSpeech</h1>
Our tightest collaboration thus far is with the <a href="https://github.com/mozilla/DeepSpeech" target="_blank" rel="noopener">DeepSpeech</a> team. Kelly Davis and crew have been implementing the DeepSpeech speech-to-text architecture, and Mycroft has been one of the earliest actual consumers of the technology. Mycroft can currently use DeepSpeech running on Mycroft Home cloud or from your own private instance.

We are also both working on implementations of the <a href="https://ai.googleblog.com/2017/12/tacotron-2-generating-human-like-speech.html" target="_blank" rel="noopener">Tacotron</a> text-to-speech architecture. Mycroft has a Mimic2 implementation and has created a complete 15-hour dataset we are using for a joint voice benchmark.

DeepSpeech is young (currently version 0.2.0-alpha.6) and still rapidly evolving on both the code and the published models. The current model is noticeably weak in noisy environments and with rapid, conversational speech. The Mycroft community is providing access to the kind of data needed to train a model to handle this. I'm very excited about what we can achieve jointly!

[caption id="attachment_39078" align="aligncenter" width="2592"]<img class="size-full wp-image-39078" src="https://mycroft.ai/wp-content/uploads/2018/06/Mozilla_MachineLearning_Team.jpg" alt="Mozilla's Machine Learning team" width="2592" height="1943" /> With the Mozilla's Machine Learning team (missing Reuben, sorry!)[/caption]
<h1><a href="https://voice.mozilla.org/" target="_blank" rel="noopener">Common Voice</a></h1>
Mozilla began Common Voice to gather the kind of language data needed for building technologies like DeepSpeech. While their <a href="https://creativecommons.org/share-your-work/public-domain/cc0/" target="_blank" rel="noopener">CC0</a> (aka "public domain") data licensing model is different to Mycroft's OpenVoice dataset, the collaborative ethos is very similar. We are sharing technical and social learning about working with a community to achieve better things together in data gathering and tagging – for a spectrum of languages.

Through this team, I met with another volunteer, Dewi Jones of the University of Bangor in Wales. He and I had several discussions about what it will take to build a fully-functional Welsh Mycroft as part of their <a href="http://techiaith.cymru/" target="_blank" rel="noopener">Welsh Language Technology</a> program. FFantastig!

[caption id="attachment_39077" align="aligncenter" width="2429"]<img class="size-full wp-image-39077" src="https://mycroft.ai/wp-content/uploads/2018/06/Mozilla_CommonVoice_Team.jpg" alt="Mozilla's Common Voice team" width="2429" height="1366" /> With the Mozilla's Common Voice team[/caption]
<h1><a href="https://iot.mozilla.org/" target="_blank" rel="noopener">Project Things</a></h1>
This new IoT framework looks to simplify and unify the physical world with web technologies into a Web of Things. Mozilla integrated <a href="https://mycroft.ai/documentation/adapt" target="_blank" rel="noopener">Mycroft's Adapt intent parser</a> into the platform several months ago to simplify working with all sorts of natural language commands. They are also working hard on their <a href="https://iot.mozilla.org/gateway/" target="_blank" rel="noopener">Things Gateway</a> built on the Raspberry Pi where Mycroft/Picroft would obviously offer some powerful possibilities.

[caption id="attachment_39079" align="aligncenter" width="4032"]<img class="size-full wp-image-39079" src="https://mycroft.ai/wp-content/uploads/2018/06/Mozilla_ProjectThings_Team.jpg" alt="Mozilla's Project Things team" width="4032" height="1960" /> With the Mozilla's Project Things team[/caption]
<h1>Scout</h1>
This caused a bit of a stir in the <a href="https://www.cnet.com/news/mozilla-working-on-scout-a-voice-controlled-web-browser-project/" target="_blank" rel="noopener">tech journalism</a> world! I won't say much, but really Scout is just an early experiment in how consumers think of voice technologies and how they might interact in collaboration with, and independently of, a screen. Mozilla has spent almost all of its existence developing the technologies for today's web, and these are inherently visual. We are all learning how consumers think of speech differently than written text.
<h1>And More...</h1>
Both Mycroft and Mozilla are very focused on enabling and representing the user, not vice versa. This is a particularly tricky thing to do in the data-driven machine learning world. Our efforts in collaborative data gathering and tagging, remote and federated learning, data ownership and licensing are leading the way to a powerful <strong>AND</strong> ethical future.

<strong>I believe <em>trust</em> is a new economic benchmark, and one at which both our organizations excel.</strong>

I really enjoyed finally meeting old and new colleagues face to face and look forward to what we can do together in the future!
<div class="mceTemp"></div>