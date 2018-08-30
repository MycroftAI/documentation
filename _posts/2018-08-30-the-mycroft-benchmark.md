---
ID: 40290
post_title: 'Improving Mycroft through Metrics: The Mycroft Benchmark'
author: Eric Jurgeson
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/the-mycroft-benchmark/
published: true
post_date: 2018-08-30 08:00:23
---
<span style="font-weight: 400;">Machine Learning requires data to improve. The best source of that data is through our Community, who Opt-In to share the data from their interactions with Mycroft. That allows us at Mycroft AI to build Open Datasets of tagged speech to improve Wake Word spotting, Speech to Text, and Text to Speech. But, to improve the software that utilizes those engines, we need a different kind of data to analyze. How does Mycroft compare to other voice assistants and smart speakers? How does Mycroft itself improve over time? How can you help?</span>
<h1><span style="font-weight: 400;">Benchmarking Mycroft</span></h1>
<span style="font-weight: 400;">A benchmark is important for a number of reasons, first and foremost being it offers us a baseline of Mycroft’s performance on a given date that we can compare once changes are in place. Then, as necessary, we can compare different configurations of Mycroft, new platforms and hardware for Mycroft, and our competition.</span>

<span style="font-weight: 400;">Over the last couple of weeks, we’ve been preparing and conducting a repeatable benchmark of Mycroft against other voice assistants in the field. This will be a new addition to the Mycroft Open Dataset; not tagged speech or intent samples, but a standard process and metrics that anyone can use to measure Mycroft and other voice assistants quantitatively. Below, I’ll report on the results of the first iteration where we compared a Mycroft Mark I to a first generation Amazon Echo and Google Home.</span>
<h2><span style="font-weight: 400;">The Process</span></h2>
<span style="font-weight: 400;">To conduct this benchmark, we had to put together a series of questions, which wasn’t as easy as it sounds. Being an emerging technology, there aren’t industry standards that exist yet. So who better to set that standard than the Open player? We prepared a starter set of 14 questions based on the observed usage of Skills by Opted-In Mycroft users (more on that later), taking into consideration industry-reported most used Skills from places like </span><a href="https://voicebot.ai/2018/03/21/data-breakdown-consumers-use-smart-speakers-today/" target="_blank" rel="noopener"><span style="font-weight: 400;">Voicebot</span></a><span style="font-weight: 400;">. That first run of questions was: </span>
<ol>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">How are you?</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">What time is it?</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">How is the weather?</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">What is tomorrow’s forecast?</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Wikipedia search Abraham Lincoln</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Tell me a joke</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Tell me the news</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Say “Peter Piper picked a peck of pickled peppers”</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Set volume to 50 percent</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">What is the height of the Eiffel Tower?</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Play Capital Cities Radio on Pandora</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Who is the lead singer of the Rolling Stones?</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Set a 2 minute timer</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Add eggs to my shopping list</span></li>
</ol>
<span style="font-weight: 400;">That list has already evolved a bit to make the benchmark more objective. For one, this test originally was meant to check the intent parsing along with response times, which will in the future be split into separate benchmarks. As an example, Google does not return any response when asked to “Wikipedia search” a topic, and both Mycroft and Alexa only accept volume adjustments between 0 and 10. For next time, the list will probably look more like this:</span>
<ol>
 	<li>Tell me about Abraham Lincoln</li>
 	<li>What is the height of the Eiffel Tower</li>
 	<li>Who is the lead singer of the Rolling Stones?</li>
 	<li>How is the weather?</li>
 	<li>What is tomorrow’s forecast?</li>
 	<li>Play Capital Cities Radio on Pandora</li>
 	<li>Play Safe and Sound by Capital Cities on Spotify</li>
 	<li>Set a 2-minute timer</li>
 	<li>Set an alarm for tomorrow morning at 7:00</li>
 	<li>What time is it?</li>
 	<li>Tell me the news</li>
 	<li>Add eggs to my shopping list</li>
 	<li>Set volume to 5</li>
 	<li>How are you?</li>
 	<li>Tell me a joke</li>
 	<li>Say/repeat/Simon says “[random sentence]”</li>
