---
ID: 40526
post_title: 'Major Picroft Update &#8211; Moving to Raspbian Stretch'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/major-picroft-update-moving-to-raspbian-stretch/
published: true
post_date: 2018-09-12 20:00:57
---
<h1><span style="font-weight: 400;">It’s Alive!</span></h1>
There's a brand new Picroft image available! <span style="font-weight: 400;"><a href="https://github.com/MycroftAI/enclosure-picroft/tree/stretch" target="_blank" rel="noopener">Click here to get setup instructions.</a> Read on to learn more.</span>

<span style="font-weight: 400;">In late 2016 I created the </span><a href="https://mycroft.ai/blog/mycroft-now-available-raspberry-pi-image/"><span style="font-weight: 400;">original Picroft</span></a><span style="font-weight: 400;"> as a way for anyone to interact with Mycroft, not just those who were able to purchase the Mark 1. Since then, Picroft has been downloaded more than 35,000 times. It has become the basis for numerous Raspberry Pi projects, like </span><a href="https://community.mycroft.ai/t/creating-my-first-skill-with-essentially-no-experience-mycroft-magicmirror-skill/3526/" target="_blank" rel="noopener"><span style="font-weight: 400;">Magic Mirrors</span></a><span style="font-weight: 400;">, </span><a href="https://www.hackster.io/gov/hey-mycroft-turn-on-the-lamp-5e2d12" target="_blank" rel="noopener"><span style="font-weight: 400;">home automation systems</span></a><span style="font-weight: 400;">, </span><a href="https://community.mycroft.ai/t/first-steps-into-the-big-wide-world/3623" target="_blank" rel="noopener"><span style="font-weight: 400;">robots</span></a><span style="font-weight: 400;">, and hundreds of other wonderful testaments to creativity.</span>

<span style="font-weight: 400;">Picroft was designed to self-update, and we did publish some new versions periodically to simplify moving to major new releases. It has held up well and essentially remained the same for the last two years.</span>

<span style="font-weight: 400;">However, the new Raspberry Pi 3B+ introduced new chipsets that broke Picroft. The original Pi 3 is still available, but this was a good reason to show Picroft some love and introduce some cool new stuff.</span>

[caption id="attachment_40527" align="alignnone" width="1316"]<a href="https://mycroft.ai/wp-content/uploads/2018/09/lightning-2018-08-01.jpg"><img class="wp-image-40527 size-full" src="https://mycroft.ai/wp-content/uploads/2018/09/lightning-2018-08-01.jpg" alt="The electricity that gave Picoft life will be how Picroft gives life to your Raspberry Pi projects." width="1316" height="640" /></a> This was the sky the night I started rebuilding the Picroft image. Fitting, right?[/caption]
<h1><span style="font-weight: 400;">What’s New?</span></h1>
<span style="font-weight: 400;">Lots of little things, and a few big things. Once things are up and running, it will still be Mycroft -- a voice interface. The main changes are at the setup and “plumbing” level. We also listened to the findings of our </span><a href="https://mycroft.ai/blog/picroft-survey-2018-results/" target="_blank" rel="noopener"><span style="font-weight: 400;">Picroft survey</span></a><span style="font-weight: 400;"> -- thanks to all who participated!</span>
<h3><span style="font-weight: 400;">Stretch’ing ourselves</span></h3>
<span style="font-weight: 400;">With the release of the Raspberry Pi 3B+ hardware changes required a new release of the Raspbian operating system. The new version is referred to as “Stretch” (following the tradition of Toy Story references). Picroft is now based on this latest version of Raspbian, allowing support for both the Raspberry Pi 3 and the 3B+.</span>
<h3><span style="font-weight: 400;">No more packages, go Git it</span></h3>
<span style="font-weight: 400;">To simplify and unify the Mycroft experience on the various platforms, we rethought how Mycroft should sit on the Raspberry Pi. At the low level, we switched from a Debian package install (which was originally a hack of the Mark 1 package that just disabled the faceplate) to a Github-based install that can be set to automatically update.</span>

<span style="font-weight: 400;">This unifies the Picroft environment with what most desktop developers are using, allowing us to simplify documentation.</span>
<h3><span style="font-weight: 400;">Wizards!</span></h3>
<span style="font-weight: 400;">One of the recurring issues users encounter is difficulty in configuring the audio pieces. Linux is incredibly flexible, but </span><i><span style="font-weight: 400;">nobody</span></i><span style="font-weight: 400;"> wants to deal with the audio subsystems if they can avoid it. Configuring sound drivers is full of alchemy and dark magic. Connecting to all the different kinds of wifi security protocols is a whole different book of incantations.  So we are including a Wizard with Picroft to help cast these spells!</span>

