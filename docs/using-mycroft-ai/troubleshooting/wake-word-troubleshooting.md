---
description: Having trouble triggering the wake word?
---

# Troubleshooting the Wake Word engine

> The microphone is working but Mycroft does not trigger when I say the Wake Word

To verify that it is the Wake Word and not the microphone causing the issue, we will get Mycroft to ask us a question that we can respond to.

In the Mycroft CLI type in an utterance like "set timer". Mycroft will then ask how long of a timer you would like, play the activation sound and turn on the microphone. Speaking now should result in your utterance being transcribed.

If your response is successfully transcribed, it is most likely the Wake Word engine causing the problem.

## Precise

### Check for AVX support on your device

Our Precise wake word engine also relies upon TensorFlow. For x86 Intel processors this requires the AVX (Advanced Vector Extensions) instruction set. To ensure your system supports AVX open a terminal and run:
```
grep avx /proc/cpuinfo
```

AVX should be listed under the flags for each CPU core. If nothing is returned it is most likely that your system does not support AVX.

The ARM architecture has a similar requirement called SIMD (Single Instruction, Multiple Data). This has been available since ARMv7 which includes the Cortex A53 used by the RaspberryPi and the Cortex A7 from the OrangePi.

#### Resolution

If your device does not have AVX or SIMD support then our Precise wake word engine will not work. Technical users may be able to build an older version of TensorFlow (1.13) from source using the instructions provided on their website that does not have this requirement.

You may still use Mycroft with the PocketSphinx wake word engine. See [Using a custom wake word](../customizations/wake-word.md) to see how to configure this.

### Check microphone input level

The Wake Word engine can have trouble detecting the specified term if the mic level is set too high.

#### Resolution
Reduce the mic level roughly 25-50% and attempt to speak again.

If you are on a laptop this can be done in your systems sound settings or volume control panel. Alternatively you can use `alsamixer` on the commandline.

We have a range of Alsamixer tips in the [Audio Troubleshooting Guide](audio-troubleshooting.md)

### Test Wake Word detection using another voice

Whilst we continue to improve our wake word models, it can still have trouble detecting the specified term from some voices.

If you think this might be the case, you can play a video from our [Youtube channel](https://www.youtube.com/channel/UC1dlmB1lup9RwFQBSGnhA-g) that uses the phrase "Hey Mycroft". Playing this through speakers near the connected microphone should trigger Mycroft.

#### Resolution

You may still be able to use Mycroft with the PocketSphinx wake word engine. See [Using a custom wake word](../customizations/wake-word.md) to see how to configure this.

## PocketSphinx

If you are using the PocketSphinx wake word engine, please see [Using a custom wake word](../customizations/wake-word.md) to examine the configuration options available.

PocketSphinx is an attractive option for a custom wake word as a new term. Whilst it is a simple text configuration, the result is less reliable than a well-trained Precise Wake Word.

## Further Information and Support

You're welcome to post questions and queries to the [Mycroft Forum](https://community.mycroft.ai/c/Help-with-Mycroft-related-issues) or join our [Wake Word channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/wake-word) to connect with others in the Community.
