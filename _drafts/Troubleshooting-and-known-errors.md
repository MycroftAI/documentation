---
ID: 32456
post_title: Troubleshooting and known errors
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?page_id=32456
published: false
---
# Troubleshooting and known errors

This section is grouped by Device to help you quickly find the information you need.


## Help us to help you

When you contact Mycroft for support, we may ask for some of the following information:

* What type of Mycroft **Device** you're using, such as Mark 1, Picroft, KDE Plasmoid and so on
* Whether your **Device** was **Paired**
* Your home.mycroft.ai account details
* Information from your Mycroft logs

## About the Mycroft logs

The Mycroft logs each follow a standard format, being:

* A timestamp
* The function or action that was called
* The **level** of the error, which can be one of:

  * DEBUG - incidental information used for debugging purposes
  * INFO - informational log entries which do not indicate an error  
  * WARNING - an error occurred, but it did not stop execution of the **Skill** or process
  * ERROR - an error occurred, and it stopped execution of a **Skill** or other process
  * CRITICAL - a significant error occurred, and it halted execution of the Mycroft functionality itself

### How to find the Mycroft logs

#### Mark 1

  On a Mark 1 **Device**, first `ssh` into the Mark 1.

  @TODO: link to instruction here on SSH'ing into the devices

  The logs on a Mark 1 are held at `/var/log/`

  To find the specific Mycroft logs, run the following Linux command:

  `ls -las | grep -i Mycroft`

  This command lists all the log files with 'Mycroft' in the file name.

  Example:

  ```
  pi@mark_1:/var/log $ ls -las | grep mycroft
     20 -rw-r--r--  1 mycroft root    17136 Oct 16 15:52 mycroft-audio.log
  22808 -rw-r--r--  1 mycroft root 23348347 Oct 17 10:19 mycroft-enclosure-client.log
  38336 -rw-r--r--  1 mycroft root 39249935 Oct 17 10:19 mycroft-messagebus.log
  24564 -rw-r--r--  1 mycroft root 25147196 Oct 17 10:19 mycroft-skills.log
     28 -rw-r--r--  1 mycroft root    23272 Oct 16 15:52 mycroft-speech-client.log
    584 -rw-r--r--  1 root    root   590008 Oct 17 10:00 mycroft-update.log
     84 -rw-r--r--  1 mycroft root    84493 Oct 16 12:50 mycroft-wifi-setup-client.log
  ```

#### Picroft

On a Raspberry Pi 3 running Picroft, first `ssh` into the Picroft.

@TODO: link to instruction here on SSH'ing into the devices

The logs on a Picroft are held at

@TODO: haven't build a Picroft yet, will need to fill this in


#### Linux

On a Linux device running Mycroft for Linux, the logs are held at;

`scripts/logs`
relative to where mycroft-core was installed.

```
$ ls -las
total 191360
    8 drwxrwxr-x 2 kathyreid kathyreid     4096 Sep  4 14:05 .
    8 drwxrwxr-x 3 kathyreid kathyreid     4096 Sep  4 14:05 ..
  344 -rw-rw-r-- 1 kathyreid kathyreid   341056 Oct 17 00:44 mycroft-audio.log
95552 -rw-rw-r-- 1 kathyreid kathyreid 97836905 Oct 17 00:44 mycroft-cli.log
   36 -rw-rw-r-- 1 kathyreid kathyreid    25499 Oct 17 00:44 mycroft-service.log
94968 -rw-rw-r-- 1 kathyreid kathyreid 97238978 Oct 17 00:44 mycroft-skills.log
  444 -rw-rw-r-- 1 kathyreid kathyreid   442637 Oct 17 00:44 mycroft-voice.log
```

#### Android

@TODO Not sure where log files are on Android

## Log file descriptions

### mycroft-audio.log

This log contains information on actions such as:

* When Mycroft loads audio services
* When Mycroft speaks
* When the Text to Speech (TTS) cache is hit
* When volume is increased or decreased

### mycroft-cli.log

This log is primarily used on Linux installations of Mycroft and contains information on actions such as:

* Errors and warnings with Mycroft services
* When a **Fallback** cannot handle an **Intent**

### mycroft-enclosure-client.log

This log contains information on actions such as:

* Loading of configurations for the **Enclosure**
* Altering properties of the **Enclosure**, such as the Eyes or Mouth on a Mark 1
* Activities related to the **Enclosure** Display Manager

### mycroft-messagebus.log

This log contains information on actions such as:

* Messages sent between Mycroft components such as **Skills** and the **Enclosure** that Mycroft is running on
* Data generated through invoking and controlling **Skills**

### mycroft-skills.log

This log contains information on actions such as:

* The outcome of Mycroft attempting to load **Skills**, such as whether a Skill was successfully loaded, blacklisted (disabled by Mycroft) or failed to load
* When an **Utterance** is spoken, which **Skill** it was matched with, and the information provided to the **Skill**
* Information related to the Mycroft Skill Manager (msm), including an msm-specific error code.

### mycroft-speech-client.log

This log contains information on actions such as:

* Loading of configuration information from the **Device**
* Registration of keywords associated with **Utterances** and **Skills**
* Any errors associated with the 'listener' functionality

### mycroft-update.log

Some **Enclosures**, like the Mark 1, will automatically try to update their software periodically. This log is the output of this log, and has similar output to what you would see if you manually ran `apt-get update`.

### mycroft-wifi-setup-client.log

Some **Enclosures**, like the Mark 1, will create a WiFi hotspot when they are first set up. This log contains messages related to the creation and tear-down of the WiFi hotspot, as well as errors and information related to clients connecting to the WiFi hotspot.

## Troubleshooting Mark 1

#### Not connected to the internet

##### If your Mark 1 loses internet connectivity

If your Mark 1 has previously been connected to the internet, and loses internet connectivity, it will Speak

`I have lost connection to the internet`