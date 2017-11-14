---
ID: 29176
post_title: Mycroft gets a Plasmoid
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/mycroft-gets-a-plasmoid/
published: true
post_date: 2017-02-23 22:38:59
---
I'm happy to announce some exciting news — Mycroft is working with Aditya Mehra from our community and the KDE Desktop developers to become part of their Plasma environment!
<h3>KDE Plasma</h3>
In case you don't know, KDE is one of the most widely used desktop environments in the Linux world.  It can run on a variety of Linux distributions including the popular Kubuntu (KDE + Ubuntu) and Fedora KDE.  A <a href="http://www.linuxquestions.org/questions/2016-linuxquestions-org-members-choice-awards-123/desktop-environment-of-the-year-4175596299/">2016 survey</a> by LinuxQuestions.org found KDE  to be the most popular Linux desktop environment (so did the <a href="http://www.linuxquestions.org/questions/2015-linuxquestions-org-members-choice-awards-117/desktop-environment-of-the-year-4175562713/">2015</a> and the <a href="http://www.linuxquestions.org/questions/2014-linuxquestions-org-members-choice-awards-113/desktop-environment-of-the-year-4175528387/">2014</a> surveys, BTW).  It is it is a shining example of a successful community-driven open source project.  And the <a href="https://www.kde.org/plasma-desktop">KDE Plasma Desktop</a> is simply a useful and beautiful interface.
<h3>KDE + Mycroft</h3>
Aditya (known as ''aix'' on the Mycroft Slack channels) is a Mycroft community member.  He got the Mycroft bug last year and started working early last summer on building GUIs for Mycroft.  He initially created a Gnome-based extension, and more recently became enthralled with the KDE Plasma Desktop environment.  So he decided to try his hand and building a Plasmoid for it.

His work on the Mycroft Plasmoid caught the attention of the KDE Development team.  Over the last few months we have been working with Aditya and the KDE developers figuring out how we can work together.  This weekend he officially moved his development repo onto the KDE servers as the first step in building an official <a href="https://cgit.kde.org/plasma-mycroft.git/">Mycroft Plasmoid</a>.
<h3>Community for the Win!</h3>
We are thrilled to be collaborating with the KDE Community on this project!  This is perfect example of what happens when open development tools and technologies are made available to smart people.  They make beautiful and interesting things!
<h3>Try It Out</h3>
So you want to give it a shot?
<h4>Installing Mycroft and the Plasmoid on KDE Neon</h4>
The Plasmoid is built on some of the latest technologies, so you need to be running KDE Plasma Desktop 5.9 or later.  If you aren't using that yet, you can try it out easily using a VM.  Head over to the <a href="https://neon.kde.org/download">KDE Downloads</a> page to get an ISO.  You can use that to either create and old-school installer CD, or you can create a VM and load the ISO directly into the virtual disc drive.

Once you have KDE, you can simply download this script and run it.  Here is a step by step:
<ol>
 	<li>Go to the Konsole (KDE's terminal)</li>
 	<li>Type:  <tt>cd ~</tt></li>
 	<li>Type:  <tt>wget https://mycroft.ai/to/install_plasmoid_kde.sh</tt></li>
 	<li>Type:  <tt>bash install_plasmoid_kde.sh</tt></li>
</ol>
That's it!  You'll be prompted a couple times to enter a password and the compile process will take a while, but it is straightforward.
<h4>Installing Mycroft and the Plasmoid on Fedora KDE</h4>
Fedora KDE users can try this too.  All you need to do is:
<ol>
 	<li>Go to the Terminal</li>
 	<li>Type:  <tt>cd ~</tt></li>
 	<li>Type:  <tt>wget https://mycroft.ai/to/install_plasmoid_fedora.sh</tt></li>
 	<li>Type:  <tt>bash install_plasmoid_fedora.sh</tt></li>
</ol>
<h4>Adding it to your Desktop</h4>
After the install completes right click on the desktop and select "Add Widget...".  Scroll through the list until you see "Project Mycroft", then just click and drag it to your desktop.
<h4>Using the Plasmoid</h4>
Click on the Mycroft icon to open it up.  You''ll need to click the ▶️️ button at the top to tell Mycroft to begin listening.  Then you can say "Hey Mycroft, register my device" to create your pairing with <a href="https://home.mycroft.ai">home.mycroft.ai</a>.  You'll immediately notice the text is both spoken and displayed on screen in the widget.

In the alpha there were special handlers for "What's the weather like?" that began to show the possibilities of combining voice interaction with a screen, combining voice and visuals.  We'll be exposing those capabilities to our Skill API soon for other developers to explore.

Join us on <a href="https://www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwip7o-056fSAhUIwmMKHTTRB7cQFgghMAA&amp;url=http%3A%2F%2Fmycroft-ai-slack-invite.herokuapp.com%2F&amp;usg=AFQjCNEspf3FKBi_9a01pZSA36pGAqReZw&amp;bvm=bv.147448319,d.cGc">Slack</a> to help shape the future of desktop computing in the<a href="https://mycroftai.slack.com/archives/mycroft_desktop"> #mycroft_desktop</a> channel!