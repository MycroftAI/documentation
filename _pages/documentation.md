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

Welcome to the documentation for all elements of Mycroft - the open source voice assistant.

Our documentation, just like our source code, is open source, [and you can contribute to improving it here](https://github.com/MycroftAI/docs-rewrite). Alternatively, please rate our documentation and leave comments on how we can improve.

- [Documentation Home](#documentation-home)
  * [About Mycroft](#about-mycroft)
      + [Contributing](#contributing)
      + [Roadmap](#roadmap)
      + [Glossary](#glossary)
  * [Getting Mycroft](#getting-mycroft)
  * [Your home.mycroft.ai account](#your-home-mycroft-ai-account)
      + [Basic commands](#basic-commands)
  * [Mark 1](#mark-1)
  * [Picroft](#picroft)
      + [Configuring Picroft audio for USB, HDMI and Bluetooth](#configuring-picroft-audio-for-usb-hdmi-and-bluetooth)
      + [Manually configuring WiFi for Picroft](#manually-configuring-wifi-for-picroft)
      + [Reconfiguring automatic updates for Picroft](#reconfiguring-automatic-updates-for-picroft)
  * [Mycroft for Linux platforms](#mycroft-for-linux-platforms)
  * [Mycroft for Docker](#mycroft-for-docker)
  * [Mycroft for Android](#mycroft-for-android)
  * [`mycroft-conf` file](#mycroft-conf-file)
  * [Mycroft Logs](#mycroft-logs)
  * [Mycroft Skills](#mycroft-skills)
      + [Developing Skills for Mycroft](#developing-skills-for-mycroft)
      + [Introduction to developing Skills for Mycroft](#introduction-to-developing-skills-for-mycroft)
      + [Automatic testing for Mycroft Skills](#automatic-testing-for-mycroft-skills)
      + [Preparing your Skill for submission to the Mycroft Skills Repo](#preparing-your-skill-for-submission-to-the-mycroft-skills-repo)
      + [Mycroft Skills Kit](#mycroft-skills-kit)
      + [Skills Acceptance Process](#skills-acceptance-process)
      + [Skill Settings](#skill-settings)
      + [Common issues in Skills development](#common-issues-in-skills-development)
      + [Repurposing Skills developed for other platforms](#repurposing-skills-developed-for-other-platforms)
      + [Conversational Context](#conversational-context)
      + [Audio Service](#audio-service)
      + [Display Control](#display-control)
      + [Fallback Skills](#fallback-skills)
	  + [Common Play Framework](#common-play-framework)
  * [Mycroft Skill Manager](#mycroft-skill-manager)
  * [Message Bus](#message-bus)
  * [Other languages in Mycroft](#language-support-in-mycroft)
  * [Adapt](#adapt)
      + [Adapt examples](#adapt-examples)
      + [Adapt tutorial](#adapt-tutorial)
  * [Mimic](#mimic)
  * [Mimic Recording Studio](#mimic-recording-studio)
  * [Precise](#precise)
  * [Padatious](#padatious)
  * [Troubleshooting and known errors](#troubleshooting-and-known-errors)
      + [Audio troubleshooting](#audio-troubleshooting)
  * [Getting help and support](#getting-help-and-support)
  
## [About Mycroft](http://mycroft.ai/documentation/mycroft-software-hardware/)

This is a useful starting point, and provides an overview of all the elements of the Mycroft ecosystem.

### [Contributing](https://mycroft.ai/documentation/contributing/)

Aimed at developers, our Contributing section provides detailed instructions on how to contribute to Mycroft.

### [Roadmap](https://mycroft.ai/documentation/mycroft-roadmap/)

Aimed at developers and investors, our Roadmap illustrates our key development effort and goals.

### [Glossary](https://mycroft.ai/documentation/glossary/)

A handy reference of all new terms you might come across while working with Mycroft.

## [Getting Mycroft](https://mycroft.ai/documentation/getting-mycroft/)

How to download and install Mycroft for your preferred **Device** or platform.

## [Your home.mycroft.ai account](https://mycroft.ai/documentation/home-mycroft-ai-pairing/)

How to pair your **Device** with home.mycroft.ai, and set basic configuration fields such as location.

### [Basic commands](https://mycroft.ai/documentation/basic-commands/)

Getting started using Mycroft Skills.

## [Mark 1](https://mycroft.ai/documentation/mark-1/)

In depth information about the Mark 1 reference hardware **Device**.

## [Picroft](https://mycroft.ai/documentation/picroft/)

In depth information about the Picroft build of Mycroft for Raspberry Pi.

### [Configuring Picroft audio for USB, HDMI and Bluetooth](https://mycroft.ai/documentation/picroft/picroft-audio/)

Learn how to configure your Raspberry Pi 3 to output audio via USB, HDMI and Bluetooth

### [Manually configuring WiFi for Picroft](https://mycroft.ai/documentation/picroft/picroft-wifi/)

Are you on an enterprise network? The automated WiFi network connection process not working? Learn how to manually configure WiFi.

### [Reconfiguring automatic updates for Picroft](https://mycroft.ai/documentation/picroft/picroft-automatic-update/)

Want to turn off automatic updates? Change what time they occur? Learn how to manually configure updates.

## [Mycroft for Linux platforms](https://mycroft.ai/documentation/linux/)

In depth information on how to build Mycroft for common Linux distributions.

## [Mycroft for Docker](http://mycroft.ai/documentation/docker/)

How to build Mycroft in a Docker container either by building an image or pulling the image off Docker Hub.

## [Mycroft for Android](https://mycroft.ai/documentation/android/)

In depth information on the Mycroft companion app for Android.

## [`mycroft-conf` file](https://mycroft.ai/documentation/mycroft-conf/)

Learn about the `mycroft.conf` file and the settings it contains. 

## [Mycroft Logs](https://mycroft.ai/documentation/logs/)

Information about which logs Mycroft keeps, where they are located, and useful diagnostic commands.

## [Mycroft Skills](https://mycroft.ai/documentation/skills/)

An overview of the Skills that can be installed on your Mycroft **Device**.

### [Developing Skills for Mycroft](https://mycroft.ai/documentation/skills/developing-skills/)

Learn about the prerequisites of a **Skill**, and what makes a good Skill.

### [Introduction to developing Skills for Mycroft](https://mycroft.ai/documentation/skills/introduction-developing-skills/)

Take your next step in Developing **Skills** for Mycroft. Learn about the structure of a **Skill**, and how to start creating your own.

### [Automatic testing for Mycroft Skills](https://mycroft.ai/documentation/skills/automatic-testing/)

Learn how to use the Integration Test Runner for automatic testing of your Mycroft Skills. 

### [Skills acceptance process](https://mycroft.ai/documentation/skills/skills-acceptance-process/)

Read more about the process used by Skill Authors, the Skill Management Team and Mycroft staff to ensure the robustness and quality of Skills in the Mycroft AI ecosystem. 

### [Preparing your Skill for submission to the Mycroft Skills Repo](https://mycroft.ai/documentation/skills/skill-submission/)

Aimed at developers, this is a step by step guide to submitting a new Skill you've developed to the Mycroft Skills Repo.

### [Mycroft Skills Kit](http://mycroft.ai/documentation/skills/msk/)

Learn how to use the Mycroft Skills Kit to make the creation, testing and submission of Skills a lot easier.

### [Skill Settings](https://mycroft.ai/documentation/skills/skill-settings/)

Aimed at Developers, this is a step by step guide to storing and retrieving persistent settings that your Skill needs.

### [Common issues in Skills development](https://mycroft.ai/documentation/skills/common-issues-in-skills-development/)

Explanations of common issues developers encounter in building new **Skills**, and helpful advice for overcoming them.

### [Repurposing Skills developed for other platforms](https://mycroft.ai/documentation/skills/repurposing-skills/)

Already develop for another voice assistant? Learn how to transfer those skills to Mycroft.

### [Conversational Context](https://mycroft.ai/documentation/skills/conversational-context/)

Want to add more natural interaction to Mycroft? Conversational context allows a **Skill** to add context to the **Intent Parser** to create a more natural interaction style.

### [Audio Service](https://mycroft.ai/documentation/skills/audio-service/)

The Audio Service handles playback of audio files within a **Skill**. If your **Skill** deals with audio files, you'll want to know about the Audio Service.

### [Display Control](https://mycroft.ai/documentation/skills/display-control/)

Display Control manages features of the **Enclosure**, such as the _mouth_ and _eyes_ on the Mark 1.

### [Fallback Skills](https://mycroft.ai/documentation/skills/fallback-skill/)

Fallback **Skills** handle an **Intent** if one can't be matched with an **Utterance** and are a useful catch-all. This documentation shows how to write a new Fallback **Skill** and set its order of precedence.

### [Common Play Framework](https://mycroft.ai/documentation/skills/common-play-framework/)

Learn how to use the `CommonPlaySkill` class instead of the regular `MycroftSkill` class to develop **Skills** which use the `play` keyword.

## [Mycroft Skill Manager](https://mycroft.ai/documentation/msm/)

Learn how to use `msm` to install, search and update **Skills**. Includes a comprehensive list of `msm` error codes, and how to resolve them. 

## [Message Bus](https://mycroft.ai/documentation/message-bus/)

Aimed at advanced Skill Authors, learn how the Mycroft `MessageBus` is used to emit and consume messages. 

## [Mycroft in other languages](https://mycroft.ai/documentation/languages)

Learn more about languages in Mycroft, and all the components that have to be in place to support additional languages.

## [Adapt](https://mycroft.ai/documentation/adapt/)

Learn more about the Adapt Intent Parser, which matches spoken words with **Intents**.

### [Adapt examples](https://mycroft.ai/documentation/adapt/adapt-examples/)

Examples of the different types of **Intent Parsing** supported by Adapt.

### [Adapt tutorial](https://mycroft.ai/documentation/adapt/adapt-tutorial/)

A tutorial on writing **Intent Parsers** using Adapt.

## [Mimic](https://mycroft.ai/documentation/mimic/)

Learn about the Mimic Text to Speech (TTS) tool.

## [Mimic Recording Studio](https://mycroft.ai/documentation/mimic-recording-studio/)

Learn about the Mimic Recording Studio that uses a corpus of phrases to help you make voice recordings that can be used in your own TTS voice. 

## [Precise](https://mycroft.ai/documentation/precise/)

Precise is a **Wake Word Listener** that listens and then 'wakes up' Mycroft, ready to hear your commands and questions.

## [Padatious](https://mycroft.ai/documentation/padatious/)

Padatious is an **Intent parser**. Unlike [Adapt](http://mycroft.ai/documentation/adapt/), which is based on Speech to Text, Padatious is trained on sounds.

## [Troubleshooting and known errors](https://mycroft.ai/documentation/troubleshooting/)

Stuck? Learn common tricks and techniques for resolving common errors.

### [Audio troubleshooting](http://mycroft.ai/documentation/troubleshooting/audio-troubleshooting/)

Audio is one of the most common areas that requires troubleshooting. 

## Getting help and support
Need to chat things over with a human? No problem. You can join our [Chat](https://chat.mycroft.ai), [Forum](https://community.mycroft.ai) or [make contact via this web form](https://mycroft.ai/contact).