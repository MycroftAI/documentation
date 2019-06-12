---
ID: 48091
post_title: Hey Mycroft, Listen to Me!
author: Nate Tomasi
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/hey-mycroft-listen-to-me/
published: true
post_date: 2019-06-12 16:00:49
---
I’ve been at Mycroft for 24 months now, and one of my major challenges is that my wife hardly uses our Mark I at home. I am passionate about Mycroft, and I want my family to see all the hard work that we put into this product.

To be fair, my wife, Ashley, doesn’t really like voice assistants. She hates Siri, and the other ones we have had she just views as an annoying “Nate” toy. But, her challenge with Mycroft is different. It’s a lot like the issue a Community Member voiced on Twitter recently.
<blockquote class="twitter-tweet" data-conversation="none" data-lang="en">
<p dir="ltr" lang="en">The voice system doesn't recognize my voice. So it's</p>
Me: "Mycroft, turn on the light."

*nothing*

"ANDY, MAKE MYCROFT TURN ON THE LIGHT!"

Andy: "Mycroft, turn on the light."

*light comes on*

I would rather just flip a switch.

— Katie (@katiek_wanders) <a href="https://twitter.com/katiek_wanders/status/1131261924006612992?ref_src=twsrc%5Etfw">May 22, 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<h2>The Problem</h2>
To make a product that uses Machine Learning as a key pillar of the technology, there are a lot of things that have to come together, but at the root it is all about data. Clean, diverse, and accessible data. The giants that are in this space have budgets to buy data, buy companies, and trick their users into always giving up privacy for the use of the product.

At Mycroft, we are presented with a real challenge, because at the heart of our company is Privacy and User Agency. What that means is we do not by default store any recordings, transcriptions, or data when people use Mycroft. To obtain the data we need to improve Mycroft, we ask those who are comfortable to <a href="https://mycroft.ai/blog/privacy-machine-learning-open-data-set-opt-feature/">contribute to our Open Dataset</a>. Contributing means specifically Opting-In to share your recordings, transcriptions, and usage data. Once Opted-In you have the right to Opt-Out and delete your dataset at any time.

The more people across different genders, accents, and ages that Opt-In, the more diverse the dataset is that trains our Precise wakeword model. You can do this in under a minute at https://account.mycroft.ai/profile! Please consider it!

<iframe src="https://www.youtube.com/embed/lnMz8qjdXt8" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

Now we are in an almost humorous Catch-22 scenario. Mycroft only hears my wife 50% of the time. So even if she is using it at the same frequency as me, the utterances submitted will be only half of what I donate to the dataset. Magnify that across the portion of our Community that has Opted-In, and now you have a ratio that is not reflective of the makeup of the world.
<h2>The Solution</h2>
We're developing a three-pronged approach here at Mycroft.

First, we need more people with varying voices to use the device and Opt-In. This builds the dataset.

We then need to tag those utterances, using the Precise Tagger which we’ll relaunch soon. We then train new global Precise models on those utterances, improving accuracy.

Lastly, we need to think outside the box for edge cases. For this last approach, we have started work to build a local machine learning tool which allows people to directly train their wake word on-device.
<h2>Personal Precise Trainer</h2>
This personal Precise trainer will let an individual record themselves speaking the wake word a few times, then perform a training on top of the general wake word model, creating a custom model which is immediately available and just for themselves.

This approach brings several benefits. For one, Mycroft is immediately able to recognize voices previously missed by the global model. Additionally, this system sets the stage for potential future features like speaker identification.

We will also add the ability to submit the local recordings to the global model, allowing you to improve the global model for others who sound like you. This is all early work, but experimental results have been very promising!

This will not be an easy or quick problem to solve, but from what I have seen so far it appears to be the right approach to design, develop, test, and release for you all.