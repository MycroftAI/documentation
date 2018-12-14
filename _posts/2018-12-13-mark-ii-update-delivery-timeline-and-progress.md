---
ID: 42379
post_title: 'Mark II Update: Delivery Timeline and Progress'
author: Nate Tomasi
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/mark-ii-update-delivery-timeline-and-progress/
published: true
post_date: 2018-12-13 19:24:35
---
<span style="font-weight: 400;">Hello Everyone,</span>

<span style="font-weight: 400;">This is an overdue update on Mark II. It is my attempt to bring you up to speed on current progress and show off some good news.</span>

<span style="font-weight: 400;">First, we need to say that Mark II will not ship in December. We’re sorry to push the timeline but as always, we want to deliver the best product possible. There was no version of Mark II we could ship in December that would meet our company or Community's standards. Read more below.</span>

<span style="font-weight: 400;">When beginning the design, development, and manufacturing of Mark II we had a great outline of tasks and dependencies needed to produce a rough timeline. After moving through the gates I can reflect that we had the high-level understanding pretty close to correct. However, we failed to identify all the risks.</span>

<span style="font-weight: 400;">In a typical software project, you can hit one of these challenges and figure out multiple solutions to work around the problem, then implement and test on a short timeline to catch back up. In hardware, you're forced to either suffer through and solve challenges with the parts you have, or start from scratch and hope you don’t run into other challenges. Coordinating parts orders and queuing up for production across multiple companies makes it very difficult to make up time. Luckily we have been able to move forward, but not before taking two steps back </span><i><span style="font-weight: 400;">to get to the right solutions</span></i><span style="font-weight: 400;">. </span>
<h1>Now to the details:</h1>
<span style="font-weight: 400;">Our biggest issue to date has been the quality and reliability of the PCB Fabrication and Assembly. This is a pretty complex, eight layer board. Three separate fab houses have prototyped the board, and only one has proven their ability to do so with near-perfect quality. That company is only able to do small-run prototypes – not large-scale production. So, we have been working with them to document their process and materials for the full-scale production house. On top of the PCB Fab, we are being very conscious about the design for heat dissipation for not only our current needs but also the future. Mark II is intended to be a fully capable AI device. Exposing the power of the FPGA has enormous potential and is going to be great to enable the team and community’s creativity. But all the smarts going into it can create some serious heat.</span>
<h2>Mechanical</h2>
<span style="font-weight: 400;">A few items came up with the mechanical design. The first was heat dissipation. After thinking about how the system could be used at 100%, we knew we needed to build in some heat safeguards. For this reason, we have adjusted the mold design to allow for more cross-circulation and also for a larger heatsink. We are currently running under the heat specs of the chips, but we want to make sure we stay that way.</span>

<span style="font-weight: 400;">There was also an acoustic microphone issue that needed a fix. We realized that we needed to isolate the microphones as much as possible from the rest of the housing for the most optimal performance. For this, we slightly repositioned and condensed the form factor of the mic board and redesigned the chamber to seal each microphone individually. Lastly, we are running into a challenge with the assembly of the fabric. We are confident that the current design of the fabric will add form and function to the device.</span>

