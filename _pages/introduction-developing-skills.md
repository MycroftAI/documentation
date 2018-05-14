---
ID: 32444
post_title: Introduction to developing Skills
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/skills/introduction-developing-skills/
published: true
post_date: 2017-12-02 22:35:25
---
# Developing a new **Skill**

- [Developing a new **Skill**](#developing-a-new-skill)
  * [Prerequisites](#prerequisites)
  * [Skill terminology](#skill-terminology)
  * [Make a new repo using the Template Skill](#make-a-new-repo-using-the-template-skill)
    + [Structure of the **Skill** repo](#structure-of-the-skill-repo)
      - [`dialog` directory](#dialog-directory)
      - [vocab directory and defining Intents](#vocab-directory-and-defining-intents)
      - [__init__.py](#init-py)
  * [Simplifying your Skill code with `intent_handler` _decorators_](#simplifying-your-skill-code-with-intent_handler-decorators)
  * [How do I disable a Skill?](#how-do-i-disable-a-skill)
  * [How to increase the priority of **Skills** during loading](#how-to-increase-the-priority-of-skills-during-loading)
  * [How do I find more information on Mycroft functions?](#how-do-i-find-more-information-on-mycroft-functions)

This page will walk you through developing a new Mycroft **Skill**. It assumes you have read through the [basic skills information](https://mycroft.ai/documentation/skills/developing-skills/)

## Prerequisites

It's a good idea to get prepared before writing your new **Skill**, as this will make your skill-writing experience go much smoother.

* **Git** - You will need to know some basic Git commands in order to create a new **Skill** for Mycroft. If you're not familiar with Git, that's OK, but you _will_ need to have [Git installed on your system. ](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
* **Python** - You will need to know some basic Python programming to get started. If you've programmed in other object-oriented languages, like Javascript or C#, then you'll be able to pick it up, but if you're totally new to programming, you'll need to do an [introductory programming course](https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-11).
* **Naming your Skill** - Choose a name for your **Skill** before creating a new repository. It's a good idea to check the [Mycroft Skills Repo](https://github.com/MycroftAI/mycroft-skills) so that you don't create a duplicate name.
* **Set up your environment** - Most people will find it easiest to test new **Skills** by setting up [Mycroft for Linux](https://mycroft.ai/documentation/linux/). `cd` into the directory where you have `mycroft-core` installed and type `./start-mycroft.sh debug`. This should open a command line interface (CLI) like that shown below:

![Starting mycroft-core in debug mode for Skills testing](https://mycroft.ai/wp-content/uploads/2017/12/mycroft-core-start-debug.png "Starting mycroft-core in debug mode for Skills testing")

* **Understand the flow of your Skill** - It's a good idea to write down on paper how your **Skill** will work, including
  * What words will the User speak to activate the **Skill**?
  * What will Mycroft speak in response?
  * What data will you need to deliver the **Skill**?
  * Will you need any additional packages or dependencies?

Once you've given these some thought, you can get started.

## Skill terminology

You'll notice some new terms as you start to develop **Skills**.

* **dialog** - A **dialog** is a phrase that is spoken by Mycroft. Different **Skills** will have different **dialogs**, depending on what the **Skill** does. For example, in a _weather_ **Skill**, a **dialog** might be `the.maximum.temperature.is.dialog`.
* **intent** - Mycroft matches **utterances** that a User speaks with a **Skill** by determining an **intent** from the **utterance**. For example, if a User speaks `Hey Mycroft, what's the weather like in Toronto?` then the **intent** will be identified as _weather_ and matched with the _Weather Skill_. When you develop new **Skills**, you need to define new **intents**.
* **utterance** - An **utterance** is a phrase spoken by the User, after the User says the **Wake Word**. `what's the weather like in Toronto?` is an **utterance**.

## Make a new repo using the Template Skill

In GitHub, `fork` the [Mycroft Skills repo](https://github.com/MycroftAI/mycroft-skills/) into your own GitHub account.

Do this by clicking the 'Fork' button.

![Forking the Mycroft Skills Repo](https://mycroft.ai/wp-content/uploads/2017/12/skills-forking-mycroft-skills-repo.png "Forking the Mycroft Skills Repo")

Then,

`git clone`

the repo you've just forked to your local machine.

For example, if your GitHub username is "JaneBloggs" then you will need to

`git clone`

from [https://github.com/JaneBloggs/mycroft-skills.git](https://github.com/JaneBloggs/mycroft-skills.git)

```bash
$ git clone https://github.com/JaneBloggs/mycroft-skills.git
Cloning into 'mycroft-skills'...
remote: Counting objects: 1529, done.
remote: Compressing objects: 100% (60/60), done.
remote: Total 1529 (delta 42), reused 46 (delta 15), pack-reused 1451
Receiving objects: 100% (1529/1529), 7.44 MiB | 565.00 KiB/s, done.
Resolving deltas: 100% (709/709), done.
Checking connectivity... done.
```

Now, we'll made a new repository for your **Skill**. The new repository has to follow a strict file structure. A **Template Skill** is available to clone from. If you're new to GitHub, you might find this guide on [how to make a repo](https://help.github.com/articles/create-a-repo/) useful.

[Example Skill Template](https://github.com/MycroftAI/mycroft-skills/tree/master/00__skill_template)  

Copy the Template Skill into a new directory. Here, we've called the new Skill `skill-training`, but your **Skill** will have a different name.

```
$ cp -R 00__skill_template skill-hello-world
$ ls -las
```

### Structure of the **Skill** repo

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

#### `dialog` directory

The `dialog` directory contains subdirectories for each spoken language the skill supports.  Each subdirectory has `.dialog` files which specify what Mycroft should say when a **Skill** is executed.

The subdirectories are named using the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) for the language. For example, Brazilian Portugues is 'pt-br', German is 'de-de', and Australian English is 'en-au'.

Here is an example where one language is supported. By default, the **Template Skill** contains one subdirectory for United States English - 'en-us'. If more languages were supported, then there would be additional language directories.

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

#### vocab directory and defining Intents

Each **Skill** defines one or more **Intents**. Intents are defined in the 'vocab' directory. The 'vocab' directory is organized by language, just like the 'dialog' directory.  

In this example, we can see that there are three **Intents**, each defined in

'IntentKeyword.voc`

**vocab** files:

```bash
mycroft-skills/skill-hello-world/vocab/en-us$ ls -las
total 40
8 drwxrwxr-x 2 kathyreid kathyreid 4096 Nov  9 00:11 .
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov  9 00:11 ..
8 -rw-rw-r-- 1 kathyreid kathyreid   22 Nov  9 00:11 HelloWorldKeyword.voc
8 -rw-rw-r-- 1 kathyreid kathyreid   52 Nov  9 00:11 HowAreYouKeyword.voc
8 -rw-rw-r-- 1 kathyreid kathyreid   17 Nov  9 00:11 ThankYouKeyword.voc
```

Just like **dialog** files, **vocab** files can have multiple lines. Mycroft will match _any_ of these phrases with the **Intent**. If we have a look at the

`ThankYouKeyword.voc`

file, we can see this in action:

```bash
$ cat ThankYouKeyword.voc
thank you
thanks
```

If the User speaks _either_

> thank you

or

> thanks

Mycroft will match this to the

`ThankYou`

**intent** in the **Skill**.

_NOTE: One of the most common mistakes when getting started with **Skills** is that the **vocab** file doesn't include all the phrases that the User might use to trigger the **intent**. _

#### __init__.py

`__init__.py`

is where most of the **Skill** is defined, using Python code.

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

```python
LOGGER = getLogger(__name__)
```

This section starts logging of the **Skill** in the `mycroft-skills.log` file. If you remove this line, your **Skill** will not log any errors, and you will have difficulty debugging.

The

`class`

definition extends the

`MycroftSkill`

class:

```python
class HelloWorldSkill(MycroftSkill):
```

The class should be named logically, for example "TimeSkill", "WeatherSkill", "NewsSkill", "IPaddressSkill". If you would like guidance on what to call your **Skill**, please join the [~skills Channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/skills).

Inside the class, methods are then defined.

```python
def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")
```

This method is the _constructor_, and the key function it has is to define the name of the **Skill**.

_NOTE: You don't have to include the constructor unless you plan to declare state variables for the Skill object. If you plan to declare state variables, then they should be defined in this block. If you don't include the constructor, the name of the **Skill** will be taken from the name of the `class`, in this case 'HelloWorldSkill'._

Example:

```python
def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")
        self.already_said_hello = False
        self.be_friendly = True
        self.hello_phrases = ['Hello', 'Hallå', 'Olá']
```

```python    
def initialize(self):
        thank_you_intent = IntentBuilder("ThankYouIntent").
            require("ThankYouKeyword").build()
        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        how_are_you_intent = IntentBuilder("HowAreYouIntent").
            require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent,
                             self.handle_how_are_you_intent)

        hello_world_intent = IntentBuilder("HelloWorldIntent").
            require("HelloWorldKeyword").build()
        self.register_intent(hello_world_intent,
                             self.handle_hello_world_intent)
```

The

`initialize()`

 function defines each of the **Intents** of the **Skill**. Note that there are three **Intents** defined in

 `initialize()`

 , and there were three **Intents** defined in **vocab** files.

Next, there are methods that handle each of the **Intents**.

```python
def handle_hello_world_intent(self, message):
        self.speak_dialog("hello.world")
```

In the

`handle_hello_world_intent()`

 method above, the method receives two _parameters_,

 `self`

 and

 `message`

 `self` is the reference to the object itself, and `message` is an incoming message from the `messagebus`. This method then calls the

 `speak_dialog()`

 method, passing to it the

 `hello.world`

 dialog. Remember, this is defined in the file "hello.world.dialog".

 Can you guess what Mycroft will Speak?

You will usually also have a

`stop()`

method. This method tells Mycroft what to do if a stop **intent** is detected.

```python
def stop(self):
    pass
```

In the above code block, the [`pass` statement](https://docs.python.org/2/reference/simple_stmts.html#the-pass-statement) is used as a placeholder; it doesn't actually have any function. However, if the **Skill** had any active functionality, the stop() method would terminate the functionality, leaving the *Skill** in a known good state.

#### Intents and regular expressions (regex)

In the examples above, we walked through how to use phrases in a `.voc` file to build an `Intent` using _entities_. In this section, we expand on how `Intents` are built, and introduce _multiple entities_, and _regular expressions_.

Throughout this section, we will be using examples from the [Date and Time Skill](https://github.com/MycroftAI/skill-date-time).

##### How .voc files are used to handle Intents

At the top of your **Skill** file, you will have a line that looks like this:

`from adapt.intent import IntentBuilder`

This tells your **Skill** to import the `IntentBuilder` class from Adapt. Adapt is an Intent-handling engine. Its job is to understand what a user Speaks to Mycroft, and to pass that information to a **Skill** for handling.

Different **Skills** require different information from the user. For example, the **Skill** to change the color of Mycroft's eyes just has one parameter - `color`. That parameter is mandatory - because you can't change the color of Mycroft's eyes without knowing what color to change them to.

Later in your **Skill** file, you will call `IntentBuilder`, with one or more parameters. The parameters can be either `required` or `optional`.

For example, here is the `@intent_handler` _decorator_ used in the [Date and Time Skill](https://github.com/MycroftAI/skill-date-time). It has three parameters; two are `required` and one is `optional`.

```python

@intent_handler(IntentBuilder("")
  .require("Query")
  .require("Time")
  .optionally("Location")
)

```

This call is then interpreted by the Adapt Intent Parser.

Internally, Adapt uses a function called `register_entity`, and tries to register `entities` based on the parameters passed to `IntentBuilder`. There are several ways that Adapt can register `entities`.

If we were building `Intent`s manually, we would do something like this:

```python

locations = [
    "Seattle",
    "San Francisco",
    "Tokyo"
]

for loc in locations:
    engine.register_entity(loc, "Location")

```

But what if we want to support more `locations`? Or make the `location` available to the **Skill** to use as a parameter in an API call?

First, Adapt will look in `.voc` files to try and register an `Intent`. For example, in the [Date and Time Skill](https://github.com/MycroftAI/skill-date-time), in the `vocab` directory, you will see several `.voc` files. Note that they each correspond to one of the parameters passed to `Intentbuilder()`.

```bash

pi@mark_1:/opt/mycroft/skills/skill-date-time/vocab/en-us $ ls -las
total 24
4 drwxr-xr-x 2 mycroft mycroft 4096 Feb 15 14:17 .
4 drwxr-xr-x 4 mycroft mycroft 4096 Feb 15 14:17 ..
4 -rwxr-xr-x 1 mycroft mycroft    8 Feb 15 14:17 Date.voc
4 -rwxr-xr-x 1 mycroft mycroft   12 Feb 15 14:17 Display.voc
4 -rwxr-xr-x 1 mycroft mycroft    9 Feb 15 14:17 Query.voc
4 -rwxr-xr-x 1 mycroft mycroft    5 Feb 15 14:17 Time.voc

```

If we take a look inside each of these files, they contain only a single word each:

* `Date.voc` => "date"
* `Display.voc => "display"
* `Query.voc`=> "what"
* `Time.voc` => "time"

Now, remember back to `IntentBuilder` and the mandatory and optional parameters? Only `Query` and `Time` were mandatory. So if a user Spoke:

`"Hey Mycroft, **what** **time** is it?"`

then Adapt would match that **Utterance** to the [Date and Time Skill](https://github.com/MycroftAI/skill-date-time), by _registering_ the `Intent`, and within the **Skill**, this would be handled by the `handle_query_time()` function.

If the user Spoke:

`"Hey Mycroft, **display** the **time** "`

which function within the Date and Time Skill do you think would handle the **Utterance**?

_ANSWER: handle_show_time()_

But what about `Location`? There isn't a `.voc` file for `Location`, so how does Adapt register an `entity` for `Location` so that `Location` can be included in an **Utterance**, recognised as an `Intent`, and handled properly by the [Date and Time Skill](https://github.com/MycroftAI/skill-date-time)?

This is done using [regular expressions](https://docs.python.org/2/library/re.html).

In the [Date and Time Skill](https://github.com/MycroftAI/skill-date-time) directory, you will see a sub-directory called `regex`. This sub-directory follows the same file structure as the `voc` directory (eg. there will be an `en-us` directory inside), and contains a file called 'location.rx':

```bash

pi@mark_1:/opt/mycroft/skills/skill-date-time/regex/en-us $ ls -las
total 12
4 drwxr-xr-x 2 mycroft mycroft 4096 Feb 15 14:17 .
4 drwxr-xr-x 4 mycroft mycroft 4096 Feb 15 14:17 ..
4 -rwxr-xr-x 1 mycroft mycroft   28 Feb 15 14:17 location.rx

```

Inside `location.rx` is a _regular expression_:

`(at|in|for) (?P<Location>.*)`

Because a `.voc` file is not present for the `Location` parameter, Adapt will then search for an equivalent `.rx` file in the `regex` directory. Instead of being restricted to the specified words in the `.voc` file, Adapt can register `Intents` using _regular expressions_, and thus support a wider range of input from the user.

Can you think of another **Skill** where a _regular expression_ `Location` would be useful?

_ANSWER: [Weather Skill](https://github.com/MycroftAI/skill-weather)_

For those who are new to Python, the `regex` used is a [Python named _group_](https://docs.python.org/2/library/re.html#regular-expression-syntax). The name of the group is case-sensitive, and correlates with the variable name used to extract the named group value.

For example, in the [Date and Time Skill](https://github.com/MycroftAI/skill-date-time), we can see one of the functions uses `Location` as an optional parameter to the function.

[Link to the code snipped below](https://github.com/MycroftAI/skill-date-time/blob/master/__init__.py#L257
)

```python
@intent_handler(IntentBuilder("").require("Query").require("Time").
                    optionally("Location"))
    def handle_query_time(self, message):
        location = message.data.get("Location")
        current_time = self.get_spoken_time(location)
        if not current_time:
```

The `Location` value is extracted by calling `message.data.get("Location")`. If the named group was named differently, such as `TheUserLocation`, then this code would look like:

```python
@intent_handler(IntentBuilder("").require("Query").require("Time").
                    optionally("TheUserLocation"))
    def handle_query_time(self, message):
        location = message.data.get("TheUserLocation")
        current_time = self.get_spoken_time(location)
        if not current_time:

```

## Simplifying your Skill code with `intent_handler` _decorators_

Your **Skill** code can be simplified using the intent_handler() _decorator_. The major advantage in this approach is that the **Intent** is described together with the method that handles the **Intent**. This makes your code easier to read, easier to write, and errors will be easier to identify.

[Learn more about what _decorators_ are in Python at this link](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators).

The intent_handler() _decorator_ tags a method to be an intent handler for the intent, removing the need for separate registration.

First, you need to `import` the `intent_handler()` library. Include the following line in the `import` section:

```
from mycroft import intent_handler
```

Then, you will be able to use the `@intent_handler` _decorator_:

```python
    @intent_handler(IntentBuilder('IntentName').require('Keyword'))
    def handler_method(self):
        # [...]
```

Using these _decorators_ the **Skill** becomes:

```python
class HelloWorldSkill(MycroftSkill):
    def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")

    @intent_handler(IntentBuilder("ThankYouIntent").require("ThankYouKeyword"))
    def handle_thank_you_intent(self, message):
        self.speak_dialog("welcome")

    @intent_handler(IntentBuilder("HowAreYouIntent")
                    .require("HowAreYouKeyword"))
    def handle_how_are_you_intent(self, message):
        self.speak_dialog("how.are.you")

    @intent_handler(IntentBuilder("HelloWorldIntent")
                    .require("HelloWorldKeyword"))
    def handle_hello_world_intent(self, message):
        self.speak_dialog("hello.world")

    def stop(self):
        pass
```

As seen above the entire initialize() method is removed and the **Intent** registration is moved to the the method declaration.

Ideally, you should use approach to **Intent** registration.

## How do I disable a Skill?

During Skill development you may have reason to disable one or more **Skills**. Rather than constantly install or uninstall them via voice, or by adding and removing them from `/opt/mycroft/skills/`, you can disable them in [the `mycroft.conf` file](https://mycroft.ai/documentation/mycroft-conf/).

First, identify the name of the **Skill**. The name of the **Skill** is the `path` attribute in the [`.gitmodules`](https://github.com/MycroftAI/mycroft-skills/blob/master/.gitmodules) file.

To disable one or more **Skills** on a Mycroft **Device**, find where your `mycroft.conf` file is stored, then edit it using an editor like `nano` or `vi`.

Search for the string `blacklisted` in the file. Then, edit the line below to include the **Skill** you wish to disable, and save the file. You will then need to reboot, or restart the `mycroft` services on the **Device**.

```
  "skills": {
    "blacklisted_skills": ["skill-media", "send_sms", "skill-wolfram-alpha, YOUR_SKILL"]
  }
```

## How to increase the priority of **Skills** during loading

During **Skill** development, you may wish to increase the priority of your **Skill** loading during the startup process. This allows you to start using the **Skill** as soon as possible.

First, identify the name of the **Skill**. The name of the **Skill** is the `path` attribute in the [`.gitmodules`](https://github.com/MycroftAI/mycroft-skills/blob/master/.gitmodules) file.

To prioritize loading one or more **Skills** on a Mycroft **Device**, find where your [`mycroft.conf` file](https://mycroft.ai/documentation/mycroft-conf/) is stored, then edit it using an editor like `nano` or `vi`.

Search for the string `priority` in the file. Then, edit the line below to include the **Skill** you wish to prioritize, and save the file. You will then need to reboot, or restart the `mycroft` services on the **Device**.

```
"priority_skills": ["skill-pairing"],
```

## How do I find more information on Mycroft functions?

You can find documentation on Mycroft functions and helper methods at the [Mycroft Core API documentation](http://mycroft-core.readthedocs.io/en/stable)