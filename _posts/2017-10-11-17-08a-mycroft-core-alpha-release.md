---
ID: 31929
post_title: '17.08a - The mycroft-core "alpha" release!'
author: Alyx Horace
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/17-08a-mycroft-core-alpha-release/
published: true
post_date: 2017-10-11 19:37:12
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]

<span style="font-weight: 400;">We have hit the milestone of our "alpha" version. What does this mean? We will be guaranteeing support for the APIs in this version going forward. Over the next 6 months we may enhance APIs, but all changes will be backwards-compatible until we move on to the 18.02b beta.</span>
<h3><b>Apache 2.0 License (</b><a href="https://github.com/MycroftAI/mycroft-core/pull/1128"><b>#1128</b></a><b>)</b></h3>
<span style="font-weight: 400;">This release includes a small but very important change to mycroft-core. It is now under Apache 2.0 licensing instead of GPLv3. This means Mycroft can be used in </span><i><span style="font-weight: 400;">any</span></i><span style="font-weight: 400;"> application, including some which were previously not possible due to strong regulatory requirements such as medical and automotive use.</span>

<span style="font-weight: 400;">As before, all who wish to join in developing this technology are welcome. Contributors who have signed our Contributor Licensing Agreement can be found at </span><a href="https://github.com/MycroftAI/contributors"><span style="font-weight: 400;">https://github.com/MycroftAI/contributors</span></a><span style="font-weight: 400;">. Thank you to everyone who has helped us reach this milestone!</span>

&nbsp;
<h3><b>The Open Dataset (</b><a href="https://github.com/MycroftAI/mycroft-core/pull/1127"><b>#1127</b></a><b>)</b></h3>
<span style="font-weight: 400;">In 0.8.22 we added the ability for users to select LEARN on Mark 1 devices to choose to contribute recordings of their device activations to reduce false-positives (inadvertent activations) and false negatives (missed activations). Now all users can choose to Opt-In to be part of the Mycroft Open Dataset and share some of their data to help us improve this technology.</span>

<span style="font-weight: 400;">All who Opt-In under their basic settings at </span><a href="https://home.mycroft.ai/#/setting/basic"><span style="font-weight: 400;">https://home.mycroft.ai/#/setting/basic</span></a><span style="font-weight: 400;"> can later choose to Opt-Out, stopping not only future data contributions but also removing any previously contributed data from future training sessions. We appreciate the help of all in building an AI for Everyone!</span>

&nbsp;
<h3><b>Padatious update to 0.3.2 (</b><a href="https://github.com/MycroftAI/mycroft-core/pull/1125"><b>#1125</b></a><b>)</b></h3>
<span style="font-weight: 400;">Padatious -- our example-based intent parser -- now supports defining named entities, intent expansion, and numeric matching. See </span><a href="https://github.com/MycroftAI/padatious#readme"><span style="font-weight: 400;">https://github.com/MycroftAI/padatious#readme</span></a><span style="font-weight: 400;"> for more details.</span>

&nbsp;
<h3><b>Script simplifications (</b><a href="https://github.com/MycroftAI/mycroft-core/pull/1107"><b>#1107</b></a><b>)</b></h3>
<span style="font-weight: 400;">Rework of the the mechanisms used to interact with Mycroft. The old mycroft.sh utilized the 'screen' command, but now with the CLI it is easier to view unified log files. Plus there was confusion over when to use start.sh and when to use mycroft.sh.</span>

<span style="font-weight: 400;">Now things are wrapped in the simple and easily discoverable scripts:</span>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">start-mycroft.sh</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">stop-mycroft.sh</span></li>
</ul>
<span style="font-weight: 400;">The start-mycroft.sh allows you to start the background services and to invoke the various tools (e.g. the CLI, unit tests, etc).</span>

&nbsp;
<h3><b>FIXES</b></h3>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">ISSUE </span><a href="https://github.com/MycroftAI/mycroft-core/issues/1105"><span style="font-weight: 400;">#1105</span></a><span style="font-weight: 400;"> - Custom activation phrases were not working (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1106"><span style="font-weight: 400;">#1106</span></a><span style="font-weight: 400;">)</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Fix for methods using multiple decorators (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1117"><span style="font-weight: 400;">#1117</span></a><span style="font-weight: 400;">)</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">ConfigurationManager saves could wipe out previously saved configs in certain cases (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1119"><span style="font-weight: 400;">#1119</span></a><span style="font-weight: 400;">)</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Fix event cancel/update. Also prune repeating and empty events needed before serialization. (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1114"><span style="font-weight: 400;">#1114</span></a><span style="font-weight: 400;">)</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Corrected typo in msm documentation (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1098"><span style="font-weight: 400;">#1098</span></a><span style="font-weight: 400;">)</span></li>
</ul>
&nbsp;
<h3><b>Misc</b></h3>
<ul>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Began Dutch translation. Thanks, </span><a href="https://github.com/valdr"><span style="font-weight: 400;">@valdr</span></a><span style="font-weight: 400;">! (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1092"><span style="font-weight: 400;">#1092</span></a><span style="font-weight: 400;">)</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Add notification of start/stop recording to the audio_test utility (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1130"><span style="font-weight: 400;">#1130</span></a><span style="font-weight: 400;">)</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Notifications are now issued at before and after fallback handling. These are "mycroft.skill.handler.start" and "mycroft.skill.handler.complete", with "fallback_handler" as the data. (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1108"><span style="font-weight: 400;">#1108</span></a><span style="font-weight: 400;">)</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Implemented LOG class in mycroft.util.log, eliminating the need to call </span><span style="font-weight: 400;">getLogger(__name__)</span><span style="font-weight: 400;"> at the top of each file.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Added '--allow-root' flag to dev_setup.sh. Also added help message. (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1115"><span style="font-weight: 400;">#1115</span></a><span style="font-weight: 400;">)</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Extracted wifi-setup from mycroft-core, as it is not needed in all use cases. It is now an independent project, </span><a href="https://github.com/MycroftAI/mycroft-wifi-setup"><span style="font-weight: 400;">https://github.com/MycroftAI/mycroft-wifi-setup</span></a><span style="font-weight: 400;">. (</span><a href="https://github.com/MycroftAI/mycroft-core/pull/1118"><span style="font-weight: 400;">#1118</span></a><span style="font-weight: 400;">)</span></li>
</ul>
[/vc_column_text][/vc_column][/vc_row]