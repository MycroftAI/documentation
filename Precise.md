---
post_title: Precise
layout: page
published: false
---

# Precise

Precise is a **Wake Word Listener**. Like its name suggests, a **Wake Word Listener**'s job is to continually listen to sounds and speech around the **Device**, and activate when the sounds or speech match a **Wake Word**.

By default, Mycroft uses [PocketSphinx](https://github.com/cmusphinx/pocketsphinx) as the **Wake Word Listener** for each Mycroft **Device**. Precise is an alternative to PocketSphinx.

## How do I install Precise as my **Wake Word Listener**?

To install Precise instead of PocketSphinx as your **Wake Word**, Speak to your **Device**:

`hey mycroft, set the Listener to precise`

Mycroft will respond

`The download has begun. This may take anywhere from between 20 seconds to 2 minutes`

_NOTE: As Precise is installing, it will download a 70Mb file to your **Device**. During this initial download period, your **Device** will not be able to respond to a **Wake Word**._

## What's the difference between PocketSphinx and Precise?

PocketSphinx recognizes **Wake Words** based on the [CMU Flite dictionary of sounds](http://www.speech.cs.cmu.edu/cgi-bin/cmudict). In contrast, Precise is based on a neural network that is trained on _sound patterns_ rather than _word patterns_. This reduces the dependence it has on particular languages or accents.

## How can I tell on my Device if Precise is the Wake Word Listener?

@TODO not sure how to do this
