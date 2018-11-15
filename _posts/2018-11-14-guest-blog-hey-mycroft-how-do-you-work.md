---
ID: 40941
post_title: 'Guest Blog &#8211; Hey Mycroft, how do you work? &#8211; STT Systems for Voice'
author: Guest Blogger
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/guest-blog-hey-mycroft-how-do-you-work/
published: true
post_date: 2018-11-14 22:30:15
---
<span style="font-weight: 400;">"Hey Mycroft, how do you work?"</span>

<span style="font-weight: 400;">Sounds like a simple question for a voice assistant to answer, right? Well, yes and no. To paraphrase a potential source, </span><a href="https://en.wikipedia.org/wiki/Virtual_assistant" target="_blank" rel="noopener"><span style="font-weight: 400;">Wikipedia’s “Virtual Assistant"</span></a><span style="font-weight: 400;"> article:</span>
<blockquote><span style="font-weight: 400;">Voice assistants use natural language processing (NLP) to match user voice input to executable commands. Many continually learn using artificial intelligence techniques including machine learning. To activate, a wake word might be used. This is a word or groups of words such as "Alexa", "Hey Mycroft", or "OK Google".</span></blockquote>
<span style="font-weight: 400;">That isn’t a bad response, but it leaves out important points and a lot of detail.</span>

<span style="font-weight: 400;">For example, NLP as Wikipedia classifies it contains multiple essential modules of the voice stack, one of the most important being Speech Recognition. Without a speech to text engine (STT), an NLP intent parser couldn’t connect a request to an action. Every voice assistant needs robust STT.</span>
<h1><b>What is Speech Recognition?</b></h1>
<span style="font-weight: 400;">“Speech Recognition” is the ability of someone (or something) to conceive and understand speech from another source.</span>

<span style="font-weight: 400;">Humans may be intelligent, but can not be considered clever until some specific goals are achieved. When a baby is born, even though it can comprehend sounds, its brain will not be able to explain them. That being said, machines are just like babies. They won’t become intelligent until you spend time teaching them, and they can’t comprehend sound until they’re trained. That point drives us to our next section.</span>
<h1><b>How does Speech Recognition work?</b></h1>
<span style="font-weight: 400;">In order for a machine to begin comprehending sounds, an input is needed. All voice assistants (including Siri, Cortana, Alexa, and Google Assistant) get their prompts from a voice input device; a Bluetooth headset, a built-in microphone or anything of that sort. But the sound alone is going to do nothing.</span>

<span style="font-weight: 400;">One of the “classic” ways to develop Speech Recognition is detecting phonemes with </span><a href="https://en.wikipedia.org/wiki/Hidden_Markov_model" target="_blank" rel="noopener"><span style="font-weight: 400;">Hidden Markov Models</span></a><span style="font-weight: 400;"> (HMMs). When still at the early ages of Speech Recognition development, the software has to learn the structure and fundamental rules of a language.</span>
<h2><b>Hidden Markov Models</b></h2>
<span style="font-weight: 400;">HMM is widely used in this area due to its design. It is generally based on the principle of determining the most suitable or proper outcome after the previous one provided to it. Depending on which words come before and after each other in a sentence, HMMs output the best guess based on its training data and context.</span>

<span style="font-weight: 400;">When you say “Hey”, the voice assistant hears the phonemes “Hh-ey”. Then it searches its database to see what word(s) match those phonemes. If it finds a match for the input then it can produce the appropriate output thus answering your question.</span>

<span style="font-weight: 400;">But what if you wanted to say “hay” instead of “hey”. This is where context comes into play. Go on and unlock your smartphone, launch the voice assistant and say something. You’ll see that it takes a small though still existent period of time to produce the output. And sometimes, it may even guess a word before it is spoken later in the sentence. This process depends on what is known as the language model.</span>

<span style="font-weight: 400;">When people talk and someone says something irrelevant, then we’d say that what he said was “out of context”, and that’s exactly what the software tries to avoid. By processing the whole sentence you provide it, the software can transcribe speech better by checking if the possible outputs match sentences from the training that include keywords. So, by seeing whether you’re talking about horses or calling out to a human, HMM Speech Recognition can more accurately guess if you said “hey” or “hay.”</span>
<h3><b>Limitations and Availability</b></h3>
<span style="font-weight: 400;">Each language can be more difficult to comprehend than others, and could contain more phonemes and various other syntactical and grammar rules. Each language requires a specifically trained HMM to work properly.</span>

<span style="font-weight: 400;">These days, using pre-made application programming interfaces (also known as APIs) that get implemented in the software’s source code, the program instantly learns all about phonemes and language rules.</span>

