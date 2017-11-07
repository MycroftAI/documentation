---
ID: 1409
post_title: 'Startup Challenges – It&#8217;s not all Rainbows and Unicorns'
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/startup-challenges-its-not-all-rainbows-and-unicorns/
published: true
post_date: 2016-02-08 13:27:17
---
I recently read a <a href="https://medium.com/kickstarter/how-zano-raised-millions-on-kickstarter-and-left-backers-with-nearly-nothing-85c0abe4a6cb#.j1msd4f40" target="_blank" rel="noopener">great article commissioned by Kickstarter about the demise of Zano</a>. For those of you who don't know, Zano raised $3.5M dollars on Kickstarter to build a drone. The company then imploded spectacularly before delivering a working product. The article was worth the time because it highlighted the many mistakes of Zano's management. One of those mistakes was failing to communicate their challenges to backers. Zano updates were almost uniformly positive right up until the company folded.

The Mycroft team has a lot more experience than Zano's team did, but we can still learn from their mistakes. That is why I've decided to spend this week updating our backers on the many challenges we face as we work to build the Mycroft platform.

Please don't mistake this update for dire news or foreshadowing of doom. The project is going well, the technology is working well and we're on track to deliver to our backers on time. I just wanted to be sure that folks understand that building something as complex as Mycroft isn't all unicorns and rainbows.

<b>Drivers</b>

The first audio chip we selected seemed to be perfect and, if we were using Windows it would have been. What we found when we went to put it to use, however, was that Linux support for the chip was extremely limited. This meant hacking together kernel modules and finding the one or two individuals out there who had tried to integrate the chip previously.

After about a week of work we decided that it made more sense to select a chip that was widely supported than to try to develop and maintain drivers for an unsupported chip. Though this little detour took some time, it did pay off in the form of a much deeper understanding of how Linux deals with audio.

<b>Neopixels</b>

We've been updating backers regularly on the progress of our hardware. This past week we finally assembled both the main board and the faceplate.

When assembling the RGB neopixels that make up Mycroft's eye rings it quickly became apparent that we were going to need to use a reflow oven to mount these parts. This meant purchasing an oven and controller. In the mean time, the parts we attempted to assemble using traditional soldering methods were ruined by heat.

We also found that the neopixels seemed to work for a short time before they began behaving unpredictably. Because this problem was intermittent we had a very hard time figuring out what was going on. Was it noise on the serial bus? Was is a power issue? Nope. After working on this problem for several days we realized that we were testing at full brighteners. The resulting heat was causing the neopixels to malfunction. We turned down the maximum brightness and suddenly the problem was gone, but so were several days of development effort.

<b>JST Connectors</b>

The same was true for the JST connectors. We selected a common connector type and pitch, but even though we have the correct wire, pins and crimpers in house it turns out that it is enormously difficult to make reliable cables using this connector type. It also turns out that it is difficult to find factory connectors that have 7 wires.

As a result we have switched to a larger pitch connector (the type used to monitor cell voltage in LiPo batteries). These connectors are much easier to work with and cables are readily available.

<a href="https://mycroft.ai/wp-content/uploads/2016/02/mycroft_brain.jpg" rel="attachment wp-att-1411"><img class="aligncenter size-medium wp-image-1411" src="https://mycroft.ai/wp-content/uploads/2016/02/mycroft_brain-300x225.jpg" alt="mycroft_brain" width="300" height="225" /></a>

<b>Microphone Noise</b>

The performance of Mycroft's microphone is critical to the platform's key word and speech recognition algorithms. Unfortunately in our initial board revision we routed the microphone audio trace too close to the serial bus connecting the Raspberry Pi to the Arduino. The result was an extremely loud background buzz in the audio stream. The noise was so loud, in fact, that we had trouble getting the AI to respond at all.

To solve the problem we moved several of the components around on the board and moved the microphone ground directly adjacent to the device ground. We tested this configuration by directly soldering a microphone to the board and it solved the problem. We are now getting crystal clear audio from the mic.

<b>Metal as a Service</b>

Though much of Mycroft's back end is hosted in the cloud, we did install a half dozen Dell servers with 24 cores and 48 Gb of ram. These servers were set up to use metal as a service. This software allows data center administrators to scale easily and deploy virtual machines with little or no effort.

In our case this worked fine, until we had a minor power glitch and, through a comedy of errors, ended up overwriting a LVM that contained several important data sets.

As can be expected of any major glitch, the problem happened right before a major demo. This caused us a lot of stress and made it very hard to get the back-end back online in a timely way. We eventually restored everything from backups, but it was a detour we could have done without.

<b>Team, Team, Team</b>

The team behind Mycroft has come together nicely. Everyone is getting along, communications have been solid and we have the right people with the right skills. That said, one of our team members is in Brazil, one in New York and one in Seattle. This sometimes makes it hard to schedule meetings, collaborate in real time or get questions answered quickly.

<b>Future Challenges</b>

There are obviously going to be additional challenges in our future. We are going to have to solve logistical problems related to inventory, scale our back end to support tens of thousands of users and raise enough money to grow the Mycroft team from 10 dedicated team members to the several dozen that are necessary to support and grow the Mycroft platform.

We've got a great team working to solve these problems. We've got the technical talent, business acumen and drive to make Mycroft a success, but it isn't easy. There are challenges and barriers, but we've got the skills to surmount them and build the world's first truly open AI.