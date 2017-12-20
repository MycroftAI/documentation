---
ID: 33925
post_title: 'Release Notes v0.9.9 &#038; v0.9.10 | Mark I Boot Sequence'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/release-notes-v0-9-9-mark-boot-sequence/
published: true
post_date: 2017-12-19 10:22:37
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]
<h3><strong>Visual Cues during Mark 1 Boot Sequence (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1308" data-error-text="Failed to load issue title" data-id="281849789" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1308">#1308</a>)</strong></h3>
The Main focus of this release was creating visual feedback during the Mark 1 boot
sequence. The eyes and faceplate now provide indicators of the stage of the system--so when you see any of the following, here's what's going on:
<ul>
 	<li>Spinning gray eyes
<em>Indicate the system just started, Arduino running and Pi booting</em></li>
 	<li>Solid gray eyes
<em>Pi booted</em></li>
 	<li>(Optional) Orange eyes, update message on faceplate
<em>Flashing new sketch to the Arduino</em></li>
 	<li>Yellow eyes
<em>Mycroft starting, waiting on internet connection</em></li>
 	<li>Yellow eyes, update message on faceplate
<em>Updating software from the web</em></li>
 	<li>Blue eyes (or user selected color)
<em>Mycroft is ready for use!</em></li>
</ul>
Additionally, the gray eye color and an update message will return during system upgrades.
<h3></h3>
<h3><strong>Command Line Interface (CLI) (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1299" data-error-text="Failed to load issue title" data-id="280796676" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1299">#1299</a>)</strong></h3>
Two new minor features for the mycroft-cli-client:
<ul>
 	<li>Ctrl+Right and Ctrl+L allow scrolling through the command line history</li>
 	<li>New ':clear log' command cleans out the old log message from the display</li>
</ul>
<h3></h3>
<h3><strong>Bugfixes</strong></h3>
<ul>
 	<li>Values in the settings.json were overwritten if skills initialize self.settings['key'] in <strong>init</strong> (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1304" data-error-text="Failed to load issue title" data-id="281520350" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1304">#1304</a>)</li>
 	<li>Bad settingsmeta.json prevented skill from loading and showed a convoluted error. Now a useful message is logged with the JSON error message and the skill continues to load. (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1300" data-error-text="Failed to load issue title" data-id="280796917" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1300">#1300</a>)</li>
 	<li>Add missing 'self.' in an obscure corner of the Enclosure code. Thanks JarbasAI! (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1302" data-error-text="Failed to load issue title" data-id="281250102" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1302">#1302</a>)</li>
 	<li>The MycroftSkill.translate*() functions were not correctly rendering mustache values with 'double mustaches', such as "This a a {{value}}" (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1303" data-error-text="Failed to load issue title" data-id="281515778" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1303">#1303</a>)</li>
 	<li>Fix Unicode issues in Portugese version of extract_datetime() utility. (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1301" data-error-text="Failed to load issue title" data-id="281236959" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1301">#1301</a>)</li>
 	<li>Missing space in shell script prevented creation of a directory when switching to Github install in mycroft-use.sh utility (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1298" data-error-text="Failed to load issue title" data-id="280759007" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1298">#1298</a>)</li>
</ul>
&nbsp;
<div class="release-header">
<h1 class="release-title text-normal"><a href="https://github.com/MycroftAI/mycroft-core/releases/tag/release%2Fv0.9.10">Minor release</a></h1>
<p class="f5 text-gray mt-1 mb-4">We also added another minor release, v0.9.10.</p>

<h3 class="f5 text-gray mt-1 mb-4"><strong>New text parsing util fuzzy_matching <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1315" data-error-text="Failed to load issue title" data-id="282405346" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1315">#1315</a></strong></h3>
</div>
<div class="markdown-body">

The function matches similar text like "orange" and "oranges" and gives a score 0-1.0.
<h3></h3>
<h3><strong>Translate </strong>named values<strong> <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1313" data-error-text="Failed to load issue title" data-id="282394221" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1313">#1313</a></strong></h3>
the MycroftSkill class now has a <code>translate_namedvalues()</code> method returning a dict with keys in the current language. The dict is read from a csv file in the `/xx-xx/File.values looking something like:
<pre lang="csv"><code># List colors and their hex RGB values
alice blue, #F0F8FF
antique white, #FAEBD7
aqua, #00FFFF
</code></pre>
<h3></h3>
<h3><strong>Misc</strong></h3>
<ul>
 	<li>improved standard of README generated by skiller.sh script and improve some text resources <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1311" data-error-text="Failed to load issue title" data-id="282374776" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1311">#1311</a></li>
 	<li>Fix PgUp and PgDn for VT100 <a class="issue-link js-issue-link tooltipped tooltipped-ne" href="https://github.com/MycroftAI/mycroft-core/pull/1310" data-error-text="Failed to load issue title" data-id="282344117" data-permission-text="Issue title is private" aria-label="#1310, CLI: interpretation of VT100 keys was flipped">#1310</a></li>
</ul>
</div>
&nbsp;

[/vc_column_text][/vc_column][/vc_row]