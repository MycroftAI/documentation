---
ID: 36808
post_title: Skills Acceptance Process
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/skills/skills-acceptance-process/
published: true
post_date: 2018-04-04 08:43:20
---
# Skills acceptance process

- [Skills acceptance process](#skills-acceptance-process)
  * [Objective](#objective)
  * [Overview](#overview)
  * [Autotest of Skills](#autotest-of-skills)
  * [Testing by Skill Author and Mycroft Community](#testing-by-skill-author-and-mycroft-community)
    + [Template for directions on how to test a Skill](#template-for-directions-on-how-to-test-a-skill)
      - [YOUR SKILL NAME GOES HERE](#your-skill-name-goes-here)
      - [How to install SKILL NAME](#how-to-install-skill-name)
      - [How to test SKILL NAME](#how-to-test-skill-name)
      - [Where feedback on SKILL NAME should be directed a](#where-feedback-on-skill-name-should-be-directed-a)
  * [Peer review by Skill Management Team](#peer-review-by-skill-management-team)
    + [Template for Skill Management Team Review](#template-for-skill-management-team-review)
      - [Review of `skill-name`](#review-of-skill-name)
        * [Standard checks (non-code checks)](#standard-checks-non-code-checks)
    + [What are the labels used on the `mycroft-skills` repo?](#what-are-the-labels-used-on-the-mycroft-skills-repo)
    + [What happens if the Skill Management Team can't test the Skill?](#what-happens-if-the-skill-management-team-cant-test-the-skill)
      - [Python code checks of the Skill](#python-code-checks-of-the-skill)
  * [Review by Mycroft AI](#review-by-mycroft-ai)
  * [Deployment](#deployment)
  * [Promotion](#promotion)

## Objective

The objective of this document is to outline how Skills are tested, reviewed, deployed and promoted. It is vital that Mycroft Skills exhibit high quality, and are well tested to encourage adoption, and ongoing development of the platform. This process contributes to that goal by providing a structured framework to follow to ensure repeatable outcomes.

It is intended that this process will be iterated over time; PRs and Issues can be raised on this process at the GitHub link given at the bottom of the document.

## Overview

The key parts of this process are;

1. Automatic testing of Skills
2. Testing by Skill Author and Mycroft Community
3. Peer review by Skill Management Team
4. Review by Mycroft AI
5. Deployment of Skill
6. Promotion of Skill

## Autotest of Skills

We've developed an Integration Test Runner that assists you in writing tests that can be executed at both an **Intent** and a **Skill** level. [Learn more about Automatic Testing of your Mycroft Skill](https://mycroft.ai/documentation/skills/automatic-testing/).

## Testing by Skill Author and Mycroft Community

During this stage of the process, the Skill Author undertakes testing, makes improvements and continutes iterating until he/she/they believe that the Skill is ready for other members of the Mycroft Community to test the Skill. The Mycroft Community then tests the Skill, and provides feedback to the Skill Author.

To aid in this step, the below checklist is provided so that a Skill Author can provide direction to the Mycroft Community on how to test the Skill.

### Template for directions on how to test a Skill

The purpose of this template is to help a Mycroft Community Skill Developer outline how a Community Member can install, configure, and test the Skill. This template is aimed at making Skills easier to test, and thereby increasing the amount of testing that is done on a Skill, and therefore the overall quality of the Skill.

#### YOUR SKILL NAME GOES HERE

* Platform <- which platform is the test being run on? ie Picroft, Mark 1, Linux
* Device version <-- what Mycroft version is the device running, ie 18.02
* Who <-- who is running the test
* Datestamp <-- time and date
* Language and dialect of tester <-- ie "English, Australian" so that we can identify any key language issues

#### How to install SKILL NAME

* Install SKILL NAME by .....
  - This might include `msm` instructions or `git clone` instructions
  - Be clear about any dependencies SKILL NAME has, and how to install dependencies if `requirements.txt` or `requirements.sh` don't work

* SKILL NAME connects to SERVICES ....
  - Be clear on what services the Skill needs to connect to, and document any attributes that need to configured in Skill Settings.
  - Be clear what OAuth authentication is required

#### How to test SKILL NAME

Specify the steps the user should take to test the Skill, such as;

* Configure the Skill Settings in home.mycroft.ai
* Speak `Intent phrase`
* Mycroft should `do something`

Indicate clearly what constitutes a pass criterion for the Skill, and what constitutes a fail criterion.

#### Where feedback on SKILL NAME should be directed to

Be clear about how feedback on the Skill should be provided, such as through Issues on GitHub, via email or via [Mycroft Chat](https://chat.mycroft.ai).

## Peer review by Skill Management Team

The Skill Management Team is a group made up of both experienced Mycroft Community Members and Mycroft AI Staff, tasked with ensuring the quality of Skills. Once a Skill Author submits a Skill to the [Mycroft Skills Repo](https://github.com/MycroftAI/mycroft-skills), the Skill Management Team does the following review, and provides feedback back to the Skill Author, who then iterates the Skill until any issues are resolved.

### Template for Skill Management Team Review

#### Review of `skill-name`

##### Standard checks (non-code checks)

* Check that the Skill installs using voice commands. Mycroft will get the user to confirm which Skill should be installed if there is ambiguity in Skill names - such as duplicate names. If possible, name the Skill so that there is minimal duplication and/or conflict. You should also verify that the Skill name can be verbally pronounced by speaking the Skill name into the Mycroft command line several times, and reading the resulting transcriptions. Suggest alternative Skill names if it is difficult to verbally pronounce the Skill name.

* Check the `dialog` directory to ensure that from a voice user interface perspective the dialogs read well. It is a good idea to run the `dialog` phrases through [mimic](https://mycroft.ai/documentation/mimic/). Sometimes the `dialog` files will need a small tweak such as a space between words, or extra vowel sounds, to sound realistic. Sometimes words don't render as expected and alternative wording should be used. Alway play every `dialog` phrase on the command line by doing `say <your dialog phrase here>` so that you can check how the `dialog` is spoken. Some of the tricks you might need to use include separating words by a space - such as `sub sonic` instead of `subsonic`, or `broad cast` instead of `broadcast`.

* Check the **Intents** defined in the `vocab` diectory. Determine if the **Intents** are likely to conflict with those from **Skills** that are installed by default, and if so, suggest alternatives if this makes sense, or at least advise the Skill Author that there are likely to be `Intent Collisions`. [Integration Test Runner](https://mycroft.ai/documentation/skills/automatic-testing/) can also assist with this.

_NOTE: Skills that are installed by default vary by `enclosure` and can be found in the `mycroft-skills` repo in the files called `DEFAULT.enclosure`. For example, the default Skills for Picroft are in a file called `DEFAULT.picroft`._

* Check the regular expressions defined in the `regex` directory - do they appear sensible? [Integration Test Runner](https://mycroft.ai/documentation/skills/automatic-testing/) can also assist with this.

* Check README for completeness - does it follow the README template and include all the relevant sections such as Intents, known issues, dependencies and so on? Is at least one category selected? _At least one category must be selected for the Skill to be displayed correctly in the [Mycroft Marketplace](https://market.mycroft.ai)._

* Check `requirements.txt` and `requirements.sh` - are the required dependencies listed? If `requirements.sh` is used, is some form of conditional processing done to match against multiple distros? Often Skill Authors will add requirements.txt using only an “library=1.x.x” instead of “library >=1.x.x”. Check to make sure that here is an equal or greater than in the requirements to help future-proof the Skill, unless a _specific_ version is needed. 

* Check `settingsmeta.json` - are the settings well laid out? Does the placeholder text make sense?

### What are the labels used on the `mycroft-skills` repo?

While a **Skill** is undergoing review, there are several *labels* used on the PR to help indicate status.

* **approved** - This Skill is ready to be merged to the current branch, ie 18.02
* **needs validation** This Skill needs validating by a Community Member and cannot be validated by Skills Team
* **new** This is a new Skill (rather than an update to an existing Skill)
* **override autotester** The Skills Team has determined that acceptance of this PR should override the AutoTester
* **under review** This Skill is being reviewed by the Skills Team
* **update** This Skill is an update to an existing Skill
* **waiting** This PR or Issue is waiting on the Skill Author to respond

![alt text](https://mycroft.ai/wp-content/uploads/2018/06/mycroft-skils-repo-labels.png "Mycroft Skills Repo labels")

### What happens if the Skill Management Team can't test the Skill?

Often, **Skills** will have niche requirements. For example, they may be dependent on third party APIs or the installation of entire software stacks. In this case, it is impractical for the Skill Management Team to test the Skill.

Instead, the Skill Management Team will seek assistance from the Community, and will invite the Community member who volunteers to add comments to the Pull Request. Then, the Skills Management Team will review the comments and merge or decline the PR.  

#### Python code checks of the Skill

* Is an appropriate LICENSE file used in the repo - such as Apache2 or GPL? 
* Inline documentation - is the code documented in line?
* Libraries - does the Skill include the correct libraries? Does it use too many libraries or dependencies?
* Callback check - do we need to do a check for the callback error that was in the Spotify Skill?
* Error handling - are there any specific checks we make for error handling or graceful degradation?
* Automatic tests - do automatic tests of the **Skill** pass?
* Skill Settings using Python Booleans - Skill Settings were updated in August 2018 to use Python Booleans instead of text Boolean values used in Python 2.4. [This is a good example of the change to check for](https://github.com/MycroftAI/skill-date-time/pull/32/files?utf8=%E2%9C%93&diff=split)

_NOTE: We do not enforce PEP8 Checks on Skills_

## Review by Mycroft AI

The purpose of this step is for a Mycroft AI staff member to do a final check of a Skill. The staff member will be looking for:

* Profanity - does the Skill contain profanity?
* Sexually explicit material - does the Skill contain sexually explicit references or language?
* Offensive or pejorative language - does the Skill contain offensive references or language, for example language that is homo-, trans-, or bi-phobic, racist, religiously intolerant etc.
* Other content that has the ability to damage the reputation of the Mycroft platform.

If any such content is found, the PR for the Skill to be added to the [Mycroft Skills Repo](https://github.com/MycroftAI/mycroft-skills) will be tagged as `flagged` and escalated for review by Mycroft AI senior management, who will then make a determination on whether the Skill will be pulled into the Mycroft repo.

## Deployment

If the **Skill** passes all reviews, it will then be merged into the [Mycroft Skills Repo](https://github.com/MycroftAI/mycroft-skills). Once it is merged, the Skill becomes available for any Mycroft **Device** to install using voice commands.

## Promotion

Once a **Skill** is deployed, the following measures may be taken by Mycroft Staff promote the **Skill** to the Mycroft Community. The Skill Author is of course welcome to do additional promotion of their own.

* Listing on [Community-Developed Skills Page](https://mycroft.ai/documentation/skills/#community-developed-skills)
* Shoutout in Mycroft Newsletter
* Notification on Mycroft Forum
* Notification in [~Skills Channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/skills)
* Notification through Mycroft social media

We also encourage the Skill Author to make a short video of the **Skill** in action to aid in promotion.