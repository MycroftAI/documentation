---
ID: 1916
post_title: 'Mycroft Core, v0.7 - Responsive Listening, 3rd Party Skills'
author: Ryan Sipes
post_excerpt: 'Today marks the release of a new version of Mycroft. This moves us from the 0.6.X versioning to 0.7 - putting us closer to a 1.0 release. This is a significant update because it contains a large rethinking of the listener that Mycroft uses. The result is our new "Responsive Listening" mode.'
layout: post
permalink: >
  https://mycroft.ai/blog/version-0-7-responsive-listening/
published: true
post_date: 2016-06-18 12:59:33
---
Today marks the <a href="https://github.com/MycroftAI/mycroft-core/releases">release of a new version of Mycroft.</a> This moves us from the 0.6.X versioning to 0.7 - putting us closer to a 1.0 release. This is a significant update because it contains a large rethinking of the listener that Mycroft uses. The result is our new "Responsive Listening" mode.

When we began experimenting with the Mycroft Core listener, the part of the code that listens for a command, we embarked on creating a concept of passive listening. Passive listening processed an audio buffer, looked for the wake word, and then processed the query. We found in practice that this allowed us to say things in a very unstructured way and they could still be processed, such as:

"What's the weather Mycroft?"

"Hey there Mr. Mycroft, I'd like to know what time it is."

"Hey Mycroft, how do you spell hippopotamus?"

This was an interesting paradigm in interacting with the device. But in practice passive listening resulted in long processing time, false positives, and parts of sentences getting processed that weren't the intended query. The best intentions never go unpunished. As a result, we took it upon ourselves this past week to provide a more consistent experience, stable experience.
<h3><strong>Introducing Responsive Listening</strong></h3>
In this 0.7 release, I'd like to introduce the concept of "Responsive Listening". Responsive listening is the kind of Call-and-Response interaction you may be accustomed to from other electronic personal assistants, such as the Amazon Echo and Google Assistant ("OK Google"). This mode is also represented in our <a href="https://www.youtube.com/watch?v=m4L0QfzUeEI" target="_blank">Kickstarter video</a>. This mode will serve as the default until such a time that we feel more natural queries can be included into the software again. A query now follows this format:

Wake word and then query. (See example below)

<strong>"Hey Mycroft</strong> (&lt;- keyword)<strong>, what time is it</strong> (&lt;- query)<strong>?"</strong>

<strong>"Hey Mycroft, what's the weather in Paris?"</strong>

<strong>"Hey Mycroft, what's the news?"</strong>

<strong>"Hey Mycroft, tell me about Abraham Lincoln."</strong>

A return to this form of interaction allows us to provide a good experience for our users which should drive adoption while we continue to experiment with many other ways of interacting with Mycroft going forward.
<h4><strong>Improved "Face" Animations</strong></h4>
Those with hardware developer kits should see improved animations on the units LED display and neopixel ring. We have worked on improving the code that governs the "face" of Mycroft and have included some animations to give users more feedback. This should make the experience of using the unit more engaging and enjoyable.

We look forward to opening the code that governs the face to the public in the near future, the final pieces needed for this are some code cleanup, commenting, and documentation. We are working hard to put this in place to allow for it to be opened up to all.
<h4><strong>3rd Party Skills
</strong></h4>
Thanks to community member The7erm ("Erm" for short), 3rd party skills can now be placed in a set folder location and loaded when the skills service is started. You can take a look at the <a href="https://github.com/MycroftAI/mycroft-core/pull/168" target="_blank">specifics of the pull request here</a>. This is the beginning of an initiative to build up an ecosystem of skills that users can install on their Mycroft instances, that customize the experience to meet their needs.

In order to continue to drive 3rd party skill development, the Mycroft team is working on setting up a skills repository from which users will be able to download and install 3rd party skills. This big initiative is quickly becoming a top priority, and will garner a good amount of resources on our end in order to accomplish it.
<h4><strong>Debian APT Repo</strong></h4>
Our systems administrator, Arron Atchison, has been working hard to package up Mycroft Core and related projects (like Mimic) as debs and put them into a APT repository. This should allow more people to easily download and install Mycroft Core and use it on various devices and distributions such as Ubuntu, Debian, and Raspbian. We are hoping this lowers the bar, allowing more people to access the technology and assess it.

The repo is not quite available yet, but should be sometime in the upcoming week. If you would like to help accelerate this process, please contact <a href="mailto:arron.atchison@mycroft.ai" target="_blank">Arron via Email</a> or <a href="https://mycroft-ai-slack-invite.herokuapp.com" target="_blank">on our Slack channel</a> (username @aatchison)
<h4><strong>Mycroft Gets a New Voice</strong></h4>
That's right, Alan "Popey" Pope so graciously offered up his voice, and our partners over at VocaliD packaged it up and we've now stuck it in Mycroft Core. So as part of the v0.7 release, Popey's voice has been included as the default. It still sounds a little robotic, but we are happy to be using it and it is being released under a creative commons license. Please pull down the new version and give it a listen.
<h4><strong>Things to Come</strong></h4>
We have quickly seen an explosion in community engagement and growth around the <a href="https://github.com/MycroftAI/mycroft-core" target="_blank">Mycroft Core Project</a>. We currently have projects underway to revamp our account management service, called Cerberus. We also have a very early <a href="https://community.mycroft.ai/t/mycroft-community-site/651" target="_blank">Community Website Project</a> underway, which we'd love the Community to participate in.

If you are interested in learning about using and contributing to Mycroft Core, <a href="https://docs.mycroft.ai/" target="_blank">see the docs</a>. Remember to check out our <a href="https://community.mycroft.ai/" target="_blank">Community forums</a> and engage with us there.