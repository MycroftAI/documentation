---
ID: 39034
post_title: >
  Picroft Survey 2018 – Results and
  Roadmap implications
author: Kathy Reid
post_excerpt: "Read more about our June 2018 Picroft survey and the key learnings we've taken from the data to help inform our Picroft Roadmap. "
layout: post
permalink: >
  http://mycroft.ai/blog/picroft-survey-2018-results/
published: true
post_date: 2018-07-02 10:00:32
---
A huge thank you to the more than 200 people who took a few minutes out of their busy day to respond to our recent <a href="http://mycroft.ai/blog/picroft-roadmap-2018/">Picroft Survey</a>. As promised, we're sharing the full results of the survey with you - in both graphical and machine readable format - and discussing what they mean for our Picroft Roadmap.
<h2>Why do we need a Roadmap?</h2>
Roadmaps are super important in <a href="https://en.wikipedia.org/wiki/Product_management">product management</a> and technology planning. They help us understand dependencies, optimize sequencing of activities and assist in planning critical resource availability. There are several inputs to a technical Roadmap;
<ul>
 	<li>customer and user feedback</li>
 	<li>emerging technology reports and industry information</li>
 	<li>internal error reports and monitoring information</li>
 	<li>strategic plans</li>
</ul>
And that's where the Picroft Survey comes in. To better understand what our priorities should be for Picroft, we wanted to better understand how our Community is <em>currently</em> using Picroft.

So, let's step through the results!
<h2>Survey results</h2>
<h3>Where are you on your Picroft journey?</h3>
<a href="https://mycroft.ai/wp-content/uploads/2018/06/picroft-journey-where-are-you.png"><img class="alignnone wp-image-39046" src="https://mycroft.ai/wp-content/uploads/2018/06/picroft-journey-where-are-you.png" alt="picroft-journey-where-are-you" width="960" height="710" /></a>
<h4>Raw data</h4>
<ul>
 	<li><a href="https://mycroft.ai/wp-content/uploads/2018/06/Picroft-Survey-June-2018.csv">Picroft Survey - Where are you in your Picroft journey?</a> (CSV, 400b)</li>
</ul>
<h4>Discussion</h4>
This question was designed to find out where the Community was on their Picroft journey so that we can target effort and resources for the biggest impact. What we <em>expected</em> to find here was that there would be a large cohort actively using Picroft, but not wanting to do more with it, and perhaps another cohort who had heard of Picroft but hadn't done any planning yet to build one. The results turned this thinking on its head. Instead we found two large cohorts who are likely under-serviced at the moment;
<ul>
 	<li>Those who have a Raspberry Pi and are <em>planning</em> to install Picroft</li>
 	<li>Those who are already up and running with Picroft and want to <em>extend it further</em></li>
</ul>
<h4>Key outcomes</h4>
<ul>
 	<li>We need to prioritize support for hardware like Google AIY Kits and other hardware that extends the <em>Picroft</em> platform</li>
 	<li>We need to look at ways to get people "up and running" quickly and easily with Picroft; we've previously had internal discussions around whether we should offer a "pre-made" Picroft kit with speakers / microphone that are known to work well.</li>
</ul>
<h3>What model Raspberry Pi do you have?</h3>
<a href="https://mycroft.ai/wp-content/uploads/2018/06/picroft-journey-which-rpi-do-you-have.png"><img class="alignnone wp-image-39051" src="https://mycroft.ai/wp-content/uploads/2018/06/picroft-journey-which-rpi-do-you-have.png" alt="picroft-journey-which-rpi-do-you-have" width="960" height="700" /></a>
<h4>Raw data</h4>
<ul>
 	<li><a href="https://mycroft.ai/wp-content/uploads/2018/06/Picroft-Survey-June-2018-1.csv">Picroft Survey - What model Raspberry Pi do you have? (CSV, 300b)</a></li>
 	<li><a href="https://mycroft.ai/wp-content/uploads/2018/06/Q2_Text.csv">Picroft Survey - What Raspberry Pi model do you have - free text responses (CSV, 1Kb)</a></li>
