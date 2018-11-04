---
ID: 40706
post_title: Introducing Mycroft Translate
author: Kathy Reid
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/introducing-mycroft-translate/
published: true
post_date: 2018-09-28 02:26:58
---
<blockquote>
<h4><em>“I just enjoy translating, it's like opening one's mouth and hearing someone else's voice emerge.” </em>
<em>― Dame <a href="https://en.wikipedia.org/wiki/Iris_Murdoch"><span style="text-decoration: underline;"><span class="authorOrTitle">Iris Murdoch</span></span></a></em></h4>
</blockquote>

<hr />

A few months ago, we outlined our desire to provide stronger language support for Mycroft, noting that <a href="http://mycroft.ai/blog/languages-are-hard/">localization support is hard</a>. The desire from our Community for better language support, especially for French, German, Dutch and Italian, was echoed in the <a href="http://mycroft.ai/blog/picroft-survey-2018-results/">2018 Picroft Survey results</a>.
<h2>We're now delighted to announce the first release of <a href="https://translate.mycroft.ai">Mycroft Translate</a> - a platform for enabling the Community to help translate Skills into other languages.</h2>
<h3>Choosing a platform for translation</h3>
Our recent <a href="http://mycroft.ai/blog/dealing-with-worthless-interns/">intern</a>, Masters of Computer Science postgraduate student, <a href="https://www.linkedin.com/in/andrew-wilson-4a709b165/">Andrew Wilson</a>, undertook an evaluation of platforms. We initially were attracted to <a href="http://zanata.org">Zanata</a> because of its intuitive user interface and ease of setup, but eventually settled on <a href="https://pootle.translatehouse.org/">Pootle</a>. Pootle has a closer alignment with our existing technology stack, being based on Python and Django. We made the decision to backend Pootle on to Postgres as the database layer, again reflecting existing deployments. Pootle is highly configurable, and extensible. That means we can add support for additional languages in the future, particularly languages that may have only small groups of speakers around the world.
<h3>Languages chosen for the initial release</h3>
For our initial release of Mycroft Translate, we've chosen a small number of languages that are available for translation, as we are anticipating some 'teething problems' with the new platform, and want to constrain these.

