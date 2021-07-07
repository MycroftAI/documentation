---
description: Questions that we frequently receive about Mycroft and our technologies.
---

# FAQ

## Can Mycroft run completely offline? Can I self-host everything?

As a privacy focused project and community, many people are interested in fully offline or self-hosted options. Mycroft has intentionally been built in a modular fashion, so this is possible however is not easy and is unlikely to provide an equivalent user experience.

To achieve this we need to look at three key technologies: backend services provided by [Home.mycroft.ai](https://home.mycroft.ai); speech recognition or speech-to-text \(STT\); and speech-synthesis or text-to-speech \(TTS\). For backend services, the [official backend known as Selene is available on Github](https://github.com/MycroftAI?utf8=%E2%9C%93&q=Selene&type=&language=) under the AGPL v3.0 license, alternatively you can use the simpler Community developed [Personal Backend](https://github.com/MycroftAI/personal-backend). You can choose to run your own STT service such as [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech/releases) or [Kaldi](https://kaldi-asr.org/), however in our opinion these do not yet provide sufficient accuracy for mainstream usage. Finally, to generate speech on device, simply select the British Male voice. The more realistic sounding voices are generated on Mycroft servers and require significant hardware to synthesize speech within a reasonable time frame.

If you are running your own services, your Mycroft installation can be directed to use those using the [mycroft.conf file](../using-mycroft-ai/customizations/mycroft-conf.md).

## How fast can Mycroft respond?

By default, to answer a request Mycroft:

1. Detects the wake word 
2. Records 3 - 10 seconds of audio 
3. Sends this audio to a cloud-based speech-to-text \(STT\) service 
4. Transcribes the audio and returns the text transcription 
5. Parses the text to understand the intent 
6. Sends the text to the intent handler with the highest confidence 
7. Allows the Skill to perform some action and provide the text to be spoken 
8. Synthesizes audio from the given text, either locally or remotely, depending on the text-to-speech \(TTS\) engine in use 
9. Plays the synthesized spoken audio.

Through this process there are a number of factors that can affect the perceived speed of Mycroft's responses:

* System resources - more processing power and memory never hurts!
* Network latency - as it is not yet possible to perform everything on device, network latency and connection speed can play a significant role in slowing down response times.
* Streaming STT - we have been experimenting with the use of streaming services. This transcribes audio as it's received rather than waiting for the entire utterance to be finished and sending the resulting audio file to a server to be processed in its entirety. It is possible to switch to a streaming STT service however at present this is not available by default and requires a paid 3rd party service. See [Switching STT Engines](../using-mycroft-ai/customizations/stt-engine.md) for a list of options available.
* Dialog structure - a long sentence will always take more time to synthesize than a short one. For this reason Mycroft breaks up longer dialog into chunks and returns one to speak whilst the next is being generated. Skill developers can help provide quicker response times by considering the structure of their dialog and breaking that dialog up using punctuation in appropriate places.
* TTS Caching - synthesized audio is cached meaning common recently generated phrases don't need to be generated, they can be returned immediately.

## How can I create my own TTS voice?

The best answer is provided by [@Thorsten](https://twitter.com/ThorstenVoice) who documented their journey to create a custom TTS model in German.

{% embed url="https://youtu.be/m-Uwb-Bg144" %}

It is worth noting that it is a significant investment of time to train your own TTS model. We strongly recommend watching Thorsten's entire video before you get started. If a 1 hour video is too long, be warned that the process will take a minimum of weeks and more likely months.

There are exciting new projects that may soon enable us to generate new voices based off minutes of recorded audio. However currently it requires 16+ hours of very consistent, high-quality audio, with the associated text metadata.

To capture this training data we have the [Mimic Recording Studio](https://github.com/mycroftAI/mimic-recording-studio). Note that this generates audio files, which can be used to train TTS models using a range of technologies, not just Mycroft's Mimic.

## The Mycroft AI Store

### Do you cover VAT / GST / other import taxes?

No. Purchases from Mycroft do not currently include any taxes or other importation fees. Unless otherwise stated, all products are shipped from the USA. This means that a product being shipped to another country may incur additional taxes and import fees. These are the sole responsibility of the customer and Mycroft will not reimburse any costs associated with these local fees and taxes.
