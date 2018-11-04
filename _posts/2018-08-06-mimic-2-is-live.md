---
ID: 39772
post_title: Mimic 2 is LIVE!
author: Michael Nguyen
post_excerpt: "Mycroft announces Version 2 Beta of Mycroft's Mimic Text to Speech engine. Version 2 is an entirely new architecture and sounds far more natural."
layout: post
permalink: http://mycroft.ai/blog/mimic-2-is-live/
published: true
post_date: 2018-08-06 06:50:14
---
<span style="font-weight: 400;">We are proud to release the beta of version 2 of Mycroft’s Mimic Text to Speech technology! Mimic is now a deep learning based Text-to-Speech (TTS) engine trained on audio recordings from a single speaker. Our team member <a href="https://www.linkedin.com/in/kusalwin/" target="_blank" rel="noopener">Kusal</a> kindly volunteered to provide the vocals for the first iteration. He spent several weeks speaking predetermined phrases into a microphone.</span>
<h1><span style="font-weight: 400;">Here are a few samples of the new Mimic generated voice in action:</span></h1>
&nbsp;
<h3>"The human voice is the most perfect instrument of all" - <strong>Arvo Part</strong></h3>
[audio wav="https://mycroft.ai/wp-content/uploads/2018/08/humanvoice.wav"][/audio]

&nbsp;
<h3>"This cake is great. It's so delicious and moist." - <strong>GlaDOS</strong></h3>
[audio wav="https://mycroft.ai/wp-content/uploads/2018/08/cakeisgreat.wav"][/audio]

&nbsp;
<h3>"I'm sorry, Dave. I'm afraid I can't do that." - <strong>HAL 9000</strong></h3>
[audio wav="https://mycroft.ai/wp-content/uploads/2018/08/sorrydave.wav"][/audio]

&nbsp;
<h1><span style="font-weight: 400;">For comparison, here is what a raw recording of Kusal’s voice sounds like:</span></h1>
<h3>"Good morning! Time to rise and shine."</h3>
[audio wav="https://mycroft.ai/wp-content/uploads/2018/08/recording.wav"][/audio]

&nbsp;

<span style="font-weight: 400;">Voice is a personal choice, and Mimic allows you to select or create a voice that fits your style and pre</span><span style="font-weight: 400;">ference. To start using this new voice, change the Voice option in your <a href="https://home.mycroft.ai/#/setting/basic" target="_blank" rel="noopener">Home settings</a> to American Male (Beta). That's it! Your devices will update to use the new voice after a minute. You can also tell Mycroft to “update your configuration.”</span>

Mimic2 will be on a 3 month trial and then will be a feature for <a href="https://mycroft.ai/product/mycroft-supporter/" target="_blank" rel="noopener">Mycroft Supporters</a>.

<span style="font-weight: 400;">Below is a technical explanation of Mimic. You can continue if you like to see what’s happening under the hood.</span>
<h2>What is the new architecture of Mimic?</h2>
<span style="font-weight: 400;">The </span><a href="https://github.com/MycroftAI/mimic2" target="_blank" rel="noopener"><span style="font-weight: 400;">Mimic2 repo</span></a><span style="font-weight: 400;"> is a fork from Keith Ito's </span><a href="https://github.com/keithito/tacotron" target="_blank" rel="noopener"><span style="font-weight: 400;">open source implementation</span></a><span style="font-weight: 400;"> of the </span><a href="https://ai.google/research/pubs/pub46150" target="_blank" rel="noopener"><span style="font-weight: 400;">Tacotron architecture</span></a><span style="font-weight: 400;"> published last year by Google Research. Keith was a huge help in getting us started, and we owe much of Mimic’s success to his excellent work.</span>

<span style="font-weight: 400;">Our initial implementation of Mimic used the concatenative approach, which relies on tiny audio recordings that are combined to form the speech. This process is labor intensive as it requires hardcoding different combinations of the audio clips to form words. The final output is clear but sounds emotionless and robotic.</span>

<span style="font-weight: 400;">The new Mimic uses deep learning, which generates higher quality speech than traditional concatenative Text-to-Speech systems. Using deep learning, we don't need to hand engineer the features in speech; instead, we let the computer learn how to generate it. With enough processing power and data, computers are capable of learning features like intonation, tone, stress, and rhythm. These features make speech sound more human-like.</span>
<h2>How it works</h2>
<span style="font-weight: 400;">Simply put, the Mimic engine takes in a string of text and maps it to an audio output. Mimic was trained on a corpus of about 20,000 English sentences that equates to about 16 hours of audio. During the recording process, Kusal had to speak clearly into a high-quality microphone in a noise isolated environment. We broke the recording sessions up into a span of two weeks to prevent vocal fatigue. The clarity and the quality of the data are critical, as with any machine learning system. Like they say:  "garbage in, garbage out."</span>

<span style="font-weight: 400;">This generation of Mimic is based on Tacotron, a groundbreaking and very successful neural network architecture for speech synthesis. It's able to take a highly compressed source of information (text) and decompress it into audio. This process is complicated because the same text can correspond to different sounds and speaking styles. Because of the various nuances in spoken language, it is difficult to generate the appropriate output sound from the input text. Try speaking these simple sentences out loud and pay attention to the different pronunciations of the same word:</span>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">I read a book last night; I like to read.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">The violinist took a bow after he dropped his bow.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">You have to use chopsticks to master their use.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">After you graduate you become a graduate.</span></li>
</ul>
<span style="font-weight: 400;">Below is a concise technical explanation of the deep learning approach. It's written with the goal of simplifying the various methods in the neural network architecture for understandability. If you'd like more in-depth details, you can read Google's </span><a href="https://arxiv.org/pdf/1703.10135.pdf" target="_blank" rel="noopener"><span style="font-weight: 400;">white paper</span></a><span style="font-weight: 400;"> on Tacotron.</span>
<h2>Generating Speech from Text</h2>
<span style="font-weight: 400;">As a high-level overview, the model takes in characters as input and outputs a raw spectrogram. An algorithm then transforms the raw spectrogram into audio waveforms. There are many neural network layers in this architecture that perform various functions. But for conciseness, the layers are grouped into 3 main modules; an Encoder, Decoder, and an Audio Reconstruction module.</span>

