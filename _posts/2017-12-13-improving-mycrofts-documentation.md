---
ID: 33640
post_title: 'Rocking the docs: improving Mycroft&#8217;s documentation'
author: Kathy Reid
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/improving-mycrofts-documentation/
published: true
post_date: 2017-12-13 20:59:33
---
Imagine you've just joined a new technology company, and one of the first tasks you're assigned is to improve and centralize the organization's developer-facing documentation. There's just one catch! That documentation exists in many different places, across several platforms, and differs markedly in accuracy, currency and style.

So how did we tackle this challenge?
<h2>Understanding the scope</h2>
Just like any project, we first needed to understand the scope and bounds of the problem we were trying to solve. What documentation was good? What was working? What wasn't? How much documentation was there? What format was it in? We needed to do a <strong>documentation audit</strong>. Luckily, <a href="https://opensource.com/users/aneta">Aneta Šteflová</a> had recently <a href="https://opensource.com/article/17/10/doc-audits">published an article on OpenSource.com</a> about this - and it provided excellent guidance.

&nbsp;

[caption id="attachment_33646" align="alignnone" width="1603"]<a href="https://mycroft.ai/wp-content/uploads/2017/12/mycroft-documentation-audit.png"><img class="size-full wp-image-33646" src="https://mycroft.ai/wp-content/uploads/2017/12/mycroft-documentation-audit.png" alt="audit" width="1603" height="372" /></a> Mycroft documentation audit, showing source, topic, medium, currency, quality and audience[/caption]

&nbsp;

Next, every piece of publicly facing documentation was assessed for the topic it covered, the medium it used, currency and quality. A pattern quickly emerged that different platforms had major deficiencies, allowing us to make a data-driven approach to decommission our existing Jekyll-based sites. The audit also highlighted just how fragmented our documentation sources were - we had developer-facing documentation across no less than seven sites. Although search engines were finding this content just fine, the fragmentation made it difficult for Developers and Users of Mycroft - our primary audiences - to navigate the information they needed. Again, this data helped us make the decision to centralize our documentation on to one platform.
<h2>Choosing a central platform</h2>
As an organisation, we wanted to constrain the number of standalone platforms in use. Over time, maintenance and upkeep of multiple platforms and integration touchpoints becomes cumbersome for any organization, but this is exacerbated for a small start-up. One of the other business drivers in platform choice was that we had two primary but very different audiences. On one hand, we had highly technical Developers who we were expecting would push documentation to its limits - and who would want to <em>contribute</em> to technical documentation using their tools of choice - <a href="https://git-scm.com/">Git</a>, <a href="https://github.com/MycroftAI">GitHub</a> and <a href="https://en.wikipedia.org/wiki/Markdown">Markdown</a>. Our second audience - end Users - would primarily <em>consume</em> technical documentation and would want to do so in an inviting, welcoming platform that was visually appealling and which provided additional features - such as the ability to identify reading time, and to provide feedback. The ability to capture feedback was also a key requirement from our side - as without feedback on the quality of the documentation we would not have a solid basis to undertake continuous quality improvement.

Would we be able to identify one platform that met all of these competing needs?

We realised that two platforms covered all of our needs:
<ul>
 	<li><a href="https://www.wordpress.org">WordPress</a>: Our existing website is built on WordPress, and we have some reasonably robust WordPress skills in-house. The flexibility of WordPress also fulfilled our requirements for functionality like reading time and the ability to capture User feedback.</li>
 	<li><a href="https://github.com">GitHub</a>: Almost <a href="https://github.com/mycroftai">all of Mycroft.AI's source code is available on GitHub</a>, and our development team use this platform daily.</li>
</ul>
But how could we marry the two?
<h2>Integrating WordPress and GitHub with WordPress GitHub Sync</h2>
Luckily, our COO, <a href="http://mycroft.ai/team/">Nate Tomasi</a>, spotted a WordPress plugin which promised to integrate the two.<a href="https://mycroft.ai/wp-content/uploads/2017/12/wordpress-github-sync.png" target="_blank" rel="https://wordpress.org/plugins/wp-github-sync/ noopener"><img class="aligncenter wp-image-33653" src="https://mycroft.ai/wp-content/uploads/2017/12/wordpress-github-sync.png" alt="wordpress github sync" width="601" height="352" /></a>

This was put through its paces on our test website, and passed with flying colors. It was easy to install, had a straightforward configuration, which just required an oauth token and webhook with GitHub, and provided two-way integration between WordPress and GitHub.

