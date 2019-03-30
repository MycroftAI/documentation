---
ID: 44432
post_title: 'Mark II Architecture Change &#8211; A Note from the CEO'
author: Kathy Reid
post_excerpt: ""
layout: post
permalink: >
  https://test.mycroft.ai/blog/mark-ii-architecture-change-a-note-from-the-ceo/
published: true
post_date: 2019-03-20 18:30:03
---
<h1>Architecture Change on Mycroft Mark II</h1>
Mycroft Community and Backers,

We set out in January 2018 to provide a smart speaker for the Mycroft ecosystem with a graphic display and substantial improvements to the audio. After taking our lumps during the Mark I manufacturing process, we decided the Mark II would go more smoothly if we brought in a vendor to handle the electrical engineering, audio processing, and firmware.

We decided to outsource this process because it would allow us to focus on software while a partner with more specific experience developed the Mark II hardware. Unfortunately our vendor hasn’t delivered. This doesn’t absolve us of responsibility because ultimately the product is our responsibility from start to finish, but it hopefully helps clarify what’s been going on behind the scenes here at Mycroft.

The <a href="https://mycroft.ai/blog/mark-ii-update-delivery-timeline-and-progress/#so-when-will-it-ship" target="_blank" rel="noopener noreferrer">last published delivery date</a> for the Mark II was the end of Q1, but it looks like we’re going to slip significantly to the right. As we said in the <a href="https://mycroft.ai/blog/mark-ii-update-january-2019-current-progress/" target="_blank" rel="noopener noreferrer">January 2019 update</a>, we won’t speculate on timelines anymore but will let you know as soon as we have clarity. We sincerely apologize for the delay.

When we selected the vendor for the Mark II, we felt confident that they would be able to deliver a great product. Our engineering and audio provider promised a “turn-key” solution that would give Mark II a lot of cutting-edge capabilities.

Unfortunately, the promised performance never materialized. Though the hardware itself seems to be capable, we have not been provided firmware, drivers, and software that work reliably. That means the screen crashes, the board overheats, and we’ve yet to see the claimed audio processing technologies working on the prototype hardware.

After fighting these problems for months at a cost of nearly $5,000 per day we’ve decided to cut our losses and move development to a proven off-the-shelf solution. The development platform we’ve adopted is running a <a href="http://rock-chips.com/a/en/products/RK32_Series/2016/1109/799.html" target="_blank" rel="noopener noreferrer">Rockchip 3229</a>. We’re deploying a four-step process to evaluate this platform as the basis for the production Mark II. We’re already in Phase 2 of validation.

Moving to a platform that has been the basis for other voice solutions in the past should accelerate our development effort. We’re now making rapid progress on the software and are optimistic given the progress of the new prototypes. We still need to produce and refine the plastics, pick a screen for the new systems, and refactor our setup software. However, since the developer boards are readily available, we are not waiting on a fabricator to print, populate, cook, test, and ship the prototype PCBs at a cost of thousands of dollars each.

One benefit of this approach is that outside developers will be able to participate in the effort without waiting for production hardware. Once we can confidently say we’ll be able to deliver using this solution, developers will be able to compile a prototype with off-the-shelf components and our supplied hardware schematics and software.

We already have a prototype of the new solution operational and will soon have the first run at the plastics printed. Chief of Design Derick Schweppe has an update with details that will be published this coming Friday. (Derick's post is now live. <a href="https://mycroft.ai/blog/mark-ii-update-revised-architecture/" target="_blank" rel="noopener noreferrer">Read it here.</a>) We’ll keep you posted on further progress as we make this change.

As always, we appreciate everyone’s support as we work through these challenges. Hardware is hard and we’re glad to have so many cheerleaders supporting our efforts.

Sincerely,

Joshua Montgomery
CEO
Mycroft AI, Inc.