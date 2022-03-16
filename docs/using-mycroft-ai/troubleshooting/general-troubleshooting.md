---
description: Troubleshooting tips and tricks
---

# General Troubleshooting

This section is grouped by Device to help you quickly find the information you need.

## All Devices

### I've made changes to my settings on home.mycroft.ai, but these are not reflected on my device

Your Mycroft device will sync settings with the home.mycroft.ai server regularly. In normal circumstances any change should be reflected on the device within 1-2 minutes.

You can also instruct your device to pull down the latest configuration, by saying:

> Hey Mycroft, update configuration

Mycroft will respond in one of two ways:

* If your configuration was out of date, and has been pulled down again, Mycroft will respond:

> Configuration updated

* If your configuration was the same on your device as on home.mycroft.ai, Mycroft will respond:

> Your device has been configured

### Check settings on my device

To see the settings that your device is using requires access to the devices shell (terminal). You can do this by SSHing into your device, or connecting a keyboard and monitor.

The configuration values in use by the system can be obtained using the Configuration Managers `get` command.

{% content-ref url="../customizations/config-manager.md" %}
[config-manager.md](../customizations/config-manager.md)
{% endcontent-ref %}

The settings values that have been retrieved from home.mycroft.ai can also be read directly from `/var/tmp/mycroft_web_cache.json`. See [mycroft.conf](../customizations/mycroft-conf.md) for more details.

{% content-ref url="../customizations/mycroft-conf.md" %}
[mycroft-conf.md](../customizations/mycroft-conf.md)
{% endcontent-ref %}

### Find the IP address of my device

To obtain your devices IP address you can say:

> Hey Mycroft, what is your IP?

Alternatively you can get the IP address from your router, or by scanning the network using a tool like nmap. Running `nmap` with the no port scan flag `-sn` returns the IP and MAC addresses, as well as the vendor name. A Mark 1 will display as "Raspberry Pi Foundation".

## Mark II

If you are experiencing any issues with your Mark II or Mark II Dev Kit, troubleshooting information is available in the Mark II documentation:

{% content-ref url="../get-mycroft/mark-ii.md" %}
[mark-ii.md](../get-mycroft/mark-ii.md)
{% endcontent-ref %}

## Mark 1

### Yellow Eyes