<span style="font-weight: 400;">There are various APIs regarding STT, but some of the best ones are Google’s Speech API, Bing Speech API, and Speechmatics. Long-standing Open Source options are CMU Sphinx and Kaldi. Many developers do not have the knowledge and resources required to develop their own STT engine. Using use one of the pre-existing engines allows them to easily add an STT feature in their programs.    </span>
<h2><b>The Role of Machine Learning</b></h2>
<span style="font-weight: 400;">But the classics are meant to be improved upon. HMMs have given way to Machine Learning based models. </span><a href="https://github.com/mozilla/DeepSpeech" target="_blank" rel="noopener"><span style="font-weight: 400;">Mozilla’s DeepSpeech</span></a><span style="font-weight: 400;"> is one STT application using Machine Learning to transcribe human speech. This has allowed a steadily growing base of developers to create new applications with Speech Recognition features.</span>

<span style="font-weight: 400;">A common example used to describe machine learning is </span><a href="https://www.google.com/about/main/machine-learning-qa/" target="_blank" rel="noopener"><span style="font-weight: 400;">teaching a machine to tell cats and dogs apart</span></a><span style="font-weight: 400;">. If you just wait around for it to magically happen, it won’t. You have to apply some supervised learning (widely used term in the AI field).</span>

[caption id="attachment_41514" align="alignnone" width="1600"]<a href="https://selmandesign.com/qa-on-machine-learning/"><img class="wp-image-41514 size-full" src="https://mycroft.ai/wp-content/uploads/2018/10/cat-dog-ml.gif" alt="An artists rendering of the Machine Learning process by Selman Design." width="1600" height="900" /></a> Selman Design: https://selmandesign.com/qa-on-machine-learning/[/caption]

<span style="font-weight: 400;">To do that, you must gather some inputs; in this case, photos of cats or dogs. Then, by tagging what each picture shows you’d feed that collection to the software. This tagged dataset is fed into an ANN (Artificial Neural Network). These are computer models that operate just like our brains. In this example, the network is rewarded for correctly identifying cats in pictures it’s never seen before. Properly rewarding for correct identifications and adjusting for misses millions of times makes the model very good at its task. After millions or billions of training cycles, it should be able to identify whether the object in question is visible in a brand new photo unknown to it.</span>
<h3><b>Computers can “see” sound?</b></h3>
<span style="font-weight: 400;">How does visual pattern matching relate to STT? Actually, all this talk of computers ‘hearing’ is, in reality, a visual process. To transcribe speech, computers visualize the sound in </span><a href="https://en.wikipedia.org/wiki/Spectrogram" target="_blank" rel="noopener"><span style="font-weight: 400;">a spectrogram</span></a><span style="font-weight: 400;">. A spectrogram isolates different frequencies and indicates how long each sound wave’s energy lasted.  </span>

<a title="By Aquegg [Public domain], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Spectrogram-19thC.png"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c5/Spectrogram-19thC.png" alt="Spectrogram-19thC" width="512" /></a>

<span style="font-weight: 400;">The same image matching that can be done with cats and dogs can be done with speech spectrograms. Instead of tagged pictures, these networks are fed hundreds of hours worth of spectrograms with the corresponding transcriptions. It’s trained and tested on new recordings and is rewarded for each correct transcription.</span>

<span style="font-weight: 400;">These are currently called “end-to-end” STT models. End-to-end models have shown success in transcribing speech in multiple languages with one model, when trained on large enough datasets including those languages. This is the cutting edge of Speech Recognition and the basis of Mozilla DeepSpeech.</span>
<h1><b>Open Datasets</b></h1>
<span style="font-weight: 400;">This is why collecting data is so important to technology companies. The more voicemail transcripts, assistant requests, and other recordings a company can capture, the better they can build their STT. That is why most companies keep their data to themselves. Mycroft, however, mostly depends on </span><a href="https://en.wikipedia.org/wiki/Open_data" target="_blank" rel="noopener"><span style="font-weight: 400;">Open Datasets</span></a><span style="font-weight: 400;">, where everyone has access to the data. Anyone is able to contribute, edit, or even adopt an amount of the data to utilize it for his or her own project.</span>

<span style="font-weight: 400;">What most people fail to understand, however, is the amount of data that is required for speech to be recognized. You’ve seen cases where Siri, for example, has booked a date at a wrong time or booked the wrong hotel room. Mispronunciations or even a slight accent can lead the software to unintended actions. But having an Open Dataset can help with that. Diversity isn’t just another feature. It’s a mandatory requirement for success.</span>