It did however have a dependency - on Markdown - which proved a little harder to implement. We trialled several Markdown plugins, but each had several quirks that interfered with the rendering of non-Markdown based content. After several days of frustration, and even an attempt to custom-write a plugin for our needs, we stumbled across <a href="https://wordpress.org/plugins/parsedown-party/">Parsedown Party</a>. There was much partying! With WordPress GitHub Sync and Parsedown Party, we had integrated our two key platforms.

Now it was time to make our content visually appealling and usable for our User audience.
<h2>Reading time and feedback</h2>
To implement the Reading Time and Feedback functionality, we built a new <a href="https://developer.wordpress.org/themes/template-files-section/page-template-files/">Page Template for WordPress</a>, and leveraged Plugins within the Page Template.

Knowing the estimated reading time of an article in advance has been <a href="https://marketingland.com/estimated-reading-times-increase-engagement-79830">proven to increase engagement with content</a> - and provides Developers and Users with the ability to decide whether to read the content now, or to bookmark it for later. We tested several WordPress plugins for reading time, but settled on <a href="https://jasonyingling.me/reading-time-wp/">Reading Time WP</a> because it was highly configurable, and could be easily embedded into WordPress Page Templates. Our decision to place Reading Time at the top of the content was designed to give the User the choice of whether to read now or save for later. With Reading Time in place, we then turned our attention to gathering User feedback and ratings for our documentation.

<a href="https://mycroft.ai/wp-content/uploads/2017/12/Screenshot-from-2017-12-08-00-55-31.png"><img class="wp-image-33655 alignleft" src="https://mycroft.ai/wp-content/uploads/2017/12/Screenshot-from-2017-12-08-00-55-31.png" alt="Reading Time WP in action" width="599" height="185" /></a>

<a href="https://mycroft.ai/wp-content/uploads/2017/12/multi-rating-pro.png">
<img class="wp-image-33657 alignleft" src="https://mycroft.ai/wp-content/uploads/2017/12/multi-rating-pro.png" alt="multi-rating-pro" width="600" height="328" /></a>

There are several rating and feedback plugins available for WordPress. We needed one that could be easily customized for several use cases, and which could aggregate or summarise ratings. After some experimentation, we settled on <a href="https://multiratingpro.com/">Multi Rating Pro</a>, because of its wide feature set, especially the ability to create a Review Ratings page in WordPress - ie a central page where staff can review ratings without having to be logged in to the WordPress back end. The only gap we ran into here was the ability to set the display order of rating options - but it will likely be added in a future release.

The WordPress GitHub Integration plugin also gave us the ability to link back to the GitHub repository where the original Markdown content was held, inviting technical Developers to contribute to improving our documentation.
<h2>Updating the existing documentation</h2>
Now that the 'container' for our new documentation had been developed, it was time to update the existing content.  Because much of our documentation had grown organically over time, there were no style guidelines to shape how keywords and code were styled. This was tackled first, so that it could be applied to all content.
<blockquote><a href="https://github.com/MycroftAI/docs-rewrite/blob/master/README.md">You can see our content style guidelines on GitHub</a></blockquote>
As part of the update, we also ran several checks to ensure that the content was technically accurate, augmenting the existing documentation with several images for better readability.

There were also a couple of additional tools that made creating internal links for documentation pieces easier. First, we installed the <a href="https://wordpress.org/plugins/wp-anchor-header/">WP Anchor Header</a> plugin. This plugin provided a very small, but very important function - adding <code>id</code> attributes to each <code>&lt;h1&gt;</code>, <code>&lt;h2&gt;</code> (and so on) element. This meant that internal anchors could be automatically generated on the command line from the Markdown content in GitHub using the <code><a href="https://github.com/jonschlinkert/markdown-toc">markdown-toc</a></code> library, then simply copied in to the WordPress content, where they would automatically link to the <code>id</code> attributes generated by WP Anchor Header.

Next, we imported the updated documentation into WordPress from GitHub, and made sure we had meaningful and easy-to-search on slugs, descriptions and keywords - because what good is excellent documentation if no one can find it?! A final activity was implementing redirects so that people hitting the old documentation would be taken to the new version.
<h2>What next?</h2>
<a href="https://mycroft.ai/documentation">Please do take a moment and have a read through our new documentation</a>. We know it isn't perfect - far from it - but we're confident that the mechanisms we've 'baked in' to our new documentation infrastructure will make it easier to identify gaps - and resolve them quickly. If you'd like to know more, or have suggestions for our documentation, please do reach out to Kathy Reid on <a href="https://chat.mycroft.ai">Chat</a> (@kathy-mycroft) or via <a href="mailto:kathy.reid@mycroft.ai">email</a>.

&nbsp;