Our decisions here are informed by a number of drivers; existing translations of Skills by the Community, our web analytics which tell us where in the world our Community is based, and additional factors - such as our desire to cater for more 'niche' languages that have limited populations - such as <i lang="cy" title="Welsh language text">Cymraeg (Welsh), <i><i lang="is" title="Icelandic language text">íslenska (Icelandic), </i></i></i>and<i lang="cy" title="Welsh language text"><i><i lang="is" title="Icelandic language text"><i lang="haw" title="Hawaiian language text"><span class="unicode">ʻ</span>Ōlelo Hawai<span class="unicode">ʻ</span>i (Hawai'ian) - </i></i></i></i>but which are vitally important for the communities who speak them<i lang="cy" title="Welsh language text"><i><i lang="is" title="Icelandic language text"><i lang="haw" title="Hawaiian language text">. </i></i></i></i>At the moment, we've opened up two <a href="https://en.wikipedia.org/wiki/CJK_characters">CJK-grouped languages</a>, although we're not sure exactly how well the platform will handle the non-Latin characters these languages require.
<h3>Quality assurance and approval workflow</h3>
Within the platform, we've implemented a workflow that ensures each translation is reviewed before being accepted. Over time, we anticipate building out volunteer translation teams for each language, with Community members able to curate provided translations. This ensures both Community ownership of language support with Mycroft, and enables strong quality control as people fluent in a language are overseeing how it is used with open source voice.

The roles and permissions within the platform are;
<table>
<tbody>
<tr>
<td style="text-align: left;"><b>Role name</b></td>
<td style="text-align: left;"><b>Role permissions</b></td>
<td style="text-align: left;"><b>How ascribed</b></td>
</tr>
<tr>
<td style="text-align: left;"><i><span style="font-weight: 400;">Registered users</span></i></td>
<td>
<ul>
 	<li style="text-align: left;"><span style="font-weight: 400;">Suggest a translation</span></li>
</ul>
</td>
<td style="text-align: left;"><span style="font-weight: 400;">At login</span></td>
</tr>
<tr>
<td style="text-align: left;"><i><span style="font-weight: 400;">Language Team Member</span></i></td>
<td>
<ul>
 	<li style="text-align: left;"><span style="font-weight: 400;">Suggest a translation</span></li>
 	<li style="text-align: left;"><span style="font-weight: 400;">Review a translation</span></li>
</ul>
</td>
<td style="text-align: left;"><span style="font-weight: 400;">By a Language Chair</span><i></i></td>
</tr>
<tr>
<td style="text-align: left;"><i><span style="font-weight: 400;">Language Chair, ie
Mycroft French Language Chair
or Mycroft Portuguese Language Chair</span></i></td>
<td style="text-align: left;">
<ul>
 	<li><span style="font-weight: 400;">Provide translations without review</span></li>
 	<li><span style="font-weight: 400;">Review suggested translations</span></li>
 	<li><span style="font-weight: 400;">Administer all translations for a language</span></li>
 	<li><span style="font-weight: 400;">Administer all user permissions for a language</span></li>
</ul>
</td>
<td>
<p style="text-align: left;"><span style="font-weight: 400;">By another Language Chair</span><i></i></p>
<p style="text-align: left;"><i><span style="font-weight: 400;">or</span></i></p>
<p style="text-align: left;"><span style="font-weight: 400;">By Mycroft Staff Member</span></p>
</td>
</tr>
</tbody>
</table>
<h3>How you can participate in Mycroft Translate efforts and help bring YOUR language to Mycroft?</h3>
Participating in Mycroft Translate is just one of the ways you can <a href="http://mycroft.ai/get-involved/">get involved</a> with the Mycroft Community. Providing translations is very straightforward, as outlined below.
<h4>Create an account and sign in</h4>
Unfortunately we haven't yet integrated the Pootle platform with <a href="https://home.mycroft.ai">home.mycroft.ai</a> - something we hope to do in the future. For now, you'll have to create a separate account on <a href="https://translate.mycroft.ai">https://translate.mycroft.ai</a>.

<em><a href="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-1.png"><img class="alignnone wp-image-40747" src="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-1.png" alt="Mycroft Translate - Create account and sign in" width="960" height="540" /></a></em>

Once you log in, you'll be able to see the Projects available for translation. All the vocab words for translation from the <a href="https://github.com/MycroftAI/mycroft-skills">Mycroft Skills repo on GitHub</a> are in the <a href="https://translate.mycroft.ai/projects/mycroft-skills/">mycroft-skills</a> project.

<a href="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-2.png"><img class="alignnone wp-image-40752" src="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-2.png" alt="Mycroft Translate - Projects available for translation" width="960" height="540" /></a>
<h4>Choose the language and project you wish to provide translations for</h4>
Next, choose the language you'd like to provide translations for from the Language dropdown.

<a href="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-3.png"><img class="alignnone wp-image-40754" src="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-3.png" alt="" width="960" height="540" /></a>

Then, choose the "mycroft-skills" project from the Project dropdown.

<a href="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-4.png"><img class="alignnone wp-image-40755" src="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-4.png" alt="Mycroft Translate - Choose a project for translation" width="960" height="540" /></a>

Next, select the Skill you wish to provide translations for.

<em><a href="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-5.png"><img class="alignnone wp-image-40757" src="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-5.png" alt="Mycroft Translate - Choose a Skill to provide translations for" width="960" height="540" /></a></em>

Next, choose 'Continue Translation'.

<em><a href="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-6.png"><img class="alignnone wp-image-40758" src="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-6.png" alt="Mycroft Translate - Continue translations" width="960" height="540" /></a></em>

Then enter your translation, and press the 'Submit' button. It's that simple!

<em><a href="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-7.png"><img class="alignnone wp-image-40759" src="https://mycroft.ai/wp-content/uploads/2018/09/Translate-Walkthrough-7.png" alt="Mycroft Translate - Enter translation" width="960" height="540" /></a>At the moment we're unable to handle multi-line translations - for instance where a phrase or sentence needs to be used to translate a word from English, but are following up to see how we can enable this. </em>
<h3>What's next on the <a href="https://docs.google.com/document/d/1otSj9YBEASCPAgD7MZmUR4m5Nal5O0fjN67y3gJRfNg/edit#heading=h.ck6l3z2vlex4">Languages Roadmap</a>?</h3>
Earlier in the year, we <a href="http://mycroft.ai/blog/many-roads-one-destination/">published our open and transparent Roadmaps for each of the key streams of the Mycroft ecosystem</a>. For the Languages stream, we anticipate firstly building more automation into the existing platform - essentially being able to import new <code>vocab</code> and <code>dialog</code> from Skills as they become available, and also export translations from Pootle into GitHub via the GitHub API. This will likely take us a few weeks, as we envisage quite a few kinks to work through.
<h3>Want more information?</h3>
We have a dedicated email address for questions related to Mycroft Translate - you can mail us at <a href="mailto:translate@mycroft.ai">translate@mycroft.ai</a>. You can also check out the <a href="https://community.mycroft.ai/c/languages">Languages topics on our Community Forum</a>, or the <a href="https://chat.mycroft.ai/community/channels/languages">Languages Channels in Mycroft Chat</a>.