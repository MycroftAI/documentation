---
ID: 39484
post_title: Many Roads, One Destination
author: Steve Penrod
post_excerpt: >
  CTO Steve Penrod has assembled these
  Mycroft Development Roadmaps into a
  Master Roadmap that will guide Mycroft
  development progress going forward.
layout: post
permalink: >
  http://mycroft.ai/blog/many-roads-one-destination/
published: true
post_date: 2018-07-20 10:30:59
---
<span style="font-weight: 400;">When working with a group, it is important to make sure everyone is pulling towards a common goal. Exploring different routes is great, but if groups are traveling to different destinations, collaboration breaks down and becomes counterproductive.</span>

<span style="font-weight: 400;">Documents known as </span><i><span style="font-weight: 400;">Roadmaps </span></i><span style="font-weight: 400;">help communicate the destination of development, along with expected milestones on the journey. They are also good at communicating the progress made so far. On a long road it is easy to forget all the ground that has been covered when anxious to get to the final destination.</span>
<h1><a href="https://docs.google.com/document/d/1QntesVNTGx-DlSK45gjFi5ToDJtDuMwYY_C-u9C3fFI" target="_blank" rel="noopener"><span style="font-weight: 400;">Roadmap of Roadmaps</span></a></h1>
<span style="font-weight: 400;">Mycroft is a particularly difficult project to roadmap because of the breadth of the technologies involved, the rapid development in the state of the art for these technologies, and the intentionally decentralized approach we are taking. I’ve settled on a slightly unusual approach: I’m publishing a master Roadmap that in turn refers to many independent Roadmaps. This helps organize it all in an easier to consume way.</span>

<span style="font-weight: 400;">I’ve broken the near-term goals into seven independent categories. Although there is some interdependence, progress can largely be made in each category at its own pace.</span>
<h1><span style="font-weight: 400;">Roadmap: </span><a href="https://docs.google.com/document/d/1Ai2LcJRYUmzw8L6BK8hKWckFYfAAwzuAUYtw9uRuXuc" target="_blank" rel="noopener"><span style="font-weight: 400;">Marketplace</span></a></h1>
<span style="font-weight: 400;">This goal has been a long time in the making. We have been building the decentralized Skill development mechanism for some time. The <code>mycroft-skills</code> repo was the first step in allowing coordination between independent Skill Authors and easy Skill discovery for users.</span>

<span style="font-weight: 400;">You can see a preview of a </span><a href="https://mycroftai.github.io/mycroft-skills/" target="_blank" rel="noopener"><span style="font-weight: 400;">Skill List</span></a><span style="font-weight: 400;"> automatically generated from the README.md files for Skills that are registered at the <code>mycroft-skills</code> repo.  Jumping from this to being able to browse and install Skills in a store is pretty straightforward. Look for a more polished Marketplace soon, bringing together Skill Authors and users.</span>
<h1><span style="font-weight: 400;">Roadmap: </span><a href="https://docs.google.com/document/d/1gSXU5-UaXSOOA7T9UWz1hT779o36pIYOard3iGXlHCA" target="_blank" rel="noopener"><span style="font-weight: 400;">Text to Speech</span></a></h1>
<span style="font-weight: 400;">In the last few months we’ve made some exciting progress implementing <a href="https://mycroft.ai/blog/available-voices/" target="_blank" rel="noopener">Mimic2</a>, a machine learning based Text to Speech engine.  We’ve also created tools to assist in creating new voices, soon making it possible for non-specialists to create a voice.</span>

The ability to use Mimic2 on your Mycroft devices is coming very soon - stay tuned.
<h1><span style="font-weight: 400;">Roadmap: </span><a href="https://docs.google.com/document/d/1o0b5r8qcxan59TxSeJxBX5x1ehcT1xWiX7b_mN6IfQw" target="_blank" rel="noopener"><span style="font-weight: 400;">Speech to Text</span></a></h1>
<span style="font-weight: 400;">Since last summer we have been building the relationship and infrastructure (technical and legal) to provide the <a href="https://voice.mozilla.org/" target="_blank" rel="noopener">Mozilla DeepSpeech</a> team with real-world recordings for training their open Speech to Text model for English. Mycroft community members have been able to <a href="https://mycroft.ai/blog/deepspeech-update/" target="_blank" rel="noopener">use DeepSpecch for Mycroft</a> since March.</span>
<h1><span style="font-weight: 400;">Roadmap: </span><a href="https://docs.google.com/document/d/1UsN9BLuHeiuuP92LEm17GSfufNcRyP1j8HB_W5FUHcE" target="_blank" rel="noopener"><span style="font-weight: 400;">Wake Word</span></a></h1>
<span style="font-weight: 400;">The Precise wake word engine has been under development since last fall, with a large effort by both the developers and the community to gather and tag utterances necessary to generate the first wake word model -- Hey Mycroft. As we make the last push in gathering the data we anticipated for the machine learning model, we can generalize some lessons from insights that can be applied to new wake words.</span>
<h1><span style="font-weight: 400;">Roadmap: </span><a href="https://docs.google.com/document/d/1GvhoqC9mUTEDLrwXVSEQ4JecuUMKaTpE1l1FNE6mMTA" target="_blank" rel="noopener"><span style="font-weight: 400;">Framework (mycroft-core)</span></a></h1>
<span style="font-weight: 400;">The framework that connects all of the above pieces, Mycroft Core, continues to mature and expand to make development quicker and easier.</span>
<h1><span style="font-weight: 400;">Roadmap: </span><a href="https://docs.google.com/document/d/1otSj9YBEASCPAgD7MZmUR4m5Nal5O0fjN67y3gJRfNg" target="_blank" rel="noopener"><span style="font-weight: 400;">Language Support</span></a></h1>
<span style="font-weight: 400;">One of the most exciting things about all of the core technologies that we are pursuing is that we can transfer the machine learning techniques directly to most new languages. I expect there will be some unanticipated challenges, but many of the barriers that used to exist -- previously requiring highly trained specialists to overcome -- have fallen away.</span>

<span style="font-weight: 400;">Tools will be made available to start this work in August, and work on a Welsh voice will begin very soon - Rhagorol!!</span>
<h1><span style="font-weight: 400;">Roadmap: </span><a href="https://docs.google.com/document/d/1VJsk9xmFig1qAP-wH_SAB-3xyKRx28Z47IwlJWJMqOM" target="_blank" rel="noopener"><span style="font-weight: 400;">Personal Server</span></a></h1>
<span style="font-weight: 400;">One of the goals of Mycroft has always been creating a technology that is usable in all sorts of situations. Our architecture severs the necessity for centralization on cloud servers. However, the computational load does call for access to equipment such as GPUs. Enabling a Personal Server which can run on a “low hanging cloud” within a user’s home remains a goal of the project and the community.</span>
<h1><span style="font-weight: 400;">Feedback Loop!</span></h1>
<span style="font-weight: 400;">Like any good learning system, Mycroft gets better with more data. (Don't forget, </span>the easiest ways to help Mycroft is to <a href="https://mycroft.ai/blog/privacy-machine-learning-open-data-set-opt-feature/" target="_blank" rel="noopener">Opt-In to the Open Dataset</a> and use Mycroft every day!)

I’m publishing all of these roadmaps with Comment permission so that we can hear back from you. Select areas of the roadmaps and click on the comment icon to the right side to add your input.

<span style="font-weight: 400;">Additionally, these are living documents and will continue to be updated as we take this journey together. Come along with us!</span>