---
ID: 38197
post_title: Languages are Hard
author: Kathy Reid
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/languages-are-hard/
published: true
post_date: 2018-05-24 13:00:30
---
<h2>Comprenez vous? ¿Entiende usted?
Voce entende? Apakah anda mengerti?’</h2>
Voice interfaces hold so much promise because of their ease of use.  But a truly intelligent voice agent should be able to listen and speak to you in your own language, right?  Many are excited about the possibility of using the Mycroft open voice assistant with their native tongue.

Currently, Mycroft only officially works in English, with Community-driven efforts underway to support French, German, Italian, Portuguese, Spanish and Swedish.  The exciting thing about the open source, Community-based approach of Mycroft is that translation can be done by more than just the individuals writing Skills. The users are empowered to band together and start support for their own language!

We’ve made a start by providing some <a href="https://mycroft.ai/documentation/language-support/adding-language/" target="_blank" rel="noopener">initial documentation if you want to experiment with language support</a>.  Here, we break down how foreign language support must be implemented at each layer of the Voice Stack, and provide an overview of our language support roadmap.
<h2>How do languages need to be supported across the voice stack?</h2>
In order for foreign language support to be useful, it needs to work across the entire <em>Voice Stack</em>. The voice stack is the combination of software components which, just like a layer cake, stack together to provide a voice service. Let’s take a look at them:
<h3>Wake Word</h3>
The <em>Wake Word</em> is the layer that tells the voice assistant to ‘wake up and start listening for commands’. It’s sometimes called a <em>hot word</em>. By default, the Wake Word on Mycroft Devices is ‘Hey Mycroft‘. Initially Mycroft used PocketSphinx for Wake Words, <a href="https://github.com/MycroftAI/mycroft-core/releases/tag/release%2Fv0.9.5" target="_blank" rel="noopener">but moved to the Precise Wake Word engine last fall</a>.

PocketSphinx and Precise work in different ways.  PocketSphinx maps <a href="https://cmusphinx.github.io/wiki/tutorialdict/" target="_blank" rel="noopener">phonemes</a> - think of these as sound building blocks - to graphemes. Graphemes are word building blocks. This way, PocketSphinx knows that the phoneme sequence <code>HH EY M AY K R O F T</code> matches the words “Hey Mycroft”. To learn more about the differences between phonemes and graphemes, <a href="http://www.readingdoctor.com.au/phonemes-graphemes-letters-word-burger/" target="_blank" rel="noopener">this blog post is a great start</a>.

In contrast, <a href="https://mycroft.ai/documentation/precise/" target="_blank" rel="noopener">Precise</a> works using a <a href="https://en.wikipedia.org/wiki/Artificial_neural_network" target="_blank" rel="noopener">neural network</a>. Learning from tagged samples of Mycroft users who have opted-in to our open dataset, Precise is able to build an accurate model of the <code>Hey Mycroft</code> Wake Word. Building a model using samples from a wide variety of genders, accents and tones means that a man with a French accent saying <code>Hey Mycroft</code> will be recognized as well as an Australian woman, even though the phoneme sounds in these languages differ significantly. The downside of this approach, of course, is that the model needs a large, diverse dataset for training.

If you wish to use a Wake Word in a language other than English at the moment, you really have two choices; each has benefits and drawbacks. You can set a custom Wake Word in your <a href="https://home.mycroft.ai/" target="_blank" rel="noopener">home.mycroft.ai</a> account using the phonemes available in the English PocketSphinx dictionary. You won’t be able to use phonemes that don’t occur in English - for example the “<em>sch</em>” sound in German, or the “<em>xo</em>” sound in Catalan. If you want to use non-English phonemes, you will need to install a PocketSphinx dictionary in your chosen language; which is not for the faint-hearted and requires advanced Linux skills.
<h3>Speech to Text</h3>
The Speech to Text (STT) layer is the part of the Voice Stack that transcribes what you say to the Mycroft device. Currently, Mycroft defaults to the excellent STT engine from Google, but anonymizes all the requests so any traffic is just seen by Google as ‘Mycroft’. <a href="https://cloud.google.com/speech-to-text/docs/languages" target="_blank" rel="noopener"> Google STT supports several languages other than English</a>, so if you speak a supported language <a href="https://mycroft.ai/documentation/mycroft-conf/" target="_blank" rel="noopener">you can edit your mycroft.conf file to try it</a>.

