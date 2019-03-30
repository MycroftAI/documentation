---
ID: 44396
post_title: Skills Review Template
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  https://test.mycroft.ai/skills-review-template/
published: true
post_date: 2019-03-29 12:13:25
---
# Skills Review Template
The overall [Skills Acceptance Process](https://mycroft.ai/documentation/skills/skills-acceptance-process/) is outlined in the Mycroft Documentation.

This template is provided to make it easier for testers to complete the process and provide relevant feedback to Skill Authors. An example of the completed process can be found on [this Pull Request](https://github.com/MycroftAI/mycroft-skills/pull/844#issuecomment-460913234). If you have any other questions or comments, please raise them in the [Skill Testing Team Chat](https://chat.mycroft.ai/community/channels/skill-testing-team).

The process has been split into three parts:
1. Code review - ensuring the code is stable and secure;
2. Information review - ensuring all info is accurate and understandable; and
3. Functional review - ensuring the experience of using the Skill is intuitive.

Testers can choose to conduct one or more of these reviews at a time, and once completed the review should be posted as a comment on the relevant [Pull Request (PR)](https://github.com/MycroftAI/mycroft-skills/pulls). Once all reviews are completed with no outstanding `Actions Required`, the Skill will be merged into the repo and automatically added to the [Mycroft Marketplace](https://market.mycroft.ai/skills).

## Instructions for use
Each post back to a PR must contain:
- Meta block - detail on the tester, and test environment
- One or more review blocks - 1. Code, 2. Information, and/or 3. Functional
- Summary block - list of any _Actions Required_ and additional comments

Each test starts with a checkbox. To mark a test successful, add an 'x' to the markdown checkbox like so:  
- [ ]  Test that has not yet been conducted, or is not considered passed
- [x]  Test that has been completed and passed  
> Please add comments about the outcome of the test, including any output generated into these block quotes following each test.

_Action Required: For any actions required by the Skill Author, please use this syntax and include it in the appropriate test, as well as in the summary section at the bottom._

## Meta
*   Platform:
*   Mycroft-core version:
*   Who: [@your-github-handle](https://github.com/your-github-handle) / @your-mycroft-chat-handle
*   Datestamp: run `date +%Y-%m-%d_%H:%M:%S_%Z`
*   Language and dialect of tester:

## 0. Automated tests
Are all automated tests passing?  
- [ ] Skill tester - Jenkins
- [ ] Continuous Integration - Travis-CI

## 1. Code Review - secure and stable
- [ ]   **Code Quality**  
Can you understand what the code is doing? Is there inline documentation? Do you have any concerns about this code running on your machine? Are there any performance issues such as nested or infinite loops? Do you have significant concerns about the overall code quality?
_NOTE: We do not enforce PEP8 Checks on Skills_

>

- [ ]   **Error Handling**  
Are there any specific checks we make for error handling or graceful degradation?

>

- [ ]   **Libraries**  
Does the Skill include the correct libraries? Does it use too many libraries or dependencies?

>

- [ ]   **Required Dependencies**  
Check `requirements.txt` and `requirements.sh` - are the required dependencies listed? If `requirements.sh` is used, is some form of conditional processing done to match against multiple distros? Often Skill Authors will add requirements.txt using only an “library=1.x.x” instead of “library >=1.x.x”. Check to make sure that there is an equal or greater than in the requirements to help future-proof the Skill, unless a _specific_ version is needed.

>

- [ ]   **Settings**  
Is the `settingsmeta.json` file well laid out? If settings are not used, has the default file been deleted? If it is the default file, the first setting section will be called "Options << Name of section".

>

- [ ]   **Integration Tests**
Does the skill include sufficient integration tests, included in the `test` folder?

>

- [ ]   **Other Files**  
Are there any other files included that are unnecessary or you are unsure of their function?

>


## 2. Information Review - accurate and understandable
This review checks the README for completeness - does it follow the README template and include all the relevant sections such as Intents, known issues, dependencies and so on?

- [ ]   **Icon**   
Does the Skill have an appropriate icon that is either included in the repo or linked from an appropriate place (eg raw.githack.com not privateicons.com or rawgit.com)?

>

- [ ]   **Description**  
Are the title, short description, and long description (under 'About') clear and concise? Do they provide enough information to understand what the Skill does? Does the title have the word "skill" included? This is strongly discouraged.

>

- [ ]   **Examples**  
Do the examples give you a clear understanding of how you can use the Skill? Is there a single example per dot-point?

>

- [ ]   **Supported Devices**  
If relevant, are the supported devices listed? An example might be a Skill that requires the screen of the Mark II. If the section is not present, all devices are considered supported.

>

- [ ]   **Categories**  
Is there at least one category listed? At least one category must be selected for the Skill to be displayed correctly in the [Mycroft Marketplace](https://market.mycroft.ai).  
Is the bolded category the most appropriate for this Skill? The bold category is considered the primary category and will be used for display in the [Marketplace](https://market.mycroft.ai/), all others are secondary and used for search results.

>

- [ ]   **Tags**  
Are listed tags appropriate for this Skill?

>

- [ ]   **License**  
Is an appropriate LICENSE file used in the repo - such as Apache-2.0 or GPL-3.0?

>


## 3. Functional Review - intuitive and expected
- [ ]   **Installation**

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

- [ ]   **Settings**  
If Skill includes a `settingsmeta.json` file - are the settings well laid out? Does the placeholder text make sense? This can also be checked on [home.mycroft.ai/#/skill](https://home.mycroft.ai/#/skill)

>

- [ ]   **Dialog**  

Check the `dialog` directory to ensure that from a voice user interface perspective the dialogs read well. Alway play every `dialog` phrase on the command line by doing `say <your dialog phrase here>` so that you can check how the `dialog` is spoken. It is a good idea to run the `dialog` phrases through [mimic](https://mycroft.ai/documentation/mimic/).   

  Sometimes the `dialog` files will need a small tweak such as a space between words, or extra vowel sounds, to sound realistic. Sometimes words don't render as expected and alternative wording should be used.  Some of the tricks you might need to use include separating words by a space - such as `sub sonic` instead of `subsonic`, or `broad cast` instead of `broadcast`.

>

#### Skill Functions
For each function of the Skill add a new checkbox with the utterance used to invoke the functionality. Confirm the output and behaviour of each. If any setup is required to perform these tests please indicate this directly before the test is described.

- [ ]   **"Are there unread messages on Mycroft Chat"**

>

- [ ]   **"Name Mycroft Chat channels with unread messages"**

>

- [ ]   **"Read all unread Mycroft Chat messages"**

>

- [ ]   **"Read messages for the channel {name}"**

>

- [ ]   **"Begin monitoring of Mycroft Chat"**

>

- [ ]   **"Stop monitoring of Mycroft Chat"**

>


## Summary
A short list of any _Actions Required_. It is also great to provide a short statement of your impressions.
*   

Once you have completed any updates, you can update this pull request by running `mycroft-msk submit /path/to/skill/directory`
