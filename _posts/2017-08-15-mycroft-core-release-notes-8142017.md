---
ID: 30936
post_title: 'Mycroft Core Release Notes: 8/14/2017'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/mycroft-core-release-notes-8142017/
published: true
post_date: 2017-08-15 13:50:51
---
We're on the road to 17.08a!  We are putting a lot of things in place as we approach our first major milestone <a href="https://mycroft.ai/themes-goals-mycroft-core-17-08a/">17.08a alpha release</a>, establishing the mechanisms and policies that will allow us work together to build on this foundation.
<h2>Installer Repo</h2>
Believe it or not, one of the trickier things about developing software is figuring out how to get it in the hands of others.  Given the broad scope of the Mycroft project and the many and varied platforms on which it can run, it has been particularly tricky for people to figure out how to even get started.  Instructions have been spread across wikis, Github README's, blog posts...

To simplify this, we have created a single <a href="https://github.com/MycroftAI/installers">Installer repository</a>.  This will be a single place to find the correct and current method to install a the KDE Plasmoid for Fedora, Raspberry Pi image, or Ubuntu developer installation script.  Look for more entries in the near future as we backfill it and add support for more platforms.
<h2>Skills Updates</h2>
We have begun a review and update of the existing "default" skills to take advantage of new capabilities of mycroft-core, to provide solid examples for those looking to develop their own skills, and to just make them better.  The first overhaul is of the <a href="https://github.com/MycroftAI/skill-weather">Weather Skill</a>.
<h3>New capabilities:</h3>
<ul>
 	<li>Request forecasts for specific days:
<em>"What's the will the weather be like on Tuesday?"</em></li>
 	<li>Support for precipitation queries:
<em>"When will it rain next?</em>"
<em>"Will it snow the day after tomorrow?"</em></li>
 	<li>Weather condition queries:
<em>"What's the humidity?"</em>
<em>"How windy is it?"</em></li>
 	<li>Sunrise and sunset info:
<em>"When will the sun rise?</em>"</li>
</ul>
This also fixed a misunderstanding of the Open Weather Map API that produced caused Mycroft to report incorrect high and low temperatures.

