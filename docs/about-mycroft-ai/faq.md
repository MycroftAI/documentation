---
description: Questions that we frequently receive about Mycroft and our technologies.
---

# FAQ

## Can I self-host everything?

As a privacy focused project and community, many people are interested in fully self-hosted options. Mycroft has intentionally been built in a modular fashion, so this is possible however is not easy and is unlikely to provide an equivalent user experience. 

To achieve this we need to look at three key technologies: backend services provided by [Home.mycroft.ai](https://home.mycroft.ai); speech recognition or speech-to-text \(STT\); and speech-synthesis or text-to-speech \(TTS\). For backend services, the [official backend known as Selene is available on Github](https://github.com/MycroftAI?utf8=%E2%9C%93&q=Selene&type=&language=) under the AGPL v3.0 license, alternatively you can use the simpler Community developed [Personal Backend](https://github.com/MycroftAI/personal-backend). You can choose to run your own STT service such as [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech/releases) or [Kaldi](https://kaldi-asr.org/), however in our opinion these do not yet provide sufficient accuracy for mainstream usage. Finally, to generate speech on device, simply select the British Male voice. The more realistic sounding voices are generated on Mycroft servers and require significant hardware to synthesize speech within a reasonable time frame. 

If you are running your own services, your Mycroft installation can be directed to use those using the [mycroft.conf file](../using-mycroft-ai/customizations/mycroft-conf.md). 





