---
description: >-
  Ready to create your first Skill? See how easy it is to get a new Skill up and
  running, then we will step through the basic anatomy of a Mycroft Skill.
---

# Your First Skill

## Prerequisites

If you haven't already, check out our [Introduction to Skill Development](introduction.md). This walk through assumes you:

* Know some basic knowledge of [Python programming](https://www.python.org/),
* have an account on [Github.com](https://github.com), and
* have a [working version of Mycroft](../using-mycroft-ai/get-mycroft/).

## Understand the flow of your Skill

It's a good idea to start by writing down how your Skill will work, including

* What words will the User speak to activate the Skill?
* What will Mycroft speak in response?
* What data will you need to deliver the Skill?
* Will you need any additional packages or dependencies?

Once you've given these some thought, you can get started.

## Mycroft Skills Kit \(MSK\)

To setup the foundations of your Skill, we will use the [Mycroft Skills Kit \(MSK\)](next-steps/mycroft-skills-kit.md) that comes installed with Mycroft. If you chose the defaults during installation, you can run MSK from your Terminal using the command: `mycroft-msk`. Running this command without any arguments will provide a brief overview of what you can do with MSK.

If you receive a "command not found", then you will need to run `msk` manually from your `mycroft-core` directory. Anytime you see `mycroft-msk` in our documentation you must replace this with:

### MSK Create

`mycroft-msk create` is an interactive script that asks you a few questions and generates a new Skill template. This template can immediately be used as a Skill, however you will most likely want to extend its functionaity.

To create your first Skill, you will be asked for a:

1. Name  To be readable within the space available on the [Mycroft Skills Marketplace](https://market.mycroft.ai) the name should be short, generally under 22 characters in length. The name must also be unique. You can check the [Marketplace](https://market.mycroft.ai) to see what other Skills already exist. 
2. Example phrases \(known as utterances\)  Utterances that you expect Users to say to Mycroft, that your Skill will respond to. 
3. Response dialog  The dialog that your Skill will respond with. 
4. Short description  A one-line description, less than 40 characters long. 
5. Long description  This can be as short or as long as you like. 
6. Author  This is most often your name, and / or Github @username 
7. Categories  The [Mycroft Skills Marketplace](https://market.mycroft.ai) categories your Skill belongs to. It's important to note that the first category you select will be set as the default category. This is where your Skill will most often appear in the Marketplace. 
8. Tags  Tags provide an additional means for Users to search for or discover relevant Skills. Unlike categories, you can set your tags to anything you like.

After inputting this data you will be asked if you would like a Github repo created for your Skill. This provides an easy way to store your Skill, and will be required if you choose to [publish your Skill in the Marketplace](marketplace-submission/).

If you have completed all of these steps, your Skill will have been created in the `/opt/mycroft/skills` directory on your device.

## Structure of a Skill

If we now navigate to our new Skill, we can see that it is made up of a number of files and folders.

```text
$ ls -l
total 20
drwxr-xr-x 3 kris kris 4096 Oct  8 22:21 dialog
-rw-r--r-- 1 kris kris  299 Oct  8 22:21 __init__.py
-rw-r--r-- 1 kris kris 9482 Oct  8 22:21 LICENSE
-rw-r--r-- 1 kris kris  283 Oct  8 22:21 README.md
-rw-r--r-- 1 kris kris  642 Oct  8 22:21 settingsmeta.yaml
drwxr-xr-x 3 kris kris 4096 Oct  8 22:21 vocab
```

We will look at each of these in turn.

### `vocab`, `dialog`, and `locale` directories

The `dialog`, `vocab`, and `locale` directories contain subdirectories for each spoken language the skill supports. The subdirectories are named using the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) for the language. For example, Brazilian Portugues is 'pt-br', German is 'de-de', and Australian English is 'en-au'.

By default, your new Skill contains one subdirectory for United States English - 'en-us'. If more languages were supported, then there would be additional language directories.

```bash
$ ls -l dialog
total 4
drwxr-xr-x 2 kris kris 4096 Oct  8 22:21 en-us
```

#### Dialog Directory

There will be one file in the language subdirectory \(ie. `en-us`\) for each type of dialog the Skill will use. Currently this will contain all of the phrases you input when creating the Skill.

```bash
$ ls -l dialog/en-us
total 4
-rw-r--r-- 1 kris kris 10 Oct  8 22:21 first.dialog
```

When instructed to use a particular dialog, Mycroft will choose one of these lines at random. This is closer to natural speech. That is, many similar phrases mean the same thing.

For example, how do you say 'goodbye' to someone?

* Bye for now
* See you round
* Catch you later
* Goodbye
* See ya!

#### Vocab Directory

Each Skill defines one or more Intents. Intents are defined in the `vocab` directory. The `vocab` directory is organized by language, just like the `dialog` directory.

We will learn about Intents in more detail shortly. For now, we can see that within the `vocab` directory you may find multiple types of files:

* `.intent` files used for defining Padatious Intents
* `.voc` files define keywords primarily used in Adapt Intents
* `.entity` files define a named entity also used in Adapt Intents

In our current example we might see something like:

```bash
$ ls -l vocab/en-us
total 4
-rw-r--r-- 1 kris kris 23 Oct  8 22:21 first.intent
```

This `.intent` file will contain all of the sample utterances we provided when creating the Skill.

#### Locale Directory

This directory is a newer addition to Mycroft and combines `dialog` and `vocab` into a single directory. This was requested by the Community to reduce the complexity of a Skills structure, particularly for smaller Skills. Any of the standard file types that we've looked at so far will be treated the same if they are contained in the `dialog`, `vocab`, or `locale` directories.

This also includes the `regex` directory that you will learn about later in the tutorial.

### \_\_init\_\_.py

The `__init__.py` file is where most of the Skill is defined using Python code. We will learn more about the contents of this file in the next section.

Let's take a look:

#### Importing libraries

```python
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
```

This section of code imports the required _libraries_. Some libraries will be required on every Skill, and your skill may need to import additional libraries.

#### Class definition

The `class` definition extends the `MycroftSkill` class:

```python
class HelloWorldSkill(MycroftSkill):
```

The class should be named logically, for example "TimeSkill", "WeatherSkill", "NewsSkill", "IPaddressSkill". If you would like guidance on what to call your Skill, please join the [~skills Channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/skills).

Inside the class, methods are then defined.

#### \_\_init\_\_\(\)

This method is the _constructor_. It is called when the Skill is first constructed. It is often used to declare state variables or perform setup actions, however it cannot utilise MycroftSkill methods as the class does not yet exist. You don't have to include the constructor.

An example `__init__` method might be:

```python
def __init__(self):
    super().__init__()
    self.already_said_hello = False
    self.be_friendly = True
```

#### initialize\(\)

Perform any final setup needed for the skill here. This function is invoked after the skill is fully constructed and registered with the system. Intents will be registered and Skill settings will be available.

```python
def initialize(self):
    my_setting = self.settings.get('my_setting')
```

#### Intent handlers

Previously the `initialize` function was used to register intents, however our new `@intent_handler` and `@intent_file_handler` decorators are a cleaner way to achieve this. We will learn all about the different [Intents](https://github.com/MycroftAI/documentation/tree/156204fdccf839a4d5c57bf46f38c17ac1fee4eb/docs/skill-development/intents.md) shortly.

In our current HelloWorldSkill we can see two different styles. 1. An Adapt handler, triggered by a keyword defined in a `ThankYouKeyword.voc` file.

```python
@intent_handler(IntentBuilder('ThankYouIntent').require('ThankYouKeyword'))
def handle_thank_you_intent(self, message):
    self.speak_dialog("welcome")
```

1. A Padatious intent handler, triggered using a list of sample phrases.

   ```python
   @intent_file_handler('HowAreYou.intent')
   def handle_how_are_you_intent(self, message):
    self.speak_dialog("how.are.you")
   ```

In both cases, the function receives two _parameters_:

* `self` - a reference to the HelloWorldSkill object itself
* `message` - an incoming message from the `messagebus`.

Both intents call the `self.speak_dialog()` method, passing the name of a dialog file to it. In this case `welcome.dialog` and `how.are.you.dialog`.

#### stop\(\)

You will usually also have a `stop()` method.

This tells Mycroft what your Skill should do if a stop intent is detected.

```python
def stop(self):
    pass
```

In the above code block, the [`pass` statement](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement) is used as a placeholder; it doesn't actually have any function. However, if the Skill had any active functionality, the stop\(\) method would terminate the functionality, leaving the Skill in a known good state.

#### create\_skill\(\)

The final code block in our Skill is the `create_skill` function that returns our new Skill:

```python
def create_skill():
    return HelloWorldSkill()
```

This is required by Mycroft and is responsible for actually creating an instance of your Skill that Mycroft can load.

_Please note that this function is not scoped within your Skills class. It should not be indented to the same level as the methods discussed above._

### LICENSE

This file contains the full text of the license your Skill is being distributed under. It is not required for the Skill to work, however all Skills submitted to the [Marketplace](https://market.mycroft.ai) must be released under an appropriate open source license.

### README.md

The README file contains human readable information about your Skill. The information in this file is used to generate the Skills entry in the [Marketplace](https://market.mycroft.ai). More information about this file, can be found in the [Marketplace Submission section](marketplace-submission/skill-readme-md.md).

### settingsmeta.yaml

This file defines the settings that will be available to a User through their account on [Home.Mycroft.ai](https://home.mycroft.ai/skills).

Jump to [Skill Settings](next-steps/skill-settings.md) for more information on this file and handling of Skill settings.

## What have we learned

You have now successfully created a new Skill and have an understanding of the basic components that make up a Mycroft Skill. Next we will dive into each component in more detail.

