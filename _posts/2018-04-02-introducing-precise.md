---
ID: 36910
post_title: 'Help us improve Wake Word precision: Introducing Precise Tagger'
author: Kathy Reid
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/introducing-precise/
published: true
post_date: 2018-04-02 12:59:36
---
In November 2017, <a href="http://mycroft.ai/blog/release-notes-0-9-5-introducing-precise/">we introduced Precise</a> - a <a href="https://en.wikipedia.org/wiki/Keyword_spotting">Wake Word listener</a> to replace the PocketSphinx engine. Precise was <a href="http://mycroft.ai/blog/were-in-beta-how-to-update-to-18-02b/">recently promoted to be the default Wake Word listener</a> for all Mycroft Devices. You might remember that Precise and PocketSphinx work in different ways. PocketSphinx recognises a Wake Word based on a speech to text translation - that is, it tries to recognize <em>words</em>. Precise takes a different approach. Instead of trying to match words, it matches based on <em>sounds</em> - think of a wave form rather than a typed string.

In order to make Precise more accurate, <a href="http://mycroft.ai/team/">Matthew from our Developer Team</a> has recently released Precise Tagger. It's a tool to train the <a href="https://en.wikipedia.org/wiki/Artificial_neural_network">neural network</a> that helps Precise distinguish between four different conditions:
<ul>
 	<li><strong>False positive:</strong> Precise detects a phrase as a Wake Word, when it is not a Wake Word</li>
 	<li><strong>Correct negative:</strong> Precise detects that a phrase is not a Wake Word correctly</li>
 	<li><strong>Correct positive:</strong> Precise detects correctly that a phrase is a Wake Word</li>
 	<li><strong>False negative:</strong> Precise does not detect a phrase as a Wake Word, when it is a Wake Word</li>
</ul>
It's super easy to help train Precise to be more accurate.

Precise Tagger will provide you with a Wake Word sample, contributed by one of the over two thousand Mycroft Community members who have opted in to providing completely anonymized open data. You will be presented with three options to 'tag' the sample  - just like the below image. Simple!

<a href="https://mycroft.ai/wp-content/uploads/2018/04/precise-tagger-button-options.png"><img class="alignnone size-full wp-image-36911" src="https://mycroft.ai/wp-content/uploads/2018/04/precise-tagger-button-options.png" alt="precise-tagger-button-options" width="659" height="391" /></a>

<a href="https://training.mycroft.ai/precise">Go to Precise Tagger and help us make Precise Wake Word listener even more accurate</a>

At the moment the tagging counter doesn't mean a lot - it's not yet integrated into home.mycroft.ai, but we're considering how we will built this into a rewards program for Mycroft Community contributors. But still, who doesn't want to be top of the leaderboard?!