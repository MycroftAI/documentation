---
ID: 2067
post_title: 'Halloween Update: Trick or Treat'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: https://mycroft.ai/blog/trick-or-treat/
published: true
post_date: 2016-11-01 15:38:59
---
I'm a big fan of Halloween.  I had over 100 kids come to my door last night displaying their creativity in both the themes and execution of their costumes, and I was happy to reward them with a little candy.  But this season is known not only for treats, but also for tricks. Unfortunately this year has brought us both.  Let me tell you about it...
<h2>The Trick</h2>
As you may recall, we were expecting to receive the first article circuit boards from the board house last week.  Instead they called us and were asking for clarification about placement of some of the components.  Their questions weren't really making sense, and after a few rounds back and forth it dawned on us — they'd built an old revision of the circuit board.  The problem finally got tracked down to human error.  A technician had simply grabbed the wrong files and they produced the wrong ones.  So we've been reminded why you do first articles.

The board house has owned-up to the mistake and are correcting it.  We aren't certain exactly how long this trick is going to take to recover from, but I'm guessing it'll be a couple weeks.  This isn't exactly a disaster like I spoke of in my <a href="https://mycroft.ai/shipping-update-and-launchkc/">September blog post</a>, but it certainly is an unexpected detour on the road to shipping.
<h2>The Treat</h2>
[caption id="attachment_2076" align="alignleft" width="300"]<a href="https://mycroft.ai/wp-content/uploads/2016/11/mycroft-exploded.png"><img class="size-medium wp-image-2076" src="https://mycroft.ai/wp-content/uploads/2016/11/mycroft-exploded-300x187.png" alt="Exploding Mycroft" width="300" height="187" /></a> Exploding Mycroft[/caption]

Despite this setback, we are pushing forward with our plan to open source the hardware design.  I'm happy to announce the Mycroft Mark 1 now is on our GitHub under the <a href="https://github.com/MycroftAI/hardware-mycroft-mark-1">hardware-mycroft-mark-1</a> repository!  Everything you need to build our first Mycroft reference device will be found there.

Open Source Software is pretty well understood, but Open Source Hardware is still a fairly new concept.  The licenses to support it are still being honed.  We are using the CERN license, which is often called the "GPL of Open Source Hardware".  It was created by <a href="http://arstechnica.com/information-technology/2011/07/for-the-good-of-all-of-us-cern-launches-open-source-hardware-effort/">CERN in Switzerland</a>, the folks who brought us the <a href="https://en.wikipedia.org/wiki/Large_Hadron_Collider#Second_run_.282015_onward.29">Large Hadron Collider</a>. However you likely won"t be able to build a super-collider — even if it is open sourced — unless you have a 27 kilometer wide backyard; and even if you did the electric bill for running a 6.5 teraelectronvolt experiment is prohibitive.  Fortunately building a Mycroft Mark 1 unit is a lot more practical, and nearly as cool.

We will also be applying to become a member of the <a href="http://www.oshwa.org/2016/10/07/announcing-the-oshwa-open-source-hardware-certification-program/">Open Source Hardware Certification Program</a> along with companies like Adafruit and Sparkfun Electronics.  We encourage everyone to produce (even for commercial purposes) or remix our design, just keep sharing any improvements with the world.
<h2>Two More Treats</h2>
We've also been pushing forward on the software platform.  On the forums we have published the <a href="https://community.mycroft.ai/t/mycroft-technology-roadmap/1014">Mycroft Roadmap for 2016-2017</a>.  This document highlights the many areas we see as important technical targets to strengthen today's Mycroft platform.  Portions will be tackled by us here at Mycroft Inc, but we also want and need to work together with the community to tackle many of the tasks.

Additionally we've published the <a href="https://community.mycroft.ai/t/mycroft-skill-lifecycle">Mycroft Skill Lifecycle</a> on the forums and have begun to fill the <a href="https://github.com/MycroftAI/mycroft-skills">mycroft-skills</a> repository on GitHub. This provides a great source of working skills and examples of how to hook Mycroft into home media and IoT devices, and more.

Please pop over to the forums, read, and join in the conversation!
<h2>Interview with the CTO</h2>
I received a request for an email interview from Jasper, a student in The Netherlands.  He had what I thought were some really great questions and I thought other people would find them interesting.  Perhaps not quite as riveting as <em>Interview with a Vampire</em>, but hopefully my answers are almost as interesting as his questions were!

<strong>Jasper:
</strong><i>What’s your ultimate goal with Mycroft?</i>

<i><strong>Steve:
</strong></i>Create "AI for Everyone"!
<ul>
 	<li>We want to make voice technology pervasive, with the same Skills (or "voice apps") available to the user wherever they want them.  Might be a phone, a desktop, a watch, or car or a coffee maker that they are talking to, but I still want to be able to ask what is on my calendar.</li>
 	<li>We want to allow people who can't use technology today because of discomfort with traditional interfaces — like the elderly — to be able to just talk to technology.</li>
 	<li>Similarly, we want to empower those physically limited, such as someone paralyzed or chair-bound</li>
