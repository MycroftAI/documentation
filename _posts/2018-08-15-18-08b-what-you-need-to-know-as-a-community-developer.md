---
ID: 40099
post_title: >
  18.08b – What you need to know as a
  Community Developer
author: Kathy Reid
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/18-08b-what-you-need-to-know-as-a-community-developer/
published: true
post_date: 2018-08-15 10:00:22
---
<h1><b>Skill Authors - what does 18.08 mean for you? </b></h1>
<span style="font-weight: 400;">The Mycroft Core 18.08 beta release is only a few short weeks away. We got </span><a href="https://community.mycroft.ai/t/what-do-you-want-to-see-from-mycroft" target="_blank" rel="noopener"><span style="font-weight: 400;">your input</span></a><span style="font-weight: 400;"> on what you’d like to see in this release and there were several excellent, if ambitious, suggestions. The recently published </span><a href="https://docs.google.com/document/d/1QntesVNTGx-DlSK45gjFi5ToDJtDuMwYY_C-u9C3fFI" target="_blank" rel="noopener"><span style="font-weight: 400;">Roadmaps</span></a><span style="font-weight: 400;"> outline planned improvements, including; </span>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">The Marketplace -- a showcase for your Skills</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Enhanced screen support for the forthcoming Mark II</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Enhanced internationalization tools</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Vocabulary overlap disambiguation</span></li>
</ul>
<h2><span style="font-weight: 400;">Steady Progress</span></h2>
<span style="font-weight: 400;">Emerging technologies require steady progress.  Much progress can be made with new features and carefully adding on to existing features.  However, sometimes progress requires tearing down an existing structure. Major releases provide the opportunity to start these kinds of remodels cleanly.</span>

<span style="font-weight: 400;">With 18.08 there will be several minor changes that we believe will have little or no impact on most Skills:</span>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Removal of the ScheduledSkill</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Merger of the dialog/announce parameters in <code>MycroftSkills.get_response()</code></span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Data typecasts for <code>settingsmeta</code> values</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Removal of <code>parsedatetime</code> module as a Mycroft Core requirement</span></li>
 	<li><span style="font-weight: 400;">Removal of deprecated <code>mycroft.util.parse.extractnumber()</code>, use <code>extract_number() </code>instead.</span></li>
</ul>
<span style="font-weight: 400;">With these changes in place, we can continue the evolution of Mycroft Core, adding the next round of new features.</span>

<span style="font-weight: 400;">None of these changes are as major as the Python 3 migration or completely new like the </span><a href="https://mycroft.ai/blog/skill-branching-18-02/" target="_blank" rel="noopener"><span style="font-weight: 400;">Skill Branching</span></a><span style="font-weight: 400;"> and intent test requirement for 18.02.  If you’ve been a Skill Author for a while, you’ll remember that 18.02 was a bit of a hurdle.  We’re safely over that hurdle now. The good news is that most if not all Skills in the 18.02 branch will be able to automatically migrate to the 18.08 Skill branch.</span>
<h2><span style="font-weight: 400;">What happens to my Skill when the 18.08 branch is made the default? </span></h2>
<span style="font-weight: 400;">We’re happy to report that if you already have </span><a href="https://mycroft.ai/documentation/skills/automatic-testing/" target="_blank" rel="noopener"><span style="font-weight: 400;">automated tests</span></a><span style="font-weight: 400;"> written for your Skill and they pass the testing framework, your Skill will be </span><i><span style="font-weight: 400;">automatically migrated to the 18.08 repo</span></i><span style="font-weight: 400;">. If your Skill doesn't pass the testing framework then you can update the code and/or tests and simply submit the Skill to the 18.08 branch using the </span><a href="https://mycroft.ai/documentation/skills/msk/" target="_blank" rel="noopener"><span style="font-weight: 400;">Mycroft Skills Kit</span></a><span style="font-weight: 400;"> (MSK).  After that, the principle of having another community member ‘vouch’ for the state of the Skill will still apply. </span>

