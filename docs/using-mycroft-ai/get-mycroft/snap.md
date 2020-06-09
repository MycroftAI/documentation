---
description: >-
  Install the Mycroft Snap, a self-contained all-inclusive package for Linux.
---

# Snap install

Mycroft is now available as a Snap package. Providing a simple and secure means of installing Mycroft on a broad range of Linux distributions.

{% hint style="info" %}
The Snap package is considered an Alpha release. It is being actively developed however a number of known issues are listed below.
{% endhint %}

If your system already supports the Snap ecosystem, Mycroft will be available in your Software Store. You can also install it manually by running:
```
snap install mycroft --beta
```

Please note: the `--beta` flag is required whilst the Snap is still being developed. Once we have released a complete version of Mycroft this flag will no longer be needed.

Once installed you can register the device at https://home.mycroft.ai 

{% page-ref page="../pairing-your-device.md" %}

## Known issues

There are a number of known issues with the early release of this Snap. This includes:
- After pairing with your account, Mycroft will immediately report that it is ready for use. There may still be some setup processes finalizing and Mycroft may not respond to commands immediately. Please give it a few more minutes to finish setting up.
- An OSError will be raised for each installation using PIP. This should not affect your usage of the system.
- Additional command line tools such as the Mycroft Skills Manager are not yet available.
- The wake word response time may also be slower than expected. This is the time between you saying "Hey Mycroft" and Mycroft acknowledging and starting to record.
- Some Skills currently fail. The Mycroft IP Skill fails to load, and Audio Record cannot write to disk.
- Currently the selected microphone device cannot be changed after installation.

Please support the development of Mycroft by reporting any additional issues on [Github](https://github.com/MycroftAI/snapcraft-mycroft-core/issues) or the [Community Forums](https://community.mycroft.ai).

## Developing Skills on the Snap

### Mycroft Skills Kit
As noted in known issues above, additional command line tools aren't yet available. This includes the Mycroft Skills Kit.

This can be installed manually from the Python Packaging Index:
```
pip install msk
```

The source code is also available from [our Github](https://github.com/MycroftAI/mycroft-skills-kit).


Alternatively you may start with a template Skill like [Hello World](https://github.com/MycroftAI/skill-hello-world).

### File locations
As the Snaps are contained and cannot access the normal filesystem, the location of some files differ from a traditional Mycroft installation. 

Skills are installed in `~/snap/mycroft/common/mycroft-data/skills/`
Logs for the Snap will show in the CLI or can be accessed directly at `~/snap/mycroft/common/logs/`

Once the Mycroft Snap is up and running, adding a Skill to the correct directory, or modifying a Skill that's already there will automatically reload the Skill allowing you to quickly iterate on your code.

## Further information and support

For general troubleshooting information see:
{% page-ref page="../troubleshooting/" %}

You can also connect with the broader Mycroft Community to access additional support through the [Community Forums](https://community.mycroft.ai) or the [~Linux Packaging channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/ubuntu-apt-packaging).