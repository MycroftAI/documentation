---
ID: 2107
post_title: >
  The Good, The Bad and the Ugly (shipping
  update)
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/the-good-the-bad-and-the-ugly-shipping-update/
published: true
post_date: 2016-12-21 20:13:17
---
This brief update is a follow-up about the first article boards we've received. You can click the video to listen while reading this post, then blame me the rest of the day when you find yourself whistling the hook.

https://www.youtube.com/watch?v=pLgJ7pk0X-s&feature=youtu.be&t=2m23s
<h2>The Good</h2>
We finally received the first articles from the board house in the first week of December. We opened the box to find ten main boards and ten front panels. All of the issues I've mentioned before with incorrectly oriented connectors had been corrected and they looked pretty good. So we began to assemble the boards using first article injection molded plastic enclosures we had received back in October.

While assembling we noted a few things (see below). But we got everything connected, plugged it in, and ... voila ... Mycroft was listening and answering us!  That was a huge relief.
<h2>The Bad</h2>
However, there were a few minor but significant issues we identified as we worked through the entire batch.
<ul>
<ol>
 	<li>One board was completely missing a component. Upon close examination we could tell the component was there at some point, but somehow broke off. The first article boards were packed in simple anti-static plastic and then placed in a box, so we suspect it was broke off during shipping. The actual production run will be packaged completely differently with individual boards protected by foam, so we believe that problem has been dealt with. Check.<br/>&nbsp;</li>
 	<li>The Neopixel "eyes" were mounted incorrectly. Each eye on the front plate is actually a small round sub-board, and we designed them to be mounted using simple standoffs. This provides an air-gap which prevents shorts at the sub-board test points. On two of the ten boards there are dead or discolored pixels in the eye which appear to be from these types of shorts. Plus that extra eighth of an inch positions the lights just right to get the diffused effect we intend through the plastic front plate. The four standoffs were not listed on the Bill of Materials (which was our mistake), so the board-house improvised and soldered the sub-board directly to the faceplate. This mistake was easy to document and won't be repeated in the production run. Check.<br/>&nbsp;</li>
 	<li>The rotary encoder was just plain wrong. They had swapped to an "equivalent" component, and it was a bad choice. The feeling of the rotation and the button click was nowhere near as smooth and definite as the part we had specified, resulting in missed clicks and inadvertent selection of the wrong item while pressing the button. And the worst part — the rotation encoding was reversed. Fortunately, this was again easy to identify and they will use the specific part originally specified. Check.<br/>&nbsp;</li>
 	<li>One of the matrix "mouth" displays has a dead column of pixels. At the time of initial manufacture we hadn't provided them with a test-jig that allows them to power-up and exercise the units. This failure was at the component level, so that testing would have quickly have caught the issue as all components in the production run will be fully tested. Check.<br/>&nbsp;</li>
 	<li>A few of the hand-soldered components didn't have a really clean cone of solder. It wasn't quite a "cold solder joint", but odd enough to note. We were told these boards did not go through the QA process they normally follow, as they consider this a functional validation more than a production run. We'll keep an eye on this promise, but for now I'll consider it checked.</li>
</ol>
</ul>
To be fair to the board house, this really isn't that unusual.  This is exactly why the concept of "first article" exists so we can spend a shorter time clean up problems on a very small batch, setting things up for a smooth big batch.

Subsequent to this we have performed sound tests, heat tests, and general usage of the boards. Aside from the dead eye and mouth pixels, all devices have held up and are functioning perfectly for us. Which also goes in the "Good" category.
<h2>The Ugly</h2>
One of the things that originally attracted me to the software industry was the clean nature of it.  In programming bits are beautifully discrete.  1 or 0.  True or false.  Yes or no.  Software does exactly what you tell it to and once it is working you can digitally "ship" and reproduce it nearly instantaneously.  But building <em>hardware</em> to run that software is a completely different thing.  We are now pushing through these ugly real-world bits.

We've been negotiating with the board house to ensure they have incentive to produce boards correctly and as quickly as promised.  This is tricky for a small business (one that doesn't have $500,000 sitting in its bank account) which is placing relatively small orders (less than 10,000 units).  We have finally come to terms which aren't perfect but are acceptable for both of us and created the production PO.

However, we are are now facing the scariest holiday in the electronics manufacturing world.  No, not Christmas.  It's Chinese New Years.  At the end of January thru early February, production and shipping in China literally shuts down.  Even if you are building everything in the US (as we are with out board house and enclosures) you are still impacted.  Many of the basic electronics components like a 40-pin header are manufactured in China and only in China.  These two weeks cause ripples for <a href="http://www.ewmfg.com/chinese-new-year/">several months before and after the holiday</a>.  The board house tells us one of the component has jumped to a 40-day lead time.  This means it would be 40 days before they even begin manufacturing the boards.  We are beating the bushes attempting to shrink this lead, but we don't have a better answer yet.

So we are looking at the real possibility that board manufacturing will be 40 days plus 4 weeks.  This isn't the message I was hoping to share, but I also don't want to leave everyone wondering what is going on.  Trust me, nobody wants to start shipping more than we do!