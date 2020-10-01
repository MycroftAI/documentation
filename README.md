
Mycroft Documentation
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Join chat](https://img.shields.io/badge/Mattermost-join_chat-brightgreen.svg)](https://chat.mycroft.ai/community/channels/documentation)
[![CLA Required](https://img.shields.io/badge/CLA%3F-Required-blue.svg)](https://mycroft.ai/cla)
==========

Mycroft is an open source privacy-focused voice assistant. It can be installed on Linux, Raspberry Pi, our reference devices, or your own custom hardware.
Head to https://mycroft.ai/documentation for all public facing documentation.
The website is automatically updated from this repo.

## Table of Contents
- [Objective](#objective)
- [Project lead and key contact](#project-lead-and-key-contact)
- [Branches](#branches)
- [Documentation standards](#documentation-standards)
  * [Conventions](#conventions)
    + [Styling conventions](#styling-conventions)
      - [How voice interactions are presented in documentation](#how-voice-interactions-are-presented-in-documentation)
      - [How to present a User Speaking](#how-to-present-a-user-speaking)
  * [Tone of voice](#tone-of-voice)
  * [Documentation checklist](#documentation-checklist)
- [Contributing](#contributing)
- [License](#license)

## Objective
The purpose of this repo is to unify all the documentation for the public-facing components of Mycroft.AI, and to reduce the fragmentation of documentation.

It is intended that the Markdown in this repo will be consumed by transformation layers or integrations to present the documentation in a user-friendly way.

## Project lead and key contact

@krisgesling - Kris Gesling [kris.gesling@mycroft.ai](mailto:kris.gesling@mycroft.ai)

## Branches

At the time of writing, the Docs Repository has only a single branch, `master`. This is the default branch for the repo.

## Documentation standards

### Conventions

The following conventions are observed in Mycroft documentation:

* All code is presented `like this`
* All Mycroft-specific terms are **bolded**
* Information is presented in 'inverted pyramid format'. This means an overview is given first, then more detailed information, then more granular information.
* Human-written documentation is done in Markdown, on GitHub
* Documentation of code is done through Google DocStrings format https://google.github.io/styleguide/pyguide.html#Comments and this then passed to documentation generators.


#### Styling conventions

The following conventions are used for styling technical terms and related phrases.

* **internet** is always written in lowercase, never as Internet unless at the start of a sentence.
* **Mark 1** is always styled as such
* **Metadata** is always styled as one word
* **Micro SD card** is always styled as such, not as micro sd card, micro SD card or alternatives
* **Picroft** is always styled as such
* **PocketSphinx** is always styled as such
* **Skill Author** is always used to refer to the developer, writer or creator of a **Skill**.
* **Speak** is always capitalized given the importance of Speaking in a voice interface.
* **User** is always capitalized as a sign of respect for our Users.

##### How voice interactions are presented in documentation

To make documentation easier to read, voice interactions should be presented in a consistent style.

##### How to present a User Speaking

When a User Speaks, it is always presented in the style of a quote:

> Hey Mycroft, what time is it?

When Mycroft Speaks, it is always presented in quote marks in preformatted style:

`"The time is 12.30"`

### Tone of voice

Mycroft documentation is written with the following tone of voice:

* Knowledgeable but never arrogant
* Helpful but encouraging of self-discovery
* Easily readable, but not dumbed down

### Documentation checklist

Use this handy checklist when creating or modifying documentation:

- [ ] Have you checked for duplicate documentation?
- [ ] Has the documentation been verified for accuracy?
- [ ] Does the documentation comply with the Style Guide?
- [ ] Does the documentation comply with tone of voice?

## Contributing
[See the Contributing Guide for Mycroft Documentation](CONTRIBUTING.md)

## License
[See the License for Mycroft Documenation](LICENSE.md)
