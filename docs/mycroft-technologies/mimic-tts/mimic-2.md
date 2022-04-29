---
description: >-
  Mimic II is a machine learning Text-to-Speech engine designed to run in the
  cloud.
---

# Mimic 2

Mimic 2 uses deep learning, generating higher quality speech than traditional concatenative Text-to-Speech systems. Using deep learning, we don’t need to hand engineer the features in speech; instead, we let the computer learn how to generate it. With enough processing power and data, computers are capable of learning features like intonation, tone, stress, and rhythm. These features make speech sound more human-like.

### How it works

Simply put, the Mimic 2 engine takes in a string of text and maps it to an audio output. Mimic 2 was trained on a corpus of about 20,000 English sentences that equates to about 16 hours of audio. During the recording process, Kusal had to speak clearly into a high-quality microphone in a noise isolated environment. We broke the recording sessions up into a span of two weeks to prevent vocal fatigue. The clarity and the quality of the data are critical, as with any machine learning system. Like they say:  “garbage in, garbage out.”

This generation of Mimic is based on Tacotron, a groundbreaking and very successful neural network architecture for speech synthesis. It’s able to take a highly compressed source of information (text) and decompress it into audio. This process is complicated because the same text can correspond to different sounds and speaking styles. Because of the various nuances in spoken language, it is difficult to generate the appropriate output sound from the input text. Try speaking these simple sentences out loud and pay attention to the different pronunciations of the same word:

* I read a book last night; I like to read.
* The violinist took a bow after he dropped his bow.
* You have to use chopsticks to master their use.
* After you graduate you become a graduate.

Below is a concise technical explanation of the deep learning approach. It’s written with the goal of simplifying the various methods in the neural network architecture for understandability. If you’d like more in-depth details, you can read Google’s [white paper](https://arxiv.org/pdf/1703.10135.pdf) on Tacotron.

### Generating Speech from Text

As a high-level overview, the model takes in characters as input and outputs a raw spectrogram. An algorithm then transforms the raw spectrogram into audio waveforms. There are many neural network layers in this architecture that perform various functions. But for conciseness, the layers are grouped into 3 main modules; an Encoder, Decoder, and an Audio Reconstruction module.

![Technical diagram of Mycroft's Mimic2 Open Source Text to Speech](https://mycroft.ai/wp-content/uploads/2018/08/mimic-2-diagram.png)

**Diagram of** [**Mimic V2**](https://github.com/MycroftAI/mimic2) **architecture**

The voice generation starts with the Encoder. A sentence is broken up into individual characters as embeddings and fed into the Feature Extraction module. The Encoder uses this module to extract out local and contextual information from the characters. The process helps define the various patterns in a sentence to aid in producing the sound of the audio output. For example, the “C” in “Chat” is pronounced differently than the “C” in “Cat.” Also, the intonation of a sentence would sound different if there is a question mark at the end versus a period. The output of the Feature Extraction module is essentially an abstract numerical data representation of the various features in a sentence. These encoded text features are used to help generate the sound.

After making a pass through the Encoder, the output of the Feature Extraction module is fed into the Decoder. The Decoder’s job is to generate a mel spectrogram from the encoded text features. A spectrogram is a pictoral representation of sound. A mel spectrogram is a form of a spectrogram that represents sounds that are tuned to the human ear.

The Frame Prediction module (FPM), produces the raw mel spectrogram by recursively generating the frames. The information from the Encoder output is used to aid in the generation process. A method in the FPM called the Attention Mechanism helps align each character with its corresponding sound. As you can see in the diagram, the decoding process takes many repeated steps. The number of steps is dependent on the audio length. The Encoder output is fed into the FPM to start the decoding process.

![](https://mycroft.ai/wp-content/uploads/2018/08/mel-spectrogram.png)**Mel Spectrogram**

The FPM produces two things: a mel spectrogram frame which contains information on what the generated audio sounds like; and an abstract numerical data representation of the state of the FPM, which we’ll call the internal state. The internal state contains information that is critical to generating the next frame. The internal state holds information like the text representation from the Encoder and the data from the previous decoding steps. These outputs are necessary because to generate the next sound in speech; it’s beneficial to know prior sounds generated and the information that generated those sounds. In reality, the FPM module is a lot more complicated, but we’ll stick to this explanation for the sake of simplicity. The FPM combines those two outputs, passes it on into the next decoding step, then does its job again. The Decoder repeats this process, building out the mel spectrogram frame by frame. Each step is taking in information from the previous step. After the final mel spectrogram output, the whole sentence is represented in speech form.

The final step in the speech generation process is the Audio Reconstruction module. This module has two main components, the post-processing net, and the Griffin-Lim algorithm. The full mel spectrogram generated from the Decoder is fed into the post-processing net. The network transforms the mel spectrogram into a linear spectrogram. This step is crucial for two reasons. First, the output needs to be converted from a mel spectrogram to a linear spectrogram before it can be reconstructed. Second, during the decoding process, the FPM makes mistakes in generating the mel spectrogram frames. The post-processing net can learn to correct these mistakes. Once the post-processing net generates the linear spectrogram, the Griffin-Lim algorithm is applied to it. Griffin-Lim is a reconstruction algorithm that can take linear spectrograms and turn it into audio waveforms. The linear spectrogram does not contain information on the phase, which is any particular point in time of a waveform. Griffin-Lim estimates the phases in a waveform from the spectrogram, but it’s not perfect. Thus each output waveform has some form of phase distortion. Phase distortion is why the voice can sound as if it’s omnipotent.
