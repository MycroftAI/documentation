---
description: >-
Mimic is a fast, light-weight Text to Speech engine developed by Mycroft AI and VocaliD.
---
# Mimic

## What is Mimic?

Mimic is a fast, light-weight [Text to Speech (TTS)](https://en.wikipedia.org/wiki/Speech_synthesis) engine based on [Carnegie Mellon University's FLITE software](http://cmuflite.org/). Mimic uses text as an input, and outputs speech using the chosen _voice_.

![Video overview of Mimic](https://www.youtube.com/watch?v=gvnhcNdXJsk)

## Why should I use Mimic instead of other open source TTS tools?

Mimic is low-latency and has a small resource footprint. Its range of high quality voices also set it apart from othe open source text-to-speech projects. Apart from being used as the voice of Mycroft, Mimic's small resource footprint makes it an attractive choice for other embedded systems.

Mimic works on Linux, Android and Windows currently, and other platforms may be supported in the future. We also anticipate adding more languages to to enable many people to access realistic voices for the first time.

## The partnership between Mycroft.AI's Mimic and VocaliD

Mimic is a powerful TTS tool, however it can also help solve other important problems. That's why Mycroft.AI has partnered with [VocaliD](https://www.vocalid.co/) to help [Dr. Rupal Patel](https://www.linkedin.com/in/rupalvocalid/) and her team bring realistic TTS voices to people with speech disorders. VocaliD's technology creates customized voices that better represent the people who use them. To use these voices, VocaliD's clients need a fast, lightweight, cross-platform engine. That's where Mimic comes in! VocaliD’s clients can use Mimic as the engine that empowers them to speak with their own unique voice.

[You may enjoy the overview video from VocaliD](https://youtu.be/b6QhgQqxdew).

### How to donate your voice to the VocaliD voicebank

Creating realistic voices also requires everyday people to share their voice with VocaliD’s Human Voicebank. [Please consider sharing your voice with VocaliD's voice bank](https://vocalid.co/voicebank).

## Installing Mimic

_NOTE: If you are installing a Mycroft build for Linux or Picroft, Mimic will be installed as part of the installation dependencies - you don't need to build it separately. Follow the instructions below if you want to build Mimic as a standalone component._

Currently, Mimic runs on Linux (ARM & Intel architectures), Mac OSX, and Windows. It has been untested on Android, and we have plans to make it available on iOS.

### Installation prerequisites

In order to build Mimic, you will need the following:

* A good C compiler - for Linux or Mac OSX, `gcc` or `clang`is recommended. For Windows, `gcc` under [`Cygwin`](https://cygwin.com/) or [`mingw32`](http://www.mingw.org/) is recommended.
* GNU `make`, `automake` and `libtool`
* `pkg-config`
* PCRE and ICU libraries and headers
* An audio engine - for Linux we recommend ALSA, and for Mac OSX and Windows we recommend PortAudio

#### Install dependencies

##### On Ubuntu or Debian Linux

`$ sudo apt-get install gcc make pkg-config automake libtool libicu-dev libpcre2-dev libasound2-dev`

##### On Fedora Linux

`$ sudo dnf install gcc make pkgconfig automake libtool libicu-devel alsa-lib-devel`

##### On Arch Linux

`$ sudo pacman -S --needed install gcc make pkg-config automake libtool icu alsa-lib`

##### On Mac OSX

First, install Brew:

`$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

Then, install `pkg-config`, `automake`, `libtool`, `icu` and `PortAudio`

`$ brew install pkg-config automake libtool portaudio icu4c`

##### On Windows

###### Cross-compiling from Linux

The fastest and most straightforward way to build Mimic for Windows is by [cross-compilation](https://en.wikipedia.org/wiki/Cross_compiler) from Linux. That is, we build Mimic on Linux _for_ Windows.

This requires additional packages to be installed.

On Ubuntu 16.04 (xenial):

`sudo apt-get install gcc make pkg-config automake libtool libicu-dev libpcre2-dev wine binutils-mingw-w64-i686 mingw-w64-i686-dev gcc-mingw-w64-i686 g++-mingw-w64-i686`

On Ubuntu 14.04 (trusty):

`sudo apt-get install gcc make pkg-config automake libtool libicu-dev libpcre2-dev mingw32 mingw32-runtime wine`

Next, run the Windows build script:

`./run_testsuite.sh winbuild`

Test that the build executed correctly. The directory into which Mimic was installed will contain a `mimic.exe` file.

`wine ./mimic.exe -t "hello world"`

To distribute the compiled Mimic executable, add everything in the `install/winbuild/bin` directory to a `.zip` file. Copy it to your Windows machine via the cloud, USB file etc.

###### Building on Windows natively

_NOTE: The build process is **much** slower on Windows, and we strongly recommend cross-compiling from Linux._

For building Mimic on Windows natively, audio device libraries and audio libraries are optional, as Mimic can write its output to a waveform file. Some of the source files are very large, and some C compilers will have difficulty building them. We recommend `gcc`.

_NOTE: Visual C++ 6.0 is know to fail on the large diphone database files._

First, clone the `git` repository:

`$ git clone https://github.com/MycroftAI/mimic.git`

Navigate to the Mimic directory:

`$ cd mimic`

Generate the build scripts:

`$ ./autogen.sh`

Configure the build scripts:

`$ ./configure --prefix="/usr/local"`

Build from source:

`$ make`

Validate the build:

`$ make check`

Install the compiled code:

`$ sudo make install`

## Using Mimic

By default, Mimic will play the text using the selected audio device. Alternatively, Mimic can output the wave file in RIFF format (.wav).

### Reading text with Mimic

To read text to an audio device, use this command:

`$ ./mimic -t TEXT`

_Example:_

`$ ./mimic -t "Hello. Doctor. Name. Continue. Yesterday. Tomorrow."`

To read text, and have Mimic output to an audio file, use this command:

`$ ./mimic -t TEXT -o WAVEFILE`

_Example:_

`$ ./mimic -t "Hello. Doctor. Name. Continue. Yesterday. Tomorrow." -o hello.wav`

To read text from a file, and have Mimic output to an audio device, use this command:

`$ ./mimic -f TEXTFILE`

_Example:_

`$ ./mimic -f doc/alice`

To read text from a file, and have Mimic output to an audio file, use this command:

`$ ./mimic -f TEXTFILE -o WAVEFILE`

_Example:_

`$ ./mimic -f doc/alice -o hello.wav`

### How to change the Voice that Mimic uses

To list the available internal voices, use this command:

`$ ./mimic -lv`

To use an internal voice, use this command:

`$ ./mimic -t TEXT -voice VOICE`

_Example:_

`$ ./mimic -t "Hello" -voice slt`

To use an external voice file, use this command:

`$ ./mimic -t TEXT -voice VOICEFILE`

_Example:_

`$ ./mimic -t "Hello" -voice voices/cmu_us_slt.flitevox`

To use an external voice via a URL, use this command:

`$ ./mimic -t TEXT -voice VOICEURL`

_Example:_

`$ ./mimic -t "Hello" -voice http://www.festvox.org/flite/packed/flite-2.0/voices/cmu_us_ksp.flitevox`

### Notes on Mimic Voices

Mimic offers several different Voices. They use different speech modelling techniques (_diphone, clustern, hts_ for example). Voices differ a lot on size, how human they sound and how easy they are to understand.

_Diphone_ Voices are less computationally expensive and quite intelligible, but they sound very robotic.

_Example:_

`./mimic -t "Hello world" -voice kal16`

_Clustergen_ Voices sound more natural and are easy to understand, but this comes at the expense of larger file size and higher computational requirements.

_Example:_

`./mimic -t "Hello world" -voice slt`

`./mimic -t "Hello world" -voice ap`

_hts_ Voices sound more robotic than _clustergen_ voices, but have much smaller file size.

_Example:_

`./mimic -t "Hello world" -voice slt_hts`

#### Are Voices compiled or loaded from a file?

Voices can be compiled (built-in) into Mimic or loaded from a `.flitevox` file. The only exception are `hts` Voices. `hts` Voices combine both a compiled function with a voice data file, `.htsvoice`. Mimic will look for the `.htsvoice` file when the `hts` voice is loaded, looking in the current working directory, the `voices` subdirectory and the `$prefix/share/mimic/voices` directory if it exists.

Voice names are identified as loadable files if the name includes a "/" (slash) otherwise they are treated as internal compiled-in voices.

The `voices/` directory contains several `flitevox` voices. Existing Flite voices can be found [here](http://www.festvox.org/flite/packed/flite-2.0/voices/). The voice referenced via a URL will be downloaded on the fly.

#### Additional Voice options

Voices accept additional debug options, specified as `--setf feature=value` in the command line. Wrong values can prevent Mimic from working.

Here are some examples:

To use simple concatenation of diphones without prosodic modification:

`./mimic --sets join_type=simple_join doc/intro.txt`

To print sentences as they are said:

`./mimic -pw doc/alice`

To make Mimic speak more slowly:

`./mimic --setf duration_stretch=1.5 doc/alice`

To make Mimic speak more quickly:

`./mimic --setf duration_stretch=0.8 doc/alice`

To make Mimic speak with a higher pitch:

`./mimic --setf int_f0_target_mean=145 doc/alice`

To print Mimic help information:

`./bin/mimic -h`

## How do I create my own custom voice to use with Mimic?

Creating a custom Voice is a large undertaking, and requires recording a large _corpora_ of audio material. We recommend contacting [VocaliD](https://www.vocalid.co/) if you are interested in a custom Voice for Mimic.
