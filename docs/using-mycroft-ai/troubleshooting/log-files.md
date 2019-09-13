---
ID: 40001
post_title: Mycroft logs
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/documentation/logs/
published: true
post_date: 2018-12-11 07:20:23
---
# Mycroft logs

- [Mycroft logs](#mycroft-logs)
  * [About the Mycroft logs](#about-the-mycroft-logs)
    + [How to find the Mycroft logs](#how-to-find-the-mycroft-logs)
  * [Log file descriptions](#log-file-descriptions)
    + [audio.log](#audiolog)
    + [bus.log](#buslog)
    + [enclosure.log](#enclosurelog)
    + [skills.log](#skillslog)
    + [update.log](#updatelog)
    + [voice.log](#voicelog)
  * [Useful diagnostic commands](#useful-diagnostic-commands)
    + [Errors in a Skill](#errors-in-a-skill)
    + [Tailing the skills.log](#tailing-the-skillslog)
  * [Log rotation](#log-rotation)

If you request Support from Mycroft, through the [Mycroft Forum](https://community.mycroft.ai), through [Mycroft Chat](https://chat.mycroft.ai) or by [contacting us](https://mycroft.ai/contact/), it is likely we will ask you for _logs_ to help us diagnose the problem. 

The [Support Skill](https://market.mycroft.ai/skill/mycroft-support-helper) automatically generates links to log files - so if you prefer a less detailed approach, then please use the Support Skill. 

This page provides information on the different log files Mycroft uses, where the logs files are located on a Mycroft **Device**, the sort of data that you will find in them, and some common commands to use to aid diagnosis of common issues with Skills and Skill Authoring. 

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

The logs on all **Devices** are held at `/var/log/mycroft/`. 

To access the logs, you will need to `ssh` into the **Device**. You can find [`ssh` instructions for Mark 1](https://mycroft.ai/documentation/mark-1/#connecting-to-the-mark-1-via-ssh) and [`ssh` instructions for Picroft](https://mycroft.ai/documentation/picroft/#connecting-to-picroft-via-ssh) on this site also. 

To find what Mycroft logs are available, run the following Linux command:

`ls -las /var/log/mycroft/`

Example (from a Ubuntu Linux install):

  ```
kathyreid@kathyreid-N76VZ:~$ ls -las /var/log/mycroft
total 2384
   4 drwxrwxrwx  2 root      root         4096 Aug  8 02:01 .
   4 drwxrwxr-x 18 root      syslog       4096 Aug 10  2018 ..
  16 -rw-rw-r--  1 kathyreid kathyreid   16010 Aug  8 02:05 audio.log
 408 -rw-rw-r--  1 kathyreid kathyreid  415043 Aug  8 10:10 bus.log
1940 -rw-rw-r--  1 kathyreid kathyreid 1982758 Aug  8 10:10 skills.log
  12 -rw-rw-r--  1 kathyreid kathyreid    8738 Aug  8 02:05 voice.log
  ```

## Log file descriptions

### audio.log

This log contains information on actions such as:

* When Mycroft loads audio services
* When Mycroft speaks
* When the Text to Speech (TTS) cache is hit
* When volume is increased or decreased

### bus.log

This log contains information on actions such as:

* Messages sent between Mycroft components such as **Skills** and the **Enclosure** that Mycroft is running on
* Data generated through invoking and controlling **Skills**
* Errors related to reading _configuration_ files

### enclosure.log

This log contains information on actions such as:

* Loading of configurations for the **Enclosure**
* Altering properties of the **Enclosure**, such as the Eyes or Mouth on a Mark 1
* Activities related to the **Enclosure** Display Manager

### skills.log

This log contains information on actions such as:

* The outcome of Mycroft attempting to load **Skills**, such as whether a Skill was successfully loaded, blacklisted (disabled by Mycroft) or failed to load
* When an **Utterance** is spoken, which **Skill** it was matched with, and the information provided to the **Skill**
* Information related to the Mycroft Skill Manager (msm), including an msm-specific error code.

### update.log

Some **Enclosures**, like the [Mark 1](https://mycroft.ai/documentation/mark-1/) and [Picroft](https://mycroft.ai/documentation/picroft/) will automatically try to update their software periodically. This log is the output of the update process, and has similar output to what you would see if you manually ran `apt-get update`. This includes the number of packages updated, which packages were removed, and which packages were held back. 

### voice.log

This log contains information on actions such as:

* Registration and activation of Wake Words
* Any errors associated with the [Precise](https://mycroft.ai/documentation/precise) Wake Word listener functionality
* Transcriptions from the Speech to Text (STT) service
* When the Text to Speech (TTS) service was activated

## Useful diagnostic commands

### Errors in a Skill

To find the errors related to a particular **Skill**, use this command once you have created an `ssh` connection: 

`cat /var/log/mycroft/skills.log | grep -i error | grep -i SKILLNAME`

where `SKILLNAME` is the name of the **Skill**. 

### Tailing the skills.log

If you are [developing new Skills for Mycroft](https://mycroft.ai/documentation/skills/developing-skills/), then we strongly recommend that you `tail` the `skills.log` log file as you are doing development work, so that you can easily observe any errors that your **Skill** is throwing. To do this, use this command: 

`tail -f /var/log/mycroft/skills.log`

To stop `tail`ing the log, press Ctrl + C. 

## Log rotation

On Picroft and Mark 1 **Devices**, _log rotation_ is implemented using the `logrotate` utility. This means that log files are _rotated_ every 24 hours to a new file. When a log file is rotated, it is given a name with a number suffix. Yesterday's log file is `logname.log.1` and the day before yesterday's is named `logname.log.2` and so on. This makes it easier to troubleshoot an error to the time or date that it occurred, and also ensures that disk space on the **Device** is not exhausted. 

On Linux installations, _log rotation_ is **not** implemented, so you may have to manually delete logs from time to time if they are taking up too much space. 

If you accidentally delete your log files, they will be recreated the next time the Mycroft services are started.

Here is an example of a Mark 1's `/var/log/mycroft` directory, showing log rotation:

```
pi@mark_1:/var/log/mycroft $ ls -las
total 89816
    4 drwxr-xr-x 2 root    root     4096 Dec 10 06:25 .
    4 drwxr-xr-x 7 root    root     4096 Dec 10 06:25 ..
    4 -rw-r--r-- 1 mycroft root      933 Dec 10 14:30 audio.log
    8 -rw-r--r-- 1 mycroft root     5633 Dec 10 06:25 audio.log.1
   40 -rw-r--r-- 1 mycroft root    38682 Nov 22 06:25 audio.log.10
   20 -rw-r--r-- 1 mycroft root    20273 Dec  7 06:25 audio.log.2
    4 -rw-r--r-- 1 mycroft root     1943 Dec  6 06:25 audio.log.3
    4 -rw-r--r-- 1 mycroft root     1121 Dec  5 06:25 audio.log.4
   12 -rw-r--r-- 1 mycroft root    10191 Dec  4 06:25 audio.log.5
    4 -rw-r--r-- 1 mycroft root     2816 Nov 29 06:25 audio.log.6
   48 -rw-r--r-- 1 mycroft root    47917 Nov 28 06:25 audio.log.7
   12 -rw-r--r-- 1 mycroft root     9871 Nov 26 06:25 audio.log.8
   16 -rw-r--r-- 1 mycroft root    15883 Nov 23 06:25 audio.log.9
44852 -rw-r--r-- 1 mycroft root 45921716 Dec  7 03:26 bus.log
    0 -rw-r--r-- 1 mycroft root        0 Dec  7 06:25 enclosure.log
    4 -rw-r--r-- 1 mycroft root      418 Dec  7 06:25 enclosure.log.1
   36 -rw-r--r-- 1 mycroft root    33976 Dec  4 06:25 enclosure.log.2
    8 -rw-r--r-- 1 mycroft root     4461 Oct 20 06:25 enclosure.log.3
 2868 -rw-r--r-- 1 mycroft root  2930854 Dec 10 14:30 skills.log
 8528 -rw-r--r-- 1 mycroft root  8730857 Dec 10 06:25 skills.log.1
 1508 -rw-r--r-- 1 mycroft root  1541451 Dec  1 06:25 skills.log.10
 8628 -rw-r--r-- 1 mycroft root  8834148 Dec  9 06:25 skills.log.2
 8460 -rw-r--r-- 1 mycroft root  8661635 Dec  8 06:25 skills.log.3
 6804 -rw-r--r-- 1 mycroft root  6966852 Dec  7 06:25 skills.log.4
 1492 -rw-r--r-- 1 mycroft root  1523841 Dec  6 06:25 skills.log.5
 1488 -rw-r--r-- 1 mycroft root  1522848 Dec  5 06:25 skills.log.6
 1576 -rw-r--r-- 1 mycroft root  1609923 Dec  4 06:25 skills.log.7
 1472 -rw-r--r-- 1 mycroft root  1506036 Dec  3 06:25 skills.log.8
 1532 -rw-r--r-- 1 mycroft root  1568671 Dec  2 06:25 skills.log.9
   16 -rw-r--r-- 1 root    root    12704 Dec 10 14:17 update.log
   64 -rw-r--r-- 1 root    root    64801 Dec  9 06:25 update.log.1
   76 -rw-r--r-- 1 root    root    75478 Dec  3 06:25 update.log.2
   72 -rw-r--r-- 1 root    root    70682 Nov 25 06:25 update.log.3
   56 -rw-r--r-- 1 root    root    57312 Nov 18 06:25 update.log.4
    4 -rw-r--r-- 1 mycroft root     3040 Dec 10 14:30 voice.log
   16 -rw-r--r-- 1 mycroft root    14094 Dec 10 06:25 voice.log.1
    8 -rw-r--r-- 1 mycroft root     4512 Nov 29 06:25 voice.log.10
    4 -rw-r--r-- 1 mycroft root     1569 Dec  9 06:25 voice.log.2
   16 -rw-r--r-- 1 mycroft root    12922 Dec  7 06:25 voice.log.3
    8 -rw-r--r-- 1 mycroft root     6272 Dec  6 06:25 voice.log.4
    4 -rw-r--r-- 1 mycroft root     2959 Dec  5 06:25 voice.log.5
   20 -rw-r--r-- 1 mycroft root    19875 Dec  4 06:25 voice.log.6
    8 -rw-r--r-- 1 mycroft root     6849 Dec  2 06:25 voice.log.7
    4 -rw-r--r-- 1 mycroft root     1788 Dec  1 06:25 voice.log.8
    4 -rw-r--r-- 1 mycroft root     1720 Nov 30 06:25 voice.log.9

```
