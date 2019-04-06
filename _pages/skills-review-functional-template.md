---
ID: 46228
post_title: Skills Functional Review Template
author: Kris Gesling
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/skills/skills-acceptance-process/skills-review-functional-template/
published: true
post_date: 2019-04-05 22:02:43
---
## Meta  
* Who: [@your-github-handle](https://github.com/your-github-handle) / @your-mycroft-chat-handle  
* Datestamp: run `date +%Y-%m-%d_%H:%M:%S_%Z`  
* Language and dialect of tester:

## 3. Functional Review - intuitive and expected  
- [ ] **Installation**

Check that the Skill installs using voice commands. Mycroft will get the user to confirm which Skill should be installed if there is ambiguity in Skill names - such as duplicate names. If possible, name the Skill so that there is minimal duplication and/or conflict. You should also verify that the Skill name can be verbally pronounced by speaking the Skill name into the Mycroft command line several times, and reading the resulting transcriptions. Suggest alternative Skill names if it is difficult to verbally pronounce the Skill name. Please provide confirmation that the Skill was successfully installed and by what means (voice or `mycroft-msm install`), as well as what utterance was detected when invoking the install voice command.

> Install method:  
> Output:  
> ```  
>  
>  
> ```  
>  
> Checking that STT transcribes correctly:  
> ```  
>  
>  
> ```

- [ ] **Settings**  
If Skill includes a `settingsmeta.json` file - are the settings well laid out? Does the placeholder text make sense? This can also be checked on [home.mycroft.ai/#/skill](https://home.mycroft.ai/#/skill)

>

- [ ] **Dialog**

Check the `dialog` directory to ensure that from a voice user interface perspective the dialogs read well. Alway play every `dialog` phrase on the command line by doing `say ` so that you can check how the `dialog` is spoken. It is a good idea to run the `dialog` phrases through [mimic](https://mycroft.ai/documentation/mimic/).

Sometimes the `dialog` files will need a small tweak such as a space between words, or extra vowel sounds, to sound realistic. Sometimes words don't render as expected and alternative wording should be used. Some of the tricks you might need to use include separating words by a space - such as `sub sonic` instead of `subsonic`, or `broad cast` instead of `broadcast`.

>

#### Skill Functions  
For each function of the Skill add a new checkbox with the utterance used to invoke the functionality. Confirm the output and behaviour of each. If any setup is required to perform these tests please indicate this directly before the test is described.

- [ ] **"Are there unread messages on Mycroft Chat"**

>

- [ ] **"Name Mycroft Chat channels with unread messages"**

>

- [ ] **"Read all unread Mycroft Chat messages"**

>

- [ ] **"Read messages for the channel {name}"**

>

- [ ] **"Begin monitoring of Mycroft Chat"**

>

- [ ] **"Stop monitoring of Mycroft Chat"**

>

### Actions Required
A short list of any _Actions Required_. It is also great to provide a short statement of your impressions from using the Skill.
*