---
ID: 34424
post_title: 'Why We&#8217;re moving to DeepSpeech on March 31 | Privacy, Speech to Text &#038; Balance'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/mycroft-speech-to-text-and-balance/
published: true
post_date: 2018-01-11 17:06:35
---
<h3>Our community asked, we're answering. Read notes from our CTO, Steve Penrod about our move to DeepSpeech.</h3>
From Steve;

Misunderstandings of how Mycroft performs Speech to Text is one of the things I hear about regularly. So today I'll provide some clarity on how it works now, why it works that way, and where we are heading with this technology in the future.
<h2>Mycroft Design Decisions</h2>
It is rare that there is only one way to solve a problem.  So every project requires thoughtful analysis of the end user's needs to select the best problem solving approach.  With careful thought, experimentation and planning it is usually possible to work out a balanced approach to solve the problem.  One of the key factors in choosing a solution is the design criteria.  What does the user value?  How does the development team best provide that value?  What is the top priority?  What can wait?  When we started Mycroft our design criteria consisted of:
<h3>Choice</h3>
One of the key things we wanted to enable is choice.  We knew that the technology we were using two years ago would likely not be the same technology we'd use in five years.  Similarly, we knew that the technology that <em>we</em> decided to use would not be the technology that <em>everyone</em> would want to use.  So we architected our system to allow choice — by both the project and by individual users — for the key technical components: Speech to Text, Text to Speech and Skills.
<h3>STT: Performance</h3>
Next we knew that the only way this would be a successful project is with a good Speech to Text (STT) engine.  Being 90% accurate sound pretty good <strong>—</strong> 90% is an A, right?  But if 90% isn't always acceptable:
<blockquote>“Please turn on the kitchen right”</blockquote>
That is close, but no-cigar if what you said was:
<blockquote>“Please turn on the kitchen light”</blockquote>
Errors like that cause frustration and quickly lead users to set aside a technology, so we wanted our software stack to default to the best experience possible.
<h3>Simplicity</h3>
Another thing we wanted was simplicity.  We didn't want to make a user spend 30 minutes setting up defaults.  I know I've looked at projects that might have been cool, but the setup was just too much of a hassle to even try.  Some systems even run on specific hardware which, if the user doesn't have it handy, makes the technology unusable. Or setting up several accounts with other systems it depended on.  Every setup step and requirement increases friction and shrinks the audience, and we wanted to make Mycroft available for everyone so simplicity was key.
<h3>Privacy</h3>
We knew from the start that voice technology was uniquely intimate.  To be useful, it has to be available all the time.   That means it has to listen <em>constantly</em>, to every single word you say.  It should ignore most of those words, but it still has to listen.

The concept of 'wake words' helps.  I can (<a href="http://money.cnn.com/2017/10/11/technology/google-home-mini-security-flaw/index.html">usually</a>) feel good that strangers aren't able to listen to me without my knowledge.  But someone still can glean intimate details by aggregating all of the queries and command I speak.
<blockquote>“Where can I buy clown makeup?”

“Are there any clown colleges?”

“When is the next clown convention in Kansas City?”</blockquote>
Maybe I don't mind the world knowing that I have this interest in clowns.  But then again maybe I don't want my clown addiction exposed when I run for a political office a decade from now.  Regardless, I shouldn't be forced to give up all my privacy just to use voice technology.
<h2>Balance</h2>
Weighing all these factors, we made some key decisions early on.

We decided to setup a Mycroft STT service on our servers which would provide transcription for our user.  This approach allowed us to choose the best STT technology to run that service.  Our initial implementation has been to use Google Speech To Text service <strong>—</strong> it was <em>by far</em> the most accurate at the time and remains so today.  Others were in the 70-80% accuracy, but Google was already at 90%+.  Thus, we give Mycroft users the best performance.

To provide privacy we decided to aggregate all of our speech to text requests into a single bucket and set the source to "MycroftAI" <strong>—</strong> not the end user individual.  So in the example above, my clown requests would all be blended in with the requests of hundreds of others.  Since there is no easy way to connect my request to me this provides privacy.

Finally, we decided to provide an easy mechanism for users to switch to other STT engines, completely eliminating Mycroft from the process if they want.  That provides choice.

This was the best balance.
<h2>Maintaining Balance</h2>
Balance is not a static thing.  Things change.  New forces come in to play.  You have to remain aware and shift to keep your balance.

There are several new technologies available today that weren't available two years ago.
<ul>
 	<li>New STT technology</li>
 	<li>More powerful hardware</li>
 	<li>Better awareness of privacy concerns</li>
</ul>
<h3>New STT: DeepSpeech</h3>
Since this summer we have been working with the <a href="https://research.mozilla.org/machine-learning/">Mozilla Machine Learning</a> team.  They created a new, open source, machine learning-based STT technology called DeepSpeech built on research started at Baidu.  We've assisted with <a href="https://voice.mozilla.org/">Project Common Voice</a> and are creating a new mechanism allowing Mycroft users to <a href="https://home.mycroft.ai/#/setting/basic">participate in building the Open Dataset</a> to provide more real-world data for use in training to improve the system.

At the beginning of the summer the word-error-rate for DeepSpeech was at around 15%. By the fall it was at 10% and it is continuing to improve as more training data is digested.  This is now in the accuracy realm needed for a voice assistant.

For those with the know-how and resources, you can already setup and use <a href="https://github.com/mozilla/DeepSpeech">DeepSpeech</a> on your own high-end equipment today.
<h3>More Powerful Hardware: GPUs and TPUs</h3>
Two years ago a Graphics Processing Unit (GPU) was an expensive accessory needed only for the latest 3D shooter or to drive the new VR toy called an Oculus Rift.

Today, GPUs are being used to mine cryptocurrencies, to power self-driving cars and, yes, to accelerate STT.  DeepSpeech on a simple CPU can run at 140% of real time, meaning it can't keep up with human speech.  But with a good GPU it can run at 33% of real time.

Tensor Processing Units (TPUs) are just emerging and promise even higher speeds for TensorFlow systems.
<h3>Privacy Awareness</h3>
Now that Amazon's Echo has become common, people are really <a href="https://www.cbsnews.com/news/google-home-amazon-echo-patents-track-listen/">starting to think about</a> what it means to have an always-on microphone in your home.  What are the incentives and motives for these services?  What do you really know about how they work?
<h2>A new balance</h2>
These shifting forces have lead us to the new balance, appropriate for today.  We are changing our default Mycroft STT engine to DeepSpeech.  This will happen on March 31st.  This means that none of our user's queries will leave the Mycroft perimeter unless the user is accessing an outside service ( weather for example ) in which case the source of the query will be "MycroftAI" and not an individual user.

That said we will continue to allow Mycroft users to choose their text to speech engine.  Users can easily select Google, Watson, or Wit.ai as a STT provider (or Kaldi, Bing, Houndify or more <a href="https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/stt/__init__.py#L173">if you are willing to get your fingers dirty</a>).

This is the new best balance.
<h2>Your Privacy Going Foward</h2>
Here at Mycroft we take privacy seriously.  We don't preserve data unless we are given explicit permission.  We don't sell data to third parties and we don't intrude on the lives our our customers.  We aren't trying to sell you products, dominate online advertising or own your digital identity.  Switching to DeepSpeech advances our goal of providing our users with the highest qualtiy, most private experience possible.  We're proud of our commitment to privacy and look forward to bringing it to more and more of the Internet over time.