---
ID: 30062
post_title: Themes and goals for Mycroft Core 17.08a
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/themes-goals-mycroft-core-17-08a/
published: true
post_date: 2017-06-05 21:01:16
---
One of the things I often hear in Silicon Valley when I talk about Mycroft is this: “The technology is so broad, the problem so difficult, the goal so distant, what is the Mycroft team going to work on first?” This is a common problem with both ambitious projects and open communities. Founders, developers, and community members want to move fast, build great new features, expanding their technology to fully inhabit the vision.

[caption id="attachment_30066" align="aligncenter" width="594"]<img class="size-full wp-image-30066" src="https://mycroft.ai/wp-content/uploads/2017/06/JonoBaconEngadgetExpandNYDay3wEW1J_BMkcPl.png" alt="" width="594" height="401" /> Jono Bacon, an all around awesome guy.[/caption]

&nbsp;

Our adviser and friend Jono Bacon pointed out to us last month that many of the teams he's worked with in the past have had the same problem. Focusing their team on a single theme so that the problems can get solved quickly. His suggestion? Jono recommended that the Mycroft team set a single theme of focus for each release cycle.

With that in mind, the leadership team sat down and gave some careful thought to where our efforts should be focused over the next several months. (By the way: To get this done in a timely way, our internal team is setting the goals for the next release. After 17.08a, we'll work to better include the community in this process – your input is important to us.)

<strong>We came up with two major themes:</strong>
<ol>
 	<li>Make it easier for developers to work with Mycroft</li>
 	<li>Polish the core user interaction and skills</li>
</ol>
<h2><strong><img class="aligncenter size-full wp-image-30079" src="https://mycroft.ai/wp-content/uploads/2017/06/diagram.001.jpeg" alt="" width="1920" height="1080" /></strong></h2>
&nbsp;
<h2><strong>Make it easier for developers to work with Mycroft</strong></h2>
Before the release of the Mycroft Raspberry Pi image in January, it was very difficult to get Mycroft running. There is a variety of services, processes, and data sources that interact to create the Mycroft user experience – figuring out how to integrate them, start them, and deploy them, was a bit of a nightmare.

Honestly – based on the feedback we've gotten from the community – we still have a long way to go to make it easy for developers to build skills on the platform. We need to work on the following:
<ol>
 	<li><strong>Discovery</strong> – Communicating what Mycroft does, why it is important, and where to get both the software and the documentation.</li>
 	<li><strong>Documentation</strong> – The documentation for Mycroft should be comprehensive and easy to navigate. Right now, documentation is largely handled by Mycroft staff, but going forward we need to make it easy for any developer or user to quickly edit and update our documentation. Success at this task will give community members who are not coders the ability to contribute to the platform in a meaningful way.</li>
 	<li><strong>Installation</strong> – Downloading and installing Mycroft on the developer's chosen platform. Mycroft is composed of several technology stacks that have to work in concert. We want to make it trivial to download and install Mycroft and Mycroft's source code.</li>
 	<li><strong>Toolchain</strong> – Though an easy installation is important for users, developers also need access to the toolchain. It should be easy for developers to execute our autotests, validate their code, submit their work to the master branch, and generate documentation.</li>
 	<li><strong>Task Selection</strong> – We have a ton of features, bugs, and data generation tasks that need to be performed. Our goal this summer is to make it easy for developers to select a task, collaborate with one another, and track progress.</li>
 	<li><strong>Contribution Management</strong> – As our community fixes bugs, implements features and generates data sets that improve the technology, we need to establish an air-tight process for reviewing contributions to pull them into the master branch. This is true of inputs to our core technology, but is also true of contributed skills.</li>
 	<li><strong>Feedback</strong> – With more and more developers working with the platform, we are going to need to get better at providing feedback, both positive and negative. Some of this feedback may take the form of constructive criticism, but it is far more likely that the response will come in the form of praise, recognition, and accolades. As a community, we need to celebrate the women and men who are making significant improvements.</li>
</ol>
<h2><strong>Polish the Core Interaction and Skills</strong></h2>
Relative to the original Amazon Echo, Mycroft actually holds up quite well. This is despite the fact that Mycroft doesn't have a far-field microphone array or any other specialized hardware built in. Unfortunately, Mycroft is being compared with the latest versions of Alexa, not the version that was shipping two years ago. Our friends at Amazon have made huge progress in the past two years.

That means we have a tall mountain to climb when it comes to building a quality user interaction. After all, we are building an AI that runs anywhere and interacts exactly like a person. Achieving this goal isn't simply a matter of building awesome skills.

To attain our objective, we need to make using Mycroft as easy as talking to a friend. Whether Mycroft is turning on the lights, starting a movie on the TV, or getting the latest baseball scores, it needs to interact like a friend would. If Mycroft doesn't understand a question, it should ask again. It should be able to keep the thread of a conversation, understand implied context, etc.

With this in mind, our second focus is improving the user interaction to make it seamless. We've brought in a fantastic UX design team and they will be working with our developers to shape the experience both overall and within each skill. As we develop best practices, we will be sure to share them widely in the form of suggested design principles for skill creation.

When we get closer to our August release date, we'll evaluate our progress in these areas and, in partnership with the community, establish themes for the following release. As always, we are happy to receive input from our community about where the technology is and where it is going. The community is, after all, the motive force behind our development.