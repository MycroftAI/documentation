---
ID: 45442
post_title: '19.02 Release Notes &#8211; Mycroft Major Release'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/19-02-release-notes-mycroft-major-release/
published: true
post_date: 2019-03-07 11:30:15
---
<h1>State of the Rebellion - Mycroft @ 19.02</h1>
Twice a year Mycroft releases major versions – in February and August. These are labeled by the year name and the month, so this release is known as 19.02. Following each major release, we continue to produce incremental improvements every two weeks on top of the major version.

As a result of this iterative methodology and open development model, a major release is not packed with a bunch of surprise new features. Rather, it is a culmination of all the work performed and carefully released during the six months since the previous release.

Additionally, the Mycroft experience consists of far more than just the Core code. Skills, Community projects, skills created by individuals, and other efforts all add up to a much bigger picture. I'll try to capture highlights of the last six months here.
<h1>Mycroft Core</h1>
Technically, all of the pieces that make up Mycroft are brought together by <a href="https://github.com/mycroftai/mycroft-core" target="_blank" rel="noopener">Mycroft Core</a>. This framework allows technologies created by individuals and teams from around the world to work in harmony.

Spanning over 400 pull requests, major changes incorporated in 19.02 include:
<h3>The Mycroft GUI (Graphical User Interface)</h3>
Built on KDE Plasma technology, the <a href="https://github.com/mycroftai/mycroft-gui" target="_blank" rel="noopener">Mycroft GUI</a> allows voice interfaces and graphical interfaces to augment each other. A future blog post will go into deeper detail about this technology.
<h3>The Common frameworks: CommonPlay, CommonQ&amp;A, CommonIOT</h3>
Nobody likes walled gardens. These frameworks allow Skills to work together to achieve what a user really wants when working with media, information retrieval, and smart devices.
<h3>Natural Language Processing tools</h3>
In addition to extending tools for parsing and formatting natural language, the tools have at least partial coverage in eight languages. This makes Mycroft one of the most powerful multilingual parsing libraries in the world.
<h3>Intent processing unification</h3>
Padatious and Adapt intent definitions can now be freely mixed and matched between and within skills.
<h3>Hundreds of other small changes and extensions</h3>
Including boot sequence/update simplification and more that make Mycroft more stable and easy to use.

Also, the <a href="https://github.com/MycroftAI/mycroft-core/releases" target="_blank" rel="noopener">19.02.0 release</a> is also our 101st successful bi-weekly release of mycroft-core!
<h1>Mimic Text To Speech Technology</h1>
Mimic lets Mycroft speak to you. We have built one of the only production-ready voice generation technology suites. Additions and updates in 19.02 include:
<h3>Recording Studio</h3>
We've released a <a href="https://github.com/MycroftAI/mimic-recording-studio" target="_blank" rel="noopener">Recording Studio</a> with all the tools for an individual to generate the recordings needed to build a voice in ANY language.
<h3>Mimic server</h3>
Tooling to support running Mimic2, GPU-intensive voices in a shared server environment.
<h3>Mimic Pronounce</h3>
<a href="https://mimic.mycroft.ai/pronounce" target="_blank" rel="noopener">Pronounce is a Community tool</a> for teaching Mimic voices to sound better.
<h1>Internationalization Support</h1>
Natural Language happens in far more than just English. Enabling technology available to every speaker has long been a goal of the project, and huge leaps have been made.
<h3>Mycroft Translate</h3>
<a href="https://translate.mycroft.ai/" target="_blank" rel="noopener">This tool</a> is empowering language communities to create their own voice assistant. Over a dozen languages have been fully translated, with nearly 50 languages underway.
<h3>Mimic and Mycroft frameworks</h3>
With full Unicode UTF-8 support, Mycroft is now ready to support virtually every language.
<h1>Community Teams</h1>
The Community is Mycroft’s not-so-secret weapon. Our dedication to a strong Community has long been part of every decision we make.

