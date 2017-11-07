---
ID: 1943
post_title: Kickstarter Delivery Update
author: Ryan Sipes
post_excerpt: >
  The Kickstarter delivery schedule has
  changed, but things are moving along at
  a fantastic pace and Mycroft is getting
  smarter every day!
layout: post
permalink: >
  http://mycroft.ai/blog/kickstarter-delivery-update/
published: true
post_date: 2016-07-15 12:08:59
---
It’s been a while since Mycroft put up an update for our Kickstarter backers, so I thought I’d take a moment to let folks know where the project stands.

I’m going to lead by telling you that the hardware failed the first FCC certification test. This will delay delivery for a month. The problem was only apparent when the lab connected cables to all of the CAT5E, USB and HDMI ports. It radiated because of the long grounding path between the Pi and the power supply. This ground was being sent through a 40 pin cable because we wanted to keep all of the components on one side of the board.

The software team has been doing a great developing the code and releasing it into the community. Our partner VocaliD did a fantastic job of capturing Alan Pope’s voice and the software stack is now running on several desktop platforms. We’ve been adding community members at a rapid pace and are working with the community to implement features and squash bugs.

This past week we released version 0.7.7 we updated the integration between the faceplate and the operating system, improved some of the deployed skills and added some additional configuration options. Yesterday we released version 0.7.8, building upon those improvements to the faceplate and making the interaction with Mycroft more fluid and enjoyable.
<h2><i>Device Changes </i> <span id="Frame3" dir="ltr"> </span></h2>
We've continued our integration of the faceplate with skills by updating it to work with the stock skill. Now, when you ask Mycroft what the stock price of a company is, it will display the company ticker and price, just like normal stock price displays!

<a href="https://mycroft.ai/wp-content/uploads/2016/07/mycroft_weather_face.jpg"><img class="aligncenter size-medium wp-image-1944" src="https://mycroft.ai/wp-content/uploads/2016/07/mycroft_weather_face-300x225.jpg" alt="mycroft_weather_face" width="300" height="225" /></a>

We've also started improving the user experience on the device by removing some of the delay with interacting with the button. Previously, when you pressed the button to stop a skill, you often had to wait a few seconds before it would actually stop. Now, skills should stop nearly instantaneously.<span id="Frame5" dir="ltr"> </span>
<h2>Wakeword Configuration</h2>
We've received many questions about changing Mycroft's name so that it will respond to whatever keyword you want. Listening to your feedback, we've made this configuration process much easier than before. Now, all you need to do is put the new name in the configuration file, as well as its pronunciation. Take a look at our <a href="https://docs.mycroft.ai/" target="_blank" rel="noopener">documentation</a> for more.<span id="Frame7" dir="ltr"></span>

As always, look at our <a href="https://docs.mycroft.ai/" target="_blank" rel="noopener">docs</a> for more information about using and contributing to Mycroft Core. Also, feel free to engage with us on our <a href="https://community.mycroft.ai/" target="_blank" rel="noopener">Community forums</a>. We'd love to hear your feedback!