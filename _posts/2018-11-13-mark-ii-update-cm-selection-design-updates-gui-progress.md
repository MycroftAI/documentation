---
ID: 41437
post_title: 'Mark II Update: CM Selection, Design Updates, GUI Progress'
author: Derick Schweppe
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/mark-ii-update-cm-selection-design-updates-gui-progress/
published: true
post_date: 2018-11-13 15:30:13
---
It has been way too long since we have had an update here about Mark II. Lots of things moving, lots of challenges, and still a few more hurdles to overcome.

<span style="font-weight: 400;">Before I get into the design update, our COO Nate has this delivery update.</span>
<blockquote><em><span style="font-weight: 400;">While we want to ensure the fastest delivery of the Mark II to our backers, our top priority is quality. Although we are over a lot of the major hurdles, there are still some coming to surface. Since this isn’t the first piece of hardware we have developed, we know there will be more. </span><span style="font-weight: 400;">Until now, we have been talking about a December shipment to our backers. The reality is, that due to delays, we can’t fulfill all backers on this timeframe.</span><span style="font-weight: 400;"> We are deep in the different stages of hardware development and working through what that timeline looks like, and figuring out all of these pieces. As soon as we get the final date from the CM and other technical resources needed to produce the Mark II, we will update the community. Apologies for the bad news, but for now, take a look at the progress that has been made recently.</span></em></blockquote>
<h2>Selecting our Contract Manufacturer</h2>
Back in May, we published <a href="https://mycroft.ai/blog/choosing-contract-manufacturer/" target="_blank" rel="noopener">this blog on picking a Contract Manufacturer</a> (CM). We continued reviewing partners and came to a decision a few months ago. We’re happy to announce now that we’ve selected <a href="https://www.teksun.us/" target="_blank" rel="noopener">Teksun</a> as our CM Partner. Teksun has a presence in the US and India, and we have been working with both sides to tie up a bunch of loose ends. Currently, they are building a small batch of boards, working on some prototypes for certification testing, and procuring enough parts to fulfill all you backers out there.

Teksun is a fully capable product development company and one of their services is tooling design. We have completed the mechanical design with DFM (Design for Manufacture) in mind, but there is still a lot of work that needs to be done to translate a finished design into a moldable part. Things like final draft analysis, adding small rounds to avoid weak spots in the plastic, and perfecting the wall thicknesses to avoid shrink marks are all considered when preparing to create the mold. We are excited to have Teksun on board and are very happy with their progress so far.
<h2>Mark II Design Updates</h2>
Slight changes are happening in the Mark II Industrial Design. We had some challenges developing and manufacturing the cloth cover, and we decided to rethink the design. Sometimes keeping it simple is the best strategy, and we think the new design looks great. The front keeps the cloth cover but the back is smooth and all business with an exposed grill for the speakers and an exposed port that improves the bass response. The front cloth faceplate is still removable, so Mark II can customizable. Since the front has a laid-back look and the back is all business, we’ve been calling it the “Reverse Mullet” internally. See the rendering below and the latest 3D printed prototype (without paint and without fabric cover).

[gallery ids="41438,41439,41440"]
<h2>GUI progress</h2>
The Graphical Interface on the Mark II is completely different than the Mark I and needs a new framework. Translating from the prototype stage to something that can scale and work well with our Community Developers requires some expertise. We are working with a team that is very familiar with Mycroft, and are experts in GUI. They are one of the biggest contributors to a very popular open source distro. We can share more of our process on this really soon.
<h2>Display Issues</h2>
Working with displays for embedded devices is a real challenge. We selected a different display for manufacturing than our original prototype. This was for various reasons, but mostly performance and availability. In order for the display to work, we need drivers from our SOC (Xilinx), and we need to have the hardware configured correctly to send the right signals to the display (our interface is Mipi). <span style="font-weight: 400;">If only it was as easy as plugging in an HDMI cable. However, there are big differences in display interfaces, and nothing is standardized enough to be plug and play.</span> We have hit delays on both of these aspects that have taken some time to sort out. Thankfully we have had a lot of help from all over the world to debug the issue and we are nearly past this hurdle. Xilinx and our GUI experts have been extremely helpful during this process. See the display working with a color bar test.

<a href="https://mycroft.ai/wp-content/uploads/2018/11/MarkIIworking_1200x600.png"><img class="alignnone wp-image-41506 size-full" src="https://mycroft.ai/wp-content/uploads/2018/11/MarkIIworking_1200x600.png" alt="Color bar test on Mark II's display" width="1200" height="600" /></a>

We should be putting it all together soon and showing some demos of the new GUI progress. Stay tuned!