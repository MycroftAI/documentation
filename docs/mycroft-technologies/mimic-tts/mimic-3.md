---
description: A fast, privacy-focused, open-source, neural Text to Speech (TTS) engine.
---

# Mimic 3

Mimic 3 is a neural text to speech engine that can run locally, even on low-end hardware like the Raspberry Pi 4.

### Voices

There are already hundreds of voices available in over twenty languages. [Samples for all available voices are available on Github.](https://mycroftai.github.io/mimic3-voices/)

Voices in Mimic 3 are keyed by a name with specific parts. These parts include the voice's language, region, training dataset, quality level, and speaker.

![Structure of a Mimic 3 voice key](https://mycroftai.github.io/mimic3-presentation/img/voice\_parts.png)

The default voice is `en_UK/apope_low`

### TTS Plugin for Mycroft AI

Mimic 3 is the default voice on the [Mark II](https://mycroft.ai/product/mark-ii/).&#x20;

#### Hardware requirements

The Mimic 3 TTS plugin will work on all Mycroft installations running Python 3.7+. However a Raspberry Pi 4 or better is recommended for real-time usage.

The Mark 1 contains a Raspberry Pi 3B so Mimic 3 can run locally, however it will be noticably slow in responding.

#### Installation

If you have Mycroft installed, you can install the plugin with:

```
mycroft-pip install plugin-tts-mimic3[all]
```

otherwise, you can use `pip` directly:

```
pip install plugin-tts-mimic3[all]
```

Language support can be selectively installed by replacing `all` with the two-character language group:

* `de` - German
* `es` - Spanish
* `fa` - Farsi
* `fr` - French
* `it` - Italian
* `nl` - Dutch
* `ru` - Russian
* `sw` - Kiswahili

Excluding `[..]` entirely will install support for English only.

See the [list of available languages here](https://mycroftai.github.io/mimic3-voices/). There are new voices and languages being added all the time.

#### Configuration

The plugin can be enabled in Mycroft using the Configuration Manager:

```
mycroft-config set tts.module mimic3_tts_plug
```

or you can manually add the following to `mycroft.conf` with `mycroft-config edit user`:

```
"tts": {
  "module": "mimic3_tts_plug"
}
```

Additional options can be set in `mycroft.conf` like:

```
"tts": {
  "module": "mimic3_tts_plug"
  "mimic3_tts_plug": {
    "<option>": <value>
  }
}
```

where options are:

* `voice` - [voice key](mimic-3.md#voices)
* `preloaded_voices` - list of voice keys to load at startup
* `length_scale` - speed of speaking (< 1 is faster, > 1 is slower)
* `noise_scale` - volatility of speaker
* `noise_w` - volatility of phoneme durations

### Web Server

A basic web server and interface is provided for quick testing and handling multiple text to speech clients.

![Mimic 3 web server interface](https://mycroftai.github.io/mimic3-presentation/img/web\_server.png)

You can run the web server with the following command:

```bash
mimic3-server --host localhost --port 59125 --preload-voice 'en_UK/apope_low'
```

With the web server running, clients can connect through the command line with the remote option:

```bash
mimic3 --remote 'http://localhost:59125' 'Some text to speak.' > output.wav
```

See below for [more command line examples](mimic-3.md#command-line-interface).

#### Mary TTS API <a href="#mary-tts-api" id="mary-tts-api"></a>

A web API compatible with [Mary TTS](http://mary.dfki.de) is also available, allowing Mimic 3 to be used in other projects like [Home Assistant](https://www.home-assistant.io/integrations/marytts/).

```bash
curl -X GET -G \
--data-urlencode "INPUT_TEXT=Some text to speak." \
--data-urlencode "VOICE=en_UK/apope_low" \
--data-urlencode 'INPUT_TYPE=TEXT' \
--data-urlencode 'OUTPUT_TYPE=AUDIO' \
--data-urlencode 'AUDIO=WAVE' \
'localhost:59125/process' \
--output output.wav
```

### Command Line Interface <a href="#command-line-interface" id="command-line-interface"></a>

The Mimic 3 command line interface makes it easy to convert text into audio.

```bash
mimic3 'Some text to speak.' > output.wav
```

Loading voice models can be slow, so the [web server](mimic-3.md#web-server) is recommended for repeated usage.

Many different voices are available in over twenty languages, with more already on the way. Specify the voice to use with the `--voice` flag and the relevant [Mimic 3 voice key](mimic-3.md#voices).

```bash
mimic3 --voice 'en_us/vctk_low' 'Using a different voice.' > output.wav
```

Voices are automatically downloaded on first use from [GitHub](https://github.com/MycroftAI/mimic3-voices/). You can list the available voices with `--voices`:

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
tree "${HOME}/.local/share/mimic3/voices"

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

```bash
mimic3 --voice 'en_us/vctk_low#p236' 'Using a different speaker.' > output.wav
```

#### Batch Processing <a href="#batch-processing" id="batch-processing"></a>

Multiple sentences can be synthesized with a single command and stored as separate audio files.

```bash
cat << EOF |
The birch canoe slid on the smooth planks.
Glue the sheet to the dark blue background.
It's easy to tell the depth of a well.
EOF
    mimic3 --output-dir output/
```

```bash
ls output/
Glue_the_sheet_to_the_dark_blue_background.wav
Its_easy_to_tell_the_depth_of_a_well.wav
The_birch_canoe_slid_on_the_smooth_planks.wav
```

Enabling CSV mode allows you to name each sentence, and set the voice or speaker.

```bash
cat << EOF |
s01|#awb|The birch canoe slid on the smooth planks.
s02|#rms|Glue the sheet to the dark blue background.
s03|#slt|It's easy to tell the depth of a well.
EOF
    mimic3 --csv-voice --voice 'en_US/cmu-arctic_low' --output-dir output/
```

```bash
ls output/
s01.wav  s02.wav  s03.wav
```

Longer texts like books can be synthesized in real-time. This example reads Alice in Wonderland:

```bash
curl --output - 'https://www.gutenberg.org/files/11/11-0.txt' | \
    mimic3 --interactive --process-on-blank-line
```

### SSML

Speech Synthesis Markup Language, or [SSML](https://www.w3.org/TR/speech-synthesis11/), is available through the command line and web interface. SSML allows you to fine tune your output.

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

## Feedback or questions? <a href="#more-questions" id="more-questions"></a>

Join us in [Mycroft Chat](https://chat.mycroft.ai/community/channels/mimic) or the [Community Forums](https://community.mycroft.ai).