</ul>
<div>tl;dr: Build the Star Trek computer.</div>
<div></div>
<div><strong>Jasper:</strong></div>
<div>
<div><em>What is the most difficult part about building a voice assistant? I’m thinking about speech to text, hardware compatibility, ‘understanding’ spoken language.</em></div>
<div></div>
<div><strong>Steve:</strong></div>
</div>
<div>
<div>It is an iterative process and we are building this by standing on the shoulders of giants.  Many before us have laid the foundation for Text to Speech, Speech to Text, Natural Language theories, etc.  Starting from scratch would have been nearly impossible and not giving those people credit would be disingenuous.</div>
<div></div>
<div>Given what we have started with, the hardest part today is getting the architecture right to support all of the platforms and skills we intend to run on.  In the long run, the hardest part will be extracting intent from only words.  So much of intent depends on the environment beyond what is contained in the words.  Recent history (what you said a couple minutes ago), long term history (what you say or do every day or every year at this time of year), voice inflection, things visible or audible in the nearby environment, etc. all allow a person to deduce meaning.</div>
</div>
<div></div>
<div><strong>Jasper:</strong>
<em>What part of the software do you think is holding back further progress? Do you think it’s possible to create a ‘perfect’ voice assistant?</em></div>
<div></div>
<div><strong><strong>Steve:
</strong></strong>
<div>'Perfect' is a tough target.  But I think we can create something that is at least as good as what you see in movies today.</div>
<div>The current impediment is the desire and need to make this honor personal privacy and security.  We can't wait to address those things like what has happened with so many other technologies.  Imagine if your voice tech was designed with little privacy/security concern like email was and you get spammed or your every word gets "leaked".</div>
</div>
<div></div>
<div><strong>Jasper:
</strong><em>Do you think being open source is an advantage or a disadvantage for Mycroft? Does Mycroft gather a lot of interest from developers and hobbyists not affiliated with the company?</em><strong>
</strong></div>
<div></div>
<div><strong>Steve:</strong></div>
<div>Both.  By its nature, Open Source allows us to address both the privacy concerns and to speed up adoption of a unifying voice platform in all kinds of devices.  Additionally we have a growing community who want to create Skills for themselves and that they can give back to the world.  But building a company around open source is still very new and makes it difficult to attract investment.</div>
<div></div>
<div><strong>Jasper:
</strong><em>How trivial do you think it is for Mycroft to have deep third party integration? How do you plan to achieve such integration, and do you work together with other companies to make sure your software works?</em><strong>
</strong></div>
<div></div>
<div><strong>Steve:</strong></div>
<div>
<div>We intend to make it as easy of possible for a Skill writer to connect voice to a web API or an Internet of Things (IoT) device.  That means helpers that make it easier than just writing straight Python.  Plus we intend to allow manufacturers to expose all the power of their particular "Enclosure" to the voice user and the Skill writer.</div>
</div>
<div></div>
<div><strong>Jasper:
</strong><em>What do you think about other comparable technologies like Amazon Echo, Google Voice Search and Apple’s Siri?</em><strong>
</strong></div>
<div></div>
<div><strong><strong>Steve:
</strong></strong>
<div>All of those are excellent.  In particular, Amazon Echo has done a great job explaining the concept of an always on voice interface.  (I've been building this since before Echo was released, and at first people didn't believe what I was describing was possible yet.)</div>
<div></div>
<div>Google has done incredible work in leveraging "big data" and cloud computing resources to train their Speech to Text (STT) engine.  It is remarkably good at general purpose STT, including things like pop culture names.  Try saying "Nicki Minaj" or "Bjork" using their voice search and it works.  That would never have been possible with pre-cloud STT.</div>
<div></div>
<div>Apple did a great job of popularizing the concept of using your voice for input with Siri.  Again, that was a big iterative step.</div>
<div></div>
<div><strong>Jasper:
</strong><em>How do you think AI will influence our lives in the future? Do you imagine everyone will have a dedicated piece of hardware in their homes to use voice assistants or AI?</em><strong>
</strong></div>
</div>
<div></div>
<div><strong>Steve:</strong></div>
<div>
<div>Absolutely.  I think nearly everyone in industrialized nations already <i>do</i> have the hardware in their home.  The phones, desktops, laptops and tablets and gaming systems of today will provide the microphone and speaker needed to tie in to voice ecosystems (ideally for everyone there will be only one, but we'll see about that.)  Additionally, the components needed are so cheap that you will see this built into traditional consumer electronics like refrigerators, lamps and coffee makers as voice access points.</div>
<div></div>
<div>For AI in general, I think the impact will be subtle but powerful.  AI won't replace humans, but it will augment everything we do.  Instead of occupying my mind and hands driving my car, it will take me where I need to go while I am free to focus on important or creative or relaxing things.  Questions that used to take a long time to answer will be done nearly instantly without breaking my thought process, so I will be able to tackle even more outlandish projects.</div>
<div></div>
<div>"Create list of everyone who graduated from high school with me and extract the three dates next summer when most of them are free.  Then send those dates to everyone and use those results to find the highest rated restaurant with available banquet facilities to hold everyone."  That phrase 10 years ago would take a committee of humans literally a year to complete.  Today it can be done in months using email and the web.  In the future it will take me as long as it took me to say it — the results will be delivered to me later and I am free to invest my time elsewhere.</div>
<div></div>
<div>So maybe somebody will finally have time to invent the teleporter to go with our Star Trek computer.  :-)</div>
</div>
<div></div>
<div></div>
<div style="font-size: 75%; text-align: right;">photo credit: Ravi_Shah <a href="http://www.flickr.com/photos/24609568@N04/30153595842">285/366 - Snack Size</a> via <a href="http://photopin.com">photopin</a> <a href="https://creativecommons.org/licenses/by/2.0/">(license)</a></div>