</ol>
<span style="font-weight: 400;">To make sure we could properly check the times of a response, I set up to record the responses on video. I set the devices next to each other in the same room on the same wifi network and did a network speed test on a laptop on the same network for reference. Once all that was taken care of, the requests began.</span>

<span style="font-weight: 400;">Issuing all the requests to each assistant took about 45 minutes. To get the best idea of when requests ended and responses started, I imported the audio into Audacity and used the waveforms to determine five points:</span>
<ul>
 	<li><span style="font-weight: 400;">The Wake Word</span></li>
 	<li><span style="font-weight: 400;">The end of the request</span></li>
 	<li><span style="font-weight: 400;">The beginning of the response</span></li>
 	<li><span style="font-weight: 400;">The start of 'real info'</span></li>
 	<li><span style="font-weight: 400;">The end of the response</span></li>
</ul>
<span style="font-weight: 400;"><em>About ‘Real Info’</em> - We wanted to see if the other assistants in the field might pad their responses with cached phrases to give more time to synthesize the real info of the response. This seems like an obvious way to improve the perception of a response. Hearing “Right now in Kansas City” - which can be easily pre-generated and cached to stream at the start of a weather response - certainly doesn’t detract from the experience. Though it does mean an extra second or so until you actually hear the temperature and weather. Deciding what is padding and when ‘real info’ starts is a subjective call right now, but we’ll be trying to define it well as things progress.</span>
<h2><span style="font-weight: 400;">The Results</span></h2>
<span style="font-weight: 400;">Now to the good stuff, or in this case, the “room for improvement” stuff. Here are the results from the first Mycroft Benchmark.</span>
<h3><span style="font-weight: 400;">Time to Response</span></h3>
<span style="font-weight: 400;">One of the biggest points we wanted to track was the ‘Time to Response.’ In this context, that means the ending of the provided request to the beginning of an audible response. We tracked that across the 14 questions using the new Mimic2 American Male voice. We found that Mycroft currently responds an average of 3.3x slower than Google and Amazon. On average for our sample, Alexa responded to requests in 1.66 seconds, Google Assistant responded in 1.45 seconds, and Mycroft in 5.03 seconds.</span>
<h3><span style="font-weight: 400;"><a href="https://mycroft.ai/wp-content/uploads/2018/08/TimeToResponse.png"><img class="size-full wp-image-40307 aligncenter" src="https://mycroft.ai/wp-content/uploads/2018/08/TimeToResponse.png" alt="The Time to Response information from the first Mycroft Benchmark." width="1200" height="675" /></a>Time to Real Info</span></h3>
<span style="font-weight: 400;">The next thing we decided to track was when the voice assistant’s response actually began answering the question it was asked. As mentioned above, this is a subjective decision for the time being, but still offers some interesting data to look at. On average, Alexa started providing real info 3.02 seconds after the request finished. Google provided real info at 3.55 seconds. Mycroft started providing real info at 5.7 seconds.<a href="https://mycroft.ai/wp-content/uploads/2018/08/TimeToRealInfo.png"><img class="size-full wp-image-40308 aligncenter" src="https://mycroft.ai/wp-content/uploads/2018/08/TimeToRealInfo.png" alt="The Time to Real Info chart from the first Mycroft Benchmark." width="1200" height="675" /></a> </span>

