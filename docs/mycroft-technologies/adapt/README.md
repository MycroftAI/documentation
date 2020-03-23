---
description: >-
  Adapt is an intent parser - meaning that it is a library for converting
  natural language into machine-readable data structures, such as JSON.
---

# Adapt

## What is the Adapt Intent Parser?

The Adapt Intent Parser is open source software. It is lightweight and is designed to run on devices with limited computing resources, such as embedded devices.

{% embed url="https://www.youtube.com/watch?v=zR9xvPtM6Ro" caption="" %}

Adapt takes in natural language as an input, and outputs a data structure that includes

* the **Intent**: what the User is trying to do
* **a match probability**: how confident Adapt is that the **Intent** has been correctly identified
* a tagged list of **entities**: that can be used by **Skills** to perform functions

Adapt is useful for interpreting natural language input. For example, you might want to create a [voice user interface](https://en.wikipedia.org/wiki/Voice_user_interface) that allows a User to play a Pandora station. The **Utterances** a User might Speak include:

* `Turn on Pandora`
* `Play Pandora`
* `Play my Joan Jett Pandora station`

The Adapt Intent Parser takes this input and generates a JSON data structure like this:

```javascript
{
    "confidence": 0.61,
    "target": null,
    "Artist": "joan jett",
    "intent_type": "MusicIntent",
    "MusicVerb": "put on",
    "MusicKeyword": "pandora"
}
```

Applications - or Mycroft Skills - can then parse the JSON data take appropriate action - such as playing Joan Jett using the open source Pandora application [Pianobar](https://6xq.net/pianobar/).

## Is Adapt right for me or my use cases?

{% hint style="info" %}
If you are looking to use Adapt in a Mycroft Skill, please see [Skill Development &gt; Intents](../../skill-development/intents/)
{% endhint %}

Adapt is useful for determining user intent quickly and accurately from natural language. It is particularly beneficial for applications with limited vocabularies - that is, where the User will only issue a small number of **Utterances**.

Adapt has a number of features.

### Lightweight

Adapt is written to run on embedded system with limited resources. Adapt can be used as the engine to parse natural language on IoT devices like remote controls and hubs.

### Portable

Adapt is written in Python. Python is very widely adopted and supported in the technical community. Because it is written in Python, Adapt will run on many different devices - from servers to a Raspberry Pi. Adapt is designed to be run cross-platform and can be deployed in software environments that include Android, iOS, Windows and Linux.

### Reliable

Because Adapt is small enough to run locally on an embedded device, it removes the dependency of having to parse intent in the cloud. This allows applications to function when they don't have an internet connection. Adapt is therefore suited to environments where the internet connection is slow, unreliable or intermittent.

### Open source

At Mycroft.AI, we believe that artficial intelligence is too important to be controlled by a few large companies. Adapt is open source, licensed under the Apache v2.0 license. Anyone can access the [source code](https://github.com/mycroftai/adapt), change the software and use Adapt Intent Parser in new applications.

[Open Source](https://en.wikipedia.org/wiki/Open-source_software) software powers the Internet. Artificial intelligence software, like Adapt Intent Parser, is gaining in importance. However, very few artificial intelligence software is open source. Here at Mycroft.AI, we believe that natural language processing is going to be a key component of many future technologies. By sharing our software we believe that we can help bring artificial intelligence to the open source community where it can be used to benefit millions of users world wide. We hope to work with other open source initiatives like [TensorFlow](https://www.tensorflow.org/) and [OpenAI](https://openai.com/) to ensure that the future of artificial intelligence is open for all.

## Who developed Adapt?

Adapt Intent Parser was developed at Mycroft.AI by a team led by [Sean Fitzgerald](https://github.com/clusterfudge). Sean was previously a developer at both Siri and Amazon Echo.

## How do I install Adapt Intent Parser?

### Requirements

Adapt Intent Parser requires Python 2.7.

### `pip` installation

`pip` is a package manager used to install and manage software packages in Python. To use `pip` you first need to install it.

#### Installing `pip` for Ubuntu / Debian based Linux

`$ sudo apt-get install python-pip python-dev`

#### Installing `pip` for Fedora / RPM based Linux

`$ sudo dnf install python-pip python-devel`

### Installing Adapt Intent Parser

_NOTE: For development on Adapt and Mycroft we use the sandboxing tool `virtualenv` to isolate Adapt from other software. This allows for dependencies to be configured just for Adapt, rather than installing them globally. This approach prevents conflicts between Adapt and other software._

#### Installing Adapt for Ubuntu, Debian or Raspbian

Install Adapt via `pip` into your project's `virtualenv`:

```bash
$ sudo apt-get install virtualenv
$ virtualenv myvirtualenv
$ . myvirtualenv/bin/activate
$ pip install -e git+https://github.com/mycroftai/adapt#egg=adapt-parser
```

## How do I contribute to Adapt Intent Parser?

### For Ubuntu, Debian and Raspbian based Linux

To develop on Adapt itself, or try the examples, check out the repo from GitHub and set up a `virtualenv`.

```bash
$ sudo apt-get install virtualenv
$ virtualenv myvirtualenv
$ . myvirtualenv/bin/activate
$ git clone https://github.com/mycroftai/adapt
$ cd adapt
$ pip install -r requirements.txt
```

Verify the installation by running the example code from the Adapt repository.

```bash
$ cd ~/adapt
PYTHONPATH=. python examples/multi_intent_parser.py "play some music by the clash"
```

### For Fedora / RPM based Linux

To develop with the latest Adapt, install it via `pip` into your project's `virtualenv`:

```bash
$ pip install virtualenv
$ virtualenv myvirtualenv
$ source myvirtualenv/bin/activate
$ pip install -e git+https://github.com/mycroftai/adapt#egg=adapt-parser
```

To develop on Adapt itself, or try the examples, check out the repo from GitHub and set up a `virtualenv`.

```bash
$ pip install virtualenv
$ virtualenv myvirtualenv
$ source myvirtualenv/bin/activate
$ git clone https://github.com/mycroftai/adapt
$ cd adapt
$ pip install -r requirements.txt
```

Verify the installation by running the example code from the Adapt repository.

```bash
$ cd ~/adapt
PYTHONPATH=. python examples/multi_intent_parser.py "play some music by the clash"
```

### For MacOS X

First, Xcode must be installed and Apple’s license agreement accepted.

`$ xcode-select --install`

Next, install the [Homebrew package manager](https://brew.sh/) and update `brew` packages.

`$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

`brew update`

Next, install Adapt dependencies with `brew` and `python-pip`.

```bash
$ brew install git python
$ pip install python virtualenv
```

To develop with the latest Adapt, install it via `pip` into your project's `virtualenv`:

```bash
$ virtualenv myvirtualenv
$ . myvirtualenv/bin/activate
$ pip install -e git+https://github.com/mycroftai/adapt#egg=adapt-parser
```

To develop on Adapt itself, or try the examples, check out the repo from GitHub and set up a `virtualenv`.

```bash
$ virtualenv myvirtualenv
$ . myvirtualenv/bin/activate
$ git clone https://github.com/mycroftai/adapt
$ cd adapt
$ pip install -r requirements.txt
```

Verify the installation by running the example code from the Adapt repository.

```bash
$ cd ~/adapt
PYTHONPATH=. python examples/multi_intent_parser.py "play some music by the clash"
```

