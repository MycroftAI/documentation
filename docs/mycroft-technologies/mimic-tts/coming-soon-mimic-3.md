---
description: A fast, privacy-focused, open-source, neural Text to Speech (TTS) engine.
---

# COMING SOON: Mimic 3

{% hint style="warning" %}
NOTE: Mimic 3 is not yet released and installation using these instructions is not yet possible.

To be the first to find out when Mimic 3 launches register for updates here:\
[https://mycroft.ai/blog/mark-ii-update/#mimic-3](https://mycroft.ai/blog/mark-ii-update/#mimic-3)
{% endhint %}

Mimic 3 is a neural text to speech engine that can run locally, even on low-end hardware like the Raspberry Pi 4.
It is the default text to speech engine on the [Mark II](https://mycroft.ai/product/mark-ii/).

* [Install Mimic 3](#installation)
* [Listen to voice samples](https://mycroftai.github.io/mimic3-voices/)
* [See example use cases](#usage)
* [Learn how it works](#how-it-works)


## Installation <a href="#installation" id="installation"></a>


### Hardware Requirements

Mimic 3 was designed to run on the Raspberry Pi 4 (64-bit OS), but will also run on other platforms:

* `amd64`
    * AMD/Intel-based desktops/laptops
    * Very fast on Ryzen 9 5950X, [RTF](#real-time-factor) less than 0.05
* `arm64`
    * Raspberry Pi 3/4 and Zero 2 with [64-bit Pi OS](https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/)
    * Usable on Pi 4, [RTF](#real-time-factor) around 0.5
* `armv7l`
    * Raspberry Pi 1/2/3/4 and Zero 2 with 32-bit Pi OS
    * Slow on Pi 3, [RTF](#real-time-factor) around 2.5


#### Real-Time Factor

The performance of a text to speech system is often measured by its real-time factor (RTF). This is the ratio of how long it takes to generate audio to how long the audio is when spoken. 
In general, **lower is better** for RTF.
An RTF of 1 means that it took one second of compute time to generate one second of spoken audio. 
An RTF of 0.5 is better than 1, however, since the same second of spoken audio now only took half a second to generate.


### Software Requirements

* Linux
    * Recommended: 64-bit Debian bullseye or Raspberry Pi OS
* Python 3.7+
    * Recommended: Python 3.9
* Python packages
    * See [requirements.txt](https://github.com/MycroftAI/mimic3/blob/master/requirements.txt)
* System packages
    * `libespeak-ng1`
    * `libatomic1` (32-bit ARM only)
    * `libgomp1` (32-bit ARM only)
    * `libatlas-base-dev` (32-bit ARM only)


### TTS Plugin for Mycroft AI

Install the necessary system packages:

``` sh
sudo apt-get install libespeak-ng1
```

On 32-bit ARM platforms (a.k.a. `armv7l` or `armhf`), you will also need some extra libraries:

``` sh
sudo apt-get install libatomic1 libgomp1 libatlas-base-dev
```

Next, install the TTS plugin in Mycroft:

```sh
mycroft-pip install mycroft-plugin-tts-mimic3[all]
```

Removing `[all]` will install support for English only.

Additional language support can be selectively installed by replacing `all` with a two-character language code, such as `de` (German) or `fr` (French).
See [`setup.py`](https://github.com/MycroftAI/mimic3/blob/master/setup.py) for an up-to-date list of language codes.

Enable the plugin in your [mycroft.conf](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/customizations/mycroft-conf) file:

``` sh
mycroft-config set tts.module mimic3_tts_plug
```

or you can manually add the following to `mycroft.conf` with `mycroft-config edit user`:

``` json
"tts": {
  "module": "mimic3_tts_plug"
}
```


See the [plugin's documentation](https://github.com/MycroftAI/plugin-tts-mimic3) for more options.


### Docker Image

A pre-built Docker image is available for `x86_64` as well as 32/64-bit ARM:


``` sh
docker run \
       -it \
       -p 59125:59125 \
       -v "${HOME}/.local/share/mycroft/mimic3:/home/mimic3/.local/share/mycroft/mimic3" \
       'mycroftai/mimic3'
```

Visit the web page at http://localhost:59125

The following convenience scripts are also available:

* [`mimic3`](https://github.com/MycroftAI/mimic3/blob/master/docker/mimic3)
* [`mimic3-server`](https://github.com/MycroftAI/mimic3/blob/master/docker/mimic3-server)
* [`mimic3-download`](https://github.com/MycroftAI/mimic3/blob/master/docker/mimic3-download)


### Debian Package

Grab the Debian package from the [latest release](https://github.com/mycroftAI/mimic3/releases) for your platform:

* `mycroft-mimic3-tts_<version>_amd64.deb`
    * For desktops and laptops (`x86_64` CPUs)
* `mycroft-mimic3-tts_<version>_arm64.deb`
    * For Raspberry 3/4 and Zero 2 with [64-bit Pi OS](https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/)
* `mycroft-mimic3-tts_<version>_armhf.deb`
    * For Raspberry Pi 1/2/3/4 and Zero 2 with 32-bit Pi OS
    
Once downloaded, install the package with (note the `./`):

``` sh
sudo apt install ./mycroft-mimic3-tts_<VERSION>_<PLATFORM>.deb
```

Once installed, the following commands will be available in `/usr/bin`:

* `mimic3`
* `mimic3-server`
* `mimic3-download`


### Python Package


Install the package:

``` sh
pip install mycroft-mimic3-tts[all]
```

Removing `[all]` will install support for English only.

Additional language support can be selectively installed by replacing `all` with a two-character language code, such as `de` (German) or `fr` (French).
See [`setup.py`](https://github.com/MycroftAI/mimic3/blob/master/setup.py) for an up-to-date list of language codes.

Once installed, the following commands will be available:

* `mimic3`
* `mimic3-download`
* `mimic3-server`


### From Source

Clone the repository:

``` sh
git clone https://github.com/mycroftAI/mimic3.git
```

Run the install script:

``` sh
cd mimic3/
./install.sh
```

A virtual environment will be created in `mimic3/.venv` and the `mycroft-mimic3-tts` Python module will be installed in editiable mode (`pip install -e`).

Once installed, the following commands will be available in `.venv/bin`:

* `mimic3`
* `mimic3-server`
* `mimic3-download`


---


## Usage <a href="#usage" id="usage"></a>

There are many ways to use Mimic 3, including:

* [From the command line](#command-line-interface)
* [As a web server](#web-server)
* [In a screen reader](#speech-dispatcher)


### Voice Keys

Voices in Mimic 3 are keyed by a name with specific parts. These parts include the voice's language, region, training dataset, quality level, and speaker.

![Structure of a Mimic 3 voice key](https://mycroft-ai.gitbook.io/img/mimic3-voice_parts.png)

The default voice is `en_UK/apope_low`

Voice models are automatically downloaded from [Github](https://github.com/MycroftAI/mimic3-voices) and stored in `${HOME}/.local/share/mycroft/mimic3` (technically `${XDG_DATA_HOME}/mycroft/mimic3`). You can also [manually download them](#downloading-voices).


### Command-Line Interface


#### Basic Synthesis

The `mimic3` command can be used to synthesize audio on the command line:

```sh
mimic3 --voice <voice> "<text>" > output.wav
```

where `<voice>` is a [voice key](#voice-keys) like `en_UK/apope_low`.
`<TEXT>` may contain multiple sentences, which will be combined in the final output WAV file. These can also be [split into separate WAV files](#multiple-wav-output).


#### SSML

A subset of Speech Synthesis Markup Language, or [SSML](https://www.w3.org/TR/speech-synthesis11/), is available through the command line and web interface. SSML allows you to fine tune your output.

```shell
cat << EOF |
<speak>
  <s>
    Spoken before pause with default voice.
  </s>
  <break time="2s" />
  <voice name="en_US/vctk_low#p236">
    <s>
      Spoken after pause in a different voice.
    </s>
  </voice>
</speak>
EOF
    mimic3 --ssml --voice 'en_US/cmu-arctic#eey' > output.wav
```

SSML even lets you mix and match languages:

```shell
cat << EOF |
<speak>
  <voice name="de_DE/thorsten_low">
    <s>
      Eine Sprache ist niemals genug.
    </s>
  </voice>
  <voice name="nl/rdh_low">
    <s>
      Eén taal is nooit genoeg.
    </s>
  </voice>
  <voice name="en_US/vctk_low">
    <s>
      One language is never enough.
    </s>
  </voice>
</speak>
EOF
    mimic3 --ssml > output.wav
```

If your SSML contains `<mark>` tags, add `--mark-file <file>` to the command-line and use `--interactive` mode. As the marks are encountered, their names will be written on separate lines to the file:

```sh
mimic3 --ssml --interactive --mark-file - '<speak>Test 1. <mark name="here" /> Test 2.</speak>'
```

The following SSML tags are supported:

* `<speak>` - wrap around SSML text
    * `lang` - set language for document
* `<s>` - sentence (disables automatic sentence breaking)
    * `lang` - set language for sentence
* `<w>` / `<token>` - word (disables automatic tokenization)
* `<voice name="...">` - set voice of inner text
    * `voice` - [voice key](#voice-keys)
* `<prosody attribute="value">` - change speaking attributes
    * Supported `attribute` names:
        * `volume` - speaking volume
            * number in [0, 100] - 0 is silent, 100 is loudest (default)
            * +X, -X, +X%, -X% - absolute/percent offset from current volume
            * one of "default", "silent", "x-loud", "loud", "medium", "soft", "x-soft"
        * `rate` - speaking rate
            * number - 1 is default rate, < 1 is slower, > 1 is faster
            * X% - 100% is default rate, 50% is half speed, 200% is twice as fast
            * one of "default", "x-fast", "fast", "medium", "slow", "x-slow"
* `<say-as interpret-as="">` - force interpretation of inner text
    * `interpret-as` one of "spell-out", "date", "number", "time", or "currency"
    * `format` - way to format text depending on `interpret-as`
        * number - one of "cardinal", "ordinal", "digits", "year"
        * date - string with "d" (cardinal day), "o" (ordinal day), "m" (month), or "y" (year)
* `<break time="">` - Pause for given amount of time
    * time - seconds ("123s") or milliseconds ("123ms")
* `<sub alias="">` - substitute `alias` for inner text
* `<phoneme ph="">` - supply phonemes for inner text
    * See `phonemes.txt` in voice directory for available phonemes
    * Phonemes may need to be separated by whitespace

SSML `<say-as>` support varies between voice types:

* [gruut](https://github.com/rhasspy/gruut/#ssml)
* [eSpeak-ng](http://espeak.sourceforge.net/ssml.html)
* Character-based voices do not currently support `<say-as>`
* [epitran](https://github.com/dmort27/epitran/) based voices do not currently support `<say-as>`


#### Long Texts

If your text is very long, and you would like to listen to it as its being synthesized, use `--interactive` mode:

```sh
mimic3 --interactive < long.txt
```

Each input line will be synthesized and played (see `--play-program`). By default, 5 sentences will be kept in an output queue, only blocking synthesis when the queue is full. You can adjust this value with `--result-queue-size`.

If your long text is fixed-width with blank lines separating paragraphs like those from [Project Gutenberg](https://www.gutenberg.org/), use the `--process-on-blank-line` option so that sentences will not be broken at line boundaries. For example, you can listen to "Alice in Wonderland" like this:

```sh
curl --output - 'https://www.gutenberg.org/files/11/11-0.txt' | \
    mimic3 --interactive --process-on-blank-line
```


#### Multiple WAV Output

With `--output-dir` set to a directory, Mimic 3 will output a separate WAV file for each sentence:

```sh
mimic3 'Test 1. Test 2.' --output-dir /path/to/wavs
```

By default, each WAV file will be named using the (slightly modified) text of the sentence. You can have WAV files named using a timestamp instead with `--output-naming time`. For full control of the output naming, the `--csv` command-line flag indicates that each sentence is of the form `id|text` where `id` will be the name of the WAV file.

```sh
cat << EOF |
s01|The birch canoe slid on the smooth planks.
s02|Glue the sheet to the dark blue background.
s03|It's easy to tell the depth of a well.
s04|These days a chicken leg is a rare dish.
s05|Rice is often served in round bowls.
s06|The juice of lemons makes fine punch.
s07|The box was thrown beside the parked truck.
s08|The hogs were fed chopped corn and garbage.
s09|Four hours of steady work faced us.
s10|Large size in stockings is hard to sell.
EOF
  mimic3 --csv --output-dir /path/to/wavs
```

You can adjust the delimiter with `--csv-delimiter <delimiter>`.

Additionally, you can use the `--csv-voice` option to specify a different voice or speaker for each line:

```sh
cat << EOF |
s01|#awb|The birch canoe slid on the smooth planks.
s02|#rms|Glue the sheet to the dark blue background.
s03|#slt|It's easy to tell the depth of a well.
s04|#ksp|These days a chicken leg is a rare dish.
s05|#clb|Rice is often served in round bowls.
s06|#aew|The juice of lemons makes fine punch.
s07|#bdl|The box was thrown beside the parked truck.
s08|#lnh|The hogs were fed chopped corn and garbage.
s09|#jmk|Four hours of steady work faced us.
s10|en_UK/apope_low|Large size in stockings is hard to sell.
EOF
  mimic3 --voice 'en_US/cmu-arctic_low' --csv-voice --output-dir /path/to/wavs
```

The second contain can contain a `#<speaker>` or an entirely different voice!


#### Interactive Mode

With `--interactive`, Mimic 3 will switch into interactive mode. After entering a sentence, it will be played with `--play-program`.

```sh
mimic3 --interactive
Reading text from stdin...
Hello world!<ENTER>
```

Use `CTRL+D` or `CTRL+C` to exit.


#### Noise and Length Settings

Synthesis has the following additional parameters:

* `--noise-scale` and `--noise-w`
    * Determine the speaker volatility during synthesis
    * 0-1, default is 0.667 and 0.8 respectively
* `--length-scale` - makes the voice speaker slower (> 1) or faster (< 1)

Individual voices have default settings for these parameters in their `config.json` files (under `inference`).


#### List Voices

```sh
mimic3 --voices
```


#### CUDA Acceleration

If you have a GPU with support for CUDA, you can accelerate synthesis with the `--cuda` flag. This requires you to install the [onnxruntime-gpu](https://pypi.org/project/onnxruntime-gpu/) Python package.

Using [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) is highly recommended. See the `Dockerfile.gpu` file in the parent repository for an example of how to build a compatible container.


### Web Server <a href="#web-server" id="web-server"></a>

A small HTTP server is available for serving multiple clients. This is faster than the command-line interface since voice models only need to be loaded once.

![screenshot of web interface](https://mycroft-ai.gitbook.io/img/mimic3-server_screenshot.jpg)


#### Running the Server

``` sh
mimic3-server
```

This will start a web server at `http://localhost:59125`

See `mimic3-server --debug` for more options.


#### Endpoints

* `/api/tts`
    * `POST` text or [SSML](#ssml) and receive WAV audio back
    * Use `?voice=` to select a different [voice/speaker](#voice-keys)
    * Set `Content-Type` to `application/ssml+xml` (or use `?ssml=1`) for [SSML](#ssml) input
* `/api/voices`
    * Returns a JSON list of available voices

An [OpenAPI](https://www.openapis.org/) test page is also available at `http://localhost:59125/openapi`


#### CUDA Acceleration

If you have a GPU with support for CUDA, you can accelerate synthesis with the `--cuda` flag. This requires you to install the [onnxruntime-gpu](https://pypi.org/project/onnxruntime-gpu/) Python package.

Using [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) is highly recommended. See the [`Dockerfile.gpu`](https://github.com/MycroftAI/mimic3/blob/master/Dockerfile.gpu) for an example of how to build a compatible container.


#### Running the Client

Assuming you have started `mimic3-server` and can access `http://localhost:59125`, then run:

``` sh
mimic3 --remote --voice 'en_UK/apope_low' 'My hovercraft is full of eels.' > hovercraft_eels.wav
```

If your server is somewhere besides `localhost`, use `mimic3 --remote <URL> ...`

See `mimic3 --help` for more options.


#### MaryTTS Compatibility

Use the Mimic 3 web server as a drop-in replacement for [MaryTTS](http://mary.dfki.de/), for example with [Home Assistant](https://www.home-assistant.io/integrations/marytts/).

Make sure to use a Mimic 3 [voice key](#voice-keys) like `en_UK/apope_low` instead of a MaryTTS voice name.


### Speech Dispatcher <a href="#speech-dispatcher" id="speech-dispatcher"></a>

Mimic 3 can be used with the [Orca screen reader](https://help.gnome.org/users/orca/stable/) for Linux via [speech-dispatcher](https://github.com/brailcom/speechd).

After [installing Mimic 3](#installation), start the [web server](#server).
Next, make sure you have `speech-dispatcher` installed:

``` sh
sudo apt-get install speech-dispatcher
```

Create the file `/etc/speech-dispatcher/modules/mimic3-generic.conf` with the contents:

``` text
GenericExecuteSynth "printf %s \'$DATA\' | /path/to/mimic3 --remote --voice \'$VOICE\' --stdout | $PLAY_COMMAND"
AddVoice "en-us" "MALE1" "en_UK/apope_low"
```

You will need `sudo` access to do this. Make sure to change `/path/to/mimic3` to wherever you installed Mimic 3. Note that the `--remote` option is used to connect to a local Mimic 3 web server (use `--remote <URL>` if your server is somewhere besides `localhost`).

To change the voice later, you only need to replace `en_UK/apope_low`.

Next, edit the existing file `/etc/speech-dispatcher/speechd.conf` and ensure the following settings are present:

``` text
DefaultVoiceType  "MALE1"
DefaultModule mimic3-generic
```

Restart speech-dispatcher with:

``` sh
sudo systemctl restart speech-dispatcher
```

and test it out with:

``` sh
spd-say 'Hello from speech dispatcher.'
```


#### Systemd Service

To ensure that Mimic 3 runs at boot, create a systemd service at `$HOME/.config/systemd/user/mimic3.service` with the contents:

``` text
[Unit]
Description=Run Mimic 3 web server
Documentation=https://github.com/MycroftAI/mimic3

[Service]
ExecStart=/path/to/mimic3-server

[Install]
WantedBy=default.target
```

Make sure to change `/path/to/mimic3-server` to wherever you installed Mimic 3.

Refresh the systemd services:

``` sh
systemctl --user daemon-reload
```

Now try starting the service:

``` sh
systemctl --user start mimic3
```

If that's successful, ensure it starts at boot:

``` sh
systemctl --user enable mimic3
```

Verify the web server is running by visiting http://localhost:59125


### Downloading Voices <a href="#downloading-voices" id="downloading-voices"></a>

Mimic 3 automatically downloads voices when they're first used, but you can manually download them too with `mimic3-download`.

For example:

``` sh
mimic3-download 'en_US/*'
```

will download all U.S. English voices to `${HOME}/.local/share/mycroft/mimic3/voices`.

You can list the available voices with `--voices`:

```bash
mimic3 --voices | awk '{print $1}'
KEY
de_DE/m-ailabs_low
de_DE/thorsten_low
el_GR/rapunzelina_low
en_UK/apope_low
en_US/cmu-arctic_low
en_US/ljspeech_low
en_US/vctk_low
es_ES/carlfm_low
es_ES/m-ailabs_low
...
```

Voice models are stored locally in your home directory:

```bash
tree "${HOME}/.local/share/mycroft/mimic3/voices"

├── de_DE
│   ├── m-ailabs_low
│   │   ├── ALIASES
│   │   ├── config.json
│   │   ├── generator.onnx
│   │   ├── LICENSE
│   │   ├── phoneme_map.txt
│   │   ├── phonemes.txt
│   │   ├── README.md
│   │   ├── SOURCE
│   │   ├── speaker_map.csv
│   │   └── speakers.txt
...
```

Some voices even have multiple speakers. This one has over [one hundred](https://mycroftai.github.io/mimic3-voices/#en\_US\_vctk\_low).

See `mimic3-download --help` for more options.


---


## How It Works

Mimic 3 uses the [VITS](https://arxiv.org/abs/2106.06103), a "Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech". VITS is a combination of the [GlowTTS duration predictor](https://arxiv.org/abs/2005.11129) and the [HiFi-GAN vocoder](https://arxiv.org/abs/2010.05646).

Our implementation is heavily based on [Jaehyeon Kim's PyTorch model](https://github.com/jaywalnut310/vits), with the addition of [Onnx runtime](https://onnxruntime.ai/) export for speed. 

![mimic 3 architecture](img/mimic3-architecture.png)


### Phoneme Ids

At a high level, Mimic 3 performs two important tasks:

1. Converting raw text to numeric input for the VITS TTS model, and
2. Using the model to transform numeric input into audio output

The second step is the same for every voice, but the first step (text to numbers) varies. There are currently three implementations of step 1, described below.


### gruut Phoneme-based Voices

Voices that use [gruut](https://github.com/rhasspy/gruut/) for phonemization.

gruut normalizes text and phonemizes words according to a lexicon, with a pre-trained grapheme-to-phoneme model used to guess unknown word pronunciations.


### eSpeak Phoneme-based Voices

Voices that use [eSpeak-ng](https://github.com/espeak-ng/espeak-ng) for phonemization (via [espeak-phonemizer](https://github.com/rhasspy/espeak-phonemizer)).

eSpeak-ng normalizes and phonemizes text using internal rules and lexicons. It supports a large number of languages, and can handle many textual forms.


### Character-based Voices

Voices whose "phonemes" are characters from an alphabet, typically with some punctuation.

For voices whose orthography (writing system) is close enough to its spoken form, character-based voices allow for skipping the phonemization step. However, these voices do not support text normalization, so numbers, dates, etc. must be written out.


### Epitran-based Voices

Voices that use [epitran](https://github.com/dmort27/epitran/) for phonemization.

epitran uses rules to generate phonetic pronunciations from text. It does not support text normalization, however, so numbers, dates, etc. must be written out.


### Components of a Voice Model

Voice models are stored in a directory with a specific layout:

* `<language>_<region>` (e.g., `en_UK`)
    * `<voice-name>_<quality>`  (e.g., `apope_low`)
        * `ALIASES` - alternative names for the voice, one per line (optional)
        * `config.json` - training/inference configuration (see [code](https://github.com/MycroftAI/mimic3/blob/master/mimic3-tts/mimic3_tts/config.py) for details)
        * `generator.onnx` - exported inference model (see `ids_to_audio` method in [`voice.py`](https://github.com/MycroftAI/mimic3/blob/master/mimic3-tts/mimic3_tts/voice.py))
        * `LICENSE` - text, name, or URL of voice model license
        * `phoneme_map.txt` - mapping from source phoneme to destination phoneme(s) (optional)
        * `phonemes.txt` - mapping from integer ids to phonemes (`_` = padding, `^` = beginning of utterance, `$` = end of utterance, `#` = word break)
        * `README.md` - description of the voice
        * `SOURCE` - URL(s) of the dataset(s) this voice was trained on
        * `VERSION` - version of the voice in the format "MAJOR.Minor.bugfix" (e.g. "1.0.2")


---


## License

Mimic 3 is available under the [AGPL v3 license](https://github.com/MycroftAI/mimic3/blob/master/LICENSE)


---


## Feedback or questions? <a href="#more-questions" id="more-questions"></a>

Join us in [Mycroft Chat](https://chat.mycroft.ai/community/channels/mimic) or the [Community Forums](https://community.mycroft.ai).
