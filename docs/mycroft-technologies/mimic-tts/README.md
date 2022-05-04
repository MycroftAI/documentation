---
description: Mimic is Mycroft AI's family of Text to Speech engines.
---

# Mimic TTS

![](../../.gitbook/assets/Mimic3-intro-banner\_v2.3.png)

Over the years, Mimic like other Mycroft components has gotten clearer, faster, and more flexible.

You can hear samples from all three Mimic systems below, speaking the same [sentence](https://clagnut.com/blog/2380/#English\_phonetic\_pangrams).

| Name                                                                                                                                          | Sample                                                                              | Local | Technology                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------- |
| <img src="https://mycroft.ai/wp-content/uploads/2017/02/mimic.png" alt="" data-size="line"> [Mimic 1](../mimic-overview/)                     | [Mimic 1 sample](https://mycroft.ai/wp-content/uploads/2022/04/mimic1\_pangram.wav) | Yes   | [Festival Lite (flite)](http://www.festvox.org/flite)                                                       |
| <img src="https://mycroft.ai/wp-content/uploads/2019/05/mimic2-logo.svg" alt="" data-size="line"> [Mimic 2](mimic-2.md)                       | [Mimic 2 sample](https://mycroft.ai/wp-content/uploads/2022/04/mimic2\_pangram.wav) | No    | [Tacotron](https://github.com/keithito/tacotron)                                                            |
| <img src="https://mycroft.ai/wp-content/uploads/2020/10/Mimic_color.png" alt="Mimic logo" data-size="line"> [Mimic 3](coming-soon-mimic-3.md) | [Mimic 3 sample](https://mycroft.ai/wp-content/uploads/2022/04/mimic3\_pangram.wav) | Yes   | [VITS: Conditional Variational Autoencoder with Adversarial Learning](https://github.com/jaywalnut310/vits) |

### COMING SOON: Mimic 3

Mimic 3 is a privacy-focused open-source neural Text to Speech (TTS) engine that can run faster than real-time on low-end devices like the Raspberry Pi 4. In human terms that means it sounds great, it can run completely offline or in the cloud, and you can verifiably trust it.

{% content-ref url="coming-soon-mimic-3.md" %}
[coming-soon-mimic-3.md](coming-soon-mimic-3.md)
{% endcontent-ref %}

### Mimic 2

Mimic 2 is our older machine learning TTS engine designed to run in the cloud. It has been the default voice for most installations of Mycroft for many years.

{% content-ref url="mimic-2.md" %}
[mimic-2.md](mimic-2.md)
{% endcontent-ref %}

### Mimic 1

Mimic 1 is a fast, light-weight TTS engine based on Carnegie Mellon University's FLITE software. It concatenates speech sounds to create complete phrases.

{% content-ref url="../mimic-overview/" %}
[mimic-overview](../mimic-overview/)
{% endcontent-ref %}

### Mimic Recording Studio

Mimic Recording Studio provides simplifies the collection of voice training data from individuals, by allowing you to speak and record phrases from a _corpus_. This data can then be used to train a voice model using Mimic 3, Mimic 2, or another machine learning TTS engine.

{% content-ref url="../mimic-overview/mimic-recording-studio.md" %}
[mimic-recording-studio.md](../mimic-overview/mimic-recording-studio.md)
{% endcontent-ref %}
