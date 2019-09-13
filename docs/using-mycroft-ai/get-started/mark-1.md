---
description: >-
  The Mark 1 device is an Enclosure for Mycroft, based on Raspberry Pi. It is
  designed as a reference hardware device, and is able to be easily modified,
  hacked and extended.
---

# Mark 1

## Prerequisites

This section of documentation assumes the following:

* That you have a Mycroft Mark 1 hardware **Device**
* That you are comfortable connecting devices to WiFi networks
* That you are comfortable issuing basic Linux commands

## Getting Started

When you received your Mark 1, you would have received a [blue-colored Getting Started guide \(PDF, 290Kb\)](https://mycroft.ai/wp-content/uploads/2017/06/Mark_1_User_Guide.pdf).

Connect the Mark 1 power supply to a power outlet, and to the Mark 1 device. _NOTE: If you are in a country other than the USA, you will need a power adapter to convert from the US power supply the Mark 1 ships with. Alternatively, use a 12V, 1A power supply for your country's power outlets._

The Mark 1 will boot up. It will then Speak:

`"I need to be connected to the internet. Plug in a network cable, or connect to the SSID Mycroft with the password 12345678 and go to http://start.mycroft.ai"`

### Getting Mark 1 connected to the internet using a network cable

Plug the Mark 1 into your router using an ethernet cable. The network should be automatically detected.

### Getting Mark 1 connected to the internet using Wifi

Using your computer or a mobile device, connect to the Wifi SSID `MYCROFT` using the password "12345678". Once you are connected to this SSID, go to the web page [http://start.mycroft.ai](https://start.mycroft.ai). A list of available WiFi networks will be presented. Select the WiFi network that you wish to connect the Mark 1 to, and enter the WiFi password. Mark 1 will attempt to connect to the WiFi network.

_NOTE: Mark 1 cannot connect to WiFi networks that operate in the 5GHz band. You must select a WiFi network that operates in the 2.4GHz band._

_NOTE: Mark 1 cannot connect to WiFi networks that operate on Channels 12 or 13 \(2467MHz and 2472MHz frequencies\). Please configure your SSID to use a different channel or frequency._

## Pairing the Mark 1

Once the Mark 1 is connected to the internet, a **Registration Code** will be Spoken, and displayed on the Mark 1's LED panel.

[View the home.mycroft.ai documentation to learn how to add your **Device** to home.mycroft.ai](http://mycroft.ai/documentation/home-mycroft-ai-pairing/).

Once paired, you can then use [basic Skills](http://mycroft.ai/documentation/basic-commands/).

## Mark 1 menu options

You can access the Mark 1 menu by pressing the top button for two seconds. Turn the top button anti-clockwise to scroll through menu options, then press the button to select that option.

The available menu options are:

* ILLUM: This option allows you to control the brightness of Mark 1's Eyes, on a scale of 0 \(eyes off\) to 30 \(maximum brightness\). The _Auto_ setting will set the brightness to 30, which is the maximum setting.
* WIFI: This option allows you to connect or re-connect Mark 1 to your WiFi. This option is useful if your router changes, or your WiFi password changes, or you're moving your Mark 1 to a new location.
* REBOOT: This option will reboot your Mark 1. _NOTE: The reboot is immediate_. This option is useful if you're experiencing issues with your Mark 1, or may be required as part of troubleshooting measures.
* OFF: This option will put your Mark 1 into Standby Mode. You won't be able to use the **Wake Word** or make **Utterances** while Mark 1 is in Standby Mode. To wake Mark 1 up from Standby, press the top button for two seconds.
* TEST: This option will immediately run a test sequence on your Mark 1. This option may be required as part of troubleshooting measures. To move through each of the tests, press the top button. Continue pressing the top button to exit the test sequence.
* SSH: This option allows you to enable [SSH](https://en.wikipedia.org/wiki/Secure_Shell) connections to the Mark 1 Device, or to block SSH if it's enabled.
* LEARN: This option allows you to enable the Learn functionality within Mycroft. If you've also opted-in on home.mycroft.ai, and Learn functionality is enabled, then Mycroft will record your voice when Speaking the **Wake Word** and **Utterances**. This data is then used anonymously to _train_ Mycroft to better recognize the **Wake Word** and **Utterances**.
* RESET: This option resets Mark 1 back to a factory default state. You may need to do this for troubleshooing, or if you're giving your Mark 1 to someone else. _NOTE: If you're resetting your Mark 1, remember to remove the Device from home.mycroft.ai so that the Pairing is removed also_
* DEMO: If this option is selected, Mark 1 will provide a short demonstration of functionality, whilst channelling his secret desire to be Eminem :-\)

## Mark 1 boot sequence

When you power on your Mark 1, the eyes on the Mark 1 will go through a series of color changes. They are explained in more detail here.

* NO EYES SHOWN: If your Mark 1 is not showing any LED pixels light up on its eyes when the power is plugged in, this means that the Arduino that powers the Neopixel eyes hasn't booted correctly. Try unplugging the power, waiting 30 seconds and then plugging the power back in.
* GREY SPINNEY EYES: On first boot, Mark 1 will show grey spinning eyes. During this time, both the Raspberry Pi 3 board, and the Arduino used to control the [Neopixel](https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels) eyes are powering up. If your Mark 1 is stuck at this stage, try unplugging the power, waiting 30 seconds and then plugging the power back in.
* SOLID GREY EYES: After around 10 seconds, the grey spinning eyes may turn into solid grey eyes. During this time, the Raspberry Pi 3 board is writing code to the Arduino board that controls the Neopixel eyes.
* SOLID YELLOW EYES: On boot, Mark 1 will check that its software is up to date. First, it will do a [network time protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) sync to ensure that the system clock is synchronised, during which you will see the word `<<< SYNC <<<` appear on the LED display. Next, Mark 1 will attempt to update the Skills that are installed on the **Device**. If your Mark 1 gets stuck at this stage, it is likely an issue with updating software or Skills. A reboot may assist, but if it does not then please contact us via [Chat](https://mycroft.ai/chat) or the [Forum](https://community.mycroft.ai) and we can assist further.
* SOLID BLUE EYES \(or color you have eyes set to in your home.mycroft.ai preferences\): after Mark 1 has finished booting and is ready for your voice commands, it will show solid blue eyes, or the solid color you have chosen in your home.mycroft.ai preferences.

## Hardware information

## Common tasks performed on the Mark 1

### Installing Skills on the Mark 1

[Please refer to the information here](http://mycroft.ai/documentation/skills/)

### Connecting to the Mark 1 via SSH

* First, ensure that you've enabled SSH access. To do this hold down Mycroft's button until you see the menu. Twist till you see  SSH, press the button again. Twist to Allow, then press again. Mycroft will then say "SSH Logins are now allowed".
* Ensure you know the IP address of your Mark 1 Device on your network. A handy way to do this is to install the IP Address **Skill**, and then Speak:

> Hey Mycroft, what's your IP address?

`"here are my available IP addresses: wlan IP address ... Those are all my available IP addresses"`

* Open up your favorite terminal program, like PuTTy on Windows, or a new terminal on Linux
* `ssh pi@IPADDRESS`
* The default password is `mycroft`, so enter this when prompted.
* If you have successfully logged in via SSH you will see a command prompt like the one below:

```text
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

You are now connected to the Mark 1 via SSH.

### Setting up SSH to the Mark 1 using SSH keys

If you would like to set up SSH access to your Mark 1 device using SSH keys instead of a password, then follow [this guide on the Raspberry Pi documentation](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md).

### Accessing the command line interface \(CLI\) of the Mark 1

If you are SSH'd into the Mark 1 device, you are able to issue commands using the command line interface \(CLI\) instead of using voice. This bypasses the Speech To Text \(STT\) component of Mycroft.

`mycroft-cli-client`

You will now be able to type **Utterances** into the CLI.

![Issuing commands to Mark 1 from the command line](https://mycroft.ai/wp-content/uploads/2017/12/mark1-utterances-from-command-line.png)

### Enabling the LEARN function

The Learn functionality

If you've also opted-in on home.mycroft.ai, and Learn functionality is enabled, then Mycroft will record your voice when Speaking the **Wake Word** and **Utterances**. This data is then used anonymously to _train_ Mycroft to better recognize the **Wake Word** and **Utterances**.

To enable the Learn functionality:

1. Make sure that you've checked the 'Opt In' checkbox at [home.mycroft.ai](https://home.mycroft.ai), Settings -&gt; Basic.

![Opting in to help build the Mycroft Open Dataset](https://mycroft.ai/wp-content/uploads/2017/12/opting-in-open-dataset.png)

1. Next press the top button on your Mark 1. Turn the button to LEARN. Press the top button again. Turn the button to ALLOW. Mycroft will Speak:

`"I will now upload interaction data to help make me smarter"`

### Upgrading to the latest version from a 2017 Mark 1

If you were one of the original Kickstarter backers or ordered a Mark 1 in 2017 your Mark 1 may be running an old version. In this case you will need to manually update your Mark 1 to the latest version. Once you complete these steps Mark 1 will automatically update in the future. There are two recommended options for updating. Option 1 is recommended for Makers, and those used to ‘tinkering’ with RPi 3 and related open hardware.

#### Option 1: Burn a new disk image to the Micro SD card

You will need:

* A long reach T10 torx screwdriver
* A Micro SD card reader/writer
* An internet connection

Method

* Download the [18.02b Mark 1 disk image](https://mycroft.ai/to/mark-1-image) from the mycroft website.
* Unplug the Mark 1 from the power supply.
* Remove the four rubber feet from the Mark 1, and put them in a safe place.
* Gently remove the base of the Mark 1.
* Gently unseat the Micro SD card.
* Using Etcher, burn the disk image to the Micro SD card. Allow Etcher to complete verification.
* Gently re-seat the Micro SD card in the Mark 1.
* Gently place the base of the Mark 1 back, and screw in the four screws.
* Replace the four rubber feet.
* Plug in the power supply.
* The Mark 1 device will power on with ‘white spinning eyes’. This will last around 20 seconds to 1 minute. Mark 1 will then have ‘full blue eyes’.
* Mark 1 will then advise that it needs to be connected to WiFi.
* Follow [the instructions to connect Mark 1 to WiFi](https://mycroft.ai/documentation/mark-1/#getting-mark-1-connected-to-the-internet-using-a-network-cable), or connect an ethernet cable to the ethernet socket on the back of the device.
* Once you are connected to WiFi, Mark 1 will advise that you need to pair the device. Pair the device on home.mycroft.ai

That’s it! Once your Mark 1 is paired, you’ll be able to use all the default Skills that come with the device, and you’ll also be able to install your own from the list at: [https://mycroft.ai/documentation/skills/\#community-developed-skills](https://mycroft.ai/documentation/skills/#community-developed-skills)

#### Option 2: Update the Mark 1 using voice commands

This option is recommended if you aren't comfortable taking apart your Mark 1 device.

You will need:

* An internet connection
* About 20 minutes to do the update - parts of the update take over an hour but you can do other things while the updates are happening.

Method

[Follow along with Kathy](https://drive.google.com/a/mycroft.ai/file/d/1bJ_aPT-bplQElSoZcZ_FQUruWa3iFJZ5/view?usp=sharing), our Community Manager, as she guides you through the upgrade process via voice.

* Take your Mark 1 out of its box, and give it a wipe over with a damp \(not wet\) cotton cloth, to remove dust. Be careful as the acrylic front plate can scratch if you use an abrasive cloth. Gently blow into the ports on the back of the device, and the ventilation holes on the top and bottom, to blow away excess dust.
* Plug Mark 1 into power
* The Mark 1 device will power on with ‘white spinning eyes’. This will last around 20 seconds to 1 minute. Mark 1 will then have ‘full blue eyes’.
* Mark 1 will then advise that it needs to be connected to WiFi.
* Follow [the instructions to connect Mark 1 to WiFi](https://mycroft.ai/documentation/mark-1/#getting-mark-1-connected-to-the-internet-using-a-network-cable), or connect an ethernet cable to the ethernet socket on the back of the device.
* Once you are connected to WiFi, Mark 1 will advise that you need to pair the device. Pair the device on home.mycroft.ai [following these instructions.](https://mycroft.ai/documentation/mark-1/#pairing-the-mark-1)
* If you hear the message Error occurred in processing pairing Skill, don’t worry, this is common for Mark 1 that are doing their first update in a little while.
* Your Mark 1 will now appear frozen; it won’t respond to voice commands.
* Reboot the Device by removing the power supply, waiting 10 seconds then plugging the power supply back in.
* You will see ‘grey spinny eyes’ then ‘full blue eyes’ after about 20 seconds to 1 minute
* Speak the command Install platform patch. Mycroft will respond with installing.
* Mark 1 will then show ‘blue eye’ and display ‘UPDATING’ on screen.
* Updating will take between 15 minutes and 90 minutes depending on your internet connection.
* Mark 1 will reboot after the update is complete.
* After the reboot, Mark 1 will show ‘white spinning eyes’ then ‘yellow eyes’ with ‘UPDATING’ on screen. When Mark 1 is ready to respond to voice commands, the device will show ‘full blue eyes’.

### How to reimage a Mark 1 Device

#### Prerequisites

To reimage a Mark 1 **Device**, you will need:

* A MicroSD card reader - whether this is built in to your computer or works via USB adapter.
* You will need [Etcher](https://etcher.io/), a disk image writer, or equivalent software that writes disk images to a MicroSD card
* A torque screwdriver to unscrew the torque screws on the Mark 1 **Device**

#### Reimaging steps

* Download the software image. Save it to your computer. [The Mark 1 disk image is available here](https://mycroft.ai/to/mark-1-image)
* Disconnect your Mark 1 from the power supply.
* Using your torque screwdriver, take apart your Mark 1. If you need help, [this video from Geeked Out Solutions may be of assistance](https://www.youtube.com/watch?v=r76ObbB2EsA).
* Remove the Micro SD card from the Raspberry Pi board on the back of the Mark 1 unit. It should come out easily, and should not need to be forced.
* Insert the Micro SD card into the SD card slot on your computer. If your computer doesn't have a Micro SD card slot, you will need an external Micro SD card reader, or a SDHC card reader with a converter.
* Open Etcher, and follow the steps to burn the Mark 1 disk image that you downloaded in the first step onto the Micro SD card.
* Remove the Micro SD card from your computer / adapter and insert it into the Micro SD slot on the Raspberry Pi. Then, put the Mark 1 unit back together using the torque screws and screwdriver.
* Connect the Mark 1 unit back to the power supply.
* The Mark 1 unit should reboot and now be functioning correctly.

For more information, [see the original forum post by Barney Woodrow](https://community.mycroft.ai/t/how-to-re-image-mark1s-sd-card/2106).

If you prefer to use the Linux command line tool `dd` to burn the disk image instead, follow these instructions:

1. Download the [Mark 1 disk image](https://mycroft.ai/to/mark-1-image)
2. Insert the Micro SD card you wish to burn the image to. It must have a storage capacity of 8GB or higher.
3. Identify the path where the MicroSD card is mounted by running the command `sudo fdisk -l`. You will be able to tell the path based on the storage size of the device.
4. Keep a note of this - it will be something like `/dev/sdb1`
5. Unmount the disk so that no other operation can write to the device while it is being imaged using the command `sudo umount /dev/sdb1`. Make sure to substitute for the location of your device.
6. Run the command `sudo dd if=path-to-your-image.img of=/dev/sdb1 bs=20M`. Make sure to substitute the location of your device, and the path to the `.img` file you downloaded.
7. This will take several minutes to run. The command prompt will return if successful, otherwise an error message will be displayed on your terminal.

#### What should I do if reimaging doesn't work?

Micro SD cards have a finite lifespan. It is possible that the Micro SD card inside the Raspberry Pi inside the Mark 1 unit has suffered hardware failure. If this occurs, you will see symptoms such as:

* Mark 1 not booting successfully
* Strange appearance of _eyes_ and _mouth_
* Mark 1 will be unresponsive to voice commands

If you believe your Micro SD card might have failed, [please make contact with us so we can look into the issue further with you](https://mycroft.ai/contact/), and if warranted, provide a replacement.

### Keeping your Mark 1 Device updated

Your Mark 1 device will check for updates around every hour. If new software is available, Mark 1 will automatically download the updates and apply them.

There's nothing else you need to do.

### Downgrading your Mark 1 Device to a lower version

The `apt` repo use to store the Mark 1 package, `mycroft-core` - does not store package versions. However, the Mark 1 **does** cache `apt` packages on the **Device** at:

`/var/cache/apt/archives`

So, in order to downgrade the Mark 1 **Device**, we need to do two things:

* remove the current `mycroft-core` package
* manually install the archived package using `dpkg`

First, we remove the current `mycroft-core` package. In the example below, the version is given as `0.9.12`, but use the version you currently have installed.

`sudo apt-get remove mycroft-core=0.9.12`

Next, find the package in the archives that you want to install:

`pi@mark_1:~ $ ls -las /var/cache/apt/archives/ | grep mycroft-core`

Then, use `dpkg` to install the archive

`sudo dpkg -i /path/to/file`

You should then reboot the Mark 1.

## Common issues on Mark 1 Devices

There are several common issues with Mark 1 Devices. They are documented here to help you.

### Mark 1 Device is frozen

If your Mark 1 Device is frozen, reboot it by:

1. Pressing the top button for 2 seconds, scrolling the button to select REBOOT then pressing the top button again to reboot.
2. If this does not work, disconnect your Mark 1 **Device** from the power source, wait 10 seconds, then plug the Mark 1 back into the power source.

## Hardware Hacking your Mark 1 Device

If you're interested in hardware hacking on your Mark 1 **Device**, the [hardware schematics](https://github.com/MycroftAI/hardware-mycroft-mark-1) are open source and available for download.
