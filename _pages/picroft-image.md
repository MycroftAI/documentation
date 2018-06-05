---
ID: 38573
post_title: Creating a new Picroft image
author: Kathy Reid
post_excerpt: >
  Follow these instructions to create your
  own Picroft image
layout: page
permalink: >
  http://mycroft.ai/documentation/picroft/picroft-image/
published: true
post_date: 2018-06-05 09:18:18
---
# Creating a new Picroft image

Are you looking for the latest Picroft disk images?

* [Picroft stable disk image](https://mycroft.ai/to/picroft-image)
* [Picroft unstable disk image](https://mycroft.ai/to/picroft-unstable)

## Introduction

This documentation shows you how to generate the base Picroft installation. Once you have a base Picroft installation, you can snapshot your installation to produce a Picroft disk image. 

### Requirements

As well as the below hardware requirements, we also assume that you are comfortable on a Linux command line. 

* Raspberry Pi 3
* 8 GB Micro SD card
* Keyboard
* HDMI monitor/cable
* Ethernet cable, network connection
* Computer for burning/creating SD images, using tools like `dd` under Linux or [dotNet Disk Imager](https://sourceforge.net/projects/dotnetdiskimager/) under Windows

## Procedure

### Install operating system

* Burn the Raspbian Lite image to the Micro SD card. The Raspbian Lite image is available from [the Raspberry Pi downloads repository](http://downloads.raspberrypi.org/raspbian_lite/images/?C=M;O=D). You can use tools like [Etcher](https://etcher.io/) to burn the disk image to the Micro SD card. 
* Insert the Micro SD card into the Raspberry Pi. Plug in the network cable, keyboard and monitor. Attach the power cable and power up. 
* Once booted, log into the Raspberry Pi using the username `pi` and password `raspberry`.
* Now, we will set some operating sysem settings. Type `sudo raspi-config` at the prompt. 

```
- '2 Hostname'\
--> Enter: `picroft`
- '3 Boot Options'\
--> 'B1 Desktop / CLI'\
--> 'B2 Console Autologin'
- '3 Boot Options'\
--> 'B2 Wait for Network at Boot'\
--> 'No'\
--> 'Ok'
- '5 Localisation Options'\
--> 'I3 Change Keyboard Layout'\
--> 'Generic 101-key PC'\
--> 'Other'\
--> 'English (US)'\
--> 'English (US)'\
--> 'The default for the keyboard layout'\
--> 'No compose key'
- '7 Advanced Options'\
-->'A1 Expand Filesystem'
```

Finish, and allow the Raspberry Pi to reboot

### Enable ssh service

Next, we enable the `ssh` service and allow it to start at boot. This allows us to connect remotely to Picroft. Type the following commands at the command prompt. 

`sudo systemctl enable ssh.service`
`sudo systemctl start ssh.service`

Once this command has completed, you can _optionally_ connect to the device via `ssh`, and unplug the monitor and keyboard. You will still need the network cable plugged in until you have WiFi configured. 

### Configuring WiFi

Next, we will edit the `wpa_supplicant.conf` file which contains the information Picroft needs to be able to connect to your WiFi. 

Type the following command: 

`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

At the end of the `wpa_supplicant.conf` file, add the SSID and password for your WiFi network. 

```
network={
ssid="_your network ssid_"
psk="_your network password_"
}
``` 

### Install Mycroft repos

Ensure you are connected to the internet, then run these commands at the command prompt: 

* `sudo apt-get update`
* `sudo apt-get install apt-transport-https -y`
* `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F3B1AA8B`
* `sudo bash -c 'echo "deb http://repo.mycroft.ai/repos/apt/debian debian main" > /etc/apt/sources.list.d/repo.mycroft.ai.list'`
* `sudo apt-get update`
* `sudo apt-get install mycroft-picroft -y`

### Install git version control 

Ensure you are connected to the internet, then run this command at the command prompt: 

* `sudo apt-get install git -y`

### Install vim

Ensure you are connected to the internet, then run this command at the command prompt: 

* `sudo apt-get install vim-tiny -y`

### Create a cron job for auto updates

Ensure you are connected to the internet, then run these commands at the command prompt: 

* `sudo crontab -e`

Choose your preferred editor, then add the following at the bottom of the `cron` file:

```bash
0 4 * * * /usr/bin/apt-get update >> /var/log/mycroft-update.log && /usr/bin/apt-get install --only-upgrade mycroft-picroft -y >> /var/log/mycroft-update.log
```

### Add configuration for platform detection

Ensure you are connected to the internet, then run these commands at the command prompt: 

* `sudo mkdir /etc/mycroft`
* `sudo nano /etc/mycroft/mycroft.conf` 

and add the following to the file:

```json
{
    "play_wav_cmdline": "aplay -Dhw:0,0 %1",
    "play_mp3_cmdline": "mpg123 -a hw:0,0 %1",
    "enclosure": {
    	"platform": "picroft",
    	"update": true,
    	"test": false
	},
	"tts": {
    	"module": "mimic",
    	"mimic": {
        	"voice": "ap",
        	"path": "/usr/local/bin/mimic"
    	}
	}
}
```

### Add Picroft components

Copy the contents of [enclosure-picroft](https://github.com/MycroftAI/enclosure-picroft/tree/master/home/pi) into `/home/pi/` subdirectory. 

@TODO provide easier instructions for copying


### Run the update script

Ensure you are connected to the internet, then run these commands at the command prompt:


* `echo "Updating Picroft scripts!"`
* `speak "Updating Picroft, please hold on."`
* `wget -N https://raw.githubusercontent.com/MycroftAI/enclosure-picroft/master/home/pi/update.sh`
* `source update.sh`
* `cp /tmp/version ~/version`

### Restart Picroft

Run these commands at the command prompt: 

* `echo "Rebooting now"`
* `speak "Update complete, restarting."`
* `sudo reboot now`

### Create a RAM disk

Next, we create a RAM disk to reduce the number of physical disk writes. In the past, we've found that the high number of physical disk writes can damage the Micro SD card. The RAM disk is used for [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication). 

Run these commands at the command prompt: 

* `sudo mkdir /ramdisk`
* Edit `/etc/fstab` and add the following line:
`tmpfs /ramdisk tmpfs rw,nodev,nosuid,size=20M 0 0`
* Edit `/etc/mycroft/mycroft.conf` and add the line
`"ipc_path": "/ramdisk/mycroft/ipc/"`
at the end. (remember the comma on the line before)

### Upgrade packages

Next, we upgrade all packages except `raspberrypi-kernel`.

Run these commands at the command prompt: 

* `sudo apt-get update`
* `echo "raspberrypi-kernel hold" | sudo dpkg --set-selections`
* `sudo apt-get upgrade`

#### Set up packagekit

[packagekit](https://en.wikipedia.org/wiki/PackageKit) is a utility that makes packaging easier. 

* Install the `packagekit` package: `apt-get install packagekit`
* Set a policy allowing the `mycroft` user to install packages using this by creating the file `/etc/polkit-1/localauthority/50-local.d/allow_mycroft_to_install_package.pkla`
and enter the following

```bash
[Allow mycroft to install packages using packagekit]
Identity=unix-user:mycroft`
Action=org.freedesktop.packagekit.package-eula-accept;org.freedesktop.packagekit.package-install ResultAny=yes
```

### Set up pip

`[pip](https://en.wikipedia.org/wiki/Pip_(package_manager))` is a package manager for Python. 

`pip` doesn't interact with `policykit` so a `sudoer` rule is needed to allow `pip install` from the `mycroft` user without a password. 

Edit the `/etc/sudoers.d/011_mycroft-nopasswd` file and add: 

`mycroft ALL=(ALL) NOPASSWD: /usr/local/bin/pip install *`

Then, remove the write flag of the file: 

`chmod -w /etc/sudoers.d/011_mycroft-nopasswd`

### Remove your WiFi nework information

If you added your WiFi network information, we want to remove it before creating an image. 

`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

Remove your network information at the end of the `wpa_supplicant.conf` file then save the file. 

```bash
network={
	ssid="_your network ssid_"
	psk="_your network password_"
}```

### Clear bash history

Next, we clear the `bash` history as a security measure. 

Run these commands at the command prompt: 

* `history -c`
* `history -w`
* `sudo shutdown now`

## Create a disk image

At this point, you can create a disk image of the MicroSD card, and save it to a `.IMG` file. 

There are several tools available to do this, including [Etcher](https://etcher.io/).