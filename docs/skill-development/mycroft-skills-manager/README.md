---
description: >-
  Mycroft Skills Manager (msm) is a command line tool used to add, manage and
  remove Skills on any Mycroft installation.
---

# Mycroft Skills Manager

Mycroft Skills Manager (MSM) is a command line tool used to add, manage and remove Skills on any Mycroft installation. It can install any Skill listed on the [Mycroft Skills Repository](https://github.com/MycroftAI/mycroft-skills) or from any Github repository. It is a handy tool for Developers and those who may frequently reconfigure, install and uninstall Skills.

## Video Tutorial

{% embed url="https://www.youtube.com/watch?v=jJjLro140Go" %}
Video Tutorial: Mycroft Skills Manager
{% endembed %}

## Information

### List all Skills

To list all Skills available in the Marketplace run:

```
mycroft-msm list
```

### Search for a Skill

To search the available Skills run:

```
mycroft-msm search <name>
```

### Show information

To show all available information on a Skill you can use the name or repository url:

```
mycroft-msm info <name/url>
```

## Install

### From the Marketplace

To install a Skill from the Mycroft Marketplace you can provide a rough title and MSM will return the most likely match.

```
mycroft-msm install cocktail
```

### From a Specific Author

If you know the author of the Skill, particularly where multiple Skills with similar names exist, the `install` command has an additional optional parameter.

If I wanted a Dice Skill, but only if it was authored by Forslund, I would run:

```
mycroft-msm install dice forslund
```

Such a Skill doesn't exist so MSM returns a list of alternative options from the same author:

```
INFO - building SkillEntry objects for all skills
INFO - Best match (0.34): cocktails by forslund
MultipleSkillMatches: cocktails, youtube-music-skill.forslund, mycroft-spotify, game-zork, fallback-aiml
```

### From a Github repository

{% hint style="warning" %}
Installing Skills from outside the Mycroft Marketplace is done at your own risk. To be included in the Marketplace, all Skills are reviewed to ensure they contain no malicious or otherwise harmful code. We strongly recommend reviewing any code you are loading onto your device.
{% endhint %}

To install a Skill that is not included in the Mycroft Marketplace use the url of the repository.

```
mycroft-msm install https://github.com/krisgesling/tea-skill
```

### From a Marketplace branch

To install a Skill from a different branch of the Mycroft-Skills Marketplace repository, use the `-b` flag:

```
mycroft-msm -b dev install weather
```

### From an Alternate Marketplace

To install a Skill from an independently managed listing of Skills, you can specify the url for that Marketplace using the `-u` flag:

```
mycroft-msm -u https://github.com/krisgesling/mycroft-skills install cocktails
```

## Updating

### All installed Skills

To update all Skills installed on a device run:

```
mycroft-msm update
```

Note that if Mycroft detects that any file in a Skill has been modified, it will not update that Skill. This is to prevent loss of any work you are doing in that directory. See [MSM Troubleshooting > Uncommitted Changes](msm-troubleshooting.md#uncommitted-changes) for tips to resolve this.

### Install and update defaults

To install all default Skills for the device, as well as update all Skills, run:

```
mycroft-msm default
```

## Removal

To uninstall or remove any Skill from the device run:

```
mycroft-msm remove <name>
```

Note that default Skills will be reinstalled by the system unless they are explicitly blacklisted. See ["How do I disable a Skill?"](../faq.md#how-do-i-disable-a-skill) for more info.

### Specifying author

The `remove` command also has an optional `author` parameter that can be used to specify which Skill you intend to be uninstalled.

```
mycroft-msm remove <name> <author>
```

## Show Help Information

To show help information describing how to use MSM's different commands, use the `-h` flag.

For a complete overview run:

```
mycroft-msm -h
```

Or for command specific information include the command.

```
mycroft-msm install -h
```
