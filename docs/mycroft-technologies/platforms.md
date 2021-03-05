---
description: >-
  A list of Mycroft hardware devices and software platforms and the repositories
  specific to them.
---

# Platforms

Mycroft has a number of devices and software platforms. Most have some unique code or may have dedicated information stored in a repository.

## Mark II

* [Mark II hardware](https://github.com/MycroftAI/hardware-mycroft-mark-II) - all of the designs and technical details of the Mycroft Mark II Prototypes.
* [mycroft-gui](http://github.com/MycroftAI/mycroft-gui) - Qt GUI Framework used by the Mark II and other projects.
* [mycroft-gui-mark-2](https://github.com/MycroftAI/mycroft-gui-mark-2) - Plasma Shell components for the Mark II including the pull-down menu and virtual keyboard.
* [skill-mark-2](https://github.com/MycroftAI/skill-mark-2) - Skill providing user interaction for device specific actions. Much of this will be moved to the Mark II enclosure.
* [skill-wifi-connect](https://github.com/MycroftAI/skill-wifi-connect) - Audio and visual prompts for the Pantacor Wifi Connect system.
* [mycroft-core\#feature/mark-2](https://github.com/mycroftai/mycroft-core/tree/feature/mark-2) - Feature branch of mycroft-core containing Mark II development code. This was branched to allow the development team to rapidly iterate. It will be merged back into the mainline project shortly.

### Deprecated

The following repositories were used by previous versions of the Mark II.

* [enclosure-mark2](https://github.com/MycroftAI/enclosure-mark2)
* [skill-mark-2-pi](https://github.com/MycroftAI/skill-mark-2-pi)

## Mark 1

* [hardware-mycroft-mark-1](https://github.com/MycroftAI/hardware-mycroft-mark-1) - all of the designs and technical details of the Mycroft Mark 1.
* [enclosure-mark-1](https://github.com/MycroftAI/enclosure-mark1) - the code run on the Arduino within a Mark 1 unit. It manages the eyes, the mouth, and the button.
* [mycroft-mark-1](https://github.com/MycroftAI/mycroft-mark-1) - Skill providing user interaction for device specific actions.
* [skill-mark1-demo](https://github.com/MycroftAI/skill-mark1-demo) - A Skill to showcase the features of the Mark 1.
* [mark-1-update-test](https://github.com/MycroftAI/mark-1-update-test) - This will mount a mark 1 production image and run a test script inside of it with qemu.
* [skill-platform-patch](https://github.com/MycroftAI/skill-platform-patch) - Updates original Mark 1 devices running mycroft-core versions less than 0.9.0, allowing them to upgrade to the latest version of Mycroft.

## Picroft

* [enclosure-picroft](https://github.com/MycroftAI/enclosure-picroft) - Build recipe and assets for creating Picroft images.

## Snapcraft

* [snapcroft-mycroft-core](https://github.com/MycroftAI/snapcraft-mycroft-core) - Snap build configuration for Mycroft.

