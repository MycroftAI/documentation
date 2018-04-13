---
ID: 32434
post_title: Picroft
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/documentation/picroft/
published: true
post_date: 2017-12-02 22:35:25
---
# Picroft

- [Picroft](#picroft)
    + [Prerequisites](#prerequisites)
      - [Hardware prerequisites](#hardware-prerequisites)
        * [Required](#required)
        * [Optional](#optional)
      - [Hardware recommendations](#hardware-recommendations)
        * [Working Microphones](#working-microphones)
        * [Incompatible Microphones](#incompatible-microphones)
        * [Working Speakers](#working-speakers)
    + [Getting Started](#getting-started)
      - [Downloading the disk image](#downloading-the-disk-image)
      - [Burn the disk image to the Micro SD card](#burn-the-disk-image-to-the-micro-sd-card)
      - [Booting up Picroft](#booting-up-picroft)
      - [Getting Picroft connected to the internet using a network cable](#getting-picroft-connected-to-the-internet-using-a-network-cable)
      - [Getting Picroft connected to the internet using Wifi](#getting-picroft-connected-to-the-internet-using-wifi)
    + [Pairing the Picroft](#pairing-the-picroft)
      - [Connecting to Picroft via SSH](#connecting-to-picroft-via-ssh)
      - [How to reimage a Picroft Device](#how-to-reimage-a-picroft-device)
      - [Keeping your Picroft updated](#keeping-your-picroft-updated)
      - [How to switch your Picroft to the `unstable` branch to test new releases](#how-to-switch-your-picroft-to-the-unstable-branch-to-test-new-releases)
      - [Connecting Picroft to a keyboard and/or monitor](#connecting-picroft-to-a-keyboard-andor-monitor)
      - [Important file locations for Picroft](#important-file-locations-for-picroft)
    + [Next steps](#next-steps)
      - [Using the GPIO pins on the Raspberry Pi 3](#using-the-gpio-pins-on-the-raspberry-pi-3)
    + [Common issues on Picroft Devices](#common-issues-on-picroft-devices)
      - [Audio issues](#audio-issues)
        * [Check which audio playback and recording devices are being recognized](#check-which-audio-playback-and-recording-devices-are-being-recognized)

Picroft is an **Enclosure** for Mycroft, designed to the run on Raspberry Pi 3 or newer models. Mycroft provides the software for Picroft, in the form of a disk image, but you will need to burn this to an SD card.

Picroft is based on [Raspbian Jessie Lite](http://downloads.raspberrypi.org/raspbian_lite/images/).

**PICROFT will not work on earlier models of Raspberry Pi, because they do not have enough processing power.**

### Prerequisites

This section of documentation assumes the following:

* That you have the hardware prerequisites for running Picroft
* That you are comfortable connecting devices to WiFi networks
* That you are comfortable issuing basic Linux commands from a **terminal** or **shell prompt**

#### Hardware prerequisites

##### Raspberry Pi compatibility chart

* Pi3 B+ : COMING SOON <-- Not currently supported
* Pi3 : SUPPORTED <-- You should get this device if you want to work on Picroft
* Pi2 : functions but very slow <-- Only use this if you must
* Pi B/A+/Zero/Zero W/Zero WH : NOT SUPPORTED

##### Required

* Raspberry Pi 3 (see compatibility chart above)
* Micro SD card, 8GB or larger _highly_ recommended
* Power adapter with micro USB for your country. [The Raspberry Pi Foundation has some excellent recommendations](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md).
* An analog Speaker that can be plugged into the 3.5mm audio jack on the RPi 3
* USB Microphone



##### Optional

* USB keyboard
* Monitor or TV connected via HDMI cable
* Ethernet cable (if not connecting via WiFi)

At the time of writing, a Picroft hardware kit is **not available** in the Mycroft Shop, but we are considering it. Please [see this Mycroft Forum discussion on which microphones and speakers are best used with Picroft](https://community.mycroft.ai/t/easiest-mic-speaker-option-for-raspberry-pi-3/1246).

#### Hardware recommendations

Below is information on specific hardware that has been tested with Picroft. If you have further recommendations, please raise an Issue or a Pull Request (PR) on this page.

##### Working Microphones

* **Blue Snoball/Snoball Ice** - Works very well
* **CM108 Based Mics** - The CM108 chip drives many low-priced microphones in various form-factors (if you run `lsusb` you'll see them as _C-Media Electronics, Inc. CM108 Audio Controller_.  All work, but some are better than others for Picroft purposes.
   * eBerry Plug and Play Home Studio - decent experience, fair range
   * Kinobo Makio - functional, but only works at close range
* **[Jabra Speak410 USB Speakerphone](http://amzn.to/2kriCvh)** - Microphone and Speaker in the same device. Microphone range is good and speaker sound is loud and crisp.
* **[mVox USB Speakerphone](http://amzn.to/2jYCxR3)** - Microphone and Speaker in the same device. Microphone range is poor and speaker sound is bad compared to the Jabra Speak410.
* **[PS3 Eye Camera](http://amzn.to/2jFC6MP)** - Affordable and microphone range is good.

##### Incompatible Microphones
* _None at this point_

##### Working Speakers

* **Logitech Z50** - Mono speaker, wired, simple, can be found for cheap.

### Getting Started

#### Downloading the disk image

First, download the [Picroft disk image](https://mycroft.ai/to/picroft-image).

We also have a [Picroft disk image](https://mycroft.ai/to/picroft-unstable) available of our `unstable` branch if desired.

#### Burn the disk image to the Micro SD card

Next, the disk image needs to be burnt to the Micro SD card.

The [Raspberry Pi official documentation provides an excellent tutorial](https://www.raspberrypi.org/documentation/installation/installing-images/) on this, using Etcher software. We recommend that you burn the Picroft image to the Micro SD card using Etcher.

![Etcher SD card image burning tool](https://mycroft.ai/wp-content/uploads/2017/12/etcher-screenshot.png "Etcher SD card image burning tool")

If you prefer to use the Linux command line tool `dd` to burn the disk image instead, follow these instructions: 

1. Download the [Picroft disk image](https://mycroft.ai/to/picroft-image)
2. Insert the Micro SD card you wish to burn the image to. It must have a storage capacity of 8GB or higher. 
3. Identify the path where the MicroSD card is mounted by running the command `sudo fdisk -l`. You will be able to tell the path based on the storage size of the device.
4. Keep a note of this - it will be something like `/dev/sdb1`
5. Unmount the disk so that no other operation can write to the device while it is being imaged using the command `sudo umount /dev/sdb1`. Make sure to substitute for the location of your device. 
5. Run the command `sudo dd if=path-to-your-image.img of=/dev/sdb1 bs=20M`. Make sure to substitute the location of your device, and the path to the `.img` file you downloaded.
6. This will take several minutes to run. The command prompt will return if successful, otherwise an error message will be displayed on your terminal.

#### Booting up Picroft

Once you've burned the disk image to the Micro SD card, insert the Micro SD card into the Micro SD card slot on the Raspberry Pi. Plug in your microphone, speakers, and if you're using a monitor and/or keyboard, plug these in too.

Next, plug in the power and switch the power on.

Our next step is to connect Picroft to the internet. 

####  Getting Picroft connected to the internet using a network cable

Plug the Picroft into your router using an ethernet cable plugged into the RJ45 port on the Raspberry Pi.

When Picroft boots, it will look for a network connection and will prompt you to set up a WiFi connection if a wired connection is not found.

#### Getting Picroft connected to the internet using Wifi

Using your computer or a mobile device, connect to the Wifi SSID `MYCROFT` using the password `12345678`. Once you are connected to this SSID, go to the web page [http://start.mycroft.ai](https://start.mycroft.ai). A list of available WiFi networks will be presented. Select the WiFi network that you wish to connect the Picroft to, and enter the WiFi password. Picroft will attempt to connect to the WiFi network.

_NOTE: Picroft cannot connect to WiFi networks that operate in the 5GHz band. You must select a WiFi network that operates in the 2.4GHz band._

If you're concerned about privacy with Picroft's WiFi setup, you can inspect our [Wifi Client code on GitHub](https://github.com/MycroftAI/mycroft-core/tree/dev/mycroft/client/wifisetup).

@TODO I don't know what the limitations are around the WiFi networks that Mycroft can connect to - for instance, can Mycroft connect to WiFi networks that use certain types of authentication like WEP, or enterprise WPA2-PSK with things like Radius that are used in the enterprise? Don't know, flagging as @TODO

### Pairing the Picroft

Once the Picroft is connected to the internet, a **Registration Code** will be Spoken.

[View the home.mycroft.ai documentation to learn how to add your **Device** to home.mycroft.ai](http://mycroft.ai/documentation/home-mycroft-ai-pairing/).

Once paired, you can then use [basic Skills](http://mycroft.ai/documentation/basic-commands/) to get started.

#### Connecting to Picroft via SSH

SSH access to Picroft is enabled by default, so you don't have to enable SSH access.

* Ensure you know the IP address of your Picroft Device on your network. A handy way to do this is to install the IP Address **Skill**, and then Speak:

> Hey Mycroft, what's your IP address?

`"here are my available IP addresses: wlan IP address ... Those are all my available IP addresses"`

* Open up your favorite terminal program, like PuTTy on Windows, or a new terminal on Linux
* `ssh pi@IPADDRESS`
* The default password is `mycroft`, so enter this when prompted.
* If you have successfully logged in via SSH you will see a command prompt like the one below:

```
$ ssh pi@192.168.0.13
pi@192.168.0.13's password:

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Oct 18 13:02:44 2017
pi@mark_1:~ $
```

You are now connected to Picroft via SSH.

#### How to reimage a Picroft Device

To reimage a Picroft **Device**, [download the latest disk image](https://mycroft.ai/to/picroft-image). Burn that to a MicroSD card using Etcher, and insert the burned MicroSD card into the Raspberry Pi, then connect the Raspberry Pi to power.

#### Keeping your Picroft updated

The easiest way to keep your Picroft updated is to burn a new disk image to your Micro SD card, and re-pair your Picroft Device.

#### How to switch your Picroft to the `unstable` branch to test new releases

If you want to help us test the next release of Picroft early, swap your `source` on the Raspberry Pi. 

_NOTE: This is the same as the `dev` branch on GitHub for `mycroft-core`._

Using a text editor, edit your `/etc/apt/sources.list.d/repo.mycroft.ai.list` file: 

By default it points to:

```
deb http://repo.mycroft.ai/repos/apt/debian debian main
```

If you want to try the `unstable` version, edit the file so that it reads: 

```
deb http://repo.mycroft.ai/repos/apt/debian debian-unstable main
```

You will then need to run `sudo apt-get upgrade && sudo apt-get upgrade` for the change to take effect. 

#### Connecting Picroft to a keyboard and/or monitor

If you would like to see the output of Picroft on a monitor (rather than SSH'ing in to Picroft), you can plug a HDMI monitor in to the HDMI slot on the Raspberry Pi. 

If you would like to connect a keyboard or mouse (rather than SSH'ing in to Picroft), connect them via the USB slots on the Raspberry Pi. 

In our experience, we've found most monitors, keyboards and mice are plug-and-play - ie. you shouldn't have to install any additional drivers. 

#### Important file locations for Picroft

If you plan to do **Skills** development work, or other development work with Picroft, you'll find knowing these file locations useful. 

* Skills - have a shortcut in `/home/pi` that points to `opt/mycroft/skills`
* `mycroft-core` - is located at `/usr/local/lib/python2.7/site-packages/mycroft_core`
* Logs - are located at `/var/log`
* `mycroft.conf` - is located at `/home/mycroft/.mycroft/mycroft.conf`
* Identity file (do not share) - is located at `/home/mycroft/.mycroft/identity/identity2.json`

### Next steps

Congratulations! You now have a fully functional Picroft, and can start exploring all the options you now have. Consider using it as a stand-alone voice assistant, or connect it to a monitor and keyboard, and develop straight away. If you don't have a monitor and keybaord, SSH is enabled by default so you can remotely connect to it straight away.

Picroft uses a Raspbian Jessie Lite image under the hood - with Mycroft pre-installed - so everything you can do with Raspbian, you can do with Picroft. You can download other packages, get it running as a server - or more!

For more help or ideas, consider joining our [Picroft channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/picroft) or reading through our [Picroft topic on the Mycroft Forum](https://community.mycroft.ai/c/mycroft-project/Raspberry-Pi).

#### Using the GPIO pins on the Raspberry Pi 3

One common question we get is - "Can I use the [general purpose input output pins (GPIO)](https://www.raspberrypi.org/documentation/usage/gpio/) on the Raspberry Pi 3 with Picroft?".

The answer is 'Yes' - but this requires some additional configuration. 

You need to add the `mycroft` user to the `gpio` group with the command 

`sudo usermod -g gpio mycroft`

You also need to install some additional packages: 

`sudo apt-get install python-rpi.gpio && sudo apt-get install python3-rpi.gpio`

### Common issues on Picroft Devices

#### Audio issues

By far the most common issue on Picroft **Devices** are audio issues - with audio devices not being recognized, audio levels not being high enough and so on. There are a couple of tricks that can help.

##### Check which audio playback and recording devices are being recognized

By default, Picroft uses the PulseAudio subsystem (as opposed to Alsa).

To identify which playback and recording devices are recognized on your Picroft system, use the command:

`pacmd list-sources`

If you are attempting to have one of your audio devices set as the primary device, take note of its number.

To change the device that is used as the default source, using the command:

`pacmd set-default-source 1`

where 1 is the number of the audio device when sources were listed.


If you prefer the Alsa sound subsystem, then you can accomplish the same task using the commands below.

To identify which playback and recording devices are recognized on your Picroft system, use the command:

`alsamixer `

You can also run a similar command line command:

`aplay -L`

which shows playback devices, and

`arecord -L`

which shows recording devices.

To edit your default audio device with Also, you will have to manually edit your

`mycroft.conf`

This file is located at:

`~/.mycroft/mycroft.conf`

Using a program like _vi_ or _nano_, add a line to the end of the file as follows:

```json
 "listener": {  
    "device_index":0  
}
```

Make sure to set the device number to the correct device.