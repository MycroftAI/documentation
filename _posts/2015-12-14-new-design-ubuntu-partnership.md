---
ID: 1157
post_title: 'Weekly Update: Design Breakdown and Ubuntu Partnership'
author: Ryan Sipes
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/new-design-ubuntu-partnership/
published: true
post_date: 2015-12-14 09:00:11
---
<h3><strong>Hardware and Design</strong></h3>
Derick Schweppe has been hard at work completing the production models for the physical device.  He took some time this week to put together an exploded view of Mycroft (pictured above) so that our fans and backers can see what makes it tick.  Here are some of the more interesting features:

<strong>Reversible Housing</strong> - The Mycroft housing is reversible.  The top and the bottom are the exact same part.  We did this primarily to save on tooling costs, but it turned out to be a great idea.  For example, the holes that allow sound out on the bottom are perfectly placed to allow cooling in from below.

<strong>Camera Ribbon Pass Through &amp; Accessory Mounting Holes</strong> - It occurred to us that many of our backers are going to want to add a camera to Mycroft, so we added a slot that makes it easy to thread a camera module cable through to the Pi's CSI camera connector.  There is a second one for folks who might also want to use the DSI display connector.

<strong>Hack Me Port</strong> - Backers with a hacker mentality can replace this insert with the mounting hardware of their choice.  It is aligned with the unit's center of gravity so it allows for mounting on a servo head, bracket, gimbal or robot of your choice.

<strong>Rear Mounting Plate</strong> - As you might remember from our video, the original design required the Pi to be installed sideways.  This allowed us to connect to the USB port in order to power the faceplate Arduino controller and to provide audio through a USB mic.  The new orientation allows us to expose all 4 USB ports as well as the ethernet port.  We will then jumper over the HDMI port.  The top of Amplifier/MIC/IO/Power PCB will include the 40 PIN IO header, RCA ports and 12V power port.  This means that users can use any of the 3 free USB ports (one will have a WiFi dongle).  The Arduino is now powered by the power board and connected to the Pi over GPIO.

<strong>Silicone Feet</strong> - The 10W speaker and amp we selected is LOUD, so we want to be sure Mycroft doesn't vibrate and dance his way off of your counter and onto the floor.  We added silicone rubber feet which insulate Mycroft from the surface.  These are removable so you can take them out if you mount Mycroft under a counter or on a robot frame.
<h3><strong>Official Ubuntu Partnership</strong></h3>
Mycroft has continued to deeper its ties with Canonical <a href="http://partners.ubuntu.com/find-a-partner?search=Mycroft" target="_blank" rel="noopener">by becoming an official Ubuntu partner for IoT</a>. We are continually grateful for Canonical and team's commitment to this technology, and their support and guidance as we continue to grow as a project. We look forward to what this partnership will bring in terms of innovation and community engagement, and have the highest hopes for a bright future in this respect.
<h3><strong>Mycroft Feature Video</strong></h3>
The team finished another feature video this week.  These feature videos will appear periodically through mid 2016.  Each video highlights one or more Mycroft feature and shows it in every day use.  Our first feature?  Netflix, and the ability to "set a scene" using IoT integration.

https://youtu.be/zIwMLisqNP8

If you haven't seen our last video, featuring an awesome drone - check it out here!

As always, we want to thank our backers and fans who have supported us up to this point, we are elated at the amazing community that has formed around the project - and look forward to what we can accomplish together!

<strong>IMPORTANT: </strong>Remember that pre-orders for Mycroft end on the 31st of December! <a href="http://igg.me/at/mycroftai/x/9533694" target="_blank" rel="noopener">You can order here!</a>