</ul>
<h4>Discussion</h4>
Again, some of our early expectations here were invalidated by the survey data. We originally thought that the largest cohort here would be the RPi 3, with perhaps an emerging cohort of RPi 3B+ owners. The RPi 3B+ cohort was much larger than we anticipated. Interestingly, we also anticipated that the cohort with older models of RPi - RPi 2, Pi Zero etc - would be a lot smaller. Unfortunately there's not going to be a lot that we can do for people with older hardware - it simply doesn't have enough compute power or RAM to be able to run the Mycroft voice stack. Another interesting finding from this question was found in the free text responses. We saw quite a few folks with Odroid devices and even an ASUS Tinkerboard.
<h4>Key outcomes</h4>
<ul>
 	<li>A unified image that runs on <strong>both</strong> RPi 3 <strong>and</strong> RPi 3B+ needs to be a high priority</li>
 	<li>We need to be as clear as we possibly can about the Picroft hardware requirements; older RPi models aren't powerful enough to run the Mycroft voice stack</li>
 	<li>The single board computing landscape is fragmented; there is wide diversity of devices - we won't be able to support a wide range of them.</li>
</ul>
<h3>What do you think our priorities should be for Picroft?</h3>
<h4><a href="https://mycroft.ai/wp-content/uploads/2018/06/picroft-journey-what-should-priorities-be.png"><img class="alignnone wp-image-39058" src="https://mycroft.ai/wp-content/uploads/2018/06/picroft-journey-what-should-priorities-be.png" alt="" width="959" height="672" /></a></h4>
<h4>Raw data</h4>
<ul>
 	<li><a href="https://mycroft.ai/wp-content/uploads/2018/06/Picroft-Survey-June-2018-2.csv">Picroft Survey - What do you think our priorities should be (CSV, 450b)</a></li>
 	<li><a href="https://mycroft.ai/wp-content/uploads/2018/06/Q3_Text.csv">Picroft Survey - What do you think our priorities should be - free text responses (CSV, 9Kb)</a></li>
</ul>
<h4>Discussion</h4>
This was an incredible eye-opener. We knew that the demand for an image based on Raspbian Stretch Lite was beginning to grow; we didn't realize it was this strong. The desire for integration with other devices also mirrored the first question around where people were on their Picroft journey. We were also a little surprised that the priority ranking for better microphone support wasn't a little higher; microphone issues the highest issue by volume with Picroft hands down - literally 8 out of 10 issues that people report with using Picroft are related to symptoms such as;
<ul>
 	<li>microphone not recognized</li>
 	<li>microphone volume to low</li>
 	<li>microphone cuts out after some time</li>
</ul>
We were also concerned the Picroft documentation wasn't quite up to standard - although this doesn't appear to be as much of a concern as being able to support RPi 3B+ and extend Picroft.

There was also excellent value in the free text comments. Several key themes emerged here including the desire for better foreign language support. <a href="http://mycroft.ai/blog/languages-are-hard/">This is difficult to achieve, as covered in this blog post</a>, however it was great to have this requirement again validated. Many of the comments requested specific hardware support for certain microphone and speaker models; again something we want to build into the next image. Again, the desire to extend Picroft with third-party hardware such as Google AIY was expressed multiple times. We also had several people mention they would like display support for the Picroft - the ability to express facial gestures similar to the Mark 1. Others mentioned closer integration with platforms like Home Assistant, Open Elec, and Magic Mirror. We've had some internal discussions already about reaching out to these communities to see if we can have more fluid experiences for people who want to use these <em>with</em> Picroft. Others expressed a desire for Picroft on other operating systems - such as Ubuntu Core. This will be more difficult to achieve; as it requires not just building an image but also <em>supporting</em> that image. Ideally we just want to be supporting one single unified Picroft image.
<h4>Key outcomes</h4>
<ul>
 	<li>Being able to support a wider range of microphones and speakers "out of the box" needs to be a priority; especially commercial grade microphones for superior sound</li>
 	<li>The ability to have better "out of the box" support for hardware such as the Google AIY kit</li>
 	<li>The Community has a strong desire for wider language support; this is going to take some time to deliver but is definitely something we want to do</li>
 	<li>Working more closely with related communities such as Home Assistant, Open Elec, and Magic Mirror for closer integration</li>
</ul>
&nbsp;

In conclusion, this was a very useful exercise for us. Thank you again for taking the time to provide your feedback, and do feel free to have a read through the data and <a href="https://community.mycroft.ai/t/picroft-survey-2018-results-and-roadmap-implications/4078">share your insights</a>.

&nbsp;