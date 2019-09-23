---
description: Troubleshooting tips and known errors
---

# General Troubleshooting

This section is grouped by Device to help you quickly find the information you need.

## All Devices

### I've made changes to my settings on home.mycroft.ai, but these are not reflected on my **Device**

Have you recently updated your _Location_ or your measurement preferences \(ie. kilometers vs miles\) in home.mycroft.ai, but these are not reflected on your **Device**?

All **Devices** pull down a local copy of configuration settings from home.mycroft.ai. You may need to instruct your **Device** to pull down your configuration again. To do this, Speak

`hey Mycroft, configuration update`

Mycroft will respond in one of two ways:

* If your configuration was out of date, and has been pulled down again, Mycroft will respond `Your device has been configured`.
* If your configuration was the same on your **Device** as on home.mycroft.ai, Mycroft will respond `Updated configuration`.

If you're comfortable SSHing into your device, SSH in and then run the following commands to see what configuration values are stored locally.

To see the city location value:

`jq ".location.city" < /var/tmp/mycroft_web_cache.json`

To see the latitude and longitude coordinates of your location:

`jq ".location.coordinate" < /var/tmp/mycroft_web_cache.json`

To see the timezone setting:

`jq ".location.timezone" < /var/tmp/mycroft_web_cache.json`

To see the listener setting:

`jq ".listener" < /var/tmp/mycroft_web_cache.json`

To see the Speech to Text \(STT\) settings:

`jq ".stt" < /var/tmp/mycroft_web_cache.json`

To see the Text to Speech \(TTS\) settings:

`jq ".tts" < /var/tmp/mycroft_web_cache.json`

We also have [more information available on `mycroft.conf` and `mycroft_web_cache.json` files](https://mycroft.ai/documentation/mycroft-conf/).

## Troubleshooting Mark 1

### Yellow Eyes

Mark 1 attempts to update its software around every hour or so. Yellow Eyes, part of the [Mark 1 boot sequence](https://mycroft.ai/documentation/mark-1/#mark-1-boot-sequence), occurs when either the software for the Mark 1 or the **Skills** on the **Device** did not update properly. Generally the solution for Yellow Eyes is to "hard reboot" the Mark 1 - that is, remove the power cable, wait at least 30 seconds, then plug the **Device** back in.

It may take several "hard reboots" to clear the Yellow Eyes symptom.

### HDMI output is not displayed

If you have connected Mark 1 to a HDMI output, and nothing is showing on the HDMI screen, reboot the Mark 1. Mark 1 needs to reboot before it can output to a HDMI screen.

### Not connected to the internet

If your Mark 1 has previously been connected to the internet, and loses internet connectivity, it will speak

`I have lost connection to the internet`

### Cannot `ssh` into Mark 1

If you `ssh` into Mark 1, \(instructions [here](https://mycroft.ai/documentation/mark-1/#connecting-to-the-mark-1-via-ssh)\), and have recently reset the **Device** to factory defaults, then you will need to re-enable `ssh`.

Press the Mark 1's top button and turn it to `SSH`, then press the button. Select `ENABLE` then press the button again to enable `ssh`.

`ssh` operates on port 22. Here is an `nmap` scan of a Mark 1 with `ssh` enabled sitting on IP address `192.168.0.2`:

```text
$ nmap -Pn 192.168.0.2

Starting Nmap 7.60 ( https://nmap.org ) at 2018-12-12 00:01 AEDT
Nmap scan report for 192.168.0.2
Host is up (0.0042s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 19.56 seconds
```

## Troubleshooting Picroft

## Troubleshooting Linux

## Troubleshooting Skills development

### Skill fails on first run with `ERROR - Failed to load skill`

If you're developing a **Skill**, and run it for the first time, you may encounter an error similar to the below:

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

The error here is that the file system permission on the **Skill**'s directory are incorrect. The directory should have owner and group permissions of `mycroft:mycroft` as per the below.

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