<span style="font-weight: 400;">All said, we're about 96% done with mechanical. There are a few pieces of Design for Manufacturing that we are still tweaking. We want to have one hundred units built before calling it complete. </span>
<h2>LCD</h2>
<span style="font-weight: 400;">Who would have known that there is no standardization in the LCD world? At the beginning of this project, Derick and I knew this was something we needed to test and clear early. The LCD drove a lot of board design decisions. We weighed options and we went with what we still feel is the best option, but we had a lot of hurdles to overcome building the driver for this screen. This was almost a two and a half month delay to get up and running.</span>
<h2>Graphics 16.04 to 18.04 (Ubuntu)</h2>
<span style="font-weight: 400;">Yet another unexpected hurdle was going from Ubuntu 16.04 to 18.04. We knew that we would make this leap eventually. But, as we began working with the KDE Neon team we realized it would take more effort to backport their latest tech to support 16.04 than to upgrade now to the latest technology. So we bit the bullet and decided to upgrade to 18.04. Upgrading Ubuntu to 18.04 sounds simple, but my understanding of the task was naive. Apparently, the toolchains needed to build audio and visual drivers were a lot more involved to upgrade and test than I imagined. We currently have some pieces working in an 18.04 environment, and some in 16.04, but are still getting everything aligned.</span>
<h2>Xilinx</h2>
<span style="font-weight: 400;">I know there has been a lot of talk about what we are using here. We basically designed the whole product around the </span><span style="font-weight: 400;">Zynq UltraScale+ EG </span><span style="font-weight: 400;">SoC. On this SoC, we have a quad-core Cortex-A53 CPU, a Mali-400 GPU, and the FPGA. It is quite a package. As we have mentioned previously, we think the best approach is using a KDE Plasma ecosystem for the graphics. For this, we needed to get OpenGL ES working with our Mali GPU and a display using a MIPI interface. Xilinx hadn’t encountered this combination of hardware before. While their support was really amazing (three teams participated from Colorado, California, and India) the problem took over a month to identify, and even longer to implement and test a solution. Ultimately we still believe these are the right choices, but this definitely introduced a big drag on the timeline. </span>
<h2>Audio</h2>
<span style="font-weight: 400;">This is the single most important improvement from Mark I to Mark II. Let's be honest with each other – the Mark I missed the “mark” on the audio aspect of the system. We now know microphone technologies like noise cancellation and beamforming are essential parts for a voice assistant to work well. </span><a href="https://aaware.com/"><span style="font-weight: 400;">Aaware</span></a><span style="font-weight: 400;"> was brought in as our partner for audio processing, but they're also the developer of the main boards and the integrator of the graphics drivers. Since the lower level pieces had to come together first, they are behind schedule on implementing and tuning the pieces they are really good at. They have provided a single direction solution for us to test out other aspects of the stack. With most of the low-level work done, Aaware is now working towards the full multi-mic array with all the bells and whistles for full-room listening.</span>
<h2>Regulatory Certifications</h2>
<span style="font-weight: 400;">We have the certifications planned out and have a testing house on standby. Of course, testing is only possible after the final pre-production run has happened. Production in this sense means that 100 units. We have to use the same plastics and production process as with the larger order. Although some parts of the subsystems have already been approved via the manufacturer's efforts, the real rock is getting the entire system evaluated and approved.</span>

<span style="font-weight: 400;">Bottom line, we need to get unit one operating completely and correctly at the hardware level first. Then units 2-10. Then 11-100. After that, we kick off the final production run needed to fulfill all of our backers.</span>
<h1>Video Update</h1>
<iframe src="https://www.youtube.com/embed/1o48-9YRe6c" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<h1><b>Questions we're getting:</b></h1>
<h3>So when will it ship?</h3>
<span style="font-weight: 400;">I know this is what everyone wants to know. I really want to be able to answer this for you with an exact date. Honestly, I wish I knew it too. What I have learned from this is that estimating time when there are too many things still to be addressed is not helpful. At this time all I can give you is that we are still aiming for Q1 2019 shipments. </span>
<h3>Are there any other major roadblocks on this project?</h3>
<span style="font-weight: 400;">I would hate to say no here and then have to eat my words. We are still working with all the pieces above, but there does feel like there is momentum building here to get over these unknowns quickly. </span>
<h3>What is the biggest lesson you have learned so far?</h3>
<span style="font-weight: 400;">Come up with a target date, add 20%, then add another 20%. Kidding aside, partners are very important. Pick them wisely and invest in the time to build the relationships. As a small and ambitious company, we rely on the Community and partners for a lot of things. Having ones that not only have the same work ethic, but also the vision of the end result is critical for success. </span>
<h3>Is Chinese New Year or other things going to slow this down?</h3>
<span style="font-weight: 400;">Yes and no. We've purchased and received t</span><span style="font-weight: 400;">he majority of the long lead time items. There is one last supplier that we are still working with. We need to get their pieces bug free to make the final purchase. Although they are not a Chinese company, it appears some of their material is. </span>
<h3>What about refunds?</h3>
At this time we are not offering refunds. We are extremely sorry about this, but as explained above, we have already procured the majority of the components needed for this under NCNR (Non-cancelable non-returnable goods). For this reason, we can not offer refunds at this time.