---
ID: 38642
post_title: >
  What should be on our Raspberry Pi and
  Picroft Roadmap?
author: Kathy Reid
post_excerpt: >
  Help us understand where our Picroft
  roadmap needs to be prioritized. Should
  we work on hardware and microphone
  support first? On supporting Stretch
  Lite?
layout: post
permalink: >
  http://mycroft.ai/blog/picroft-roadmap-2018/
published: true
post_date: 2018-06-07 10:29:28
---
<a href="https://mycroft.ai/documenation/picroft">Picroft</a> - Mycroft on a Raspberry Pi - is the most popular way for people to get familiar with Mycroft software and to start experimenting with Skills and our other tools such as Precise, Padatious, and Mimic. To date, we’ve had tens of thousands of downloads of our <a href="https://mycroft.ai/to/picroft-image">Picroft disk image</a>, and it’s wonderful to be able to unite affordable open ARM-based hardware with our software to deliver an open source voice assistant.

Picroft has been around <a href="https://mycroft.ai/blog/mycroft-now-available-raspberry-pi-image/">since January 2017, when the first disk image was made available</a>. Since that time, it’s been based on the <a href="http://downloads.raspberrypi.org/raspbian_lite/images/">Raspbian Jessie Lite image</a>, and has been targeted at the Raspberry Pi 3 Model B. With <a href="https://www.raspberrypi.org/blog/raspberry-pi-3-model-bplus-sale-now-35/">new models of Raspberry Pi hardware being introduced</a> (particularly the powerful Pi3B+)  we are now at a crossroads.

The Raspbian Jessie Lite image is dated, and we must now consider a move to Raspbian Stretch Lite.
<h3>Differences between Raspbian Jessie and Raspbian Stretch</h3>
Raspbian Stretch contains several improvements over Raspbian Jessie.
<ul>
 	<li>The Bluetooth stack now uses the <a href="https://github.com/Arkq/bluez-alsa">Bluez-ALSA</a> package instead of PulseAudio; this means that PulseAudio is not installed by default</li>
 	<li>Instead of automatically logging in as the pi user, Stretch has implemented login with the passworded name of the current user</li>
 	<li>In another security measure, the <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9417">Broadpwn</a> vulnerability in the BCM43xx wireless chipset is also resolved in Stretch</li>
</ul>
<h3>What are the ‘Lite’ versions of Raspbian?</h3>
The Raspbian distro is available in two flavours - a main distribution and a ‘Lite’ version. The ‘Lite’ version is cut-down and removes the desktop environment, which consumes memory and CPU, providing only a command line interface (CLI). For example, the main Stretch distribution includes the audio creation tool, <a href="https://sonic-pi.net/">Sonic Pi</a>, which can be used to create incredible synthesized sounds (and some pretty kick-ass drum and bass if you ask Kathy).

The intent of the ‘Lite’ version is primarily for development and IoT purposes - where having a ‘heavy’ desktop environment impedes the function that the Raspberry Pi is being used for.

That’s exactly why we’ve chosen the ‘Lite’ version of Raspbian to power Picroft in the past - we want to reserve as much CPU and memory as possible for functions such as text-to-speech (TTS) processing and Wake Word recognition.
<h3>What are our challenges for the next Picroft version?</h3>
It sounds straightforward doesn’t it - we simply re-package Picroft using Stretch Lite as the base distribution, rather than Jessie Lite. However it’s a little more complicated than that.

Stretch significantly reworked the audio subsystem.  In general this is a good thing, but some of these changes broke compatibility with the way Mycroft accesses the microphone.  Until this is solved, transitioning to Stretch won’t be possible. Unfortunately for the Raspberry Pi 3+ the new wifi chipset requires Stretch and won’t work with Jessie.

We intend to have a single unified image for the Raspberry Pi 3 and Pi 3+.  But at the moment we are at an awkward spot where only the Pi3 is functional with Mycroft.  <a href="https://community.mycroft.ai/t/raspberry-pi-3-model-b-compatibility/3297/6">Fortunately some of our community members have had luck experimenting in this vein, so we are optimistic this can be resolved</a>.

While most parts of Picroft work ‘out of the box’, audio configuration is the most problematic part of getting a Picroft up and running, particularly if you want to use audio out through Bluetooth or HDMI; we want to improve this to reduce frustration for new Picroft users.
<h3>What’s the current state of play and where do we go from here?</h3>
We have many competing demands on the Picroft roadmap.
<ul>
 	<li>Is Picroft inherently a developer platform, and as such should we be focusing on <a href="https://mycroft.ai/documentation/skills/introduction-developing-skills/">debugging tools for Skill Authors</a>?  Or is it being used for “production” purposes and needs more support for a broader range of microphones?  Should there be different images to support these two functions?</li>
 	<li>Can we create native support for the popular <a href="https://aiyprojects.withgoogle.com/">Google AIY hardware</a>, and most importantly can we distribute it on the same Picroft image?  AIY requires special drivers.</li>
 	<li>Can we support <a href="https://www.raspberrypi.org/blog/magic-mirror/">Magic Mirror systems with Picroft</a>?  This likely needs the more powerful Raspberry Pi 3+ which can support running a GUI.</li>
 	<li>Should we engage with other dedicated images for tools that could benefit from voice control, such as <a href="https://openelec.tv/">OpenELEC</a> or <a href="https://www.home-assistant.io/">Home Assistant</a>?</li>
</ul>
As you can see, our roadmap here is not straightforward - and your feedback can help shape where we take it, ensuring that we align our actions with community needs.
<h3>How can you help?</h3>
<a href="https://www.surveymonkey.com/r/picroft-june-2018">We’d really appreciate you letting us know how you use Picroft. </a>What model Raspberry Pi are you using? What speakers and microphone do you use? Do you have a Raspberry Pi Model 3B+ and are hanging out for a working Picroft image?<a href="https://www.surveymonkey.com/r/picroft-june-2018"> Take our super-quick survey and help us help you. </a>

If you’re an advanced user, you might even want to have a go at <a href="http://mycroft.ai/documentation/picroft/picroft-image/">building your own Picroft image.</a>

Let us know what you think below.