---
description: Having trouble with your audio?
---

# Audio Troubleshooting

{% hint style="warning" %}
This troubleshooting guide is not intended for the Mark II. If you are experiencing any audio troubles with a Mark II or Mark II Dev Kit, please reach out to our team directly at: https://mycroft.ai/contact/
{% endhint %}

Before troubleshooting it is a good idea to restart Mycroft's services and see if the problem is still present. You can do this by running:

```
mycroft-start restart all
```

Of if the helper commands aren't available:

```
~/mycroft-core/start-mycroft.sh restart all
```

## Mycroft's audio system

Mycroft utilizes pulseaudio for sound input and output.

Mark 1 and Picroft devices have pulseaudio set up correctly for the `mycroft` user. On picroft, any mic or speakers you add to it may need to be configured as Mycroft uses the default input and output from pulse.

Systems without pulseaudio installed are not likely to function as expected. Systems with both jack and pulseaudio may need additional configuration to work correctly.

## Device compatibility

We are often asked, "will my {very specific audio device} work?"

The answer is generally, maybe. However there is no way for us to test all of the hardware variations everytime we make a change to the code.

Most USB mics and speakers are usable with pulseaudio. In general, if your OS can recognize the device as an audio endpoint pulse will be able to connect it. A variety of microphones and speakers have been used successfully.