Mark 1 attempts to update its software around every hour or so. Yellow Eyes, part of the [Mark 1 boot sequence](https://mycroft.ai/documentation/mark-1/#mark-1-boot-sequence), occurs when either the software for the Mark 1 or the Skills on the device did not update properly. Generally the solution for Yellow Eyes is to "hard reboot" the Mark 1 - that is, remove the power cable, wait at least 30 seconds, then plug the device back in.

It may take several "hard reboots" to clear the Yellow Eyes symptom.

### HDMI output is not displayed

If you have connected Mark 1 to a HDMI output, and nothing is showing on the HDMI screen, reboot the Mark 1. The Mark 1 needs to reboot before it can output to a HDMI screen.

### Not connected to the internet

If your Mark 1 has previously been connected to the internet, and loses internet connectivity, it will speak

`I have lost connection to the internet`

### Cannot `ssh` into Mark 1

If you `ssh` into Mark 1, (instructions [here](https://mycroft.ai/documentation/mark-1/#connecting-to-the-mark-1-via-ssh)), and have recently reset the device to factory defaults, then you will need to re-enable `ssh`.

Press the Mark 1's top button and turn it to `SSH`, then press the button. Select `ENABLE` then press the button again to enable `ssh`.

`ssh` operates on port 22. Here is an `nmap` scan of a Mark 1 with `ssh` enabled sitting on IP address `192.168.0.2`:

```
$ nmap -Pn 192.168.0.2

Starting Nmap 7.60 ( https://nmap.org ) at 2018-12-12 00:01 AEDT
Nmap scan report for 192.168.0.2
Host is up (0.0042s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 19.56 seconds
```

## Linux

### AttributeError: '\_curses.window' object has no attribute 'get\_wch' (with a custom Python installation)

Some custom installations of Python (with systems such as [pyenv](https://github.com/pyenv/pyenv/)) may get this error when running the interactive Mycroft terminal client. This error occurs because `curses` wide character support hasn't been fully built into the custom Python installation.

The following explanation and instructions are specific to Ubuntu Linux (where [this issue](https://github.com/MycroftAI/mycroft-core/issues/2426) was found) but can be used as a general guide for other distributions as needed.

To resolve this issue, make sure that the following packages are installed:

```
sudo apt install libncursesw5 libncursesw5-dev
```

These packages provide "shared libraries for terminal handling (wide character support)".

After these packages are installed, recompile your Python installation. For pyenv, the command would be:

```
pyenv install <python-version>
```

It will ask for confirmation that you want to rebuild the Python version. After confirming the rebuild, your new Python installation should no longer show the above error when running the Mycroft terminal client.

### Removing and rebuilding your virtual environment

If your CLI won't run, it is highly likely to be an issue with the Mycroft virtual environment. The easiest solution we've found has been to remove and reinstall the virtual environment.

First, delete the existing virtual environment:

```bash
sudo rm -r ~/mycroft-core/.venv/
```

Next, we run the setup script again:

```bash
mycroft-core$ ./dev_setup.sh
```

This will rebuild your virtual environment.

### Installation warns about bad interpreter

When running `dev_setup.sh`, if you encounter a warning about a "bad interpreter", it is likely from having a space in the installation path:

```
./dev_setup.sh: /opt/test path/mycroft-core/.venv/bin/pip: "/opt/test: bad interpreter: No such file or directory
Warning: Failed to install all requirements. Continue? y/N
```

If you can't install to a path without spaces, you will have to manually verify the `requirements.txt` entries are installed to your virtual environment.

### UnicodeDecodeError during setup

This most likely indicates that your unicode locale is not set.

If you are using Docker, ensure that you have a section in your Dockerfile setting up the locale such as:

```
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
```

It has also been [reported](https://github.com/MycroftAI/mycroft-core/issues/2637) that connecting to a machine using RDP was a possible work around 🤷

## Skills development

### Skill fails on first run with `ERROR - Failed to load skill`

If you're developing a Skill, and run it for the first time, you may encounter an error similar to the below:

```bash
12:30:32.158 - mycroft.skills.core:load_skill:142 - INFO - First run of mycroft-skill-cat-facts
12:30:32.164 - mycroft.skills.core:load_skill:156 - ERROR - Failed to load skill: mycroft-skill-cat-facts
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/site-packages/mycroft_core-0.9.7-py2.7.egg/mycroft/skills/core.py", line 144, in load_skill
    skill.settings.store()
  File "/usr/local/lib/python2.7/site-packages/mycroft_core-0.9.7-py2.7.egg/mycroft/skills/settings.py", line 323, in store
    with open(self._settings_path, 'w') as f:
IOError: [Errno 13] Permission denied: '/opt/mycroft/skills/mycroft-skill-cat-facts/settings.json'
```

The error here is that the file system permission on the Skill's directory are incorrect. The directory should have owner and group permissions of `mycroft:mycroft` as per the below.

```bash
4 drwxr-xr-x  4 mycroft mycroft  4096 Nov 24 14:34 .
4 drwxrwxrwx 38 mycroft mycroft  4096 Nov 27 12:50 ..
4 drwxr-xr-x  3 mycroft mycroft  4096 Nov 23 16:57 dialog
4 drwxr-xr-x  8 mycroft mycroft  4096 Nov 27 12:36 .git
4 -rw-r--r--  1 mycroft mycroft    20 Nov 23 16:57 .gitignore
8 -rw-r--r--  1 mycroft mycroft  6265 Nov 23 16:57 init.py
8 -rw-r--r--  1 mycroft mycroft  7509 Nov 24 14:34 init.pyc
12 -rw-r--r--  1 mycroft mycroft 11357 Nov 23 16:57 LICENSE
4 -rw-r--r--  1 mycroft mycroft   695 Nov 24 14:33 README.md
4 -rw-r--r--  1 mycroft mycroft    35 Nov 25 19:28 settings.json
```

If your permissions are different to those shown above, change them by running the following commands:

```bash
cd /opt/mycroft/skills/
sudo chown mycroft:mycroft -R your-skill-name
```
