---
ID: 33414
post_title: Release notes v0.9.7
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/release-notes-v0-9-7/
published: true
post_date: 2017-11-29 04:25:38
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]
<div class="release-header">
<h1 class="release-title">v0.9.7 is Here.</h1>
<p class="release-authorship">Thanks to our team member, <a href="https://github.com/forslund">forslund</a>, for rolling this out.</p>

</div>
<h2></h2>
&nbsp;

&nbsp;
<div class="markdown-body">
<h2>E-mail Send <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1230" data-error-text="Failed to load issue title" data-id="274364340" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1230">#1230</a></h2>
The skills API now includes a <code>self.send_email()</code> method, allowing the skill to send an e-mail to the user. This is practical if the skill wants to send a link to the user, or for things such as shopping lists.

</div>
<h2></h2>
&nbsp;

&nbsp;
<div class="markdown-body">
<h2>Metrics <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1247" data-error-text="Failed to load issue title" data-id="276136116" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1247">#1247</a></h2>
The Device API now includes a <code>metrics</code> method, allowing skills and core to upload information to the Mycroft server should the user allow it. The method is very general purpose and can take any method as long as it can be serialized to json.

Skills developer can easily access this functionality using the <code>self.report_metric</code> method in the Skill API.

</div>
<h2></h2>
&nbsp;

&nbsp;
<div class="markdown-body">
<h2>Misc</h2>
<ul>
 	<li>Added support for Google Cloud API SST, big thanks to <a class="user-mention" href="https://github.com/ahayworth">@ahayworth</a> for providing this. <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1226" data-error-text="Failed to load issue title" data-id="273666003" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1226">#1226</a></li>
 	<li>The AudioService can now add files to currently playing playlist <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1197" data-error-text="Failed to load issue title" data-id="270698546" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1197">#1197</a></li>
 	<li>Listening can now be triggered from the messagebus by sending <code>mycroft.mic.listen</code><a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1244" data-error-text="Failed to load issue title" data-id="275943616" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1244">#1244</a></li>
 	<li>Remove pystache dependency <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1235" data-error-text="Failed to load issue title" data-id="274777484" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1235">#1235</a></li>
 	<li>Improve lip synch <a class="issue-link js-issue-link tooltipped tooltipped-ne" href="https://github.com/MycroftAI/mycroft-core/pull/1242" data-error-text="Failed to load issue title" data-id="275573191" data-permission-text="Issue title is private" aria-label="#1242, Improve mouth synchronization with speech">#1242</a></li>
 	<li>Code cleanup and bugfixes, Many thanks to <a class="user-mention" href="https://github.com/gauravmann">@gauravMann</a> for cleaning up the usage of mutables as default arguments.</li>
</ul>
</div>
[/vc_column_text][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][divider line_type="No Line" custom_height="50"][/vc_column][/vc_row]