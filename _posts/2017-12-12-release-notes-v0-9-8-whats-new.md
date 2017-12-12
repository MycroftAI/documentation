---
ID: 33735
post_title: >
  Release Notes v0.9.8 | Skill Creators
  Rejoice
author: Alyx Horace
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/release-notes-v0-9-8-whats-new/
published: true
post_date: 2017-12-12 10:45:27
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]
<div class="release-header">
<h1 class="release-title text-normal"><a href="https://github.com/MycroftAI/mycroft-core/releases/tag/release%2Fv0.9.8">Skill creators rejoice</a></h1>
</div>
<div class="my-4">

Release v0.9.8 is loaded with skill creation tools. Bettering the lives of Developers and Users alike. You can find the source code, as always, in our <a href="https://github.com/MycroftAI/mycroft-core/releases/tag/release%2Fv0.9.8">Github</a>.

</div>
<div class="markdown-body">
<h3><strong>Get response <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1278" data-error-text="Failed to load issue title" data-id="279195658" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1278">#1278</a></strong></h3>
<code>get_response()</code> method added to MycroftSkill. The method allows skill creators to synchronously wait for a users response inside an intent handler. The method takes a dialog reference as an argument. The referenced dialog will be spoken and listening will be triggered. The user response will be returned from the method.
<div class="highlight highlight-source-python">
<pre>    <span class="pl-k">def</span> <span class="pl-en">echo</span>(<span class="pl-smi">self</span>, <span class="pl-smi">message</span>):
        response <span class="pl-k">=</span><span class="pl-c1">self</span>.get_response(<span class="pl-s"><span class="pl-pds">'</span>what.should.I.repeat<span class="pl-pds">'</span></span>)
        <span class="pl-c1">self</span>.speak(response)</pre>
</div>
<h3></h3>
<h3><strong>Global skill settings <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1290" data-error-text="Failed to load issue title" data-id="280182333" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1290">#1290</a></strong></h3>
Skill settings are now defaulted per user, not per device. This means instead of having multiple entries for a skill under the "Skills" tab, a single entry will be visible and used by all devices.
<h3></h3>
<h3><strong>Skiller <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1282" data-error-text="Failed to load issue title" data-id="279661320" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1282">#1282</a></strong></h3>
skiller.sh script updated. The <code>skiller.sh</code> script creates a standard template for building a new skill, including skill class, readme, and license.
<h3></h3>
<h3><strong>Translate text <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1288" data-error-text="Failed to load issue title" data-id="279989530" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1288">#1288</a></strong></h3>
New translate methods to help the internationalization of skills. The new methods are,<code>translate()</code><code>translate_template()</code> and <code>translate_list()</code>.
<div class="highlight highlight-source-python">
<pre>        body <span class="pl-k">=</span> <span class="pl-c1">self</span>.translate_template(<span class="pl-s"><span class="pl-pds">'</span>email.template<span class="pl-pds">'</span></span>, {<span class="pl-s"><span class="pl-pds">'</span>from<span class="pl-pds">'</span></span>: data[<span class="pl-s"><span class="pl-pds">'</span>name<span class="pl-pds">'</span></span>]})
        <span class="pl-c1">self</span>.send_email(<span class="pl-c1">self</span>.translate(<span class="pl-s"><span class="pl-pds">'</span>You have a message!<span class="pl-pds">'</span></span>), body)</pre>
</div>
The above example will get the localized version of the <code>email.template.dialog</code> file, and render one of the entries as a string. The string will then be sent as the body in an e-mail message.
<h3></h3>
<h3><strong>Unnamed intents <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1280" data-error-text="Failed to load issue title" data-id="279459563" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1280">#1280</a></strong></h3>
<code>IntentBuilder</code> can now be used with empty names:<code>IntentBuilder('').require('intent')...</code> If left empty, the handler method name will be used.
<h3></h3>
<h3><strong>Misc changes</strong></h3>
<ul>
 	<li>Corrected test coverage <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1272" data-error-text="Failed to load issue title" data-id="278118427" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1272">#1272</a></li>
 	<li>Speech related fixes, correct <code>isSpeaking</code> <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1283" data-error-text="Failed to load issue title" data-id="279667892" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1283">#1283</a>, Fix protection from intermixing utterances. <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1291" data-error-text="Failed to load issue title" data-id="280252603" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1291">#1291</a></li>
 	<li>Update CLI, minor fixes and changes to the keyboard interface. <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/1284" data-error-text="Failed to load issue title" data-id="279702600" data-permission-text="Issue title is private" data-url="https://github.com/MycroftAI/mycroft-core/issues/1284">#1284</a></li>
 	<li><code>mycroft.awoken</code> is now sent when speech client is awoken from sleep. <a class="issue-link js-issue-link tooltipped tooltipped-ne" href="https://github.com/MycroftAI/mycroft-core/pull/1279" data-error-text="Failed to load issue title" data-id="279353173" data-permission-text="Issue title is private" aria-label="#1279, Add mycroft.awoken message when listener is awoken">#1279</a></li>
 	<li>fix status messages sent from msm to mycroft messagebus. <a class="issue-link js-issue-link tooltipped tooltipped-ne" href="https://github.com/MycroftAI/mycroft-core/pull/1275" data-error-text="Failed to load issue title" data-id="278453231" data-permission-text="Issue title is private" aria-label="#1275, Fix data field in msm messagebus messages.">#1275</a></li>
</ul>
</div>
[/vc_column_text][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][divider line_type="No Line" custom_height="60"][/vc_column][/vc_row]