---
ID: 33614
post_title: 'Picroft &#8211; editing automatic update settings'
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/picroft/picroft-automatic-update/
published: true
post_date: 2017-12-06 12:10:34
---
# Picroft - editing automatic update settings

- [Picroft - editing automatic update settings](#picroft---editing-automatic-update-settings)
  * [To turn off checking for updates at boot](#to-turn-off-checking-for-updates-at-boot)
  * [To change the time that Picroft checks for updates, or to disable auto-update](#to-change-the-time-that-picroft-checks-for-updates-or-to-disable-auto-update)

By default, Picroft will check for updates at two separate times: 

* On boot
* If left plugged in overnight

@TODO - can we be more specific about the trigger - is it time based?

To edit these defaults, follow these instructions. 

## To turn off checking for updates at boot

Edit the `auto_run.sh` file and comment out the check for updates section with a `#`

```
nano auto_run.sh
```

In the section that says: 

```
   # First, force an upgrade if one is available
   if ping -q -c 1 -W 1 google.com >/dev/null 2>&1
   then
      echo "Checking for updates to Mycroft..."
      sudo apt-get update -o Dir::Etc::sourcelist="sources.list.d/repo.mycroft.ai.list" \
                     -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"
      sudo apt-get install --only-upgrade mycroft-core mimic -y
   fi
   echo ""
   echo "========================================"
   python -c "import mycroft.version; print 'Mycroft Core Version: '+mycroft.version.CORE_VERSION_STR"
   echo "========================================"
```

comment out all lines. To comment them out, copy and paste the following:

```
   # First, force an upgrade if one is available
   #if ping -q -c 1 -W 1 google.com >/dev/null 2>&1
   #then
      #echo "Checking for updates to Mycroft..."
      #sudo apt-get update -o Dir::Etc::sourcelist="sources.list.d/repo.mycroft.ai.list" \
                     -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"
      #sudo apt-get install --only-upgrade mycroft-core mimic -y
   #fi
   #echo ""
   #echo "========================================"
   #python -c "import mycroft.version; print 'Mycroft Core Version: '+mycroft.version.CORE_VERSION_STR"
   #echo "========================================"
```

## To change the time that Picroft checks for updates, or to disable auto-update

To do this, we edit the [cron jobs](https://en.wikipedia.org/wiki/Cron) for the root user

```
sudo crontab -u root -e
```

You can either comment out the one line or change the time. By default, it's a 0400hrs UTC time. The line is as follows:

```
0 4 * * *  /usr/bin/apt-get update  >> /var/log/mycroft-update.log  && /usr/bin/apt-get install --only-upgrade mycroft-core mimic -y  >> /var/log/mycroft-update.log
```

If you're new to cron jobs, or haven't edited a `crontab` before, [this tutorial from Ubuntu](https://help.ubuntu.com/community/CronHowto) will be helpful.