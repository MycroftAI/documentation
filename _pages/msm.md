---
ID: 33749
post_title: Mycroft Skills Manager – msm
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/documentation/msm/
published: true
post_date: 2017-12-12 10:56:48
---
# Mycroft Skills Manager - msm

- [Mycroft Skills Manager - msm](#mycroft-skills-manager---msm)
  * [What is Mycroft Skills Manager - msm?](#what-is-mycroft-skills-manager---msm)
  * [Using Mycroft Skills Manager - msm](#using-mycroft-skills-manager---msm)
  * [msm error codes](#msm-error-codes)

## What is Mycroft Skills Manager - msm?

Mycroft Skills Manager (msm) is a command line tool used to add, manage and remove **Skills** on any Mycroft installation. It can install any **Skill** listed on the [Mycroft Skills Repository](https://github.com/MycroftAI/mycroft-skills). `msm` is a handy tool for Developers and those who may frequently reconfigure, install and uninstall **Skills**.

## Using Mycroft Skills Manager - msm

`msm` has recently been rewritten in Python (`msm` was previously a `bash` script). In order to use `msm`, you will first need to enter the Mycroft _virtual environment_, `venv`, using the following command:

`mycroft-core$ source .venv/bin/activate`

``(.venv) kathyreid@kathyreid-N76VZ:~/mycroft-core$``

You can then run `msm`:

`(.venv) kathyreid@kathyreid-N76VZ:~/mycroft-core$ msm update`

To see a list of all the available `msm` commands, type `msm -h`:

```
(.venv) kathyreid@kathyreid-N76VZ:~/mycroft-core$ msm -h

msm: Mycroft Skill Manager
usage: msm [option] [repo | name]

Options:
  default                  installs the default skills, updates all others
  install <repo>           installs from the specified github repo
  install <name> [name...] installs the mycroft-skill matching <name>
  remove <name> [name...]  removes the specified github repo
  list                     list all mycroft-skills
  update                   update all installed skills
  search <name>            search mycroft-skills for match for <name>
  info <name>              shows information about the skill matching <name>
  info <repo>              shows information about the skill in the specified repo

Params:
  <repo>   full URL to a Github repo
  <name>   one or more substrings to match against submodule names
           in the https://github.com/MycroftAI/mycroft-skills repo

Examples:
  msm search twitter
  msm search date-time-skill
  msm install "daily meditation"
  msm remove "daily meditation"
  msm install https://github.com/penrods/Wink.git
```


For instance to see information on a **Skill**, type:

`msm info mycroft-mark-1`


To list all available **Skills**, type:

`msm list`

This will show available **Skills**, and indicate which ones you have installed:

```
rss-skill
sentiment-analysis-skill
skill-australian-news [installed]
skill-autogui
skill-caffeinewiz
```

Search is very handy functionality if you're looking for a particular **Skill**:

```
pi@mark_1:/opt/mycroft/skills $ msm search twitter
Possible match: twitter-skill
```

Update is very handy for updating all the **Skills** on your **Device**:

`msm update`

```
INFO - Nothing new for mycroft-ip
INFO - Nothing new for mycroft-timer
INFO - Nothing new for mycroft-release-test
INFO - Nothing new for mycroft-weather
INFO - Nothing new for chatbot
INFO - Nothing new for mycroft-speak
INFO - Nothing new for fallback-wolfram-alpha
INFO - Nothing new for mycroft-naptime
INFO - Nothing new for plasma-activities-skill
INFO - Nothing new for mycroft-pairing
```

### `msm` errors

The deprecated version of `msm` had several error codes. Instead, this version relies on standard Python errors.

Here are some common errors, what they mean, and how to resolve them.

#### Git authentication failed

```bash
ERROR - Error running update_skill on skill-radio-rne: GitException(Git command failed: GitCommandError(['git', 'fetch'], 128, b"remote: Invalid username or password.\nfatal: Authentication failed for 'https://github.com/ChrisFernandez/skill-radio-rne/'", b''))
```

This error usually means that the GitHub repository for the **Skill** no longer exists, or has moved. Remove the **Skill** using `msm remove [Skill Name]` and then install a new **Skill**.

#### Uncommitted changes

```bash
ERROR - Error running update_skill on TranslateSkill: SkillModified(Uncommitted changes:
	 M requirements.sh
)
```
