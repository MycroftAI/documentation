---
ID: 30685
post_title: 'Mycroft Core Release Notes: 7/20/2017'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/mycroft-core-release-notes-7202017/
published: true
post_date: 2017-07-24 08:58:17
---
We hit the big 5 - 0!  This is the 50th release of mycroft-core, the central code that connects the entire Mycroft ecosystem.  Here are details:

<h2>Release Validation Process</h2>

<p>This was a fairly pedestrian release, which is one of the actually exciting aspects.  We have implemented a new Release Validation process, which means getting from an "unstable" build based on the code that sits in the <a href="https://github.com/MycroftAI/mycroft-core">'dev' branch of our Github repo</a> to an <a href="https://github.com/MycroftAI/mycroft-core/releases">official release</a> is now clearly defined.  To be stable-worthy, a release must comply with these basics:</p>

<ul>
<li>Users can install or upgrade on common platforms (Mark 1, Picroft, Ubuntu / Github)</li>
<li>Mark 1 and Picroft users can connect to wifi, as well as pair with Mycroft Home</li>
<li>On all platforms, skill installation is possible</li>
<li>On all platforms, the system will automatically upgrade when a new release is available</li>
</ul>

<p>If these essential requirements are met, then any issue can be resolved.  The pragmatist in me knows completely bug-free is impossible, so this defines "good enough" clearly.</p>

<h2><a href="https://github.com/MycroftAI/mycroft-core/releases/tag/release%2Fv0.8.19">mycroft-core 0.8.19</a></h2>

<h3>Fixes</h3>

<ul>
<li>ISSUE <a class="issue-link js-issue-link" title="msm may not handle mk1 correctly." href="https://github.com/MycroftAI/mycroft-core/issues/887" data-id="240786132" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#887</a>: Mycroft Skills Manager (MSM) was failing on a Mark 1 with skills that had missing library requirements. (PR <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/907" data-url="https://github.com/MycroftAI/mycroft-core/issues/907" data-id="242430298" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#907</a>)</li>

<li>Fixed missing period in cached WAV files from the Text to Speech system. They were missing a period before the file extension, e.g. "cachedfilewav" instead of "cachedfile.wav". (PR <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/921" data-url="https://github.com/MycroftAI/mycroft-core/issues/921" data-id="244079085" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#921</a>)</li>

<li>Fixed bug that prevented the "expect_response" mechanism from triggering. (PR <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/920" data-url="https://github.com/MycroftAI/mycroft-core/issues/920" data-id="243625974" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#920</a>)</li>
</ul>

<h3>Developer & API Enhancements</h3>

<ul>
 	<li>Added official support for running Kaldi locally as a STT server. (PR <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/878" data-url="https://github.com/MycroftAI/mycroft-core/issues/878" data-id="240501556" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#878</a>)
This is a backup</li>
 	<li>Added script for updating dev environment. (PR <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/issues/914" data-url="https://github.com/MycroftAI/mycroft-core/issues/914" data-id="243076667" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#914</a>)</li>
 	<li>Added new intent fallback system for dealing with unhandled intents. Multiple Skills can now register as fall-back handlers with a self-assigned priority. Handlers are invoked by priority until one handles the intent. (PR <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/899" data-url="https://github.com/MycroftAI/mycroft-core/issues/899" data-id="241804030" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#899</a>)</li>
 	<li>Skills are no longer need to provide a name parameter when calling their base initializer. It now defaults to the classname of the skill. (PR <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/918" data-url="https://github.com/MycroftAI/mycroft-core/issues/918" data-id="243615439" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#918</a>)</li>
</ul>

<h2>Picroft Unstable Build</h2>

A publicly available "unstable" build of Picroft is now available which fixes a problem that cropped up recently with an expired GPG key, but it also implements a new auto-update system that will keep the Picroft installation in sync with the contents of the 'master' branch of the <a href="https://github.com/MycroftAI/enclosure-picroft">enclosure-picroft repo</a>.

<p>You can download and install an <a href="https://github.com/MycroftAI/enclosure-picroft#picroft-08">unstable Picroft image</a> right now.  We expect this to be declared stable soon.</p>