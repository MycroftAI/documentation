---
ID: 32458
post_title: Mycroft Documentation
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/documentation/
published: true
post_date: 2017-12-02 22:35:25
---
# Documentation Home

Welcome to the documentation for all elements of the Mycroft - the open source voice assistant.

Our documentation, just like our source code, is open source, [and you can contribute to improving it here](https://github.com/MycroftAI/docs-rewrite). Alternatively, please rate our documentation and leave comments on how we can improve.

@TODO The links here won't work yet because they're linking to GitHub; fixing them will be one of the steps of the documentation implementation plan.

- [Documentation Home](#documentation-home)
  * [About Mycroft](#about-mycroft)
    + [Contributing](#contributing)
    + [Release notes](#release-notes)
    + [Roadmap](#roadmap)
    + [Glossary](#glossary)
  * [Getting Mycroft](#getting-mycroft)
  * [Your home.mycroft.ai account](#your-homemycroftai-account)
    + [Basic commands](#basic-commands)
  * [Mark 1](#mark-1)
  * [Picroft](#picroft)
  * [Mycroft for Linux platforms](#mycroft-for-linux-platforms)
  * [Mycroft for Android](#mycroft-for-android)
  * [Mycroft Skills](#mycroft-skills)
    + [Introduction to developing Skills for Mycroft](#introduction-to-developing-skills-for-mycroft)
    + [Preparing your Skill for submission to the Mycroft Skills Repo](#preparing-your-skill-for-submission-to-the-mycroft-skills-repo)
    + [Skill Settings](#skill-settings)
    + [Common issues in Skills development](#common-issues-in-skills-development)
    + [Repurposing Skills developed for other platforms](#repurposing-skills-developed-for-other-platforms)
    + [Conversational Context](#conversational-context)
    + [Audio Service](#audio-service)
    + [Display Control](#display-control)
    + [Fallback Skills](#fallback-skills)
  * [Language support in Mycroft](#language-support-in-mycroft)
    + [Configuring Mycroft for French language support](#configuring-mycroft-for-french-language-support)
    + [Configuring Mycroft for Italian language support](#configuring-mycroft-for-italian-language-support)
    + [Configuring Mycroft for German language support](#configuring-mycroft-for-german-language-support)
    + [Configuring Mycroft for Spanish language support](#configuring-mycroft-for-spanish-language-support)
  * [Adapt](#adapt)
    + [Adapt examples](#adapt-examples)
    + [Adapt tutorial](#adapt-tutorial)
  * [Mimic](#mimic)
  * [Precise](#precise)
  * [Padatious](#padatious)
  * [FAQ](#faq)
  * [Troubleshooting and known errors](#troubleshooting-and-known-errors)
    + [Known errors and workarounds](#known-errors-and-workarounds)
  * [Getting help and support](#getting-help-and-support)

## [About Mycroft](About-Mycroft.md)

This is a useful starting point, and provides an overview of all the elements of the Mycroft ecosystem.

### [Contributing](Contributing-to-Mycroft.md)

Aimed at developers, our Contributing section provides detailed instructions on how to contribute to Mycroft.

### [Release notes](Release-Notes.md)

Release notes for all major **Devices**, such as Mark 1 and Picroft.

### [Roadmap](Mycroft-Roadmap.md)

Aimed at developers and investors, our Roadmap illustrates our key development effort and goals.

### [Glossary](Mycroft-Glossary.md)

A handy reference of all new terms you might come across while working with Mycroft.

## [Getting Mycroft](Getting-Mycroft.md)

How to download and install Mycroft for your preferred **Device** or platform.

## [Your home.mycroft.ai account](Your-home.mycroft.ai-account-and-Pairing-your-Devices.md)

How to pair your **Device** with home.mycroft.ai, and set basic configuration fields such as location.

### [Basic commands](Basic-commands-to-get-started-with-Mycroft.md)

Getting started using Mycroft Skills.

## [Mark 1](Mark-1.md)

In depth information about the Mark 1 reference hardware **Device**.

## [Picroft](Picroft.md)

In depth information about the Picroft build of Mycroft for Raspberry Pi.

## [Mycroft for Linux platforms](Mycroft-for-Linux.md)

In depth information on how to build Mycroft for common Linux distributions.

## [Mycroft for Android](Mycroft-for-Android.md)

In depth information on the Mycroft companion app for Android.

## [Mycroft Skills](Skills.md)

An overview of the Skills that can be installed on your Mycroft **Device**.

### [Introduction to developing Skills for Mycroft](Introduction-to-developing-Skills.md)

Aimed at developers, this section is an introduction to developing new Skills for Mycroft

### [Preparing your Skill for submission to the Mycroft Skills Repo](Preparing-your-Skill-for-submission-to-the-Mycroft-Skills-Repo.md)

Aimed at developers, this is a step by step guide to submitting a new Skill you've developed to the Mycroft Skills Repo.

### [Skill Settings](Skill-Settings.md)

Aimed at Developers, this is a step by step guide to storing and retrieving persistent settings that your Skill needs.

### [Common issues in Skills development](Common-issues-in-Skills-development.md)

Explanations of common issues developers encounter in building new **Skills**, and helpful advice for overcoming them.

### [Repurposing Skills developed for other platforms](Repurposing-Skills-developed-for-other-platforms.md)

Already develop for another voice assistant? Learn how to transfer those skills to Mycroft.

### [Conversational Context](Conversational-Context.md)

Want to add more natural interaction to Mycroft? Conversational context allows a **Skill** to add context to the **Intent Parser** to create a more natural interaction style.

### [Audio Service](Audio-Service.md)

The Audio Service handles playback of audio files within a **Skill**. If your **Skill** deals with audio files, you'll want to know about the Audio Service.

### [Display Control](Skill-Display-Control.md)

Display Control manages features of the **Enclosure**, such as the _mouth_ and _eyes_ on the Mark 1.

### [Fallback Skills](Fallback-Skill.md)

Fallback **Skills** handle an **Intent** if one can't be matched with an **Utterance** and are a useful catch-all. This documentation shows how to write a new Fallback **Skill** and set its order of precedence.

## [Language support in Mycroft](Language-support-in-Mycroft.md)

Learn more about languages support in Mycroft.

### [Configuring Mycroft for French language support](Language-support-in-Mycroft-8211-French.md)

Parlez-vous français? Follow these steps to change Mycroft's language to French (BCP 47: fr)

### [Configuring Mycroft for Italian language support](Language-support-in-Mycroft-8211-Italian.md)

Parli italiano? Follow these steps to change Mycroft's language to Italian (BCP 47: it)

### [Configuring Mycroft for German language support](Language-support-in-Mycroft-8211-German.md)

Sprechen Sie Deutsch? Follow these steps to change Mycroft's language to German (BCP 47: de)

### [Configuring Mycroft for Spanish language support](Language-support-in-Mycroft-8211-Spanish.md)

Puedes hablar español? Follow these steps to change Mycroft's language to Spanish (BCP 47: es)

## [Adapt](Adapt.md)

Learn more about the Adapt Intent Parser, which matches spoken words with **Intents**.

### [Adapt examples](Adapt-Examples.md)

Examples of the different types of **Intent Parsing** supported by Adapt.

### [Adapt tutorial](Adapt-Tutorial.md)

A tutorial on writing **Intent Parsers** using Adapt.

## [Mimic](Mimic.md)

Learn about the Mimic Text to Speech (TTS) tool.

## [Precise](Precise.md)

Precise is a **Wake Word Listener** that listens and then 'wakes up' Mycroft, ready to hear your commands and questions.

## [Padatious](Padatious.md)

Padatious is an **Intent parser**. Unlike [Adapt](Adapt.md), which is based on Speech to Text, Padatious is trained on sounds.

## [FAQ](FAQ.md)

Our most frequently asked questions

## [Troubleshooting and known errors](Troubleshooting-and-known-errors.md)

Stuck? Learn common tricks and techniques for resolving common errors.

## Getting help and support

<<<<<<< HEAD:_drafts/Mycroft-Documentation.md
Need to chat things over with a human? No problem. You can join our [Chat](https://chat.mycroft.ai), [Forum](https://community.mycroft.ai) or [make contact via this web form](https://mycroft.ai/contact).
=======
TBA
>>>>>>> bdb1ccc79459c2ab91bfce146b33223e95df0182:_pages/documentation.md