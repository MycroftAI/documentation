---
ID: 33601
post_title: 'Picroft &#8211; outputting audio'
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/picroft/picroft-audio/
published: true
post_date: 2017-12-06 08:53:08
---
# Picroft - outputting audio

- [Picroft - outputting audio](#picroft---outputting-audio)
  * [How to output audio via HDMI](#how-to-output-audio-via-hdmi)
  * [How to output audio through USB](#how-to-output-audio-through-usb)
  * [How to output audio through Bluetooth](#how-to-output-audio-through-bluetooth)

If you are developing on Picroft, and want to do audio-related **Skills** development, you will find this information on outputting audio useful. 

## How to output audio via HDMI

* You will need your Picroft set up on your Raspberry Pi 3
* You will need an HDMI cable to plug into TV or speakers

1. Connect a keyboard and/or monitor to Picroft, or alternatively, `ssh` into Picrot. By default the user is `pi` and the password is `mycroft`. 
2. Run `nano auto_run.sh` (or use your preferred text editor)
3. Add a `#` in front of the line `sudo amixer cset numid 3 "1"` to comment it out
4. Remove the `#` at the start of the line `sudo amixer cset numid 3 "2"`
5. Reboot Picroft

Audio should now play through the device you have the HDMI cable connected to (ie TV or speakers). 

## How to output audio through USB

* You will need your Picroft set up on your Raspberry Pi 3
* You will need an HDMI cable to plug into TV or speakers

Typically, USB audio should be connected to `hwplug:1,0` but to verify, run this command: 

`aplay -L`

Next, find the `hwplug` output for the device you want to use. Take this, and update the `mycroft.conf` file accordingly. This file is located at `/etc/mycroft/mycroft.conf` on Picroft. 

`"play_wav_cmdline": "aplay -Dhw:0,0 %1"`

now becomes 

`"play_wav_cmdline": "aplay -Dplughw:1,0 %1"`

You can now run `./auto_run.sh` to start the program back up and test and ensure the output comes through the USB speakers.

##  How to output audio through Bluetooth

* You will need your Picroft set up on your Raspberry Pi 3
* You will need a Bluetooth audio device to connect to

First, we need to enable Bluetooth. 

1. Edit the `/etc/mycroft/mycroft.conf` file
2. Add `"port": "/dev/ttyAMA1"` to the enclosure settings

Next, we set up the Bluetooth connection. 

Using `bluetoothctl -a`, follow these steps: 

* Agent on
* Scan on
* Note the Bluetooth speaker address
* Pair the address
* Trust the address
* Connect to the address

To enable auto connect, follow these steps: 

In the `/usr/local/sbin` directory, create a file called `startBTAudio.sh`. 

The file should have the following contents: 

```
 #!/bin/sh
echo "connect BTSPEAKERADDRESS" | bluetoothctl -a
echo "exit" | bluetoothctl -a
```

In the `/etc/systemd/system` directory, create two files: 

The first file should be called `BTSpeaker.service` and have the following contents: 

```
[Unit]
Description=Bluetooth Speaker Auto Connect
            
[Service]
Type=simple
ExecStart=/usr/local/sbin/startBTAudio.sh
```

The second file should be called `BTSpeaker.timer` and have the following contents: 

```
[Unit]
Description=Run BTSpeaker Service After 30s	
	
[Timer]
OnBootSec=30s
Unit=BTSpeaker.Service	
	
[Install]
WantedBy=multi-user.target
```

Next, run `systemctl enable BTSpeaker.timer`

Next, we connect the audio. 

1. First, install `pulseaudio-module-bluetooth` by running `apt-get install pulseaudio-module-bluetooth`
2. Run `pacmd list-sinks`and note the Bluetooth sink name
3. Edit `/etc/pulse/deault.pa` and add `set-default-sink SINKNAME` and add `load-module module-native-protocol-unix auth-anonymous=1 socket=/tmp/pulse-socket`
4. Edit `/home/mycroft/.config/pulse/client.conf` and add `default-server = unix:/tmp/pulse-socket`
5. Edit `/etc/mycroft/mycroft.conf` and set `default_wav_cmdline` to `"aplay -Dpulse %1"` and set `default_mp3_cmdline` to `"mpg123 -o pulse %1"`

Reboot the Picroft and test that audio is outputting to the Bluetooth device.
