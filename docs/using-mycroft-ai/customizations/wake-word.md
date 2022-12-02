---
description: >-
  You might want to change the Wake Word to a phrase that's easier for you to
  speak, is more culturally appropriate, or just more personal and fun for you.
---

# Using a Custom Wake Word

Like its name suggests, a Wake Word Listener's job is to continually listen to sounds and speech around the Device, and activate when the sounds or speech match a Wake Word.

Mycroft provides an open source Wake Word Listener called Precise. However we also provide native support for PocketSphinx, and other technologies can be added and utilized. Here we will look at how to use custom Wake Words using Precise and PocketSphinx.

At a high-level Precise provides more accurate and reliable results, but requires the collection of voice samples and some experience in machine learning to train a new Wake Word. PocketSphinx on the other hand can be used to quickly configure any new Wake Word through a text configuration file, but provides less reliable results.

## Precise

Precise is the default Wake Word Listener and handles detection of "Hey Mycroft" for the majority of Mycroft Users.

Precise is based on a neural network that is trained on _sound patterns_ rather than _word patterns_. This reduces the dependence it has on particular languages or accents.

### Available Wake Word Models

Models produced by the Mycroft team are available at:

{% embed url="https://github.com/MycroftAI/precise-data/tree/models" %}

The Mycroft Community have started a repository of Precise training data and pre-trained models that can be used:

{% embed url="https://github.com/MycroftAI/precise-community-data" %}

### Training a Wake Word Model

Training your own custom Wake Word model for Precise requires at least functional experience using the Linux commandline and an understanding of basic machine learning concepts. It requires time and training data.

