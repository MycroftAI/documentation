---
ID: 1334
post_title: >
  Creating the Production Prototype, and
  Adapt 0.2 Released!
author: Ryan Sipes
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/production-prototype-adapt-2/
published: true
post_date: 2016-01-20 15:05:31
---
The hardware team has the first production prototype boards off the printer and they are on their way. Once they show up we'll start integrating them into our first production prototype, which will be very similar, if not identical, to the unit that our backers will be getting. No more benchtops covered in jumper wires!

[caption id="attachment_1337" align="alignnone" width="1280"]<img class="alignnone size-full wp-image-1337" src="https://mycroft.ai/wp-content/uploads/2016/01/mycroft_splayed.jpg" alt="mycroft_splayed" width="1280" height="960" /> Arron testing Mycroft hardware with jumper wires on the bench.[/caption]
<h3>Adapt Update</h3>
Adapt will now run on Python 3. Igor Vuk, a member of the Mycroft community took the time to make the Adapt engine work with Python 3. Thanks so much Igor for your contribution!

Other community members are making contributions and doing interesting things with Adapt as well! For instance, community member: B00703D is building an IRC bot using open source python-based IRC bot Sopel and the Adapt Intent Parser.
<h3>New Skills</h3>
In addition to several performance improvements, the dev team has built out some of the promised skills this week. We've implemented a reminder skill that lets you tell Mycroft to remind you of a task in the future. For instance, you could say "Hey Mycroft, remind me to take out the trash at 7 AM" and you can count on a reminder to take out the trash promptly at 7:00 AM.

We've also implemented a sleep skills that allows you to put Mycroft to "sleep" so that he ignores his keyword. This is useful if you are having a lot of conversations about Mycroft in your offices, or using the work Mycroft a lot during a presentation (so this skill is very relevant to the Mycroft team). You can wake Mycroft easily with "Wake up Mycroft".
<h3>System Core Update</h3>
[caption id="attachment_1355" align="alignnone" width="3225"]<img class="alignnone size-full wp-image-1355" src="https://mycroft.ai/wp-content/uploads/2016/01/front_back.png" alt="Back of faceplate PCB, that connects the LED matrixes, microphone, and IR sensor." width="3225" height="1122" /> Back of faceplate PCB, that connects the LED matrixes, microphone, and IR sensor.[/caption]

We're now able to write the Arduino sketch via the Raspberry Pi using the ICSP header on the Arduino board. This allows us to update both the Mycroft software and the faceplate software at the same time. We've also implemented a service that listens to the onboard message bus and triggers the various faceplate behaviors. This allows us to accurately time the animations and expressions on the screen to coincide with the AI's behavior.