<span style="font-weight: 400;">During the initial setup, the user is now presented with a series of simple questions to configure the network connection, pick the type of microphone and audio output they want to use, and configure security options based on their intended use.  Configuration happens automatically, and tests immediately verify the speaker output and sound levels, and the microphone input.</span>
<h3><span style="font-weight: 400;">MOAR Microphones</span></h3>
<span style="font-weight: 400;">We have a great community who have proven that Mycroft can operate with nearly any kind of hardware. Over the next few days, the Picroft image will incorporate support for the Google AIY Voice Kit array microphone. In the future, there will be an easy path for automating the install of other microphones, such as the <a href="https://www.matrix.one/products/creator" target="_blank" rel="noopener">Matrix Creator</a> and <a href="https://www.seeedstudio.com/ReSpeaker-4Mic-Array-for-Raspberry-Pi-p-2941.html" target="_blank" rel="noopener">Seeed ReSpeaker</a>.</span>
<h3><span style="font-weight: 400;">Environment Helpers</span></h3>
<span style="font-weight: 400;">As I developer, I feel justified in making fun of every time one of us answers a question by saying something like:</span>

<i><span style="font-weight: 400;">Oh, that is really simple. First <code>pip install pyjokes</code>. Then just type <code>python -m test.integrationstests.skills.runner</code>. You are in the virtual environment, right? Oh, well you just need to do <code>source /opt/venvs/mycroft-core/bin/activate</code> before that. Still not working? Oh, were you in the venv when you did the pip install? ...</span></i>

<span style="font-weight: 400;">I’ll let you in on a secret -- this is also a pain for us and we probably mistype these commands half the time.</span>

<span style="font-weight: 400;">As part of this overhaul, we’ve unified most Mycroft related commands under a <code>mycroft-</code> prefix. This is particularly helpful because you can now take advantage of Linux’s excellent auto-completion by typing <code>my&lt;TAB&gt;</code> to get to <code>mycroft-</code>, then hit TAB two more times to see all the options available for you.</span>

<span style="font-weight: 400;">Helpers include:</span>
<ul>
 	<li><span style="font-weight: 400;">mycroft-help</span> <span style="font-weight: 400;">Get brief summaries of the commands</span></li>
 	<li><span style="font-weight: 400;">mycroft-pip</span> <span style="font-weight: 400;">Install Python packages inside the Mycroft venv</span></li>
 	<li><span style="font-weight: 400;">mycroft-msm</span> <span style="font-weight: 400;">Invoke the Mycroft Skills Manager</span></li>
 	<li><span style="font-weight: 400;">mycroft-msk</span> <span style="font-weight: 400;">Mycroft Skill Kit, submit and manage skills in the community repos</span></li>
 	<li><span style="font-weight: 400;">mycroft-speak</span> <span style="font-weight: 400;">Make mycroft speak for you (handy inside scripts)</span></li>
 	<li><span style="font-weight: 400;">mycroft-say-to</span> <span style="font-weight: 400;">Send a string to Mycroft, just like you spoke it (also handy for scripts)</span></li>
</ul>
<span style="font-weight: 400;">These same tools are also available under all other environments now.</span>
<h1><span style="font-weight: 400;">What Else Can You Look Forward To?</span></h1>
<span style="font-weight: 400;">We’ll be providing Skills that are unique to the Picroft environment, allowing you to attach buttons to the GPIO pins to emulate the Mark 1 button. Or use this example to do whatever else you might want to do -- this is your Picroft!</span>

<span style="font-weight: 400;">As mentioned above, we’d like to expand the microphone and audio hardware supported by Picroft. With a little help from community members, I expect we’ll have support for various USB and Bluetooth mics and speakers soon. <a href="https://community.mycroft.ai/t/major-picroft-update-moving-to-raspbian-stretch/4522" target="_blank" rel="noopener">Join us on the forums</a> to give feedback on AIY integration, how to pipe in new mics, and what you'd like to connect over GPIO.</span>
<h1><span style="font-weight: 400;">Gimme, Gimme, Gimme!!!</span></h1>
<span style="font-weight: 400;">You can download the new Picroft image from </span><a href="https://mycroft.ai/to/picroft-image" target="_blank" rel="noopener">https://mycroft.ai/to/picroft-image</a><span style="font-weight: 400;">. Learn all about it (including exactly how it was built) from </span><a href="https://github.com/MycroftAI/enclosure-picroft/tree/stretch" target="_blank" rel="noopener">https://github.com/MycroftAI/enclosure-picroft/tree/stretch</a><span style="font-weight: 400;">.</span>

<span style="font-weight: 400;">Go, download, and hack!</span>