An instructional overview is available on the [Precise repository on Github](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#how-to-train-your-own-wake-word). Community member El-tocino has also provided a short write up of their [tips for getting the best result](https://github.com/el-tocino/localcroft/blob/master/precise/Precise.md).

### Configuring Your Precise Wake Word

For this example we shall use a pre-trained model named `computer-en`. Each model consists of two files:

* `computer-en.pb` - the model itself; and
* `computer-en.pb.params` - a small configuration file containing the parameters for that model.

The two files must be consistently named as they are in the example above. They must also be stored in the same directory, however it does not matter where on the file system this directory is as we will point Mycroft to them. By default Mycroft stores these in your home directory at `~/.mycroft/precise`. Multiple models can be on your system at any given time so we can leave any existing model files there.

Once you have your Wake Word model, you must tell Mycroft which model you want to use in your [`mycroft.conf`](mycroft-conf.md) file. This is best done using the [Configuration Manager](config-manager.md). To edit your User level configuration run:

```bash
mycroft-config edit user
```

We will then define our Wake Word and any attributes we want to give it. Each hotword is declared as it's own block under the `hotwords` key. The name of this block defines the name of the Wake Word. For this example, we will call our Wake Word `computer`. Each Precise Wake Word settings block must include at least the Wake Word `module` being used (in our case `precise`), and the location of the model files on the device.

```javascript
"hotwords": {
  "computer": {
      "module": "precise",
      "local_model_file": "/home/pi/.mycroft/precise/computer-en.pb",
  }
}
```

Multiple Wake Words can be declared in this fashion, but only one can be active at any time.

To define which Wake Word will be active, under `listener` we must add a `wake_word` attribute and provide it the name of our Wake Word. In our example it would be:

```javascript
"listener": {
  "wake_word": "computer"
}
```

#### Optional Attributes

There are two optional attributes for Precise Wake Words:

* `sensitivity` (default 0.5)
* `trigger_level` (default 3)

The sensitivity value is a float and ranges between 0.0 - 1.0 with sensitivity increasing as the value increases. A value of 0.1 will minimize false positives while a value of 0.9 will recognize almost anything. The default value is 0.5.

The trigger level relates to consecutive positive samples and is an integer between 1 - infinity with practical values ranging betwen 1 and 10. The higher the value the less likely Mycroft is to activate unintentionally. However high values will make it less likely to intentionally activate Mycroft. The default value is 3.

#### Example Configuration

Putting the example above together in an otherwise unmodified User level `mycroft.conf`, would be:

```javascript
{
  "max_allowed_core_version": 20.8,
  "listener": {
    "wake_word": "computer"
  },
  "hotwords": {
    "computer": {
        "module": "precise",
        "local_model_file": "/home/user/.mycroft/precise/computer-en.pb",
        "sensitivity": 0.1,
        "trigger_level": 7
    }
  }
}
```

{% hint style="info" %}
Remember in the example above, there must be two files for the model to operate:

* `/home/user/.mycroft/precise/computer-en.pb`
* `/home/user/.mycroft/precise/computer-en.pb.params`
{% endhint %}

## PocketSphinx

The simplest method to add a custom Wake Word to Mycroft is to use PocketSphinx. This is done by defining the phonemes that make up the Wake Word. It does not require any training, however is less reliable than a well-trained Precise Wake Word.

First decide what your wake word or phrase will be. For the purposes of this example, we're going to use the phrase:

> Yo Mike

### Getting Phonemes

We need to identify the phoneme sounds for this Wake Word. This can be done using the [CMU Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict). For our example `Yo Mike`, we get

> Y OW . M AY K .

#### About Phonemes

Phonemes are basic units of sound. They are a way to represent the different sounds in speech in a standard way. English spelling varies so much that it cannot be used for this purpose. For example, the "j" sound in "juice" is the same as the "g" sound in "giant".

You can see the similarity when these words are written as phonemes:

* `JH UW S .` = juice
* `JH AY AH N T .` = giant

The period (or full stop) indicates the end of a word.

### Other Settings

Other settings are available to further tune how sensitive the Speech to Text (STT) engine is in recognizing the Wake Word. These are added to the `listener` block of your `mycroft.conf`.

*   **Sample rate (Hz)**

    The rate at which the audio stream is sampled. The default is 16KHz. You shouldn't need to change this, unless the microphone you are using needs a much higher or lower sample rate.
*   **Channels**

    The audio channel that should be sampled for the Wake Word. The default is 1, and you shouldn't have to change this unless your microphone is not operating on audio channel 1.
*   **Wake Word**

    In plain English text, the Wake Word that Mycroft should listen for.
*   **Phonemes**

    The phonemes corresponding to the Wake Word. If your Wake Word phrase is more than one word, remember to include a period (.) at the end of each phoneme.
*   **Threshold (scientific notation)**

    The level of sensitivity at which the Wake Word should trigger Mycroft to respond. To _increase_ the sensitivity, _reduce_ the Threshold. The Threshold is given in [scientific notation](https://en.wikipedia.org/wiki/Scientific\_notation). Use this [handy converter](http://www.easysurf.cc/scintd.htm) to convert between decimal and scientific notation.
*   **Threshold multiplier (float)**

    This multiplier acts on the Threshold, and may be an easier way to make adjustments rather than scientific notation.
*   **Dynamic Energy Ratio (float)**

    Dynamic Energy Ratio (DER) is one signal feature used in [speech recognition](https://en.wikipedia.org/wiki/Speech\_recognition) to identify characteristics of audio, such as whether a person has stopped or started speaking. DER is similar to signal-to-noise-ratio. A high ratio indicates a high difference in signal between speech and no speech, and a low ratio indicates a small difference in signal between speech and no speech.

    If Mycroft is being _too sensitive_, reduce this value. If Mycroft _is not being sensitive enough_, increase this value.

```javascript
{
  "listener": {
    "multiplier": 1.0,
    "energy_ratio": 1.5
  }
}
```

#### Adding PocketSphinx Settings to `mycroft.conf`

For the `Yo Mike` example we started with, an example `~/.mycroft/mycroft.conf` file might look like:

```javascript
{
  "max_allowed_core_version": 19.2,
  "listener": {
    "wake_word": "yo mike"
  },
  "hotwords": {
    "yo mike": {
      "module": "pocketsphinx",
      "phonemes": "Y OW . M AY K .",
      "threshold": 1e-18
    }
  }
}
```

{% hint style="danger" %}
Warning: By default, Mycroft only provides an English language model for PocketSphinx. \
You will get an error attempting to use PocketSphinx if you have set your language attribute to anything other than "en-us".
{% endhint %}

## Applying new settings

Mycroft doesn't automatically apply new settings when the `mycroft.conf` file is modified. You must restart Mycroft by rebooting the device, or using the command:

```bash
mycroft-config reload
```

## Switching Wake Word Listeners

As per the [Technology Overview](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/overview#wake-word-detection), there are two available listeners: 1. Precise (default) 2. PocketSphinx

Precise is likely appropriate for most users, however on legacy hardware PocketSphinx may be desired.

{% hint style="info" %}
**Troubleshooting a broken listener?**\
You can type the speak command into the CLI (`./start-mycroft.sh cli` or `mycroft-cli-client`).
{% endhint %}

To change the Wake Word Listener to PocketSphinx, speak:

> Hey Mycroft, set the listener to PocketSphinx

Mycroft will respond

`"I've set the Listener to PocketSphinx"`

To return to Precise, speak:

> Hey Mycroft, set the Listener to default

or

> Hey Mycroft, set the Listener to Precise

Mycroft will respond

`"I've set the Listener to Precise"`

### How do I tell which Wake Word Listener my Mycroft Device is using?

To find out which Wake Word Listener is active for the Mycroft Device you are using, simply Speak:

> Hey Mycroft, what is the Listener?

or

> Hey Mycroft, tell me what Listener you are using

If you are using Precise, Mycroft will respond:

`"The current Listener is Precise"`
