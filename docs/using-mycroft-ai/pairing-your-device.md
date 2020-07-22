---
description: >-
  Pairing makes information available to your Device to personalise your
  experience, such as which units of measurement you prefer, and your general
  location.
---

# Pairing Your Device

Each of your Mycroft **Device\(s\)** must be **Paired** with your [home.mycroft.ai](https://home.mycroft.ai) account.

Pairing makes information available to your Device to personalise your experience, such as which units of measurement you prefer, and your general location.

Pairing is also used for services that require API authentication, such as

* Wolfram Alpha
* Google Speech to Text
* Weather Skill API and OpenWeather

## Creating a home.mycroft.ai account

You can [create a home.mycroft.ai account](https://home.mycroft.ai/#/signup) by using

* Your Facebook account or;
* Your Google account or;
* Your GitHub account or;
* By signing up with your email address and choosing a password

### The Open Dataset

By default, Mycroft will not store your usage data or keep any recordings of your voice.

When creating an account, you will be asked if you would like to Opt-In to the Open Dataset. If you chosee to Opt-In then Mycroft will record your voice when Speaking the Wake Word and Utterances. This data is de-identified and used anonymously to _train_ Mycroft to better recognize the Wake Word and Utterances. It will also be provided to key partners such as Mozilla, to assist in the development of speech recognition tools such as [DeepSpeech](https://github.com/mozilla/DeepSpeech).

If you change your mind at any time, you can change your selection under the Agreements section of [your Profile](https://account.mycroft.ai/profile).

## Adding a Device

To add a Device to your home.mycroft.ai account, you will need a 6-character **Registration Code**. The Registration Code is provided in different ways depending on which **Device** you have.

### Getting a Registration Code

After your device has connected to the internet, Mycroft will speak a unique six character code. For the Registration Code CKAMP7, Mycroft would say:

```text
I'm connected to the internet and need to be registered. Go to home.mycroft.ai and use the Registration Code
C for Charlie
K for Kilo
A for Apple
M for Mike
P for Pa
number 7
```

Your pairing code will be different.

#### Mark 1

After you have connected your Mark 1 to Wifi, Mycroft will speak a 6-character **Registration Code**. This code will also appear on Mycroft's LED screen.

If you're stuck connecting to Wifi, please read the [Mark 1 Getting Started Guide \(PDF, 290Kb\)](https://mycroft.ai/wp-content/uploads/2017/06/Mark_1_User_Guide.pdf).

#### Picroft

After you have connected your Picroft to Wifi, Mycroft will speak a 6-character **Registration Code**.

If you're stuck connecting to Wifi, please read the [Picroft documentation](http://mycroft.ai/documentation/picroft/).

#### Linux

After your Mycroft for Linux installation is successfully installed, Mycroft will speak a 6-character **Registration Code**.

### Pairing your Device\(s\) to your home.mycroft.ai account

Once you have your Registration Code, you can then go to home.mycroft.ai -&gt; Add Device.

Use your Pairing Code, and provide a meaningful name and location for the Device. This will help you in the future if you have multiple devices. All other options will be pre-filled from your [default device settings](pairing-your-device.md#defaults), but can be changed for each individual device.

![Adding a new Device](https://mycroft.ai/wp-content/uploads/2019/06/Add-device.png)

Once complete, click 'NEXT' to pair the Device. Wait a few seconds, and then you'll be taken to a new screen confirming your Pairing has been successfully completed.

Congratulations! Your Mycroft Device is now paired, and is ready to start accepting your commands.

### Where is my identity information stored in the Mycroft code?

Once you have paired your Mycroft Device, pairing information is stored in:

`~/.mycroft/identity/identity2.json`

DO NOT SHARE THIS INFORMATION WITH OTHERS - IT IS YOUR MYCROFT IDENTITY

You may be asked for this information by Mycroft support staff while troubleshooting Device and/or Pairing issues.

## Device Settings

From the User menu in the top right, choose 'Devices'.

### Devices

This is list of all Mycroft devices paired with your account. From here you can add a new device, or change settings for existing devices.

Settings available:

* **Name** - a unique name for your device.
* **Placement** - location of your device e.g. Kitchen, Bedroom or Office. This is in place for location based utterances such as "turn off the light" which should only turn off lights in the current location, not all lights connected to your account.
* **Geographical Location** - your devices approximate geographical location, used for queries such as the local weather and time.
* **Voice** - By default, Mycroft will use the `American Male` voice, however you are free to choose other voices.
* **Wake Word** - By default, Mycroft will listen for "Hey Mycroft" to activate. A number of other pre-trained Wake Words are available. Additional configuration options are available through [advanced settings](pairing-your-device.md#advanced-settings) or by training your own [Precise](https://mycroft.ai/documentation/precise) Wake Word model.

### Preferences

These allow you to choose your preferred:

* Units of measurement

  \(_NOTE: choosing Miles instead of Kilometers will also switch your temperature format to Fahrenheit instead of Celsius_\)

* Time format
* Date format

All your Mycroft devices will use this information to tailor your experience.

### Defaults

The Device Default settings define your base configuration and will be used for any new device being added to your account. These may then be modified for each device.

### Advanced settings

Advanced users may configure additional options using an on-device configuration file. This includes setting an alternative speech-to-text engine, text-to-speech engine, or wake word listener. See the [`mycroft.conf` documentation](https://mycroft.ai/documentation/mycroft-conf/) for more detail.

