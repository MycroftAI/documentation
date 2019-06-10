---
ID: 48042
post_title: 'The Mycroft Home Redesign &#8211; Recap'
author: Chris Veilleux
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/the-mycroft-home-redesign-recap/
published: true
post_date: 2019-06-07 16:00:06
---
<em>Stop being afraid of what could go wrong, and start being excited about what could go right.</em>
<p style="padding-left: 40px;">- Tony Robbins</p>
During my career as a software engineering professional, I have encountered more people who fear change than those who embrace it. In my first programming job at a large company, change was abhorred. At another company, “refactoring” was considered a dirty word. I’ve been in many a heated debate about change, about risk out-weighing reward, and about the impact of change on velocity. My inclination is usually to favor change, because even though short-term discomfort and breakage is inevitable, so is the long-term benefit.

When I first started at Mycroft more than a year ago, our CTO expressed an interest in revamping the APIs and web applications, collectively named “Tartarus”. A few months later, I started to set my mind to it. After some consideration, the revamp became a complete re-architecture and “Selene” was born (Adam Selene was an alias for Mycroft in The Moon is a Harsh Mistress). After the new technology stack was selected, we built a <a href="https://mycroft.ai/blog/the-mycroft-skill-marketplace-first-step-into-our-new-web-presence/" target="_blank" rel="noopener noreferrer">proof-of-concept application</a>: <a href="https://market.mycroft.ai/skills" target="_blank" rel="noopener noreferrer">the Marketplace</a>. Then, about six months ago, we embarked on the project to convert Tartarus to the new Selene architecture. A couple of weeks ago, we launched the new software.
<h2>Why re-architect Tartarus?</h2>
A complete re-architecture of an entire software application should not be taken lightly. So why did we decide on such a drastic course of action? Here are the major reasons:
<ul>
 	<li>The old APIs were coded in Java and used a Neo4j graph database. Tartarus was the only application in the Mycroft ecosystem using these technologies. The overwhelming majority of Mycroft’s technology stack uses Python and PostgreSQL. Changing our APIs to use these prevailing technologies shrinks our overall technology stack, which is beneficial considering the limited resources we have available to maintain it.</li>
 	<li>Tartarus’ website, home.mycroft.ai, was written in React. Calm down, React fans. React is a fine library. However, we chose to move to Angular. Why? Well, Angular is a framework instead of a library. As such, it has a more opinionated and “batteries included” approach. Again, we have limited resources at Mycroft, so this was a big selling point. Having worked with Angular for the last several months, I have become a fan.</li>
 	<li>The old technology stack was architected to handle a massive load of millions of concurrent users, which we honestly don’t anticipate experiencing for quite some time. As such, it was expensive to operate and maintain. The new stack simplifies the code, which will improve our ability to fix bugs and add new functionality. It also has a smaller footprint, cutting the cost of running the applications by 60%.</li>
 	<li>We have learned a lot from using Tartarus for a few years. There are some things, like how skill settings were propagated across devices and the user experience of home.mycroft.ai, that we wanted to improve upon.</li>
</ul>
After we decided to re-architect, we needed to decide how to attack the problem. A piecemeal approach to the conversion was considered, to mitigate the risks associated with such a large undertaking. The issue we had with that approach was keeping the Neo4j and Postgres databases in sync until all of Tartarus was converted to Selene. In my experience, keeping two databases in sync is more fraught with risk than doing the conversion all at once.
<h2>Enhancements and New Features</h2>
While the goal of this project was to replicate the functionality of Tartarus, we were also able to make a few changes that I hope will improve the Mycroft experience.
<ul>
 	<li>There is nowhere in our software that uses your gender or birthday, so we removed these from the profile page.</li>
 	<li>We had some feedback from users that having geographical information at both the account level and the device level was confusing. To address this issue, we only collect geographical information at the device level now.</li>
 	<li>Collection of geographical information changed from a free-form text field to a set of predefined values for Country, Region, City and Time Zone.</li>
 	<li>The ability to define default device attributes has been added. This was done to make the device pairing flow easier for users.</li>
 	<li>The process of adding a new account has been updated to include setting up your profile.</li>
</ul>
<h2>No good deed goes unpunished…</h2>
Overall, the conversion from Tartarus to Selene went well. However, as with any project of this magnitude, there have been some bumps along the way. Since the launch a couple of weeks ago, we have been squashing bugs; some small, some less small.

The biggest issue was a small bug with unfortunately big consequences. A mistake in a database update statement resulted in skill settings being applied to multiple accounts. This was not only inconvenient, it also potentially exposed login credentials for the services saved in several skills, such as Pandora. This fortunately only impacted 36 users out of the 30,000+ using Mycroft. We wiped those credentials as soon as this was discovered and notified the affected users, but we were dismayed it was possible for this exposure to happen to anyone.

This reinforced the need for a capability we have been intending to implement for quite some time. Thus, we are moving up the task to encrypt individual skill settings.
<h2>We’re far from done!</h2>
While we have put a lot of work into making our APIs and web applications more user-friendly over the last six months, there is still much to do. There is some Tartarus functionality that has not yet been converted to Selene (the Precise and DeepSpeech taggers, for example). There is also some new functionality we would like to introduce that didn’t make it into the initial release, like the ability to group devices and apply skill settings to individual devices. Continuing to improve the visual appeal of the website is also on my list, among other things.
<h2>A team effort</h2>
Thanks to everyone who have helped us get this far in the project. My team did most of the technical work. There were some integrations with the voice assistant software that our Mycroft Core developers helped us resolve. Our design team provided a lot of input into the look and feel of the new website. Last, but certainly not least, the Mycroft Community has been helpful in testing and identifying things that we overlooked during both the preview period and in the days following the initial release.

I’m grateful to be involved with such an exciting technology and supportive community. It’s exciting to be done with the reconstruction so we can move on to building new things on our nimble new foundation!