<img class="aligncenter wp-image-39780 size-full" src="https://mycroft.ai/wp-content/uploads/2018/08/mimic-2-diagram.png" alt="Technical diagram of Mycroft's Mimic2 Open Source Text to Speech" width="747" height="522" />
<p style="text-align: center;"><b>Diagram of </b><a href="https://github.com/MycroftAI/mimic2" target="_blank" rel="noopener"><b>Mimic V2</b></a><b> architecture</b></p>
<span style="font-weight: 400;">The voice generation starts with the Encoder. A sentence is broken up into individual characters as embeddings and fed into the Feature Extraction module. The Encoder uses this module to extract out local and contextual information from the characters. The process helps define the various patterns in a sentence to aid in producing the sound of the audio output. For example, the "C" in "Chat" is pronounced differently than the "C" in "Cat." Also, the intonation of a sentence would sound different if there is a question mark at the end versus a period. The output of the Feature Extraction module is essentially an abstract numerical data representation of the various features in a sentence. These encoded text features are used to help generate the sound.</span>

<span style="font-weight: 400;">After making a pass through the Encoder, the output of the Feature Extraction module is fed into the Decoder. The Decoder's job is to generate a mel spectrogram from the encoded text features. A spectrogram is a pictoral representation of sound. A mel spectrogram is a form of a spectrogram that represents sounds that are tuned to the human ear.</span><b></b>

<span style="font-weight: 400;">The Frame Prediction module (FPM), produces the raw mel spectrogram by recursively generating the frames. The information from the Encoder output is used to aid in the generation process. A method in the FPM called the Attention Mechanism helps align each character with its corresponding sound. As you can see in the diagram, the decoding process takes many repeated steps. The number of steps is dependent on the audio length. The Encoder output is fed into the FPM to start the decoding process.</span>
<p style="text-align: center;"><b><img class="size-full wp-image-39794 aligncenter" src="https://mycroft.ai/wp-content/uploads/2018/08/mel-spectrogram.png" alt="" width="1016" height="782" />Mel Spectrogram</b></p>
<span style="font-weight: 400;">The FPM produces two things: a mel spectrogram frame which contains information on what the generated audio sounds like; and an abstract numerical data representation of the state of the FPM, which we'll call the internal state. The internal state contains information that is critical to generating the next frame. The internal state holds information like the text representation from the Encoder and the data from the previous decoding steps. These outputs are necessary because to generate the next sound in speech; it's beneficial to know prior sounds generated and the information that generated those sounds. In reality, the FPM module is a lot more complicated, but we'll stick to this explanation for the sake of simplicity. The FPM combines those two outputs, passes it on into the next decoding step, then does its job again. The Decoder repeats this process, building out the mel spectrogram frame by frame. Each step is taking in information from the previous step. After the final mel spectrogram output, the whole sentence is represented in speech form.</span>

<span style="font-weight: 400;">The final step in the speech generation process is the Audio Reconstruction module. This module has two main components, the post-processing net, and the Griffin-Lim algorithm. The full mel spectrogram generated from the Decoder is fed into the post-processing net. The network transforms the mel spectrogram into a linear spectrogram. This step is crucial for two reasons. First, the output needs to be converted from a mel spectrogram to a linear spectrogram before it can be reconstructed. Second, during the decoding process, the FPM makes mistakes in generating the mel spectrogram frames. The post-processing net can learn to correct these mistakes. Once the post-processing net generates the linear spectrogram, the Griffin-Lim algorithm is applied to it. Griffin-Lim is a reconstruction algorithm that can take linear spectrograms and turn it into audio waveforms. The linear spectrogram does not contain information on the phase, which is any particular point in time of a waveform. Griffin-Lim estimates the phases in a waveform from the spectrogram, but it’s not perfect. Thus each output waveform has some form of phase distortion. Phase distortion is why the voice can sound as if it’s omnipotent.</span>
<h2>What's next?</h2>
<span style="font-weight: 400;">That's it! That's a simplified version of how Mimic takes in text and transforms it to audible speech. Mimic Text to Speech is in ongoing development, as it is not indistinguishable from a human yet. A few community members have asked about the possibility of using </span><a href="https://ai.googleblog.com/2017/12/tacotron-2-generating-human-like-speech.html" target="_blank" rel="noopener"><span style="font-weight: 400;">Tacotron2</span></a><span style="font-weight: 400;">, Google's shiniest TTS architecture. Architecturally, some argue Tacotron2 is more straightforward then Tacotron, but the most significant difference is the use of WaveNet in the Audio Reconstruction module. WaveNet produces exceptionally human-like speech quality, but the tradeoff is that the compute time is not practical. We've tried WaveNet on a Tesla K80 which Google Colab provides, and it took 13 minutes to generate 0.9 seconds of audio. While it sounds excellent, this is not practical for today. Other implementations hold some promise, such as </span><a href="https://github.com/tomlepaine/fast-wavenet" target="_blank" rel="noopener"><span style="font-weight: 400;">Fast Wavenet</span></a><span style="font-weight: 400;">. We will continue to develop and share our open source Mimic implementation while watching out for new developments that we can incorporate from this rapidly progressing space.</span>