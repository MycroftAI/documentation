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

## What is Mycroft Skills Manager - msm? 

Mycroft Skills Manager (msm) is a command line tool used to add, manage and remove **Skills** on any Mycroft installation. It can install any **Skill** listed on the [Mycroft Skills Repository](https://github.com/MycroftAI/mycroft-skills). `msm` is a handy tool for Developers and those who may frequently reconfigure, install and uninstall **Skills**. 

## Using Mycroft Skills Manager - msm

_NOTE: If you are using `mycroft-core` on Linux, then you will need to `cd` into `mycroft-core/msm` and call `msm` using `./msm [command]`_

To bring up a list of all available `msm` commands, SSH into your **Device** and then type `msm -h`: 

```
$ msm -h
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


## msm error codes

If `msm` encounters an error during installation, deletion or searching for a **Skill**, an error code and error message will be shown on screen. This table is a quick reference guide to help you troubleshoot any errors `msm` displays.

| **Error code** | **Meaning** | **How to resolve it** |
| --- | --- | --- |
| `5 ERROR:  Missing virtualwrapper, cowardly refusing to install skills` | Virtualwrapper is a set of extensions to the virtualenv tool. Mycroft uses virtualenv extensively to manage Python package dependencies. This error indicates that virtualwrapper isn&#39;t installed or couldn&#39;t be found. | First, try **  workon mycroft** Then try your command. If this doesn&#39;t work, use **  pip install virtualwrapper** Then try your command again. |
| `20 Skill already installed.  Perhaps you meant to use update?` | You tried to install a Skill that was already installed. | You may have wanted to update the Skill instead. |
| `101 ERROR: Unable to find/access ${mycroft\_skill\_folder}!` | By default, the Skills are stored on every Device (Picroft, Mycroft for Linux etc) at the path /opt/mycroft/skills. MSM cannot access this directory. | Check that the directory exists, and that it has appropriate permissions. This directory should have permissions mycroft:mycroft (mycroft owner, mycroft group) |
| `102 ERROR: Unable to access directory ${name}!` | Trying to access a Skill directory that either does not exist, or which the mycroft user does not have permission to traverse. | If you are developing a Skill, make sure the path to any directories (for instance to resources like mp3 files) is correct. Check that the permissions on the directory allow the mycroft user to traverse it. |
| `111` | Mycroft was unable to curl the file https://raw.githubusercontent.com/MycroftAI/mycroft-skills/master/.gitmodules | Check your internet connection and try again. |
| `112` | Mycroft was unable to wget  the file https://raw.githubusercontent.com/MycroftAI/mycroft-skills/master/.gitmodules | Check your internet connection and try again. |
| `120 ERROR: Unable to activate 'mycroft' virtualenv, requirements not installed.` | Mycroft uses a virtual environment to manage Python dependencies. If you see this error, the virtual environment is not installed, or is in error.   | Reinstall your virtual environment, using this [documentation](https://mycroft.ai/documentation/linux/#removing-and-rebuilding-your-virtualenv) |
| `121 Unable to install requirements for skill ${name}` | Each Skill is able to define pre-requisite software that has to be installed - requirements - in the files requirements.txt in the Skill directory. This error indicates that the requirements could not be installed. Dependencies in requirements.txt use pip, whereas dependencies in requirements.sh use bash. | Identify why the requirements could not be installed, and if necessary, install them manually. |
| `122 Running requirements.sh failed!` | When a Skill is installed it will execute requirements.sh to do advanced setup operations.   Attempting to run this shell script failed. | Check the script and attempt to execute it manually. |
| `123 ERROR: Unable to chown install directory ${name}!` | MSM is trying to change ownership of the Skill directory, but cannot. | Check that the parent directory, /opt/mycroft/skills, is set so the user running Mycroft (mycroft on a Mark 1 or Picroft) is the owner of the directory. |
| `201 Multiple matches for ${str}, be more specific.` | Upon attempted installation of the Skill, there were multiple matches for the Skill. | Please be more specific when attempting to install Skills. |
| `202 ${str} skill was not found` | Upon attempted installation of the Skill, the skill name given could not be found. | Ensure you have the spelling of the Skill correct, or try installing another Skill. |
| `249 Failed to remove ${name}` | Upon attempted deletion of the Skill, the Skill's directory could not be removed. | Please check the permissions on your /opt/mycroft/skills directory, and ensure the permissions are 775 `mycroft:mycroft`. |
| `251 Multiple matches for ${str}, be more specific.` | There are multiple matches for the Skill you tried to remove. | Please be more specific when attempting to remove Skills. |
|  `252 ${str} was not found in the mycroft-skills repo` | The Skill you tried to remove was not found in the mycroft-skills repo. | Ensure you have the spelling of the Skill correct, or try removing another Skill. |