This skill also demonstrates methods for using strings with translation support, the new decorator intent definition mechanism, and how to perform natural-language date extractions.
<h2><a href="https://github.com/MycroftAI/mycroft-core/releases/tag/release%2Fv0.8.20">mycroft-core 0.8.20</a></h2>
Finally, the last release of mycroft-core added some major new capabilities for skill writers to be creative with!
<h2>Audio Service (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/433" data-url="https://github.com/MycroftAI/mycroft-core/issues/433" data-id="197495993" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#433</a>)</h2>
This include a Major unification of audio handling in Mycroft.  The AudioService now manages all sound output, including text to speech, music files and audio streams. This enables:
<ul>
 	<li>Audio will lower/pause and resume when Mycroft speaks</li>
 	<li>Skills can queue-up multiple audio files/streams for playback</li>
 	<li>Unified playback skip/pause/resume/stop</li>
 	<li>Audio can be redirected to external players besides the local speaker.  Currently there is support for VLC and Mopidy. (Kodi and Chromecast on the way!) <em>"Hey Mycroft, play the news in the kitchen"</em></li>
</ul>
See the <a href="https://github.com/MycroftAI/skill-npr-news">NPR News</a> and <a href="https://github.com/MycroftAI/skill-playback-control">Playback Control</a> skills for examples of interacting with the audio service.
<h2>FEATURE: Skill Graphic Output / DisplayManager (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/838" data-url="https://github.com/MycroftAI/mycroft-core/issues/838" data-id="236561540" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#838</a>)</h2>
Skills can draw to the Mark 1 face (or future enclosures) by sending encoded or PNG graphics!  Graphics are sent via EnclosureAPI.mouth_display_png(). Graphics are automatically converted to two colors if necessary.

This required creating the concept of the <em>active skill</em> which owns the display. Now you can say <em>"Hey Mycroft, what time is it?"</em> to the <a href="https://github.com/MycroftAI/skill-date-time">Date-Time Skill</a> to see an example of a skill drawing to the display when it is 'inactive'.
<h2>FEATURE: Skill Settings Web UI (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/933" data-url="https://github.com/MycroftAI/mycroft-core/issues/933" data-id="246431016" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#933</a>)</h2>
Skill developers can now add a settingsmeta.json file into their skill. With that, mycroft-core will automatically send the metadata to home.mycroft.ai, allowing users to input the settings via a web UI. Then entered values are sent back as a settings.json file which can be used by the skill.

Example settingsmeta.json:
<pre class="highlight highlight-source-json">{
   <span class="pl-s"><span class="pl-pds">"</span>identifier<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>PandoraSkill<span class="pl-pds">"</span></span>,
   <span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Pandora<span class="pl-pds">"</span></span>,
   <span class="pl-s"><span class="pl-pds">"</span>skillMetadata<span class="pl-pds">"</span></span>: {
      <span class="pl-s"><span class="pl-pds">"</span>sections<span class="pl-pds">"</span></span>: [
         {
            <span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Login<span class="pl-pds">"</span></span>,
            <span class="pl-s"><span class="pl-pds">"</span>fields<span class="pl-pds">"</span></span>: [
               {
                  <span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>email<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>type<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>email<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>label<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Email<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>value<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span><span class="pl-pds">"</span></span>
               },
               {
                  <span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>password<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>type<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>password<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>label<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Password<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>value<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span><span class="pl-pds">"</span></span>
               }
            ]
         }
      ]
   }
}

This feature is still under development and will likely change, but we wanted to get it out to developers ASAP since this is such a valuable mechanism.</pre>
<h2>FIXES</h2>
<ul>
 	<li>ISSUE <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/issues/960" data-url="https://github.com/MycroftAI/mycroft-core/issues/960" data-id="247681684" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#960</a>: Stop command would stop stopping if any skill handler for mycroft.stop has an error (and stops). (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/961" data-url="https://github.com/MycroftAI/mycroft-core/issues/961" data-id="247687954" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#961</a>)</li>
 	<li>ISSUE <a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/issues/950" data-url="https://github.com/MycroftAI/mycroft-core/issues/950" data-id="247452717" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#950</a>: Upgrade netifaces in requirements.txt to netifaces==0.10.6 (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/951" data-url="https://github.com/MycroftAI/mycroft-core/issues/951" data-id="247454844" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#951</a>)</li>
 	<li>FIX: Using an undeclared "logger" could crash during exception handling (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/963" data-url="https://github.com/MycroftAI/mycroft-core/issues/963" data-id="247842896" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#963</a>,<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/964" data-url="https://github.com/MycroftAI/mycroft-core/issues/964" data-id="247847329" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#964</a>)</li>
</ul>
<h2>MSM Enhancements</h2>
<ul>
 	<li>Clarified MSM return codes, distinguishing 'duplicate' and 'missing' skill requests (thanks el-tocino!) (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/945" data-url="https://github.com/MycroftAI/mycroft-core/issues/945" data-id="247286487" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#945</a>)</li>
 	<li>FIX: Correct user ownership on /opt/mycroft subdirectories when needed (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/947" data-url="https://github.com/MycroftAI/mycroft-core/issues/947" data-id="247429297" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#947</a>)</li>
</ul>
<h2>Misc</h2>
<ul>
 	<li>Add a standard commit message template (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/952" data-url="https://github.com/MycroftAI/mycroft-core/issues/952" data-id="247463399" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#952</a>)</li>
 	<li>Restrict requirement to mock==2.0.0 (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/949" data-url="https://github.com/MycroftAI/mycroft-core/issues/949" data-id="247452501" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#949</a>)</li>
 	<li>Upgrade requirement to netifaces==0.1.6 (<a class="issue-link js-issue-link" href="https://github.com/MycroftAI/mycroft-core/pull/951" data-url="https://github.com/MycroftAI/mycroft-core/issues/951" data-id="247454844" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#951</a>)</li>
</ul>
<h2>Mark 1 Arduino Code Released</h2>
Last, but not least:  We released the code used to drive the Arduino which controls the faceplate and interacts with the knob on the Mark 1.  You can find it all in the <a href="https://github.com/MycroftAI/enclosure-mark1">enclosure-mark-1 repo</a> on Github.  It is all released under the Apache 2.0 license, so have fun building on top of it for your own projects!