---
ID: 32976
post_title: Precise
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?page_id=32976
published: false
---
# Precise

- [Precise](#precise)
  * [How do I install Precise as my **Wake Word Listener**?](#how-do-i-install-precise-as-my-wake-word-listener)
  * [What's the difference between PocketSphinx and Precise?](#whats-the-difference-between-pocketsphinx-and-precise)
  * [How can I tell on my Device if Precise is the Wake Word Listener?](#how-can-i-tell-on-my-device-if-precise-is-the-wake-word-listener)

Precise is a **Wake Word Listener**. Like its name suggests, a **Wake Word Listener**'s job is to continually listen to sounds and speech around the **Device**, and activate when the sounds or speech match a **Wake Word**.

By default, Mycroft uses [PocketSphinx](https://github.com/cmusphinx/pocketsphinx) as the **Wake Word Listener** for each Mycroft **Device**. Precise is an alternative to PocketSphinx.

## How do I install Precise as my **Wake Word Listener**?

To install Precise instead of PocketSphinx as your **Wake Word**, Speak to your **Device**:

`hey mycroft, set the Listener to precise`

Mycroft will respond

`Downloading the new listener, this will take a bit and you won't be able to use me until it completes. Give me a minute before attempting to activate me again. `

_NOTE: As Precise is installing, it will download a 40Mb file to your **Device**. During this initial download period, your **Device** will not be able to respond to a **Wake Word**._

## How do I tell which **Wake Word Listener** my Mycroft **Device** is using?

To find out which **Wake Word Listener** is active for the Mycroft **Device** you are using, simply Speak:

`hey Mycroft, what is the listener`

or

`hey Mycroft, tell me what listener you are using`

If you are using Precise, Mycroft will respond:

`The current listener is Precise`

## What's the difference between PocketSphinx and Precise?

PocketSphinx recognizes **Wake Words** based on the [CMU Flite dictionary of sounds](http://www.speech.cs.cmu.edu/cgi-bin/cmudict). In contrast, Precise is based on a neural network that is trained on _sound patterns_ rather than _word patterns_. This reduces the dependence it has on particular languages or accents.
