---
ID: 40775
post_title: 'The Mycroft Personal Server &#8211; Starting the Conversation'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/mycroft-personal-server-conversation/
published: true
post_date: 2018-10-01 11:33:02
---
<span style="font-weight: 400;">In my July post where I introduced the Mycroft </span><a href="https://mycroft.ai/blog/many-roads-one-destination/" target="_blank" rel="noopener"><span style="font-weight: 400;">Roadmaps</span></a><span style="font-weight: 400;">, I laid out plans for a Mycroft </span><a href="https://docs.google.com/document/d/1VJsk9xmFig1qAP-wH_SAB-3xyKRx28Z47IwlJWJMqOM" target="_blank" rel="noopener"><span style="font-weight: 400;">Personal Server</span></a><span style="font-weight: 400;">. I’ve had conversations with many about the concept, but exact goals and designs haven’t been established yet. I see this as a highly Community-centric project, so I’d like to start a conversation so we can all get on the same page.</span>
<h1><span style="font-weight: 400;">What is it?</span></h1>
<span style="font-weight: 400;">Mycroft is inherently modular, allowing pieces of the system to be moved around as appropriate for the specific implementation. Up to this point, the typical implementation runs the majority of Mycroft on a device such as a Mark 1, Raspberry Pi, or laptop. This includes Wake Word processing, intent parsing, and text to speech(TTS)</span><span style="font-weight: 400;"> (more on Mimic2 TTS below)</span><span style="font-weight: 400;">.</span>

<span style="font-weight: 400;">For normal operation, there is one critical piece isn’t included in that list -- Speech to Text (STT). The typical Mycroft device today uses Mycroft’s </span><a href="http://home.mycroft.ai" target="_blank" rel="noopener"><span style="font-weight: 400;">Home</span></a><span style="font-weight: 400;"> to perform the STT operation. This is automatic and invisible to most users.</span>

<span style="font-weight: 400;">The server also offers several other services that are important:</span>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Mimic2 for those using this new voice technology</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">General </span><a href="https://home.mycroft.ai/#/setting/basic" target="_blank" rel="noopener"><span style="font-weight: 400;">user settings</span></a></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Web interface to specific </span><a href="https://home.mycroft.ai/#/skill" target="_blank" rel="noopener"><span style="font-weight: 400;">Skill Settings</span></a></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">The </span><a href="https://market.mycroft.ai" target="_blank" rel="noopener"><span style="font-weight: 400;">Marketplace</span></a><span style="font-weight: 400;"> to find and install new skills</span></li>
</ul>
<span style="font-weight: 400;">In my view, the Personal Server would provide some version of all of these services. It should allow a household to run all of their Mycroft equipment without any network necessary until a Skill needs to access the internet to retrieve information.</span>

<span style="font-weight: 400;">This means the personal server would at minimum need to run Speech to Text (DeepSpeech), Text to Speech (Mimic), and provide a configuration web interface.</span>
<h1><span style="font-weight: 400;">Why would anyone need this?</span></h1>
<span style="font-weight: 400;">There are several very good reasons for implementing this capability.</span>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;"><strong>Slow, unreliable internet</strong> - </span><span style="font-weight: 400;">I’m personally spoiled by Google Fiber here in Kansas City and forget that not everyone in the world has gigabit connection speeds.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;"><strong>Limited or expensive internet</strong> - </span><span style="font-weight: 400;">Similar to the above, but slightly different motivation</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;"><strong>No internet</strong> - </span><span style="font-weight: 400;">Yes, this exists. Imagine locations in the mountains, on boats, or the far side of the moon.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;"><strong>Privacy concerns</strong> - </span><span style="font-weight: 400;">Every time data leaves your control, there is a possibility of others misusing it, not safeguarding it adequately, or it being intercepted.</span></li>
</ul>
<span style="font-weight: 400;">For those willing to accept the responsibility, keeping all operations within a home provides the ultimate in reliability and security.</span>
<h1><span style="font-weight: 400;">What a Personal Server Isn’t</span></h1>
<span style="font-weight: 400;">The Personal Server is intended to be Personal -- not Enterprise Grade. The main reason for this is simplicity. For example, if you don’t have to perform Speech to Text requests for thousands of users, the odds of collision are very low. That means STT requests can be run sequentially instead of requiring a bank of STT servers that can handle a high load.</span>

<span style="font-weight: 400;">A Personal Server also isn’t for everyone. You don’t have to be a High Geek but it will require some significant computational resources, like an always-on PC with a high-quality GPU.</span>
<h1><span style="font-weight: 400;">Does this mean Home is no longer needed?</span></h1>
<span style="font-weight: 400;">No, for several reasons.</span>

<span style="font-weight: 400;">Firstly, many people will still want the convenience of just plugging in their device and running it. No worries about setting up a server, no challenges accessing the web UI from their phone without firewall magic, etc. It just works.</span>

<span style="font-weight: 400;">Second, there is still value in having a central collaboration hub. Mycroft has always been about communal efforts, and Community requires gathering places. Home provides a place to:</span>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Share and assist in tagging data to advance the technology</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Discover new information</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Download voices, and skills from others</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Provide a gateway to access other Mycroft devices and Mycroft-hosted services</span></li>
</ul>
<h1><span style="font-weight: 400;">Your Thoughts?</span></h1>
<span style="font-weight: 400;">All of the above are </span><i><span style="font-weight: 400;">my</span></i> <i><span style="font-weight: 400;">thoughts</span></i><span style="font-weight: 400;">. But as I said at the beginning, I want this to be a conversation. What do you want and see for the Mycroft Personal Server? Are there concerns I’m overlooking? Would you like to be involved in the building of this, taking control of your own fate?</span>

<span style="font-weight: 400;">Please join us on our <a href="https://community.mycroft.ai/t/the-mycroft-personal-server-starting-the-conversation/4691" target="_blank" rel="noopener">Community Forum</a> to participate in the conversation!</span>