<span style="font-weight: 400;">We can see that the graph is a good bit tighter here, and in one case, “Tell me the news,”  Mycroft actually comes out on top. My presumption is that Mycroft’s competition is adding some phrasing to the beginning of responses that require API hits or pulling up a stream. Though, it also included the reason behind the outlier that is Google’s response to the News query - a nearly 16 second notification about being able to search for specific topics or news sources. I also did a quick look at the time between the response starting and when the assistant provided Real Info. On average, Alexa spoke for 1.36 seconds before providing Real Info. Google Assistant spoke for 2.1 seconds before Real Info. Mycroft spoke for 0.66 seconds before providing Real Info.</span>
<h3><span style="font-weight: 400;">Where to go from here</span></h3>
<span style="font-weight: 400;">This benchmark was especially helpful in comparing Mycroft objectively to Google and Amazon. Eventually, we’ll be able to broaden it to others in the space. Now the trick is figuring out how to improve the experience, then return to this benchmark periodically to reassess.</span>

<span style="font-weight: 400;">For improvements to the experience, we have another source of metrics from which we’ll be able to get actionable information: the Mycroft Metrics Service.</span>

<span style="font-weight: 400;">Our Opted-In Community Members have timing information for their interactions with Mycroft anonymously uploaded to a database for analysis. </span>This is how we determined the Mycroft Community’s most used Skills (that is, the Opted-In users most used Skills) for the 14 questions of the Benchmark. Apart from Skill usage, we have visibility of what steps are carried out in an interaction, and how long each step takes. From there we can determine what steps of a Mycroft interaction take the longest, and work to speed them up or find creative improvements to the Voice User Experience.

<span style="font-weight: 400;">We’ll also revise the benchmark to be more explicit in comparing the timing of responses. It's likely we'll create one or more subjective measures for quality of response. As Skills expand, the number of questions will certainly expand too.</span>

<span style="font-weight: 400;">There’s also the question of where this information will live and be available to the community. The blog is a great place for explaining a new process but isn’t great for storing and displaying data. We’ve had some </span><a href="https://github.com/MycroftAI/mycroft-skills-data" target="_blank" rel="noopener"><span style="font-weight: 400;">Skill Data</span></a><span style="font-weight: 400;"> published on the Github since May. A repo and/or Github.io page will likely be the residence of data, graphs, and more regular updates on Mycroft Metrics and Benchmarking. That will make it free and available for anyone to use, whether you’re comparing the speed of your local system to others, planning an improvement to Mycroft Core to speed up interactions, or creating a visualization for research. This data is Open and yours to use. Since that will take some time to set up, <a href="https://docs.google.com/spreadsheets/d/1Oc7Vocn3DMKprXc11ybkD1_pAItRgSGlHJCS_S_0fFk/edit?usp=sharing" target="_blank" rel="noopener">here is a Google Sheet</a> to give you immediate access to the first round of data.</span>
<h2><span style="font-weight: 400;">How can you help?</span></h2>
<span style="font-weight: 400;">I’m so glad you asked! Like I mentioned, metrics come back only for Community Members who have Opted-In to the Open Dataset. So the best way to help is to Opt-In and use Mycroft! That way, we get a population of interactions that is as broad as possible. People on different networks in different locations using different devices interacting with Mycroft in different ways provides the best information for Mycroft and the community to make decisions on.</span>

<span style="font-weight: 400;">To Opt-In:</span>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Go to home.mycroft.ai and Log In</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">In the top right corner of the screen, click your name</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Select “Settings” from the menu. You’ll arrive at the </span><a href="https://home.mycroft.ai/#/setting/basic" target="_blank" rel="noopener"><span style="font-weight: 400;">Basic Settings</span></a><span style="font-weight: 400;"> page</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Scroll to the bottom and once you’ve read about the Open Dataset, check “I agree” to Opt-In</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">That’s it!</span></li>
</ul>
<span style="font-weight: 400;">Once you’ve done that you’ll not only be providing the metrics from your interactions, but also helping build STT, Wake Word spotting, and Intent Parsing for Mycroft. We always want to thank those members of our community who have Opted-In to help make AI for Everyone.</span>

<span style="font-weight: 400;">Have an idea to improve Mycroft’s metrics and benchmarking? Maybe a question on the process? Let us know on the forum.</span>