<span style="font-weight: 400;">But there is a reliance on well-tagged datasets in machine learning. Remember Tay? The AI robot made by Microsoft was released to Twitter on its own without any supervision and after 24 hours it spewed racist and crude remarks due to the data Microsoft allowed it to ingest.</span>

<span style="font-weight: 400;">Spoil the system and the boomerang will turn back your way and strike you. Training datasets must be clean and well-tagged to be effective.</span>
<h2><b>What if you could improve the responses yourself?</b></h2>
<span style="font-weight: 400;">This is where Mycroft differs from the other players in the field. Being open source, everyone with access to the Internet can help make Mycroft better. The only thing standing between you and a better voice assistant is a thin wall you can easily demolish by creating an account. In order to do so, start at </span><a href="https://home.mycroft.ai/?utm_source=sttblog&amp;utm_medium=top" target="_blank" rel="noopener"><span style="font-weight: 400;">home.mycroft.ai</span></a><span style="font-weight: 400;">.</span>

<span style="font-weight: 400;">Once there, you can contribute to</span><a href="https://www.youtube.com/watch?v=UKXpXvdsI-w" target="_blank" rel="noopener"> <span style="font-weight: 400;">Mycroft’s Open Dataset just by Opting-In</span></a><span style="font-weight: 400;"> and using Mycroft. To go a step further, people can help make Mycroft better by tagging data - listening to various sentences and judging whether the software “heard” right or wrong. This helps in creating a diversity of clean inputs. Thus, with a lot of “practice” Mycroft could understand both a native English/American speaker and an Asian/African/European one with success.</span>

<span style="font-weight: 400;">That’s the reason Mycroft is doing so well at the moment and will continue to do even better than most other companies.</span>
<h2><b>How You Can Help Mycroft Improve</b></h2>
<span style="font-weight: 400;">There’s always space for improvement, and in this case, you can directly aid in making Mycroft better.</span>

Creating an account is very easy, just go <a href="https://home.mycroft.ai/?utm_source=sttblog&amp;utm_medium=bottom" target="_blank" rel="noopener">here</a><span style="font-weight: 400;">. Don’t worry, you don’t necessarily have to own a Mycroft device. You could always </span><a href="https://mycroft.ai/get-mycroft/" target="_blank" rel="noopener"><span style="font-weight: 400;">download</span></a><span style="font-weight: 400;"> and install Mycroft on your Linux computer or Raspberry Pi.</span>

<span style="font-weight: 400;">Then you will be able to access what I like to call a couple of mini-games. I say that because they are actually fairly entertaining. These are the </span><a href="https://home.mycroft.ai/#/precise" target="_blank" rel="noopener"><span style="font-weight: 400;">Precise tagger</span></a><span style="font-weight: 400;"> and the </span><a href="https://home.mycroft.ai/#/deepspeech" target="_blank" rel="noopener"><span style="font-weight: 400;">DeepSpeech tagger</span></a><span style="font-weight: 400;">.</span>

<span style="font-weight: 400;">In the Precise tagger, you’ll be helping Mycroft learn how to better identify whether a spoken phrase is “Hey Mycroft” or not. Pretty simple, right?</span>

<span style="font-weight: 400;">For the DeepSpeech tagger, you will get to hear a word or phrase and at the same time, you’ll be given a string of text. Your goal is to judge whether what you heard exactly matches the provided text. This doesn’t only help Mycroft, but it actually helps in building a dataset which will be shared with Mozilla for training the DeepSpeech STT engine.</span>

<span style="font-weight: 400;">Both mini-games will award you with points for every task so you can level up and get to the leaderboard. So not only are you helping a great cause but you can also get the satisfaction of being an important contributor.</span>
<h2><b>The Open Future of Voice Starts with You</b></h2>
<span style="font-weight: 400;">All this wouldn’t be possible if Mycroft’s platform wasn’t open source, meaning that everyone can help make it better. Apart from what we already mentioned, you could also write your own code or, in the case you are not a developer, simply download Picroft, Opt-In to the Open Dataset, and use Mycroft. You can find everything you need </span><a href="https://mycroft.ai/get-started/" target="_blank" rel="noopener"><span style="font-weight: 400;">here</span></a><span style="font-weight: 400;">!</span>

<span style="font-weight: 400;">So now that you know how the whole thing works, it is time to take things into your own hands. You can support Mycroft by investing to become a community partner. It doesn’t matter whether you are a developer or just another technology aficionado. Your actions count the same and together we can all help the world better. Even if you are not you could use Mark I or II.</span>

<span style="font-weight: 400;">The whole point of Mycroft is that technology should be accessible by everyone and respectively, everyone should aid in creating an open and safe future!</span>