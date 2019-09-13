# Precise

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

[//]: # "Note: Edit table using http://truben.no/table/"
[//]: # "============================ Table Start =================================="

|   | Open Source | Accurate | Languages | Model Trainer | Commercial Use | GitHub |
| - | ----------- | -------- | --------- | ------------- | -------------- | ------ |
| **Precise** | ![Yes][yes] | ![Yes][yes] | Python | [Open Source Script][precise-train] | Permitted | [MycroftAI/mycroft-precise][precise-github] |
| **Snowboy** | ![No][no] | ![Yes][yes] | Node, Java, Python, GO, Perl, iOS, Android | [Web API][snowboy-train] | [License Fee][snowboy-license] | [Kitt-AI/snowboy][snowboy-github] |
| **Porcupine** | ![No][no] | ![Yes][yes] | C, Python, Android | [Closed Binary][porcupine-train] | [License Fee][porcupine-license] | [Picovoice/Porcupine][porcupine-github] |
| **PocketSphinx** | ![Yes][yes] | ![No][no] | Almost all | [Open Source Script][pocketsphinx-train] | Permitted                                                                                                   | [cmusphinx/pocketsphinx][pocketsphinx-github] |

[//]: # "============================= Table End ==================================="

[open-source]: https://images2.imgbox.com/ef/76/SevHcNcX_o.png
[closed-source]: https://images2.imgbox.com/5b/24/h1uct6GA_o.png
[yes]: https://images2.imgbox.com/c7/63/UVtCmPfa_o.png
[no]: https://images2.imgbox.com/99/47/lm3vjOzO_o.png
[precise-train]: https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word
[precise-github]: https://github.com/MycroftAI/mycroft-precise

[snowboy-train]: http://docs.kitt.ai/snowboy/#restful-api
[snowboy-license]: https://github.com/Kitt-AI/snowboy/blob/master/README_commercial.md#evaluation-license-faq
[snowboy-github]: https://github.com/kitt-ai/snowboy

[porcupine-train]: https://github.com/Picovoice/Porcupine/tree/master/tools/optimizer
[porcupine-license]: https://github.com/Picovoice/Porcupine#license
[porcupine-github]: https://github.com/Picovoice/Porcupine

[pocketsphinx-train]: https://cmusphinx.github.io/wiki/tutorialam/
[pocketsphinx-github]: https://github.com/cmusphinx/pocketsphinx

## Adding Custom Wake Words

### PocketSphinx Wake Words

The simplest method to add a custom Wake Word to Mycroft is to use PocketSphinx. This is done by defining the phonemes that make up the Wake Word, so does not require any training.

First decide what your wake word will be and get the string of phonemes using the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict). Then add a `hotwords` block to your [`mycroft.conf` file](https://mycroft.ai/documentation/mycroft-conf/#changing-your-wake-word).

### Precise Wake Word Models
Training your own custom Wake Word model for Precise requires at least functional experience using the Linux commandline and an understanding of basic machine learning concepts. It requires time and training data.

An instructional overview is available on the [Precise repository on Github](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#how-to-train-your-own-wake-word). Community member El-tocino has also provided a short write up of their [tips for getting the best result](https://github.com/el-tocino/localcroft/blob/master/precise/Precise.md).

## Additional Support
If you have questions, you can reach out to others in the Community via the [Troubleshooting channel in Chat](https://chat.mycroft.ai/community/channels/troubleshooting).