Beyond the original Skills Management Team (the official owner of the <a href="https://github.com/mycroftai/mycroft-skills" target="_blank" rel="noopener">Mycroft Skills</a> repo), we have added the following teams over the last few months:
<h3>Core Community Developers</h3>
These programmers have voice in the development of and full rights to edit Mycroft Core
<h3>Skill Tester Team</h3>
This team is Community members working to guarantee Skills work for everyone. If you're interested, <a href="https://goo.gl/forms/mTSRlAsMaMjelX482" target="_blank" rel="noopener">fill out this form</a>!
<h3>Mimic Administration Team</h3>
Community management of the voices of Mycroft
<h3>United Skill Writers</h3>
A collective of some of the best and brightest Mycroft Skill developers, coming together to adopt critical Skills whose authors are no longer able to keep their Skill up to date.
<h1>Picroft</h1>
The first exposure to Mycroft for tens of thousands has been Picroft – the pre-built image for running Mycroft on the Raspberry Pi. It was not ignored between 18.08 and now. Here are some highlights:
<h3>Raspbian Stretch</h3>
This update enables Picroft to work with the latest Pi 3+
<h3>New “wizard” setup</h3>
Now it is easy to get started no matter how you intend to use Mycroft
<h3>Support for AIY, Matrix Voice and other microphones</h3>
Quick and easy startup for popular mics, with more to come.
<h1>Websites</h1>
Even a voice agent can benefit from a web interface! There are big changes contained within the release that have either rolled out recently, or you'll be seeing soon.
<h3>Marketplace</h3>
Exploring and installing Skills is now easy with a modern interface. <a href="https://market.mycroft.ai/" target="_blank" rel="noopener">Check out some new skills</a>!
<h3>Our new Home</h3>
In a few days, a major overhaul of the Mycroft web will be released. It will be as shiny on the outside as it is under the hood.
<h3>Personal Server</h3>
Building on the original work of Jarbas, an <a href="https://github.com/MycroftAI/personal-backend" target="_blank" rel="noopener">official community project</a> has launched to with the goal of providing the ultimate privacy guarantee – self-hosting.
<h1>Skills!</h1>
Skills are what gives Mycroft its smarts. It just keeps getting better.
<h3>"Top 10" skills</h3>
The Mycroft AI team has been reviewing and reworking the most popular Skills used in voice assistants, making them more capable and easy to use.
<h3>Community skills</h3>
Some of the coolest recent additions:

<a href="https://market.mycroft.ai/skill/theia-ide" target="_blank" rel="noopener">Theia</a> on-device development/debugger

<a href="https://market.mycroft.ai/skill/fallback-recommendations-skill" target="_blank" rel="noopener">Skill Recommendations</a>

<a href="https://market.mycroft.ai/skill/emby" target="_blank" rel="noopener">Emby</a> music server

IoT: <a href="https://market.mycroft.ai/skill/lifx-mycroft" target="_blank" rel="noopener">LifX</a> and <a href="https://github.com/openhab/openhab-mycroft" target="_blank" rel="noopener">OpenHAB</a>

<a href="https://market.mycroft.ai/skill/bedtime-stories-skill" target="_blank" rel="noopener">Bedtime Stories</a> and <a href="https://market.mycroft.ai/skill/fairytalez" target="_blank" rel="noopener">Fairytalez</a>
<h1>Special Thanks!</h1>
As always, the support of the Community is what keeps us going. Whether is it code for a new Skill or feature, financial support, assistance translating, or participation in Community Teams and initiatives or simply joining the discussion – every kind of support is valuable.

I want to give a special shout out to the KDE Plasma Team. Despite the ongoing challenges around the graphics hardware, their expertise has allowed us to produce a remarkably simple yet flexible and powerful graphical framework. Collaborating with them has been a pleasure and inspiration, and I look forward to a long relationship between our Communities!