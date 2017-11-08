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

This page will walk you through developing a new Mycroft **Skill**. It assumes you have read through the [basic skills information](skills.md)

### Prerequisites

It's a good idea to get prepared before writing your new **Skill**, as this will make your skill-writing experience go much smoother.

* **Git** - You will need to know some basic Git commands in order to create a new **Skill** for Mycroft. If you're not familiar with Git, that's OK, but you _will_ need to have [Git installed on your system. ](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
* **Python** - You will need to know some basic Python programming to get started. If you've programmed in other object-oriented languages, like Javascript or C#, then you'll be able to pick it up, but if you're totally new to programming, you'll need to do an [introductory programming course](https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-11).
* **Naming your Skill** - Choose a name for your **Skill** before creating a new repository. It's a good idea to check the [Mycroft Skills Repo](https://github.com/MycroftAI/mycroft-skills) so that you don't create a duplicate name.
* **Set up your environment** - Most people will find it easiest to test new **Skills** by setting up [Mycroft for Linux](Mycroft-for-Linux.md). `cd` into the directory where you have `mycroft-core` installed and type `/start_mycroft.sh debug`. This should open a command line interface (CLI) like that shown below:

![Starting mycroft-core in debug mode for Skills testing](../img/mycroft-core-start-debug.png "Starting mycroft-core in debug mode for Skills testing")

* **Understand the flow of your Skill** - It's a good idea to write down on paper how your **Skill** will work, including
  * What words will the User speak to activate the **Skill**?
  * What will Mycroft speak in response?
  * What data will you need to deliver the **Skill**?
  * Will you need any additional packages or dependencies?

Once you've given these some thought, you can get started.

### Skill terminology

You'll notice some new terms as you start to develop **Skills**.

* **dialog** - A **dialog** is a phrase that is spoken by Mycroft. Different **Skills** will have different **dialogs**, depending on what the **Skill** does. For example, in a _weather_ **Skill**, a **dialog** might be `the.maximum.temperature.is.dialog`.
* **intent** - Mycroft matches **utterances** that a User speaks with a **Skill** by determining an **intent** from the **utterance**. For example, if a User speaks `Hey Mycroft, what's the weather like in Toronto?` then the **intent** will be identified as _weather_ and matched with the _Weather Skill_. When you develop new **Skills**, you need to define new **intents**.
* **utterance** - An **utterance** is a phrase spoken by the User, after the User says the **Wake Word**. `what's the weather like in Toronto?` is an **utterance**.

### Make a new repo using the Template Skill

First, `git clone` the [Mycroft Skills repo](https://github.com/MycroftAI/mycroft-skills/) to your local machine.

```bash
$ git clone https://github.com/MycroftAI/mycroft-skills/
```

Now, we'll made a new repository for your **Skill**. The new repository has to follow a strict file structure. A **Template Skill** is available to clone from. If you're new to GitHub, you might find this guide on [how to make a repo](https://help.github.com/articles/create-a-repo/) useful.

[Example Skill Template](https://github.com/MycroftAI/mycroft-skills/tree/master/00__skill_template)  

Copy the Template Skill into a new directory. Here, we've called the new Skill `skill-training`, but your **Skill** will have a different name.

```bash
$ cp -R 00__skill_template skill-hello-worldls -las
```

#### Structure of the **Skill** repo

The structure of the **Template Skill** directory looks like this:

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

The `dialog` directory contains subdirectories for each spoken language the skill supports.  Each subdirectory has `.dialog` files which specify what Mycroft should say when a **Skill** is executed.

The subdirectories are named using the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) for the language. For example, Brazilian Portugues is `pt-br`, German is `de`, and Australian English is `en-au`.

Here is an example where one language is supported. By default, the **Template Skill** contains one subdirectory for United States English - `en-us`. If more languages were supported, then there would be additional language directories.

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

There will be one file in the language subdirectory (ie. `en-us`) for each type of **dialog** the **Skill** will use. In the example above, there are three types of **dialog** used by the **Skill**. Let's take a look at a **dialog** file.

```bash
$ cat hello.world.dialog
Hello world
Hello
Hi to you too
```

You will notice that each line of **dialog** is slightly different. When instructed to use a particular **dialog**, Mycroft will chose one of these lines at random. This is closer to natural speech. That is, many similar phrases mean the same thing.

For example, how do you say 'goodbye' to someone?
* Bye for now
* See you round
* Catch you later
* Goodbye
* See ya!

##### vocab directory and defining Intents

Each **Skill** defines one or more **Intents**. Intents are defined in the `vocab` directory.The `vocab` directory is organized by language, just like the `dialog` directory.  

In this example, we can see that there are three **Intents**, each defined in `IntentKeyword.voc` **vocab** files:

```bash
mycroft-skills/skill-hello-world/vocab/en-us$ ls -las
total 40
8 drwxrwxr-x 2 kathyreid kathyreid 4096 Nov  9 00:11 .
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov  9 00:11 ..
8 -rw-rw-r-- 1 kathyreid kathyreid   22 Nov  9 00:11 HelloWorldKeyword.voc
8 -rw-rw-r-- 1 kathyreid kathyreid   52 Nov  9 00:11 HowAreYouKeyword.voc
8 -rw-rw-r-- 1 kathyreid kathyreid   17 Nov  9 00:11 ThankYouKeyword.voc
```

Just like **dialog** files, **vocab** files can have multiple lines. Mycroft will match _any_ of these phrases with the **Intent**. If we have a look at the `ThankYouKeyword.voc` file, we can see this in action:

```bash
$ cat ThankYouKeyword.voc
thank you
thanks
```

If the User speaks _either_ `thank you` or `thanks`, Mycroft will match this to the `ThankYou` **intent** in the **Skill**.

_NOTE: One of the most common mistakes when getting started with **Skills** is that the **vocab** file doesn't include all the phrases that the User might use to trigger the **intent**. _

#### `__init__.py`

`__init__.py` is where most of the **Skill** is defined, using Python code.

@TODO talk here about the Copyright notice

Let's take a look:

```python
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
```

This section of code imports the required _libraries_. These libraries will be required on every **Skill**. Your skill may need to import additional libraries.

```python
__author__ = 'eward'
```

This section defines the _author_ of the **Skill**. This value is usually set to the GitHub username of the author.







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
