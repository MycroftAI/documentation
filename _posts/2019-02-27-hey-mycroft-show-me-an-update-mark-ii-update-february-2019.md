---
ID: 45175
post_title: 'Hey Mycroft, Show me an Update &#8211; Mark II Update February 2019'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/hey-mycroft-show-me-an-update-mark-ii-update-february-2019/
published: true
post_date: 2019-02-27 16:00:51
---
<span style="font-weight: 400;">In our </span><a href="https://mycroft.ai/blog/mark-ii-update-january-2019-current-progress/"><span style="font-weight: 400;">January Mark II Update</span></a><span style="font-weight: 400;">, we highlighted the five areas that were in progress. All five have been making changes and improvements, but it’s been a slow journey for the hardware and we’ll have much more to say in March. Fortunately, we have been able to push forward quickly with development for the Mark II graphics software and now, you can get a head start!</span>
<h1><span style="font-weight: 400;">Lemons into Lemonade</span></h1>
<span style="font-weight: 400;">The Mycroft GUI architecture has been built around the cross-platform KDE Plasma technologies and a network communication protocol. This creates several opportunities to allow the devs to continue refining the graphical interface on independent development hardware.</span>

<span style="font-weight: 400;">Additionally, the architecture allows the connection of off-device screen displays which I expect we will be exploring more in the future. Imagine a richer Magic Mirror or smart dashboard experience controlled by voice.</span>
<h1><span style="font-weight: 400;">KDE Plasma</span></h1>
<span style="font-weight: 400;">I've spoken previously of our </span><a href="https://mycroft.ai/blog/mark-ii-update-january-2019-current-progress/#graphics-kde-mycroft"><span style="font-weight: 400;">work with the KDE Plasma team</span></a><span style="font-weight: 400;">, and I continue to be impressed by the individuals and technologies they've brought to the cause. The first floor of the graphical interface that we’ve built on top of their foundational technology is robust and feature-rich.</span>

<span style="font-weight: 400;">The core of the graphical system is built around the concept of “Pages” built using QML. The Q markup language (QML) is a hybrid of Javascript and CSS which has been refined over the past decade. It is well-suited for rapid interface development and optimized for smooth animations and device independence – adjusting to the size of the presentation screen.</span>

<span style="font-weight: 400;">Since the beginning of the year, we have closed the loop on this front. With QML, we can display information and pass back information to Mycroft as well as Skills running under Mycroft. This allows Mycroft to combine verbal and visual interactions seamlessly and beautifully.</span>
<h1><span style="font-weight: 400;">A Picture is Worth a Thousand Words</span></h1>
<span style="font-weight: 400;">The old adage is true – many times a graphic display is far more efficient for conveying information than words. A single-day forecast can be spoken efficiently, but speaking a 10-day forecast is painfully slow and ineffective.</span>

<span style="font-weight: 400;">So, I’ll follow that advice and let the following video do the rest of the talking.</span>

<iframe src="https://www.youtube.com/embed/-HJKDKgW2jI" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<h1><span style="font-weight: 400;">Where’s the Beef?</span></h1>
<span style="font-weight: 400;">Talk is good, and pictures are worth 1000 words, but what about the code? Well, guess what! You can see everything we’ve got for Mycroft GUI development and even start building skills with graphics! The repo is at <a href="https://github.com/mycroftai/mycroft-gui">https://github.com/mycroftai/mycroft-gui</a> and we can’t wait to see what you make!</span>