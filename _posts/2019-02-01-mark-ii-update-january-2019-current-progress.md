---
ID: 43920
post_title: 'Mark II Update: January 2019 Current Progress'
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/mark-ii-update-january-2019-current-progress/
published: true
post_date: 2019-02-01 13:00:05
---
We’re late.  Our team was pushing pretty hard to get the Mark II out in December and, clearly, that didn’t happen.

The good news is that the hardware is largely complete.  We’ve made several test runs of the printed circuit board as well as the enclosure, mic board, enclosure, and even the retail box.  We still have a bit of work to do on the plastics to get full performance from the mics, but that work is down to a few minor tweaks.

The challenges we’ve faced in getting the device shipped fall into two categories:
<ul>
 	<li>Component availability</li>
 	<li>Firmware, drivers and low-level software</li>
</ul>
To be fair we also have work to do on Mycroft Core which is due to release to production on February 28, but that release has been scheduled for two years, so it isn’t the limiting factor.

We’d like to have a delivery timeline report in every update. But, until we have a crystal clear idea of that timeline, we will not be speculating anymore. We know that this is one of the biggest reasons you are reading this, but in the end, the number one goal is quality. We know our core Community is in this with us, and we hope all our backers will agree.

Since our last update there have been five main teams working on different aspects of the Mark II:
<ul>
 	<li>Mycroft Developers</li>
 	<li>Mycroft Design</li>
 	<li>Aaware</li>
 	<li>Xilinx</li>
 	<li>KDE</li>
</ul>
Each of these has different and overlapping jobs that are all coming together to make this product. Currently, the Aaware team is the center point for all the hardware, and KDE is helping bring up the graphics side. Mycroft Design is working on the mechanical and UX side, and Mycroft Developers are working to bring all the new pieces together to make the Mark II actually run the stack.
<h3><strong>Screen: Aaware/Xilinx/Mycroft</strong></h3>
Getting pixels to show up on a screen has surprisingly been the most difficult part of the Mark II. Although screens and graphics are a well-understood realm of computer software (unlike rapidly evolving voice technologies), the industry’s techniques used to shrink physical devices and costs have resulted in far less standardization than we expected.

We have overcome challenges around the screen backlight power management and a thorny LCD driver issue. Remaining is a low-level issue that appears to be a conflict between the screen driver and disk IO, likely IRQ timing bugs. This results in screen flicker and corruption and is still being chased by the hardware suppliers.
<h3><strong>Graphics: KDE/Mycroft</strong></h3>
<a href="https://mycroft.ai/wp-content/uploads/2019/01/MarkII-GUI.jpg"><img class="alignnone wp-image-43929" src="https://mycroft.ai/wp-content/uploads/2019/01/MarkII-GUI.jpg" alt="Mark II update - showing off graphics progress" width="1000" height="706" /></a>

On the software side, the stack we are building with the KDE Plasma team has been very successful. A future blog post will go deeper into the architecture and APIs, but suffice it to say that the maturity of the KDE and Qt graphics technologies has jived very well with the flexibility of the Mycroft architecture and skill framework.
<h3><strong>Mic Tuning: Aaware/Mycroft</strong></h3>
We are hearing some reverberations in our Microphone recordings on the Mark II. Although the performance is still good we need to eliminate some mechanical issues to really optimize the design. The openings for the mems microphones need to be mechanically optimized to get their best performance, we are going through another round of prototypes to improve the mechanical design of our microphone assembly.

[gallery columns="2" size="medium" ids="43930,43931"]
<h3><strong>Center Mic: Aaware/Mycroft</strong></h3>
In our audio tests, the center Microphone is occluded. This is a relatively simple fix on paper, we just need to open up the grill for the center microphone. However, in reality, there might need to be some special considerations for the center microphone since the distance from the opening is further than the others.
<h3><strong>Heat Issues: Aaware/Mycroft</strong></h3>
The fabric cover on the Mark II has allowed us to perforate the entire front of the device with large ventilation holes. However, it is getting a little warmer than our original specifications. Mark II isn’t overheating and shutting down, but we would like to increase the cooling performance before we are satisfied. We are trying CPU management to overcome the issue, but if that isn’t enough we may try different fabric weaves and different heatsink designs.