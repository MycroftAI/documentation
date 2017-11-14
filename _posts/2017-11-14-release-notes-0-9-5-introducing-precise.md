---
ID: 32926
post_title: >
  Release Notes 0.9.5 | Introducing
  Precise
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/release-notes-0-9-5-introducing-precise/
published: true
post_date: 2017-11-14 00:49:43
---
V0.9.5 is here - and we're rolling out Precise.
<h2>Precise wake word engine <a class="issue-link js-issue-link tooltipped tooltipped-ne" href="https://github.com/MycroftAI/mycroft-core/pull/1199" data-error-text="Failed to load issue title" data-id="271107162" data-permission-text="Issue title is private" aria-label="#1199, Precise Wake Word Listener">#1199</a>, <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1207" data-error-text="Failed to load issue title" data-id="272050566" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1207">#1207</a></h2>
New machine-learning based wake word listener. This system includes a feedback loop, allowing user-contributed information to be incorporated into the training database, improving the wake-word performance. This happens when Opt In has been chosen at home.mycroft.ai.

Precise is enabled by changing /etc/mycroft/mycroft.conf to include:
{"hotwords": {"hey mycroft": {"module": "precise"}}}.
<h2>API enhancements</h2>
<ul>
 	<li>Add MycroftSkill.get_intro_message() method which skills can override when they wish to provide instructions to the user after installation. (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1211" data-error-text="Failed to load issue title" data-id="272514951" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1211">#1211</a>)</li>
 	<li>Extend scheduled event mechanism with MycroftSkill.get_event_status(), MycroftSkill.remove_event() (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1193" data-error-text="Failed to load issue title" data-id="270159417" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1193">#1193</a>)</li>
</ul>
<h2>Utility changes</h2>
<ul>
 	<li>Add <code>msm list</code> command to show already installed skills; and <code>msm info &lt;skill&gt;</code> command to display info from the README.md in the skill's Github repo. Thanks <a class="user-mention" href="https://github.com/thecalcaholic">@theCalcaholic</a>! (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1201" data-error-text="Failed to load issue title" data-id="271715663" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1201">#1201</a>, <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/issues/1202" data-error-text="Failed to load issue title" data-id="271716394" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1202">#1202</a>, <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/issues/1203" data-error-text="Failed to load issue title" data-id="271716803" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1203">#1203</a> )</li>
 	<li>Add 'all' option for mycroft-stop utility to mirror mycroft-start (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1212" data-error-text="Failed to load issue title" data-id="272601855" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1212">#1212</a>)</li>
 	<li>Changed mycroft-use utility to autoremove when switching from unstable to stable builds. (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1213" data-error-text="Failed to load issue title" data-id="272649715" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1213">#1213</a>)</li>
 	<li>Add 'home' and 'home-test' options to mycroft-use to simplify backend testing. Also added platform support and extended the 'github' option. (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1182" data-error-text="Failed to load issue title" data-id="269295768" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1182">#1182</a>)</li>
</ul>
<h2>Misc</h2>
<ul>
 	<li>Wakeword validation, defaulting to "Hey Mycroft" when user-entered settings fail. (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1188" data-error-text="Failed to load issue title" data-id="269956783" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1188">#1188</a>)</li>
 	<li>Add event scheduler tests (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1189" data-error-text="Failed to load issue title" data-id="269963941" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1189">#1189</a>)</li>
 	<li>Reduced requirements.txt to only the packages actually used by mycroft-core, removing those only needed for default skills. (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1192" data-error-text="Failed to load issue title" data-id="270145406" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1192">#1192</a>, <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1215" data-error-text="Failed to load issue title" data-id="272684532" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1215">#1215</a>, <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1216" data-error-text="Failed to load issue title" data-id="272731099" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1216">#1216</a>)</li>
 	<li>Added stop() to the AudioService. Thanks, <a class="user-mention" href="https://github.com/akailash">@akailash</a>! (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/issues/1194" data-error-text="Failed to load issue title" data-id="270168972" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1194">#1194</a>)</li>
 	<li>Configuration system fix (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1196" data-error-text="Failed to load issue title" data-id="270697918" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1196">#1196</a>)</li>
 	<li>Padations 0.3.7, fixing several minor bugs (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1198" data-error-text="Failed to load issue title" data-id="270794854" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1198">#1198</a>)</li>
 	<li>The remote configuration file was prematurely loaded at import time. Now it is loaded when the Session is created. (<a class="issue-link js-issue-link tooltipped tooltipped-ne" href="https://github.com/MycroftAI/mycroft-core/pull/1204" data-error-text="Failed to load issue title" data-id="271826099" data-permission-text="Issue title is private" aria-label="#1204, Move session config from global scope">#1204</a>)</li>
</ul>
&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;