A [list of tested hardware](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft#tested-hardware) is maintained by the Community in the Picroft documentation.

If you have the device on hand, try it out and see. If the information on this page isn't able to get it going, try asking in the [Community Chat](https://chat.mycroft.ai) or [Forum](https://community.mycroft.ai).

## Microphone - Audio Input

> The microphone can't hear me or the CLI shows no change in the input meter while speaking.

### 1. Test if Mycroft is receiving mic input

The simplest way to visualize the audio input being received by Mycroft is to run the CLI. On your device you can view the CLI by running:

```
mycroft-cli-client
```

If Mycroft was not already running you can start Mycroft and the CLI together using:

```
mycroft-start debug
```

![Picroft basic commands](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-21-04-21-07.png)

The terminal window will then be filled by the CLI as pictured here. In the lower right-hand corner is a "Mic level". If no mic input is being received by Mycroft, this area will be blank. In this case please proceed to the next test.

On the other hand, if an audio stream is being received, the lines and the number here should jump around, and spike when you speak directly into the microphone. In this case we can be fairly sure that the microphone is working. It may be the Wake Word that is not responding.

{% content-ref url="wake-word-troubleshooting.md" %}
[wake-word-troubleshooting.md](wake-word-troubleshooting.md)
{% endcontent-ref %}

### 2. Test your mic outside of Mycroft

To see why the microphone is not working we first want to test it outside of Mycroft.

To do this we will record ten seconds of audio on the default input device and write it to the file `test.wav`. From the commandline on the device run:

```
arecord -d 10 test.wav
```

You can now play it back to hear what is recorded with:

```
aplay test.wav
```

If successful continue to the next test - 3. Mycroft Audio Test.

#### System does not recognize device

If the first test was not successful, your device is not installed correctly. If your operating system cannot use the device, then Mycroft will not be able to access it either.

See the PulseAudio section for help in configuring audio devices with the system.

### 3. Mycroft Audio Test

Mycroft comes with a built-in audio test. This tool will attempt to record, then play back a short audio clip using the default microphone (source) and speakers (sink). To start the test run:

```
mycroft-start audiotest
```

If the test is successful and you hear the recorded audio back, it should be possible for Mycroft to use the intended microphone.

#### Specifying an input device

By default Mycroft will use the system default device for all audio. In most cases this provides a more consistent, flexible and reliable experience. If however other methods do not work, we can specify the exact input device Mycroft should use in our `mycroft.conf` file. For information on this configuration file, see [https://mycroft.ai/documentation/mycroft-conf/](https://mycroft.ai/documentation/mycroft-conf/).

We first need to know the device name. This can be found by running the audio test with the `-l` flag

```
mycroft-start audiotest -l
```

As well as running the test, a list of audio devices will be displayed. The output we need looks like:

```
====================== Audio Devices ======================
 Index    Device Name
  4:       HDA Intel PCH: ALC269VB Analog (hw:1,0)
  6:       pulse
  7:       default
```

A specific device can be added to your user level configuration file using the [Configuration Manager](../customizations/config-manager.md) by running:

```bash
mycroft-config set listener.device_name "DEVICE_NAME"
```

Where "DEVICE\_NAME" is taken from the audio device output. Note the "(hw:1,0)" is not required.

Using the output from the audiotest example above, if we wanted to use the device at Index 4, we would run:

```bash
mycroft-config set listener.device_name "HDA Intel PCH: ALC269VB Analog"
```

#### Set the default device in pulseaudio

The other option is to set the default device in pulseaudio. See the PulseAudio section further down this page for more details.

## Speakers - Audio Output

### USB audio devices

If Mycroft audio output fails (No speech or audio) when using a USB sound card or output device, you can modify the play command lines used by Mycroft to use a different program.

To accomplish this, from your Terminal edit the System level configuration using the [Configuration Manager](../customizations/config-manager.md) by running:

```
mycroft-config edit system
```

This file can also be edited directly at `/etc/mycroft/mycroft.conf`.

In this configuration file, set the following values as such:

```javascript
{
  "play_wav_cmdline": "aplay %1",
  "play_mp3_cmdline": "mpg123 %1",
  [...]
}
```

## Pulseaudio settings

### Show current settings and info

`pactl info`

For mycroft, the lines most relevant are the Default Source: and Default Sink:.

```
  picroft:~$ pactl info
  Server String: unix:/run/user/1000/pulse/native
  Library Protocol Version: 30
  Server Protocol Version: 30
  Is Local: yes
  Client Index: 813
  Tile Size: 65472
  User Name: pi
  Host Name: picroft
  Server Name: pulseaudio
  Server Version: 8.0
  Default Sample Specification: s16le 2ch 44100Hz
  Default Channel Map: front-left,front-right
  Default Sink: alsa_output.pci-0000_00_1b.0.analog-stereo
  Default Source: alsa_input.pci-0000_00_1b.0.analog-stereo
  Cookie: ab8a:0b4d
```

### List available output devices

Use `pactl list sinks short` to list output devices available to the current user:

```
picroft:~$ pactl list sinks short
1       alsa_output.pci-0000_00_1b.0.analog-stereo      module-alsa-card.c      s16le 2ch 44100Hz       SUSPENDED
```

### List available input devices

`pactl list sources short` will list input devices available to the current user:

```
picroft:~$ pactl list sources short
1       alsa_output.pci-0000_00_1b.0.analog-stereo.monitor      module-alsa-card.c      s16le 2ch 44100Hz       SUSPENDED
2       alsa_input.pci-0000_00_1b.0.analog-stereo       module-alsa-card.c      s16le 2ch 44100Hz       SUSPENDED
```

### Changing pulseaudio input and output

If you need to adjust the device you're using for input or output, first determine the number of the source or sink you wish to set it to. Then use `pactl set-default-source` (for input) or `pactl set-default-sink` (for output) to update:

```
$ pactl set-default-source 2
$ pactl set-default-sink 1
```

This would set the default input to be device 2 and the default output device to be 1. Your numbers will vary. A successful change will not have any additional output listed. Verify with `pactl info`

### Echo cancellation

Pulseaudio has an echo cancellation module that can be loaded.

```
$ pactl load-module module-echo-cancel
```

This is system wide. If not previously enabled, you will need to restart any applications using pulse. For documentation, see [https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#index45h3](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#index45h3) Additional usage and tips can be found [https://wiki.archlinux.org/index.php/PulseAudio/Troubleshooting](https://wiki.archlinux.org/index.php/PulseAudio/Troubleshooting)

### Pulseaudio modules

Find out what modules are installed:

```
$ pactl list modules short
```

For more information like usage counts and properties, remove the `short`.

### Missing pulseaudio

If you see an issue in the logs with `Popen(play_wav_cmd)` and `OSError: [Errno 2] No such file or directory` this usually indicates that mycroft cannot find pulseaudio. Make sure it's installed and mycroft is able to access it. On Debian based systems like Ubuntu you can install the package by running:

```
sudo apt-get install pulseaudio
```

## Alsamixer

`alsamixer` is a utility provided by the ALSA sound system on Raspbian Stretch that allows you to select an audio playback (output) and input (capture) device.

To run `alsamixer`, type `Ctrl +C` to exit the guided setup and you will be at the Linux command line. Type `alsamixer` as shown below:

```bash
(.venv) pi@picroft:~ $ alsamixer
```

You will see a screen similar to the one below, and may have different options depending on which audio devices you have connected.

![Picroft alsamixer initial screen](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-27-23-05-12.png)

Different devices will have a different command key for choosing 'Capture' devices, in this case it is `F4`.

If you do not see any capture devices, as shown below, then you may need to select a different sound card.

![Picroft alsamixer no audio capture device](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-27-23-05-25.png)

To select a different sound card, follow the instructions on your version of `alsamixer`. In this case, the command key for choosing 'Select sound card' is `F6`. Use the arrow keys on your keyboard to navigate up and down the list to choose your preferred soundcard.

![Picroft alsamixer select sound card](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-27-23-05-52.png)

`alsamixer` usually has an option to see **all** capture and playback devices. In this case, the command key to see all devices is `F5`.

![Picroft alsamixer show all audio capture and playback devices](https://mycroft.ai/wp-content/uploads/2018/12/Screenshot-from-2018-12-27-23-06-09.png)

## Other useful commands

`lsusb` can be used to see what USB devices are connected to the system. `lsusb -v` can be also used, but produces significantly more output.

`groups` will list all the system groups the current user is a part of. In dev instances of mycroft, can be used to see if the mycroft user is part of the audio group. If running list sinks or list sources you see null or no devices for the user, use this command to verify if you're part of the `audio` group.

`alsamixer` is a command-line utility to adjust volume and muting of both inputs and outputs.

`pulseaudio -k` kills the current instance of pulseaudio.

`pulseaudio --start` will start pulseaudio.

`pavucontrol` is a GUI mixer client for X.

`pacmd` is an interactive shell version of `pactl`. Use `help` to see more once in the shell.
