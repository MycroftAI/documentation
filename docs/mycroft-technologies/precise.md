---
description: >-
  Precise is a Wake Word Listener based on a neural network trained on sound
  samples.
---

# Precise

Like its name suggests, a Wake Word Listener's job is to continually listen to sounds and speech around the Device, and activate when the sounds or speech match a Wake Word. Unlike other hotword detection products, Mycroft Precise is fully open source.

## Precise vs PocketSphinx

Precise has been the default **Wake Word Listener** for each Mycroft Device since mid-March 2018. Precise is based on a neural network that is trained on _sound patterns_ rather than _word patterns_. This reduces the dependence it has on particular languages or accents.

[PocketSphinx](https://github.com/cmusphinx/pocketsphinx) is an alternative to Precise. Unlike Precise, PocketSphinx recognizes **Wake Words** based on the [CMU Flite dictionary of sounds](http://www.speech.cs.cmu.edu/cgi-bin/cmudict).

### How do I change the **Wake Word Listener** to PocketSphinx

To change the **Wake Word Listener** to PocketSphinx if it has been set to Precise, Speak:

> Hey Mycroft, set the Listener to default

or

> Hey Mycroft, set the listener to PocketSphinx

Mycroft will respond

`"I've set the Listener to PocketSphinx"`

To return to Precise, speak:

> Hey Mycroft, set the Listener to Precise

Mycroft will respond

`"I've set the Listener to Precise"`

### How do I tell which **Wake Word Listener** my Mycroft **Device** is using?

To find out which **Wake Word Listener** is active for the Mycroft **Device** you are using, simply Speak:

> Hey Mycroft, what is the Listener?

or

> Hey Mycroft, tell me what Listener you are using

If you are using Precise, Mycroft will respond:

`"The current Listener is Precise"`

### How do I install Precise as my **Wake Word Listener**?

If Precise is not already installed, speak to your **Device**:

> `Hey Mycroft, set the Listener to Precise`

Mycroft will respond

`"Downloading the new listener, this will take a bit and you won't be able to use me until it completes. Give me a minute before attempting to activate me again."`

_NOTE: As Precise is installing, it will download a 40Mb file to your **Device**. During this initial download period, your **Device** will not be able to respond to a **Wake Word**._

## Other hotword detection technologies

Unlike other accurate hotword detection products, Mycroft Precise is fully open source.

|  | Open Source | Accurate | Languages | Model Trainer | Commercial Use | GitHub |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Precise** | ![](https://images2.imgbox.com/c7/63/UVtCmPfa_o.png) | ![](https://images2.imgbox.com/c7/63/UVtCmPfa_o.png) | Python | [Open Source Script](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word) | Permitted | [MycroftAI/mycroft-precise](https://github.com/MycroftAI/mycroft-precise) |
| **Snowboy** | ![](https://images2.imgbox.com/99/47/lm3vjOzO_o.png) | ![](https://images2.imgbox.com/c7/63/UVtCmPfa_o.png) | Node, Java, Python, GO, Perl, iOS, Android | [Web API](http://docs.kitt.ai/snowboy/#restful-api) | [License Fee](https://github.com/Kitt-AI/snowboy/blob/master/README_commercial.md#evaluation-license-faq) | [Kitt-AI/snowboy](https://github.com/kitt-ai/snowboy) |
| **Porcupine** | ![](https://images2.imgbox.com/99/47/lm3vjOzO_o.png) | ![](https://images2.imgbox.com/c7/63/UVtCmPfa_o.png) | C, Python, Android | [Closed Binary](https://github.com/Picovoice/Porcupine/tree/master/tools/optimizer) | [License Fee](https://github.com/Picovoice/Porcupine#license) | [Picovoice/Porcupine](https://github.com/Picovoice/Porcupine) |
| **PocketSphinx** | ![](https://images2.imgbox.com/c7/63/UVtCmPfa_o.png) | ![](https://images2.imgbox.com/99/47/lm3vjOzO_o.png) | Almost all | [Open Source Script](https://cmusphinx.github.io/wiki/tutorialam/) | Permitted | [cmusphinx/pocketsphinx](https://github.com/cmusphinx/pocketsphinx) |

## Adding Custom Wake Words

### PocketSphinx Wake Words

The simplest method to add a custom Wake Word to Mycroft is to use PocketSphinx. This is done by defining the phonemes that make up the Wake Word, so does not require any training.

First decide what your wake word will be and get the string of phonemes using the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict). Then add a `hotwords` block to your [`mycroft.conf` file](../using-mycroft-ai/customizations/mycroft-conf.md).

### Precise Wake Word Models

Training your own custom Wake Word model for Precise requires at least functional experience using the Linux commandline and an understanding of basic machine learning concepts. It requires time and training data.

An instructional overview is available on the [Precise repository on Github](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#how-to-train-your-own-wake-word). Community member El-tocino has also provided a short write up of their [tips for getting the best result](https://github.com/el-tocino/localcroft/blob/master/precise/Precise.md).

## Additional Support

If you have questions, you can reach out to others in the Community via the [Troubleshooting channel in Chat](https://chat.mycroft.ai/community/channels/troubleshooting).

