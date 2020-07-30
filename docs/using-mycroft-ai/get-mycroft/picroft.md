---
description: >-
  Picroft is a ready-made way to run Mycroft on a Raspberry Pi 3, 3B+ or 4 and
  is provided as a disk image that you can burn to a Micro SD card.
---

# Picroft

## Quick links

* [Picroft stable disk image](https://mycroft.ai/to/picroft-image)
* [Picroft unstable disk image](https://mycroft.ai/to/picroft-unstable)
* [`enclosure-picroft` repo on GitHub](https://github.com/MycroftAI/enclosure-picroft)
* [Picroft topic on the Mycroft Community Forum](https://community.mycroft.ai/c/mycroft-project/Raspberry-Pi)
* [Picroft chatroom in Mycroft Chat](https://chat.mycroft.ai/community/channels/picroft)

## About Picroft

Picroft is based on [Raspbian Buster Lite](http://downloads.raspberrypi.org/raspbian_lite/images/).

Picroft is entirely open source, and PRs and Issues are warmly welcomed on the [Picroft GitHub repo](https://github.com/MycroftAI/enclosure-picroft).

## What do I need to run Picroft?

In order to set up Picroft, you will need to have a basic understanding of the Linux \(Raspbian\) command line, be comfortable connecting devices to WiFi networks, and have a little patience when setting up audio devices.

### Hardware requirements and compatibility chart

| Model | Level of support |
| :--- | :--- |
| Pi4 | Supported |
| Pi3 B+ | Supported |
| Pi3 B | Supported |
| Pi 2 | Functions very slowly, limited wifi support |
| Pi B | Not supported |
| Pi A+ | Not supported |
| Pi Zero, Zero W, Zero WH | Not supported |

As well as a Raspberry Pi, you will also need:

* Micro SD card, 8GB or larger _highly_ recommended
* Power adapter with micro USB for your country. [The Raspberry Pi Foundation has some excellent recommendations](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md).
* An analog Speaker that can be plugged into the 3.5mm audio jack on the RPi _or_ a USB Speaker  \(_Bluetooth on Picroft is difficult to get working and is not recommended_\)
* USB Microphone

Installing Picroft may be easier if you also have:

* USB keyboard
* Monitor or TV connected via HDMI cable
* Ethernet cable \(if not connecting via WiFi\)

### Tested hardware

The following is a Community maintained list of hardware that has been used with Picroft. Whilst every effort is made to keep this list updated, upstream software changes may cause future problems with device compatibility. Mycroft can not guarantee that any specific hardware will work with Picroft.

If you are looking for a low-cost option to try out Picroft, we can recommend the PlayStation Eye \(often called a PS3 Eye\).

| Brand | Model | Status | Type | Notes |
| :--- | :--- | :--- | :--- | :--- |
| AmazonBasics | 	LJ-USM-001 | Working | USB Conference Microphone |
| Andrea Electronics | C1-1028100-3 | Working | USB Dongle (Mic array & Speaker 3.5mm) | Superbeam Array Microphone Bundle SUMA (`08a8:0016`) |
| Blue | Snowball iCE | Working | Microphone |  |
| Creative | VF0790 | Working | Mic and camera |  |
| Google | AIY v1 | Working | Mic and speaker |  |
| Jabra | Speak 410 | [Problems reported](https://community.mycroft.ai/t/no-audio-output-on-picroft-with-jabra-410/3415) | Mic and speaker | Premium microphone and speaker combination |
| Logitech | C270 | Working | Mic and camera |  |
| Logitech | C525 | Working | Mic and camera |  |
| Logitech | Webcam Pro 9000 | Working | Mic and camera |  |
| Logitech | Z50 | Working | Speaker |  |
| Matrix | Voice | Working | Mic array |  |
| PlayStation | Eye \(PS3 Eye\) | Working | Mic and camera | An excellent introductory model if you are just checking Picroft out. |
| Seeed Studio | Mic Array 2.0 | Working | Mic array | Premium microphone array |

If you experience any audio problems, please see the [Audio Troubleshooting Guide](../troubleshooting/audio-troubleshooting.md).

{% page-ref page="../troubleshooting/audio-troubleshooting.md" %}

### Bluetooth devices

Bluetooth audio devices are notoriously difficult and are not supported by default. At the time of writing, [this thread on the Community Forums](https://community.mycroft.ai/t/bluetooth-hsp-hfp/8199) is a good starting point. 

If you have had success using Bluetooth devices with Picroft please contribute your experience and help us update this documentation for a more positive wireless future.

## Getting started with Picroft

### Downloading the disk image

First, download the [Picroft disk image](https://mycroft.ai/to/picroft-image).

We also have a [Picroft disk image](https://mycroft.ai/to/picroft-unstable) available of our `unstable` branch if desired.

### Burn the disk image to the Micro SD card

Next, the disk image needs to be burnt to the Micro SD card.

The [Raspberry Pi official documentation provides an excellent tutorial](https://www.raspberrypi.org/documentation/installation/installing-images/) on this, using Etcher software. We recommend that you burn the Picroft image to the Micro SD card using Etcher.

![Etcher SD card image burning tool](https://mycroft.ai/wp-content/uploads/2017/12/etcher-screenshot.png)

If you prefer to use the Linux command line tool `dd` to burn the disk image instead, follow these instructions:

1. Download the [Picroft disk image](https://mycroft.ai/to/picroft-image)
2. Insert the Micro SD card you wish to burn the image to. It must have a storage capacity of 8GB or higher.
3. Identify the path where the MicroSD card is mounted by running the command `sudo fdisk -l`. You will be able to tell the path based on the storage size of the device.
4. Keep a note of this - it will be something like `/dev/sdb1`
5. Unmount the disk so that no other operation can write to the device while it is being imaged using the command `sudo umount /dev/sdb1`. Make sure to substitute for the location of your device.
6. Run the command `sudo dd if=path-to-your-image.img of=/dev/sdb1 bs=20M`. Make sure to substitute the location of your device, and the path to the `.img` file you downloaded.
7. This will take several minutes to run. The command prompt will return if successful, otherwise an error message will be displayed on your terminal.

### Seeing the output from Picroft

There are two ways to see the output from a Picroft **Device**:

1. Plug Picroft into a HDMI monitor or television, and attach a USB keyboard.  If you are planning to connect Picroft to a WiFi network, you will first need to connect to a HDMI monitor or television so that you can manually configure Picroft's WiFi settings.
2. `ssh` into Picroft once Picroft is connected to a wired or wireless network

#### Connecting Picroft to a keyboard and monitor

If you would like to see the output of Picroft on a monitor \(rather than SSH'ing in to Picroft\), you can plug a HDMI monitor in to the HDMI slot on the Raspberry Pi.

If you would like to connect a keyboard or mouse \(rather than SSH'ing in to Picroft\), connect them via the USB slots on the Raspberry Pi.

In our experience, we've found most monitors, keyboards and mice are plug-and-play - ie. you shouldn't have to install any additional drivers.

### Booting up Picroft

Once you've burned the disk image to the Micro SD card, insert the Micro SD card into the Micro SD card slot on the Raspberry Pi. Plug in your microphone, speakers, and if you're using a monitor and/or keyboard, plug these in too.

Next, plug in the power and connect the Micro USB cable to the RPi. This "power on" the device.

If you have a HDMI monitor connected, you should start to see some output on screen.

If you're going to `ssh` into Picroft, do the following:

### `ssh` into Picroft

SSH access to Picroft is enabled by default, so you don't have to enable SSH access.

* Ensure you know the IP address of your Picroft Device on your network. If your Picroft is already _paired_, then a handy way to do this is to install the IP Address **Skill**, and then Speak:

> Hey Mycroft, what's your IP address?

`"here are my available IP addresses: wlan IP address ... Those are all my available IP addresses"`

If not, you will need to know what IP address your Picroft has. You may need to log in to your router to find out the IP address of your Picroft.

* Open up your favorite terminal program, like PuTTy on Windows, or a new terminal on Linux
* `ssh pi@IPADDRESS`
* The default password is `mycroft`, so enter this when prompted.
* If you have successfully logged in via SSH you will see a command prompt like the one below:

```text
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

## Setting up Picroft

On first boot, you will see a screen which looks similar to the one below:

![Picroft initial boot screen](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-20-23-13-36.png)

Picroft will then ask you whether you would like to do the guided setup, or drop straight to a command line. If you are new to Picroft, we recommend that you complete the guided setup.

#### Selecting audio output and audio input

_NOTE: Audio output and audio input is the single most problematic part of Picroft setup; we've tried to provide lots of guidance here to get you up and running, but you may need to experiment to find a solution for your chosen audio output and input devices._

The guided setup will then ask you to select your audio output device, as shown below:

![Picroft select audio output](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-20-23-17-42.png)

Enter the number `1`, `2`, `3` or `4` corresponding to:

```text
1) Speakers via 3.5mm output (aka 'audio jack' or 'headphone jack')
2) HDMI audio (e.g. a TV or monitor with built-in speakers)
3) USB audio (e.g. a USB soundcard or USB mic/speaker combo)
4) Google AIY Voice HAT and microphone board (Voice Kit v1)
```

Next, test and adjust the volume. You may need to reboot your Picroft in order for the audio output device to be correctly selected.

The final step of the guided setup is microphone configuration. You will be asked to select your audio input device, as shown below:

![Picroft select audio input](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-20-23-18-27.png)

Enter the number `1`, `2`, `3` or `4` corresponding to:

```text
1) PlayStation Eye (USB)
2) Blue Snoball ICE (USB)
3) Google AIY Voice HAT and microphone board (Voice Kit v1)
4) Matrix Voice HAT.
5) Other (unsupported -- good luck!)
```

The guided setup will then do a microphone test to ensure your chosen microphone is working OK.

#### What can I do if the guided setup doesn't set my audio input or output device correctly?

If you experience any audio problems, please see the [Audio Troubleshooting Guide](../troubleshooting/audio-troubleshooting.md).

{% page-ref page="../troubleshooting/audio-troubleshooting.md" %}

### Pairing the Picroft

Once the Picroft is connected to the internet, and you have run through the guided setup, Picroft will reboot. Picroft will boot into the `mycroft-cli-client` screen, and a **Registration Code** will be spoken, and will also be shown on the `mycroft-cli-client` screen, as shown below:

![Picroft pairing](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-20-23-53-32.png)

[View the home.mycroft.ai documentation to learn how to add your **Device** to home.mycroft.ai](http://mycroft.ai/documentation/home-mycroft-ai-pairing/).

Once paired, you can then use [basic Skills](http://mycroft.ai/documentation/basic-commands/) to get started. For example, you can ask questions like 'Tell me about Abraham Lincoln' - shown below:

![Picroft basic commands](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-21-04-21-07.png)

### Connecting Picroft to a wired or WiFi network

#### To connect to a wired network

Simply plug the ethernet cable into the RJ45 \(ethernet\) socket on the RPi. Picroft will then attempt to connect to the network, and request a DHCP address.

_You will need to connect to your router, or use other networking diagnostics, to identify what IP address your Picroft has been allocated on the network._

#### To connect to a WiFi network

By default, Picroft is **not** configured for WiFi. Picroft can connect to most 2.4GHz WiFi networks, but this has to be manually configured.

First, you need to be able to edit files on the filesystem of the Picroft. There are two ways to do this.

1. Plug the Picroft into a keyboard and HDMI monitor then type `Ctrl + C` to get to the command line _or_
2. _if you are already connected using a wired connection **and** you know the Picroft's IP address_, [SSH in to the Picroft device ](https://mycroft.ai/documentation/picroft/#connecting-to-picroft-via-ssh)

#### Editing the `wpa_supplicant.conf` file

Next, we edit the `wpa_supplicant.conf` file. This file controls WiFi connections for the Raspberry Pi.

1. Type `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
2. Using the down arrow key, navigate to the bottom of the file, and add credentials for your SSID. You may also need to add the relevant [two-character country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements).

```text
    country=US
    network={
            ssid="MyNetworkSSID"
            psk="mypassword"
    }
```

1. Type `Ctrl + X` to exit and `Y` then `Enter` to save your changes.
2. Type `sudo reboot now`

_You will need to connect to your router, or use other networking diagnostics, to identify what IP address your Picroft has been allocated on the network._

**Manually configuring WPA2 Enterprise WiFi with MSCHAPV2 authentication**

If you are on an enterprise network, your network security might use WPA2 with MSCHAPV2 authentication. Configuring Picroft to use MSCHAPV2 is similar to the above, but requires some additional steps.

First, we need to generate a hash of your SSID's password.

```text
echo -n your_password| iconv -t utf16le | openssl md4
```

This will use the [NTLM hash](https://en.wikipedia.org/wiki/NT_LAN_Manager) which is a 16 bit MD4 hash. Make sure to copy this as we will need it for later steps.

Next, run the following commands:

```text
cd /etc/wpa_supplicant
sudo nano wpa_supplicant.conf
```

Add the following to the bottom of the `wpa_supplicant.conf` file, replacing `ssid` with your SSID name, `identity` with your username and `password` with the hash generated earlier. Type `Ctrl + O` to save, then `Ctrl + x` to exit.

```text
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

_NOTE: Picroft cannot connect to WiFi networks that operate on Channels 12 or 13 \(2467MHz and 2472MHz frequencies\). Please configure your SSID to use a different channel or frequency. These channels are often used in Germany and other European countries._

## Next steps

Congratulations! You now have a fully functional Picroft, and can start exploring all the options you now have. Consider using it as a stand-alone voice assistant, or connect it to a monitor and keyboard, and develop straight away. If you don't have a monitor and keybaord, SSH is enabled by default so you can remotely connect to it straight away.

Picroft uses a Raspbian Stretch Lite image under the hood - with Mycroft pre-installed - so everything you can do with Raspbian, you can do with Picroft. You can download other packages, get it running as a server - or more!

For more help or ideas, consider joining our [Picroft channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/picroft) or reading through our [Picroft topic on the Mycroft Forum](https://community.mycroft.ai/c/mycroft-project/Raspberry-Pi).

### Useful commands for Picroft

There are several commands that are packaged into Picroft to help you with advanced functionality:

* `mycroft-cli-client`: This command will start the Mycroft CLI client if you are on the Linux command line
* `mycroft-help`: This command brings up help information
* `mycroft-mic-test`: This command re-runs the microphone test from the guided setup
* `mycroft-msk`: This command runs the [Mycroft Skills Kit](../../mycroft-technologies/mycroft-skills-kit.md)
* `mycroft-msm`: This command runs the [Mycroft Skills Manager](../../mycroft-technologies/mycroft-core/msm.md)
* `mycroft-pip`: This command runs `pip` within the Mycroft Python `virtual environment` \(`venv`\). This is useful if you are installing dependencies for **Skills**.
* `mycroft-say-to`:  This command sends a command to Picroft, just like you had 'spoken' a command. This is useful if your microphone is not working.
* `mycroft-setup-wizard`: This command re-runs the guided setup
* `mycroft-skill-testrunner`: This command runs the `testrunner` - used to run unit tests for a **Skill**. This is useful if you are doing **Skills** development with Mycroft
* `mycroft-speak`: This command gets Mycroft to 'speak' using Text to Speech.
* `mycroft-venv-deactivate`: This command deactivates the Mycroft Python `virtual environment` and is useful if you want to install other software on the Picroft device.
* `mycroft-wipe`: This command wipes Picroft back to factory default status. This will unpair the device and remove any configuration changes you have made.

### Important file locations for Picroft

If you plan to do **Skills** development work, or other development work with Picroft, you'll find knowing these file locations useful.

* Skills - have a shortcut in `/home/pi` that points to `/opt/mycroft/skills`
* `mycroft-core` - is located at `/home/pi/mycroft-core`
* Logs - are located at `/var/log/mycroft/`
* `mycroft.conf` - is located at `/home/mycroft/.mycroft/mycroft.conf`
* Identity file \(do not share\) - is located at `/home/mycroft/.mycroft/identity/identity2.json`

### Maintaining your Picroft

#### How to reimage a Picroft Device

To reimage a Picroft **Device**, [download the latest disk image](https://mycroft.ai/to/picroft-image). Burn that to a MicroSD card using Etcher, and insert the burned MicroSD card into the Raspberry Pi, then connect the Raspberry Pi to power.

#### Keeping your Picroft updated

To keep `mycroft-core` and the Skills on your Picroft updated, first `ssh` in to Picroft, then run the `update.sh` script:

```bash
(.venv) pi@picroft:~ $ bash update.sh
```

This script will update both `mycroft-core` and the **Skills** on your Picroft device.

#### Building your own Picroft image

The Picroft image building instructions can now be found on GitHub at; [https://github.com/MycroftAI/enclosure-picroft/blob/stretch/image\_recipe.md](https://github.com/MycroftAI/enclosure-picroft/blob/stretch/image_recipe.md)

### Using the GPIO pins on the Raspberry Pi

One common question we get is - "Can I use the [general purpose input output pins \(GPIO\)](https://www.raspberrypi.org/documentation/usage/gpio/) on the Raspberry Pi with Picroft?".

The answer is 'Yes' - but this requires some additional configuration.

You need to add the `pi` user to the `gpio` group with the command

`sudo usermod -g gpio pi`

You also need to install some additional packages:

`sudo apt-get install python-rpi.gpio && sudo apt-get install python3-rpi.gpio`

This [example GPIO Skill](https://github.com/MycroftAI/picroft_example_skill_gpio) provides some good examples of how to use GPIO input and output in your Mycroft Skill.