We intend to move to DeepSpeech as our default STT layer in the future, and you can <a href="https://mycroft.ai/blog/deepspeech-update/#trying-thing-out" target="_blank" rel="noopener">try DeepSpeech on Mycroft</a> now. This offers many more options, including the potential to host DeepSpeech on your own server and, potentially, directly on your device.  However this is still young technology -- currently version 0.3 -- and the only trained model is currently English. <a href="https://github.com/mozilla/DeepSpeech/issues/692" target="_blank" rel="noopener">We are working with Mozilla to expand its language range in the future</a> and to generalize the process to support every language!
<h3>Intent Parser</h3>
Once the Speech to Text layer has turned spoken words into text we call it an <em>Utterance</em>. The Utterance is then run through our Intent Parsers layer. The role of an <em>Intent Parser</em> within the Voice Stack is to match an  Utterance with the intended action in a specific <em>Skill</em> - that is, find the “Intent” of the user.

In the Mycroft Voice Stack, there are two different Intent parsing phases:
<ul>
 	<li><a href="https://mycroft.ai/documentation/adapt/" target="_blank" rel="noopener"><strong>Adapt</strong></a>: Keywords from the <code>vocab</code> files and patterns from the <code>regex</code> files of the Skills are combined into Intent rules and used to find text matches.   This will generate a confidence score for any matching Intent. Flow of control is passed to the Skill with the highest Intent confidence score.</li>
</ul>
If Adapt can’t parse the Intent…
<ul>
 	<li><a href="https://mycroft.ai/documentation/padatious/" target="_blank" rel="noopener"><strong>Padatious</strong></a>: A neural network determines the confidence score based on Intent examples provided by Skills. Flow of control is still passed to the Skill with the highest Intent confidence score.</li>
</ul>
If neither Intent Parser finds a match, the flow of control is passed to a <em>Fallback Skill</em> like Wolfram|Alpha to handle the Utterance.

Before the Utterance is run through the intent parsers, a language-specific <em>normalization</em> occurs.  Normalization cleans up the transcription, doing things like converting contractions to their expanded form (e.g. “What’s the weather like” becomes “What is the weather like”).  This code must be added to <code>mycroft-core</code> itself for each new language. For example, normalization in Portuguese, which distinguishes between masculine and feminine forms of a word, would need to account for both masculine and feminine phrases.
<h3>Skills</h3>
In the Voice Stack, the role of the Skill is to do the ‘heavy lifting’ and provide the user with the outcome they wanted - such as reporting the news or weather, or playing a piece of music.

The Mycroft skills system has supported multiple languages from the beginning.  To support a new language, each Skill must translate three different pieces:
<h4>Vocabulary</h4>
Independent directories within the Skill hold vocab for the various language codes.  For example, a skill written originally in English will have several files like <code>vocab\en-us\Word.voc</code>, with the English language pieces in the <code>*.voc</code> files.  Adding German support involves creating <code>vocab\de-de\Word.voc</code> files holding the German version of the same words.

A Skill might also use regular expressions in parsing, contained in its<code>*.rx</code> files.  For a <code>regex</code> pattern match not only do these words differ between languages, but also the phrasing and placement of words changes.

For example, let’s take the phrase “How’s the weather today”. In most European languages, the phrasing follows the structure “question - keyword - day”. However, in Turkish, note the two phrases:
<ul>
 	<li><code>“Bugün hava nasıl?”</code> - “How’s the weather today?” (Literally, “Today, how’s the weather?”)
<code>“Hava nasıl?”</code> - “How’s the weather?”</li>
</ul>
The structure is “day - question - keyword”. This means that not only would regex files need to be rewritten to support Turkish, but the structure of the expressions needs to be changed as well. This process can be complicated further by languages which classify objects as masculine and feminine, because more regular expressions are required to cover all the cases needed to correctly identify an Intent.
<h4>Dialog</h4>
Most Skills have lines of text spoken when a Skill completes a task or spoken when information is returned through an API.  These Dialog files need to be changed for a new language.
<h4>Skill internals</h4>
Within some Skills, extra conditional processing may be required to handle new languages.  For example translating phrases that come back from an API in English into the target language, converting “cloudy” to “bewölkt” in German.
<h3>Text to Speech</h3>
A Skill will normally complete execution by speaking a line of Dialog to the user - like saying “the weather in Geelong today is clear skies and 22 degrees Celsius”. This is the Text to Speech layer of the Voice Stack, and its role is just that - to speak written information.

