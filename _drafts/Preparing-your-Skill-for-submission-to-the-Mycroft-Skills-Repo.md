---
ID: 32646
post_title: >
  Preparing your Skill for submission to
  the Mycroft Skills Repo
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?page_id=32646
published: false
---
# Preparing your Skill for submission to the Mycroft Skills Repo
@TODO should this be a separate page of content? I think it probably should, because the **intent** of the developer is different. One one page, the key task is to learn more about Skills to be able to create a new Skill, but the key task is different - it's about submitting a complete Skill to the Mycroft Skills Repo. The task is different, it should be a different page.

### Step 3 Generate README.md
To get your **Skill** added, generate the README.md file for your **Skill** using the [Meta Editor](http://rawgit.com/MycroftAI/mycroft-skills/master/meta_editor.html). Fill out all the relative fields, and it will generate the Markdown to put into your README.md file.

### Step 4 Add Submodule
Next we need to add the Submodule for your **Skill**. For more help on Submodules in GitHub, feel free to check out [this guide](https://github.com/blog/2104-working-with-submodules)

Or, type the following in the terminal, assuming you are in the directory where you cloned `mycroft-skills`:

```bash
git submodule add $remote $name-your-skill
```
where ``$remote` is the git address for your repo [example] (https://github.com/mycroftai/skill-configuration) and ``$name-your-skill` is the name you have given to your **Skill**. In general, we normally use BLANK-skill as a format for **Skill** names.

This should have edited the ``.gitmodule` file and added something similar to the bottom of the file:
```
+[submodule "NAME OF YOUR SKILL"]
 +	path = name-of-your-skill-skill
 +	url = URL.FOR.YOUR.SKILL.git
```

### Step 5 Modify Skills Repo README.md
Modify the table section in the `README.md` file of the `mycroft-skills` repo to include the file direct link to your repo like the following example. Include the `<br>` tag and the phrase to trigger your skill:

```
| :heavy_check_mark:  | [home-assistant](https://github.com/btotharye/mycroft-homeassistant#readme)| Control your devices in home-assistant<br>```turn on office
```

Ensure to put a proper status as well from the list below:



**Status meaning:**
:heavy_check_mark: good working order
:construction:     still being developed and not ready for general use (for reference/collaboration)
:question:         untested (by us)
:skull:            Broken, but good for ideas!

### Step 6 Submit PR (Pull Request) to have your **Skill** listed
Once you've got your repo organized properly, submit the PR consisting of the following:
* Ensure you use [Meta Editor](http://rawgit.com/MycroftAI/mycroft-skills/master/meta_editor.html) to create your standardized README.md file
* The URL of your repo
* A short name for the skill
* A one sentence description of what it does
* The development status of the skill (under construction or working)

### MSM Compliance
To make your skill capable of being installed via MSM (the Mycroft Skill Manager) you need two additional files.
* `requirements.txt`
* `requirements.sh`

requirements.txt is a list of all `pip` libraries your skill needs (if any).

requirements.sh is a shell script that executes and installs package dependancies  your **Skill** needs (if any).
So, if you need a specific `pip` library installed, like `gensim`, you can have it automatically installed in the correct vm using `msm`.

This requirements.txt file would look like this:
```
gensim
```
That's it!