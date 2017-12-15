---
ID: 32442
post_title: Developing Skills for Mycroft
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/skills/developing-skills/
published: true
post_date: 2017-12-03 06:39:38
---
# Developing Skills for Mycroft

Are you looking for the [system-generated documentation for the Mycroft Skills API?](http://mycroft-core.readthedocs.io/en/stable/)

## Prerequisites

Before starting to develop **Skills** for Mycroft, you should already have these prerequisites:

* You should have a basic understanding of the [Python programming language](https://www.python.org/).
* You should be familiar with version control using [Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control), and [GitHub basics](https://guides.github.com/activities/hello-world/) such as forking and committing.
* You should have a basic understanding of [regular expressions](https://regexr.com/).
* You should have a basic understanding of [conversational user interface](https://en.wikipedia.org/wiki/Voice_user_interface), a subset of [user experience](https://en.wikipedia.org/wiki/User_experience).

## An overview of Mycroft components

If you haven't yet read the [overview of Mycroft components](http://mycroft.ai/documentation/mycroft-software-hardware/), it's worth doing so. 

## What makes a good **Skill**?

There are many components to what mkes a good **Skill**.

* **Fulfilling a need the user has**: Good **Skills** meet one or more needs the user has. Popular **Skills** are popular because people use them frequently - for instance to set alarms, reminders, and to identify the time in other time zones. On the other hand, a **Skill** that, say, recites π to a 100 digits might be pretty cool, but when was the last time you needed to know π to 100 digits? Contrast that with the last time you set a reminder on your phone.

* **Having an easy to use voice interface**: Just like a web page that has thought put into the user interface is much more pleasant to use, a **Skill** that has a well designed voice interface is a delight, not a chore, to use. You should anticipate the task the user is trying to accomplish, and how to make that as straightforward as possible.

If you have an idea for a **Skill**, it's a great idea to join [Mycroft Chat](https://chat.mycroft.ai), specifically the [~skills](https://chat.mycroft.ai/community/channels/skills) channel, and share what your plans are. You'll be able to get constructive and helpful feedback on your **Skill** from an experienced community.

## The Mycroft Skill Manager (MSM)

The [Mycroft Skills Manager](https://mycroft.ai/documentation/msm/) - MSM - is a tool that is being increasingly used to find, deploy and resolve dependencies within **Skills**. It is important that you make your Skills compliant with `msm` so that they are easy to find and install in the future.