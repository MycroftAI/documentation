---
ID: 32272
post_title: Release Notes v0.9.4
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: https://mycroft.ai/blog/releasenotes094/
published: true
post_date: 2017-11-03 07:48:23
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]
<h2><strong>New Voice!</strong></h2>
The long-awaited new feminine voice for Mycroft is now available! Members at home.mycroft.ai can choose the 'American Female' voice at <a href="https://home.mycroft.ai/#/setting/basic">https://home.mycroft.ai/#/setting/basic</a>. The Alan Pope voice still is and always will be available for all. (<a href="https://github.com/MycroftAI/mycroft-core/pull/1173">#1173</a>)
<h2><strong>Default skills...redefined</strong></h2>
The core default skills are now defined by a list on the mycroft-skills repo (see <a href="https://github.com/MycroftAI/mycroft-skills/blob/master/DEFAULT-SKILLS">https://github.com/MycroftAI/mycroft-skills/blob/master/DEFAULT-SKILLS</a>). This decouples the list from a specific build, allowing new defaults to be added at any time. Additionally, platforms can also have unique defaults -- for example allowing a KDE installation of Mycroft to pull down KDE/desktop related skills (see <a href="https://github.com/MycroftAI/mycroft-skills/blob/master/DEFAULT-SKILLS.kde">https://github.com/MycroftAI/mycroft-skills/blob/master/DEFAULT-SKILLS.kde</a>). The current list of platforms is 'picroft', 'mark-1' and 'kde'.

The list of default skills is defined by the community run Mycroft Skills Team.
<h2><strong>Portuguese Internationalization</strong></h2>
<ul>
 	<li>Began Portuguese (Pt-pt) support. Thanks <a href="https://github.com/jarbasai"><strong>@JarbasAI</strong></a>! (<a href="https://github.com/MycroftAI/mycroft-core/pull/1049">#1049</a>, <a href="https://github.com/MycroftAI/mycroft-core/pull/1177">#1177</a>)</li>
</ul>
<h2><strong>Fixes</strong></h2>
<ul>
 	<li>The Chromecast audio backend would stop playback on initial connection, sometimes interfering with existing playback. (<a href="https://github.com/MycroftAI/mycroft-core/pull/1123">#1123</a>)</li>
 	<li>ISSUE <a href="https://github.com/MycroftAI/mycroft-core/issues/1141">#1141</a>: The TTS audio cache could be cleared before or during playback, occasionally interfering with responses (especially when the disk is nearly full). Also allowed minimum_size not just a minimum percentage, which is less useful when dealing with very large drives. (<a href="https://github.com/MycroftAI/mycroft-core/pull/1168">#1168</a>)</li>
 	<li>Upgraded to Padatious 0.3.6, fixing issues with registering entities. (<a href="https://github.com/MycroftAI/mycroft-core/pull/1149">#1149</a>)</li>
 	<li>Modified dev_setup.sh build of py2cairo and pygobject to avoid "too many arguments" message on Arch Linux. Thanks <a href="https://github.com/darkphoenix"><strong>@DarkPhoenix</strong></a>! (<a href="https://github.com/MycroftAI/mycroft-core/pull/1157">#1157</a>)</li>
 	<li>The next spoken utterance was consumed if no speech was occurring when mycroft.audio.stop_speaking() was called. (<a href="https://github.com/MycroftAI/mycroft-core/pull/1167">#1167</a>)</li>
 	<li>Error messages were spoken during skill download even when "speak=False" was specified (<a href="https://github.com/MycroftAI/mycroft-core/pull/1183">#1183</a>)</li>
</ul>
<h2><strong>Misc</strong></h2>
<ul>
 	<li>Major refactor of the mycroft.configuration module. This clarifies and simplifies some of the logic and allows patches to survive a reload of the config. (<a href="https://github.com/MycroftAI/mycroft-core/pull/1110">#1110</a>, <a href="https://github.com/MycroftAI/mycroft-core/pull/1176">#1176</a>, <a href="https://github.com/MycroftAI/mycroft-core/pull/1179">#1179</a>)</li>
 	<li>Allow msm.sh, mycroft-start.sh and mycroft-stop.sh to be invoked from different working directories. Thanks <a href="https://github.com/roadriverrail"><strong>@roadriverrail</strong></a>! (<a href="https://github.com/MycroftAI/mycroft-core/pull/1021">#1021</a>)</li>
 	<li>Added g++ to dev_setup.sh dependencies (<a href="https://github.com/MycroftAI/mycroft-core/pull/1150">#1150</a>)</li>
 	<li>Reduced some of the 'noise' in the logs. (<a href="https://github.com/MycroftAI/mycroft-core/pull/1180">#1180</a>)</li>
 	<li>Disabled experimental "Location" context from the default. It was lingering and causing confusion at times, but is still available for more experimentation. (<a href="https://github.com/MycroftAI/mycroft-core/pull/1181">#1181</a>)</li>
 	<li>In the 'mycroft-use' utility, separated the connection between the mycroft-core implementation and the backend. Now specifying 'stable' and 'unstable' only changes the Debian package. To change the backend connection, specify 'home' or 'home-test' in a subsequent call, e.g. "mycroft-use unstable" followed by "mycroft-use home-test".</li>
</ul>
[/vc_column_text][/vc_column][/vc_row]