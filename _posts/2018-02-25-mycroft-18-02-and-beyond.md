---
ID: 35090
post_title: Mycroft 18.02 and Beyond
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/mycroft-18-02-and-beyond/
published: true
post_date: 2018-02-25 10:17:43
---
Where is Mycroft technology going? Here is what's in store for the 18.02 milestone and beyond.
<h1>Community Involvement</h1>
As an open source project, one of the greatest strengths we have is how many are interested in what we are doing, volunteering ideas, and submitting code. On the flip side of this, the most difficult challenge is coming to a consensus on <em>exactly what</em> we should be doing as a group.

Of course, individuals are always welcome and able to pursue their own projects and experiments. But common goals help us all plan and collaborate better.

To kick off the process we are publishing what we have come up with inside the core team. We love community feedback, so please join us in our community forums with your thoughts and comments!

&nbsp;
<h1>Goals for 18.02</h1>
In the coming week, we will be creating our 18.02 milestone release. For this milestone we had some specific technology targets in mind, laying the foundation for our future. They included:
<ul>
 	<li><strong>Precise wake word engine</strong>
We started the project in 2015 using some existing tools and technologies. We preferred open technologies when possible and chose PocketSphinx for our wake-word engine. This was a good starting point, but the fundamental technology used has limitations that are unlikely to improve significantly. We've created the Precise engine specifically for this task. This uses machine learning techniques, running models generated from voice-clips contributed by the community. This leads to the next goal...</li>
 	<li><strong>Feedback Loops</strong>
Machine learning requires data for training. Data is used to create models, which is used by the mechanisms to generate more (and presumably better) data. This improved data is tagged and the training process starts all over again. This is what we are calling a Feedback Loop. That's how Mycroft gets "smarter" the more it is used. All of these use only the data from our community members who choose to help with our Opt In – these contributions are invaluable, thank you all! We've started several of these loops as of today:
<ul>
 	<li><em>Precise</em>
As mentioned above, this powers our wake-word engine</li>
 	<li>The <em>Mycroft Open Dataset</em> for DeepSpeech
The Mozilla DeepSpeech team will be using this data to improve their Speech to Text models</li>
 	<li><em>Persona</em>
More on this soon – it will let Mycroft have opinions and customized knowledge</li>
</ul>
</li>
 	<li><strong>Better speech output</strong>
Speech is what Mycroft is all about, and the quality of that speech immediately shapes the experience. We have added some tools to help with speech synthesis in general – assisting in the pronunciation of things like "API" regardless of the engine. More importantly, the Mimic engine we started with was a solid start, offering the unique ability to run locally on limited power equipment. But it does have a distinctly "robotic" quality.
To provide a more natural voice, we are introducing Mimic 2, based on the work of <a href="https://keithito.com/">Keith Ito</a>. Mimic 2 sounds great but needs a more powerful computer to generate, so it cannot run on low-powered hardware like a Raspberry Pi. So for now, this will be implemented as an online option. The original Mimic always going to be an option for those wanting to stick with an efficient local TTS engine.</li>
 	<li><strong>Improved dialog tools
</strong>Being able to tell your voice agent what to do in one-shot has been a good start. But for a system to be able to truly act like a person, it sometimes should ask follow-up questions as a dialog. The MycroftSkill.converse() tool has been around since 17.08, but the MycroftSkill.get_response() method make writing interactive skills _so_ much easier! Combined with more powerful parsing, fuzzy matching, and output formatting tools, it is far easier to create a natural speech interaction.</li>
 	<li><strong>Enhanced Skill Settings</strong>
The initial release of Skill Settings was very basic – each instance of a skill could put a label on a textbox on Home; that was it. It's since grown to include all of the basics needed to provide a rich set of options – checkboxes, comboboxes, section grouping, rich-text labels and color-theming. Settings also became global, allowing a single interface for all your Mycroft devices.</li>
 	<li><strong>Mycroft Skill Manager (MSM)</strong>
The original MSM introduced last spring was a good start for an important task – an easy way to install skills. In this year MSM got connected to the Mycroft Skills repo, given a voice interface, and generalized to support dynamic default skills with different defaults for multiple platforms. The next major iteration of MSM introduces versioning.
Rather than a skill auto-updating to the head of its repo, by default only the version which was submitted and reviewed for inclusion in the release-specific Mycroft Skill list will be installed. This provides a mechanism for skill authors to support multiple APIs (for example 17.08 or 18.02) and for the project to retire older APIs. It also provides confidence for a user that only peer-reviewed code is being placed on their equipment.</li>
 	<li><strong>Python 3</strong>
This is an under-the-hood change, but a critical one. Python 2.7 has enjoyed broad support by major coding libraries, but Python 3 is now widely supported also. Perhaps most importantly, Python 3 embraces Unicode, making translation support in Mycroft a much easier task going forward.</li>
 	<li><strong>Send it to me</strong>
Email remains a great way to memorialize and share information. Mycroft can send your registered account information. This enables things like "create a support ticket", "send me the source on that" (after asking a question), "send me my shopping list" and more!</li>
 	<li><strong>Skill Translation tools</strong>
The Mycroft Skill system is built for translation. We have extended this with tools making it easier to support translatable dialog elements, templates, lists and named values.</li>
 	<li><strong>Common Context terms</strong>
Mycroft has shared context, and this context is most powerful when the terminology is agreed-upon between skills. This allows the "him" in "Send me him a text that I'll be 5 minutes late" in an SMS skill to know who you meant when right before you asked the Calendar skill "When is my appointment with Puddles the Clown"?</li>
</ul>
&nbsp;
<h1>Roadmap for 18.08</h1>
As we pass the 18.02 milestone, we need to roadmap where the 18.08 milestone will take us. Initially, we are looking at a few initiatives:
<ul>
 	<li><strong>Skill Store</strong>
Github has been useful, but it is only developer-pretty. Time for an easy interface!</li>
 	<li><strong>DeepSpeech STT
</strong>As announced earlier, DeepSpeech is becoming the preferred STT engine for Mycroft. Initially, it will be cloud-based, although it can already be run locally by those willing to get their fingers dirty.</li>
 	<li><strong>Translation suite</strong>
Several have undertaken translation efforts giving us the start of Portuguese, German, Italian and French support – thank you all! But this is not simple and keeping translations synchronized as resources change is not easy. A few simple tools should make this easy for anyone to contribute.</li>
 	<li><strong>Individual Skill Isolation</strong>
A major architectural change will be necessary, but this will enhance interoperability, stability, and security.</li>
 	<li><strong>Overlapped vocabulary resolution</strong>
Words aren't always adequate to determine which skill to activate. "Turn it off" can be directed at several skills – did you mean the coffee maker or the music? Both skills need to be invoked to determine which device you mean because it is currently on.</li>
 	<li><strong>Grow the DisplayManager</strong>
Screens are a common part of the Mycroft experience, and the DisplayManager provides the abstraction allowing Mycroft to handle them all – be it the Mark 1 faceplate, the KDE Plasmoid UI, the forthcoming Mark II touchscreen or any other visual interface. The initial EnclosureAPI is growing to a full DisplayManager to support these expanding needs.</li>
 	<li><strong>Personal Backend</strong>
Mycroft-core comes configured to use the home.mycroft.ai backend. For the majority of people, this is a good balance of convenience and privacy. However, some have a need or desire to host their own version of the services provided by Home.</li>
</ul>
<h1></h1>
<h1>Shape your future!</h1>
Join us on our <a href="https://community.mycroft.ai">forum</a> to provide your voice as part of the community. The future is in your hands!

&nbsp;

&nbsp;

&nbsp;

&nbsp;