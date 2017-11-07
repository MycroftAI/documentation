---
ID: 32444
post_title: Introduction to developing Skills
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?page_id=32444
published: false
---
## Developing a new **Skill**

### Step 1 Make a new repo using the Skill Repo Template

If you want to submit a skill, simply make a repo for it with a file and directory structure like the template below. If you're new to GitHub, you might find this guide on [how to make a repo](https://help.github.com/articles/create-a-repo/) useful.

[Example Skill Template](https://github.com/MycroftAI/mycroft-skills/tree/master/00__skill_template)  

#### Structure of the **Skill** repo

The structure of the **Skill** repo template looks like this:

```
$ ls -las
total 128
 8 drwxrwxr-x   5 kathyreid kathyreid  4096 Oct 27 00:22 .
 8 drwxrwxr-x 136 kathyreid kathyreid  4096 Oct 27 00:22 ..
 8 drwxrwxr-x   3 kathyreid kathyreid  4096 Oct 27 00:22 dialog
 8 -rw-rw-r--   1 kathyreid kathyreid  3768 Oct 27 00:22 __init__.py
56 -rw-rw-r--   1 kathyreid kathyreid 49360 Oct 27 00:22 LICENSE
 8 -rw-rw-r--   1 kathyreid kathyreid   187 Oct 27 00:22 README.md
 8 -rw-rw-r--   1 kathyreid kathyreid   116 Oct 27 00:22 requirements.sh
 8 -rw-rw-r--   1 kathyreid kathyreid    79 Oct 27 00:22 requirements.txt
 8 drwxrwxr-x   3 kathyreid kathyreid  4096 Oct 27 00:22 test
 8 drwxrwxr-x   3 kathyreid kathyreid  4096 Oct 27 00:22 vocab
 ```

##### `dialog` directory

The `dialog` directory contains subdirectories for each spoken language the skill supports. Each subdirectory has `.dialog` files which specify what Mycroft should say when a **Skill** is executed.

The subdirectories are named using the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) for the language. For example, Brazilian Portugues is `pt-br`, German is `de`, and Australian English is `en-au`.

Here is an example where one language is supported. If more languages were supported, then there would be additional language directories.

```bash
$ ls -las -R
.:
total 24
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Oct 27 23:32 .
8 drwxrwxr-x 6 kathyreid kathyreid 4096 Oct 27 23:32 ..
8 drwxrwxr-x 2 kathyreid kathyreid 4096 Oct 27 23:32 en-us

./en-us:
total 40
8 drwxrwxr-x 2 kathyreid kathyreid 4096 Oct 27 23:32 .
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Oct 27 23:32 ..
8 -rw-rw-r-- 1 kathyreid kathyreid   32 Oct 27 23:32 hello.world.dialog
8 -rw-rw-r-- 1 kathyreid kathyreid   91 Oct 27 23:32 how.are.you.dialog
8 -rw-rw-r-- 1 kathyreid kathyreid   88 Oct 27 23:32 welcome.dialog
```

##### Intents

Each **Skill** defines one or more **Intents**, and has a `.dialog` file for each **Intent**. In this example, we can see that there are three **Intents**:

* Hello world
* How are you
* Welcome

The `.dialog` files specify the speech that Mycroft should use if an **Utterance** is matched with an **Intent** in a **Skill**.

##### Inside the `welcome.dialog` file

```
$ cat welcome.dialog
Any time.
Glad to be of service.
Glad to help.
My Pleasure.
No problem.
You're welcome.
```

When an **Utterance** is matched to an **Intent** defined in a **Skill**, Mycroft will then use the phrases in the `.dialog` file for the **Intent**.

An **Intent** can have multiple phrases. In the example above, each of the phrases is equivalent to "You're welcome", and would be Spoken in response to "Thank you".

Each variant of the **Intent** is on a separate line. Mycroft will choose a variant at random and Speak the line when the **Skill** is executed.

#### `__init__.py`

`__init__.py` is where most of the **Skill** is defined, using Python code.

@TODO we need to give an example or guide here about how this file inherits from the `MycroftSkill` class.

### Step 2 Clone Repo
Clone the `mycroft-skills` repo to a local directory. If you're new to GitHub, you might find this guide on [how to clone](https://help.github.com/articles/cloning-a-repository) useful.

```bash
$ git clone https://github.com/MycroftAI/mycroft-skills.git
Cloning into 'mycroft-skills'...
remote: Counting objects: 1529, done.
remote: Compressing objects: 100% (60/60), done.
remote: Total 1529 (delta 42), reused 46 (delta 15), pack-reused 1451
Receiving objects: 100% (1529/1529), 7.44 MiB | 565.00 KiB/s, done.
Resolving deltas: 100% (709/709), done.
Checking connectivity... done.

```

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