---
ID: 46629
post_title: Test the New Mycroft Home Beta
author: Chris Veilleux
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/test-the-new-mycroft-home-beta/
published: true
post_date: 2019-04-18 15:31:13
---
Over the last few months, we have been working on a major overhaul of our Mycroft Home site. The project is nearly complete technically, so we would like to invite the Community into the Mycroft Home Beta to kick the tires and give feedback before we officially launch.

We are approaching this in three phases:
<ul>
 	<li><span style="text-decoration: line-through;">Alpha </span> &lt;-  Completed, thanks to everyone who provided feedback</li>
 	<li>Beta  &lt;-  We are here</li>
 	<li>Release  &lt;-  Soon after Beta, assuming no major issues</li>
</ul>
<h3>Exploring the New Web Interface</h3>
In the Beta, there will be a few important features that aren't 100% complete. However, the major systems are active and functional for exploration. We have pre-loaded the new database from the current Home (home.mycroft.ai) database, so you don't need to recreate accounts.

NOTE: Github login is not available yet. As a workaround you can either use other attached social media accounts or click on the "Forgot Password?" link. The email account associated with Github will receive the password reset message, then you can log in using that email address and the new password you create.

During this Beta preview, you can freely play with profile and settings. You can even add a new dummy account to try the new account setup feature. The database supporting the Beta release is completely independent of the main Home site database, so changes will not be reflected there.
<h3>Pairing Devices to Mycroft Home Beta</h3>
Although we have imported device information from your main Home account to give you a good feel for how the site will work, the devices are still paired with the production Home server. Skill settings will not be populated unless you pair a device to the new server, and changes to device settings will not be reflected on devices still paired to Home.

To pair a device to the new server – allowing full functionality including Skill settings – follow these directions:

Switch your device to the 'dev' branch. For a Mark 1 run <code>mycroft-use unstable</code>
Edit your mycroft.conf to point to the new server: <code>sudo nano /etc/mycroft/mycroft.conf</code>
<pre>{
  "server": {
    "url": "https://api.mycroft-test.net"
  },
  ... whatever is already in the mycroft.con ...
}
</pre>
NOTE: Whenever we reset the Beta databases, you will have to re-pair your device. You should simply be prompted by Mycroft to do so, but be aware that this will happen at least once when we switch from Beta to the production release.

With a paired device, the Skills settings will be fully available. There are no new features beyond the new user interface, but stay tuned...

We welcome any and all feedback during this preview period. Post your comments and suggestions to the <a href="https://chat.mycroft.ai/community/channels/home-troubleshooting" target="_blank" rel="noopener noreferrer">~home-troubleshooting</a> channel in Mattermost. We will also use this channel to update you on any new functionality or bug fixes released during the preview. Without further ado, please enjoy the...
<h1><a href="https://account.mycroft-test.net/" target="_blank" rel="noopener noreferrer">Home Beta Preview</a></h1>
(https://account.mycroft-test.net/)