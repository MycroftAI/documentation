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

## Quick links

* [Picroft stable disk image](https://mycroft.ai/to/picroft-image)
* [Picroft unstable disk image](https://mycroft.ai/to/picroft-unstable)
* [`enclosure-picroft` repo on GitHub](https://github.com/MycroftAI/enclosure-picroft)
* [Picroft topic on the Mycroft Community Forum](https://community.mycroft.ai/c/mycroft-project/Raspberry-Pi)
* [Picroft chatroom in Mycroft Chat](https://chat.mycroft.ai/community/channels/picroft)

## About Picroft

Picroft is a ready-made way to run Mycroft on a Raspberry Pi 3 or Raspberry Pi 3B+ and is provided as a disk image that you can burn to a Micro SD card. _Picroft will not work properly on other Raspberry Pi models_.

Picroft is based on [Raspbian Stretch Lite](http://downloads.raspberrypi.org/raspbian_lite/images/).

Picroft is entirely open source, and PRs and Issues are warmly welcomed on the [Picroft GitHub repo](https://github.com/MycroftAI/enclosure-picroft).

As of December 2018, Picroft includes built-in support for the Google AIY voice HAT.

## What do I need to run Picroft?

In order to set up Picroft, you will need to have a basic understanding of the Linux (Raspbian) command line, be comfortable connecting devices to WiFi networks, and have a little patience when setting up audio devices.

### Hardware requirements and compatibility chart

| Model                    | Level of support                            |
|--------------------------|---------------------------------------------|
| Pi3 B+                   | Supported                                   |
| Pi3 B                    | Supported                                   |
| Pi 2                     | Functions very slowly, limited wifi support |
| Pi B                     | Not supported                               |
| Pi A+                    | Not supported                               |
| Pi Zero, Zero W, Zero WH | Not supported                               |

As well as a Raspberry Pi, you will also need:

* Micro SD card, 8GB or larger _highly_ recommended
* Power adapter with micro USB for your country. [The Raspberry Pi Foundation has some excellent recommendations](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md).
* An analog Speaker that can be plugged into the 3.5mm audio jack on the RPi 3 _or_ a USB Speaker  (_Bluetooth on Picroft is difficult to get working and is not recommended_)
* USB Microphone

Installing Picroft may be easier if you also have:

* USB keyboard
* Monitor or TV connected via HDMI cable
* Ethernet cable (if not connecting via WiFi)

While we don't currently offer a Picroft kit with microphone and speaker to purchase [from our Shop](https://mycroft.ai/shop), we've provided links below to components we know to work "out of the box".

_NOTE: We do not gain any profit or benefit from the links below, they are provided only to assist you in acquiring compatible components._

| Type of component       | Model           | Where to buy                                                                                                                                                                                                                                                                                                                                                                                                               | Notes |
|-------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| Microphone              | Blue Snowball   |  United States [Amazon.com](https://www.amazon.com/Blue-Snowball-Microphone-Textured-White/dp/B000EOPQ7E), Australia [JB Hifi](https://www.jbhifi.com.au/blue-mic/blue-snowball-ice-usb-microphone-blackout/770060/), United Kingdom [Amazon.co.uk](https://www.amazon.co.uk/Blue-Microphones-Snowball-Omnidirectional-Microphone/dp/B000EOPQ7E)                                                                              |       |
| Microphone (and camera) | PS3 Eye         | United States [Amazon.com](https://www.amazon.com/Sony-PlayStation-Camera-Bulk-Packaging-Pc/dp/B0072I2240)                                                                                                                                                                                                                                                                                                                    | An excellent introductory model if you are just checking Picroft out.       |
| Microphone and speaker  | Jabra Speak 410 |  United States - [Amazon.com](https://www.amazon.com/Jabra-PHS001U-Speakerphone-Retail-Packaging/dp/B007SHJIO2/ref=sr_1_3?ie=UTF8&qid=1545394940&sr=8-3&keywords=jabra+speak+410), Australia - [ITSPOT.com.au](https://www.itspot.com.au/jabra-speak-410-uc-speakerphone-p466658.html?ref=ShopBot), United Kingdom - [Amazon.co.uk](https://www.amazon.co.uk/Jabra-Conference-Speakerphone-optimised-Microsoft/dp/B004ELA7TA)   |  Premium microphone and speaker combination.     |
| Speaker                 | Logitech Z50    |  United States [Amazon.com](https://www.amazon.com/Z50-smartphone-tablet-laptop-Grey-x/dp/B00EZ9XLF8), Australia - [Good Guys](https://www.thegoodguys.com.au/logitech-computer-speaker-z50-blue-2453262 ),  United Kingdom [Amazon.co.uk](https://www.amazon.co.uk/Logitech-Z50-Speaker-Ocean-Blue/dp/B00FSF2ODS )                                                                                                           |       |

## Getting started with Picroft

### Downloading the disk image

First, download the [Picroft disk image](https://mycroft.ai/to/picroft-image).

We also have a [Picroft disk image](https://mycroft.ai/to/picroft-unstable) available of our `unstable` branch if desired.

### Burn the disk image to the Micro SD card

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

### Seeing the output from Picroft

There are two ways to see the output from a Picroft **Device**:

1. Plug Picroft into a HDMI monitor or television, and attach a USB keyboard.  If you are planning to connect Picroft to a WiFi network, you will first need to connect to a HDMI monitor or television so that you can manually configure Picroft's WiFi settings.
2. `ssh` into Picroft once Picroft is connected to a wired or wireless network

## Connecting Picroft to a wired or WiFi network

### To connect to a wired network

Simply plug the ethernet cable into the RJ45 (ethernet) socket on the RPi. Picroft will then attempt to connect to the network, and request a DHCP address.

_You will need to connect to your router, or use other networking diagnostics, to identify what IP address your Picroft has been allocated on the network._

### To connect to a WiFi network

By default, Picroft is **not** configured for WiFi. Picroft can connect to most 2.4GHz WiFi networks, but this has to be manually configured.

First, you need to be able to edit files on the filesystem of the Picroft. There are two ways to do this.

1. Plug the Picroft into a keyboard and HDMI monitor then type `Ctrl + C` to get to the command line _or_
2. _if you are already connected using a wired connection **and** you know the Picroft's IP address_, [SSH in to the Picroft device ](https://mycroft.ai/documentation/picroft/#connecting-to-picroft-via-ssh)

#### Editing the `wpa_supplicant.conf` file

Next, we edit the `wpa_supplicant.conf` file. This file controls WiFi connections for the Raspberry Pi.

1. Type `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
2. Using the down arrow key, navigate to the bottom of the file, and add credentials for your SSID

```
    network={
            ssid="MyNetworkSSID"
            psk="mypassword"
    }
```

3. Type `Ctrl + X` to exit and `Y` then `Enter` to save your changes.
4. Type `sudo reboot now`

_You will need to connect to your router, or use other networking diagnostics, to identify what IP address your Picroft has been allocated on the network._

##### Manually configuring WPA2 Enterprise WiFi with MSCHAPV2 authentication

If you are on an enterprise network, your network security might use WPA2 with MSCHAPV2 authentication. Configuring Picroft to use MSCHAPV2 is similar to the above, but requires some additional steps.

First, we need to generate a hash of your SSID's password.

```
echo -n your_password| iconv -t utf16le | openssl md4
```

This will use the [NTLM hash](https://en.wikipedia.org/wiki/NT_LAN_Manager) which is a 16 bit MD4 hash.  Make sure to copy this as we will need it for later steps.

Next, run the following commands:

```
cd /etc/wpa_supplicant
sudo nano wpa_supplicant.conf
```

Add the following to the bottom of the `wpa_supplicant.conf` file, replacing `ssid` with your SSID name, `identity` with your username and `password` with the hash generated earlier. Type `Ctrl + O` to save, then `Ctrl + x` to exit.

```
network={
    ssid="ssid network name"
	priority=1
	proto=RSN
	key_mgmt=WPA-EAP
	pairwise=CCMP
	auth_alg=OPEN
	eap=PEAP
	identity="user_name"
	password=hash:hash_key_here
	phase1="peaplabel=0"
	phase2="auth=MSCHAPV2"
}
```

Next, reboot the Picroft using `sudo reboot now`. If these steps have worked, you will be connected to your enterprise WiFi shortly after rebooting.

_You will need to connect to your router, or use other networking diagnostics, to identify what IP address your Picroft has been allocated on the network._

#### Known errors with Picroft and WiFi

_NOTE: Picroft cannot connect to WiFi networks that operate in the 5GHz band. You must select a WiFi network that operates in the 2.4GHz band._

_NOTE: Picroft cannot connect to WiFi networks that operate on Channels 12 or 13 (2467MHz and 2472MHz frequencies). Please configure your SSID to use a different channel or frequency. These channels are often used in Germany and other European countries._

### Booting up Picroft

Once you've burned the disk image to the Micro SD card, insert the Micro SD card into the Micro SD card slot on the Raspberry Pi. Plug in your microphone, speakers, and if you're using a monitor and/or keyboard, plug these in too.

Next, plug in the power and connect the Micro USB cable to the RPi. This "power on" the device.

If you have a HDMI monitor connected,  you should start to see some output on screen.

If you're going to `ssh` into Picroft, do the following:

## `ssh` into Picroft

SSH access to Picroft is enabled by default, so you don't have to enable SSH access.

* Ensure you know the IP address of your Picroft Device on your network. If your Picroft is already _paired_, then a handy way to do this is to install the IP Address **Skill**, and then Speak:

> Hey Mycroft, what's your IP address?

`"here are my available IP addresses: wlan IP address ... Those are all my available IP addresses"`

If not, you will need to know what IP address your Picroft has. You may need to log in to your router to find out the IP address of your Picroft.

* Open up your favorite terminal program, like PuTTy on Windows, or a new terminal on Linux
* `ssh pi@IPADDRESS`
* The default password is `mycroft`, so enter this when prompted.
* If you have successfully logged in via SSH you will see a command prompt like the one below:

```
$ ssh pi@192.168.0.13                 <-- in this case, the IP address was 192.168.0.13, your IP address may vary
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

### Setting up Picroft

On first boot, you will see a screen which looks similar to the one below:

![Picroft initial boot screen](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-20-23-13-36.png "Picroft initial boot screen")

Picroft will then ask you whether you would like to do the guided setup, or drop straight to a command line. If you are new to Picroft, we recommend that you complete the guided setup.

#### Selecting audio output and audio input

_NOTE: Audio output and audio input is the single most problematic part of Picroft setup; we've tried to provide lots of guidance here to get you up and running, but you may need to experiment to find a solution for your chosen audio output and input devices._

The guided setup will then ask you to select your audio output device, as shown below:

![Picroft select audio output](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-20-23-17-42.png "Picroft select audio output")

Enter the number `1`, `2`,  `3` or `4` corresponding to:

```
1) Speakers via 3.5mm output (aka 'audio jack' or 'headphone jack')
2) HDMI audio (e.g. a TV or monitor with built-in speakers)
3) USB audio (e.g. a USB soundcard or USB mic/speaker combo)
4) Google AIY Voice HAT and microphone board (Voice Kit v1)
```

Next, test and adjust the volume. You may need to reboot your Picroft in order for the audio output device to be correctly selected.

The final step of the guided setup is microphone configuration. You will be asked to select your audio input device, as shown below:

![Picroft select audio input](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-20-23-18-27.png "Picroft select audio input")

Enter the number `1`, `2`,  `3` or `4` corresponding to:

```
1) PlayStation Eye (USB)
2) Blue Snoball ICE (USB)
3) Google AIY Voice HAT and microphone board (Voice Kit v1)
4) Matrix Voice HAT.
5) Other (unsupported -- good luck!)
```

The guided setup will then do a microphone test to ensure your chosen microphone is working OK.

#### What can I do if the guided setup doesn't set my audio input or output device correctly?

There are a few tricks that we know of to get your audio input or output device working correctly - however, these are somewhat technical and will require typing commands on the Linux command line interface (CLI).

##### Alsamixer

`alsamixer` is a utility provided by the ALSA sound system on Raspbian Stretch that allows you to select an audio playback (output) and input (capture) device.

To run `alsamixer`, type `Ctrl +C` to exit the guided setup and you will be at the Linux command line. Type `alsamixer` as shown below:

```bash
(.venv) pi@picroft:~ $ alsamixer
```

You will see a screen similar to the one below, and may have different options depending on which audio devices you have connected.

![Picroft alsamixer initial screen](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-27-23-05-12.png "Picroft alsamixer initial screen")

Different devices will have a different command key for choosing 'Capture' devices, in this case it is `F4`.

If you do not see any capture devices, as shown below, then you may need to select a different sound card.

![Picroft alsamixer no audio capture device](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-27-23-05-25.png "Picroft alsamixer no audio capture device")

To select a different sound card, follow the instructions on your version of `alsamixer`. In this case, the command key for choosing 'Select sound card' is `F6`.  Use the arrow keys on your keyboard to navigate up and down the list to choose your preferred soundcard.

![Picroft alsamixer select sound card](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-27-23-05-52.png "Picroft alsamixer select sound card")

`alsamixer` usually has an option to see **all** capture and playback devices. In this case, the command key to see all devices is `F5`.

![Picroft alsamixer show all audio capture and playback devices](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-27-23-06-09.png "Picroft alsamixer show all audio capture and playback devices")

##### pulseaudio

If `alsamixer` does not work for you, then you may have some success with `pulseaudio`. We've recently updated the Picroft repo to include `pulseaudio`, but if you haven't updated for a little while then you may need to manually install it.

```bash
(.venv) pi@picroft:~ $ sudo apt-get install pulseaudio
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  fontconfig-config fonts-dejavu-core libasound2-plugins libavcodec57
  libavresample3 libavutil55 libcairo2 libdrm-amdgpu1 libdrm-freedreno1
  libdrm-nouveau2 libdrm-radeon1 libfontconfig1 libgl1-mesa-dri
  libgl1-mesa-glx libglapi-mesa libgsm1 libllvm3.9 libmp3lame0 libopenjp2-7
  libopus0 liborc-0.4-0 libpixman-1-0 libpulsedsp libsensors4 libshine3
  libsnappy1v5 libsoxr0 libspeex1 libspeexdsp1 libswresample2 libtdb1
  libtheora0 libtwolame0 libtxc-dxtn-s2tc libva-drm1 libva-x11-1 libva1
  libvdpau-va-gl1 libvdpau1 libvpx4 libwavpack1 libwebp6 libwebpmux2
  libwebrtc-audio-processing1 libx264-148 libx265-95 libxcb-dri2-0
  libxcb-dri3-0 libxcb-glx0 libxcb-present0 libxcb-render0 libxcb-shm0
  libxcb-sync1 libxdamage1 libxfixes3 libxrender1 libxshmfence1 libxvidcore4
  libxxf86vm1 libzvbi-common libzvbi0 mesa-va-drivers mesa-vdpau-drivers
  pulseaudio-utils rtkit va-driver-all vdpau-driver-all
Suggested packages:
  opus-tools lm-sensors speex pavumeter pavucontrol paman paprefs
The following NEW packages will be installed:
  fontconfig-config fonts-dejavu-core libasound2-plugins libavcodec57
  libavresample3 libavutil55 libcairo2 libdrm-amdgpu1 libdrm-freedreno1
  libdrm-nouveau2 libdrm-radeon1 libfontconfig1 libgl1-mesa-dri
  libgl1-mesa-glx libglapi-mesa libgsm1 libllvm3.9 libmp3lame0 libopenjp2-7
  libopus0 liborc-0.4-0 libpixman-1-0 libpulsedsp libsensors4 libshine3
  libsnappy1v5 libsoxr0 libspeex1 libspeexdsp1 libswresample2 libtdb1
  libtheora0 libtwolame0 libtxc-dxtn-s2tc libva-drm1 libva-x11-1 libva1
  libvdpau-va-gl1 libvdpau1 libvpx4 libwavpack1 libwebp6 libwebpmux2
  libwebrtc-audio-processing1 libx264-148 libx265-95 libxcb-dri2-0
  libxcb-dri3-0 libxcb-glx0 libxcb-present0 libxcb-render0 libxcb-shm0
  libxcb-sync1 libxdamage1 libxfixes3 libxrender1 libxshmfence1 libxvidcore4
  libxxf86vm1 libzvbi-common libzvbi0 mesa-va-drivers mesa-vdpau-drivers
  pulseaudio pulseaudio-utils rtkit va-driver-all vdpau-driver-all
0 upgraded, 68 newly installed, 0 to remove and 0 not upgraded.
Need to get 30.2 MB of archives.
After this operation, 221 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
```

## Pairing the Picroft

Once the Picroft is connected to the internet, and you have run through the guided setup, Picroft will reboot. Picroft will boot into the `mycroft-cli-client` screen, and a **Registration Code** will be spoken, and will also be shown on the `mycroft-cli-client` screen, as shown below:

![Picroft pairing](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-20-23-53-32.png "Picroft pairing")

[View the home.mycroft.ai documentation to learn how to add your **Device** to home.mycroft.ai](http://mycroft.ai/documentation/home-mycroft-ai-pairing/).

Once paired, you can then use [basic Skills](http://mycroft.ai/documentation/basic-commands/) to get started. For example, you can ask questions like 'Tell me about Abraham Lincoln' - shown below:

![Picroft basic commands](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-21-04-21-07.png "Picroft basic commands")

## Maintaining your Picroft

### How to reimage a Picroft Device

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

You will then need to run `sudo apt-get update && sudo apt-get upgrade` for the change to take effect.

#### Connecting Picroft to a keyboard and monitor

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

Picroft uses a Raspbian Stretch Lite image under the hood - with Mycroft pre-installed - so everything you can do with Raspbian, you can do with Picroft. You can download other packages, get it running as a server - or more!

For more help or ideas, consider joining our [Picroft channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/picroft) or reading through our [Picroft topic on the Mycroft Forum](https://community.mycroft.ai/c/mycroft-project/Raspberry-Pi).

#### Using the GPIO pins on the Raspberry Pi 3

One common question we get is - "Can I use the [general purpose input output pins (GPIO)](https://www.raspberrypi.org/documentation/usage/gpio/) on the Raspberry Pi 3 with Picroft?".

The answer is 'Yes' - but this requires some additional configuration.

You need to add the `mycroft` user to the `gpio` group with the command

`sudo usermod -g gpio mycroft`

You also need to install some additional packages:

`sudo apt-get install python-rpi.gpio && sudo apt-get install python3-rpi.gpio`

This [example GPIO Skill](https://github.com/MycroftAI/picroft_example_skill_gpio) provides some good examples of how to use GPIO input and output in your Mycroft Skill.

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






=========================================================================

That's all, setup is complete!  Now we'll pull down the latest software
updates and start Mycroft.  You'll be prompted to pair this device with
an account at https://home.mycroft.ai, then you'll be set to enjoy your
Picroft!

To rerun this setup, type 'mycroft-setup-wizard' and reboot.

Press any key to launch Mycroft...


Mycroft is your open source voice assistant.  Full source
can be found at: /home/pi/mycroft-core

Mycroft-specific commands you can use from the Linux command prompt:
  mycroft-cli-client       command line client, useful for debugging
  mycroft-msm              Mycroft Skills Manager, to manage your Skills
  mycroft-msk              Mycroft Skills Kit, create and share Skills

Scripting Utilities:
  mycroft-speak <phr>      have Mycroft speak a phrase to the user
  mycroft-say-to <utt>     send an utterance to Mycroft as if spoken by a user

Mycroft's Python Virtual Environment (venv) control:
  mycroft-venv-activate    enter the venv
  mycroft-venv-deactivate  exit the venv
  mycroft-pip              install a Python package within the venv

Other:
  mycroft-mic-test         record and playback to directly test microphone
  mycroft-help             display this message

For more information, see https://mycroft.ai and https://github.com/MycroftAI

***********************************************************************