The default TTS engine used in Mycroft is Mimic. Mimic is currently available only in English, so if Mimic tries to speak foreign words, or words with diacritical marks (such as say the ö sound in Swedish), then the pronunciation will be unnatural.

Mycroft, being modular, allows you to select other TTS engines.  The Google TTS engine has more language options available. Again,  if you want to configure this for your language, you need to <a href="https://mycroft.ai/documentation/mycroft-conf/" target="_blank" rel="noopener">edit your <code>mycroft.conf</code> file</a>.

Building a new Text to Speech engine like Mimic is very difficult, requiring expert level understanding of languages to build the phonetic mappings, plus generating the voice pieces for the synthesis.
<h2>What does the language roadmap look like?</h2>
As you can see, providing language support is no easy task.  We are continually improving, and the following steps are part of building the tools to officially support more languages.
<h3>Training other Wake Words in Precise</h3>
Once the current ‘Hey Mycroft’ Wake Word in Precise has an accurate model, we will be opening up the Precise Tagger to allow tagging of other Wake Words, including Wake Words in other languages.  Since Precise itself is trained directly from recordings, it is already multi-language ready.
<h3>Moving to DeepSpeech for STT</h3>
Estimates say DeepSpeech requires 10,000 hours of tagged samples to provide a workable STT model for a language. The English dataset is still being built as well as the actual machine learning code that runs DeepSpeech.  Gathering 10,000 hours would be a huge amount of work for any individual, but spread over many collaborators it is a much more manageable task. We are creating the tools to collect and tag these training datasets as a community.
<h3>Adoption of Python 2.7 =&gt; Python 3 for Mycroft Core and all Skills</h3>
Mycroft began with Python 2.7, which does not have built-in <a href="https://en.wikipedia.org/wiki/Unicode" target="_blank" rel="noopener">Unicode</a> support. Unicode helps represent text in languages which do not use the Latin alphabet (the alphabet used to write English).  With the recent transition to Python 3, this hurdle has been cleared.
<h3>Mimic 2 for TTS</h3>
We are putting resources into a new method for Text to Speech. Mimic 2 is based on a neural network and as such is “trained” rather than “programmed”.  We estimate that it will take around 20 hours of recorded speech to yield a reasonable language model in nearly any language.  These recordings need to be clear and of one single voice in order to accurately train the model, but this is still much easier than getting a Ph.D. in order to be able to build support in the original Mimic.

The first English language voice is being created, as well as working out the kinks in the recording process.  Recommendations and tools will soon be available for the Community to build their own voices.
<h3>Harvesting tools for vocab and dialog files within Skills</h3>
Over the next few months, we're creating a harvesting tool to identify all the vocab and dialog files within Mycroft Core and Skills that need to be translated.  This will make it easy to see what needs to be done to support each language, and make it easier to keep up as new Skills are being created and old ones change. This will require no programming skill to assist in bringing Mycroft to your favorite language.
<h3>What can I do right now?</h3>
So what can you do right now to help advance language efforts?
<ul>
 	<li><strong>Help with Precise Tagging:</strong> The sooner we have the <code>Hey Mycroft</code> Wake Word training well, the sooner we can move on to training other Wake Words. You can tag Precise samples at <a href="https://home.mycroft.ai/" target="_blank" rel="noopener">home.mycroft.ai</a> under "Tagging."</li>
 	<li><strong>Opt-In to our Open Dataset:</strong> So that we can gather a diverse set of spoken samples with many voice types and accents, we need lots of people contributing to the <a href="https://home.mycroft.ai/#/setting/basic" target="_blank" rel="noopener">Open Dataset</a>.</li>
 	<li><strong>Have web-dev skills?</strong>  <a href="https://mycroft.ai/contact" target="_blank" rel="noopener">Contact us!</a>  We’d love help with the harvesting project and associated web interfaces.</li>
 	<li>Be patient! As you can see, multi-language support isn’t easy.  But the Mycroft Community has the best potential to support not just the<strong> most profitable</strong> languages, but <strong>all of the languages</strong>.</li>
</ul>