<span style="font-weight: 400;">If you are submitting a new Skill to the 18.08 branch, then it will be reviewed and processed using the </span><a href="https://mycroft.ai/documentation/skills/skills-acceptance-process/" target="_blank" rel="noopener"><span style="font-weight: 400;">Skill Acceptance Process</span></a><span style="font-weight: 400;">. </span>
<h2><span style="font-weight: 400;">What action do I need to take now to prepare for the 18.08 branch? </span></h2>
<span style="font-weight: 400;">Skill Developers can begin testing immediately following the 18.02.13 release on August 15th.  At that point the dev branch of <code>mycroft-core</code> will begin to be updated with the changes listed above, leading up to the release of 18.08 at the end of the month.</span>
<ul>
 	<li style="font-weight: 400;"><b>Update older Skills to Python 3 and ensure tests are written</b><span style="font-weight: 400;"> - if you have a Skill you haven’t yet submitted to the </span><span style="font-weight: 400;"><code>mycroft-skills</code></span><span style="font-weight: 400;"> repo - perhaps it was written for Python 2.7 - then now is a good time to update it for Python 3.4+, and to write </span><a href="https://mycroft.ai/documentation/skills/automatic-testing/" target="_blank" rel="noopener"><span style="font-weight: 400;">automated tests</span></a><span style="font-weight: 400;">. Use the <a href="https://mycroft.ai/documentation/msk" target="_blank" rel="noopener">Mycroft Skills Kit</a> to help define both Intents and tests for those Intents.</span></li>
 	<li style="font-weight: 400;"><b>Ensure the README.md for your Skill is generated by the Meta Editor </b><span style="font-weight: 400;">- the </span><a href="https://mycroft.ai/skills" target="_blank" rel="noopener"><span style="font-weight: 400;">Skills List</span></a><span style="font-weight: 400;"> and forthcoming Marketplace will use the information in the <code>README.md</code> from the Skill’s GitHub repository to build the card with information about the Skill.  Skill Authors have full control of the content but should use the </span><a href="https://rawgit.com/MycroftAI/mycroft-skills/master/meta_editor.html" target="_blank" rel="noopener"><span style="font-weight: 400;">Meta Editor</span></a><span style="font-weight: 400;"> to generate a file which is compatible with the parsing used by the automated systems. If a <code>README.md</code> file doesn’t follow the expected format then your Skill may not be represented well the Skills List or Marketplace. </span><span style="font-weight: 400;">Skill updates which are just <code>README.md</code> changes will be automatically accepted by the Skills Management Team. They are not put through a testing regimen.  This makes it easy for you to quickly correct any presentation issues.</span></li>
 	<li style="font-weight: 400;"><b>The Marketplace </b><span style="font-weight: 400;">- This new interface will allow Mycroft users to easily browse all the available Skills from the </span><span style="font-weight: 400;"><code>mycroft-skills</code> </span><span style="font-weight: 400;">repo, and deploy and manage those Skills on devices they own.  Look for it on </span><a href="https://home.mycroft.ai" target="_blank" rel="noopener"><span style="font-weight: 400;">Home</span></a><span style="font-weight: 400;"> soon!</span></li>
</ul>
<span style="font-weight: 400;"> <a href="https://mycroft.ai/wp-content/uploads/2018/08/Skill-Marketplace-Example.png"><img class="aligncenter wp-image-40110 size-full" src="https://mycroft.ai/wp-content/uploads/2018/08/Skill-Marketplace-Example.png" alt="This is an early example of Mycroft's Skill Marketplace for open source voice assistant skills" width="1200" height="827" /></a></span>
<h2><span style="font-weight: 400;">When is the change to the 18.08 branch happening? </span></h2>
<span style="font-weight: 400;">The 18.08 branch of <code>mycroft-skills</code> will become active August 30th - and there will be a two-week period leading up to this when you will be able to test your Skills against the 18.08 branch to identify any major changes that impact your Skill. Breaking changes this release are limited, so it should be easy to prepare for making the 18.08 branch the default. </span>
<h2><span style="font-weight: 400;">Thank you, Skill Management Team!</span></h2>
<span style="font-weight: 400;">This couldn’t have happened without the assistance of the Mycroft Skill Management Team.  These volunteers helped create and refine the </span><a href="https://mycroft.ai/documentation/skills/skills-acceptance-process/" target="_blank" rel="noopener"><span style="font-weight: 400;">Skill Acceptance Process</span></a><span style="font-weight: 400;"> to approve new Skills.   We’d like to say a special thanks to Aditya Mehra (<a href="https://github.com/AIIX" target="_blank" rel="noopener">@aix</a>), Ryan Snedegar (<a href="https://github.com/el-tocino" target="_blank" rel="noopener">@eltocino</a>) and Joshua Johnson (<a href="https://github.com/TREE-Ind" target="_blank" rel="noopener">@joshua-tree</a>) for all their efforts.</span>
<h2><span style="font-weight: 400;">Where do I go for assistance and support?</span></h2>
<span style="font-weight: 400;">Join us in the </span><a href="https://chat.mycroft.ai/community/channels/dev" target="_blank" rel="noopener"><span style="font-weight: 400;">~dev channel</span></a><span style="font-weight: 400;"> or </span><a href="https://chat.mycroft.ai/community/channels/skills" target="_blank" rel="noopener"><span style="font-weight: 400;">~skills channel</span></a><span style="font-weight: 400;"> on Mycroft Chat for assistance.</span>