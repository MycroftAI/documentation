---
ID: 30270
post_title: >
  Having the Right license is just as
  important as having a License
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: http://mycroft.ai/blog/right-license/
published: true
post_date: 2017-06-28 10:12:29
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]Our goal here at Mycroft AI is to create an assistant that runs anywhere and interacts exactly like a person. We envision a future where Mycroft is run by both enthusiasts and large international conglomerates. By small charities and large banks. To make the technology accessible we need to publish it under a legal framework that encourages adoption by individuals and organizations both large and small.
<h2>Overall Objectives</h2>
From the beginning, the intention with Mycroft was to produce a body of work that was available to everyone. Those involved in the early project realized closed systems created walled gardens that would inherently discourage collaboration. Given the huge task ahead, they knew the vision could only be achieved by collaborating with thousands of developers globally. The wider the code was used, the more valuable it would become to everyone. That is the win-win of open source!
<h2>Open Source License</h2>
It was obvious that "open source" was the way to create collaboration. The team built their first prototypes and last year published them on Github. However, Github requires selecting exactly which license to release code under. The GNU Public License — aka GPL — always comes to mind when talking open source. And everyone wants the latest, so the most recent revision was selected, GPLv3. The mycroft-core code was released under GPLv3 and the library Adapt was released under LPGLv3.
<h2>My Concerns</h2>
Since I joined the Mycroft team I've had concerns about the licenses that were chosen. For some time I have been thinking about and discussing the challenges of the GPL licenses... see my posts on StackOverflow about <a href="https://softwareengineering.stackexchange.com/a/326325/239488">GPL with Classpath Exception</a>. One big challenge that I see is that the licenses were crafted largely for C world, using terms such as "object code" in the <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">GPL</a> and "linking" in the <a href="https://www.gnu.org/licenses/lgpl-3.0.en.html">LGPL</a>. These concepts are vague in the world of Python, and vague is not good when talking about the law.
<h2>Anti-Tivoization</h2>
Additionally, version 3 of the GPL included a clause referred to as "anti-tivoization". As the name suggests, it was added because of the Tivo. It forces hardware that utilizes GPLv3 software to not only publish the code but also include a mechanism to allow the end-user to replace the software.

This sounds fair at first, but in the world of industrial, medical and automotive equipment there are often regulations and policies for safety purposes. Providing a path for a user to replace regulated software is sometimes illegal. As a result, GPLv3 software cannot be used in that equipment.
<h2>Patent-left</h2>
Finally, GPLv3 also introduces an idea sometimes called patent-left. Code under GPLv3 must also grant patent rights to downstream users. This hasn't been fully tested in a court case yet, but a fair interpretation of it leads to the very real potential that a patent license could be automatically granted to any company by making trivial use of the GPLed code. And since there are no taksie-backsies with the GPL — once you publish code, the license cannot be revoked — they could legitimately lose the ability to enforce a patent with a single ill-planned commit by a junior programmer. To any company with a patent portfolio, this prospect is terrifying. For more on this, see <a href="http://www.internationallawoffice.com/Newsletters/IT-Internet/International/Osborne-Clarke/Open-source-software-and-patents-how-the-GPLv3-affects-patent-portfolios">this article</a>.
<h2>Unintended Repercussions</h2>
The net result? By selecting GPLv3 we've made Mycroft less open, less collaborative and less useful than it would have been under more open licenses like MIT, BSD or Apache. Individuals and companies that want to make use of the software in commercial applications are taking risks with their patent portfolios and run the risk of ending up on the wrong side of a copyright suit. While adopting GPLv3 is probably a moral victory, in practice the license makes the software less accessible and less collaborative.
<h2>Relicensing</h2>
Because of this, we've made the decision to undergo the painful process of changing the license. This is not a simple, easy or inexpensive because it requires the permission of everyone who has contributed to the project, but we feel this change is critical to our community's success.
<h2>GPLv3 → Apache 2.0</h2>
We only want to do this once so our team has been working with DLA Piper, one of the top firms in the open source world, to review lots of different options. After careful consideration, our team feels the Apache 2.0 license provides the best legal protection for both the contributors and users of Mycroft. The Apache Software Foundation has expended lots of time creating terms that are legally safe and binding. As a result, the Apache web server has been widely adopted around the world in commercial, non-profit, private scenarios. It underpins many technologies, both open and closed and has thrived. This is the model we want to follow.
<h2>Impact?</h2>
For most of you, the net result of this is... nothing will be different. Only existing contributors will need to take action during the relicensing effort. Future contributors will need to take an additional step during development to clarify the legal status of their contributions, but that is a topic for another post.

But the real impact of this change is that Mycroft will be easy and clean for <em>anyone</em> to adopt in whatever they are building. Speakers, TVs, medical devices, industrial equipment, STEAM projects and more. After this is complete we'll be much closer to the goal we set out to achieve – producing an AI for Everyone.[/vc_column_text][/vc_column][/vc_row]