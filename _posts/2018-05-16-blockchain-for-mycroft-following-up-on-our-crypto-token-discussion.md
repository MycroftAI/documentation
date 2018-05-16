---
ID: 37884
post_title: 'Blockchain for Mycroft: Following Up on our Crypto Token Discussion'
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/blockchain-for-mycroft-following-up-on-our-crypto-token-discussion/
published: true
post_date: 2018-05-16 15:35:23
---
<span style="font-weight: 400;">A few weeks ago I wrote a <a href="https://mycroft.ai/blog/a-distributed-service-security-blockchain-and-a-mycroft-token/" target="_blank" rel="noopener">blog post</a> where I explored the idea of building a decentralized back-end for Mycroft using blockchain technology. Since then we’ve had a <a href="https://community.mycroft.ai/t/a-distributed-service-security-blockchain-and-a-mycroft-token/3338" target="_blank" rel="noopener">number of conversations</a> with Mycroft supporters from around the interweb, so I thought I’d take this opportunity to circle back.</span>
<h1>Is Blockchain Necessary?</h1>
<span style="font-weight: 400;">One of the biggest themes was determining the necessity of adding blockchain. After all, we could simply build a distributed system using peer-to-peer technology, or better yet, focus on the core technology to build something that is valuable without blockchain. </span>

<span style="font-weight: 400;">In aerospace engineering we often say, “you don’t bolt a bathtub to an airplane just because you have a bathtub handy.” You should only adopt technology that solves a current problem and, in the best case, helps solve several others while making room for future advancements. As we looked at our current challenges, we saw:</span>
<ol>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Openness and Privacy are both desired, but seem at odds with each other. But blockchains advance both extremely well.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Centralization creates a single point of failure. Blockchains are built on distribution, yielding stronger overall systems.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Current software development models are distributed, but the financial models are still built around centralization of banks, credit card processors, and single large organizations that bring in revenue from users and distribute as they see fit. Blockchain currencies have created new economic transaction methods that support highly dynamic networks and, importantly, can compensate developers for their contributions to the platform.</span></li>
</ol>
<span style="font-weight: 400;">As we examined blockchain and debated the tough questions, it felt like the technology <em>could be</em></span><span style="font-weight: 400;"> a very good fit for Mycroft and our ideals.</span>
<h1>Is Blockchain Right?</h1>
<span style="font-weight: 400;">Another question we got was whether a blockchain solution for Mycroft will scale. For readers unfamiliar with the challenges of blockchain technology, scalability has been a huge problem. Large chains like Bitcoin are currently incapable of processing transactions at a rate that would be useful in day to day commerce. So in the meantime, we are following scaling development in progress by leaders like Ethereum and (soon) Telegram's TON. Current research outputs from the open source communities working in the blockchain ecosystem indicate this will be resolved in 12–24 months' time, and we would relish an opportunity to participate in scaling research and development alongside the community.</span>

<span style="font-weight: 400;">Oh, and that is another thing, does it make sense for Mycroft to develop its own chain? Yes. Unequivocally yes. We’ve carefully evaluated solutions from existing blockchain communities and none have the features we are looking for. We need to protect user privacy, store large volumes of data, and securely distribute API services. Unfortunately nothing out there meets our needs today, though off-chain solutions like <a href="https://github.com/lightningnetwork/lnd" target="_blank" rel="noopener">Lightning Labs’ LND</a> comes close. If something did exist and came with the resources to implement it we’d certainly make use of it. As it stands now we’d have the responsibility, and opportunity, to tailor our chain to the exact needs of our community.</span>

<span style="font-weight: 400;"> We also need to be sure that, if we deploy a chain, it incorporates privacy by design. Existing chains focus on transparency and non-repudiation much more than they focus on privacy, so to achieve our goals without forking an existing project, we’d need to develop our own chain. Believe me, we won’t undertake that effort lightly.</span>

<span style="font-weight: 400;">Finally, we got a lot of questions about what a Mycroft crypto mining community might look like. Will it be large enough? Yes. A Mycroft token would be designed so that the Mark I, Mark II, or Mark III (you didn’t know about that one, did you) will be able to mine the coin. That means we will instantly have thousands of devices participating in the network if, of course, our users opt-in.</span>

<span style="font-weight: 400;">We are also discussing methods of avoiding bad behavior on the part of crypto miners and currency manipulators. If we decided to go this route (and no decision has been made as of today), we’d want to incentivize:</span>
<ol>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Provision of secure storage.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Development and maintenance of useful Skills.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Data sharing for the purposes of improving the machine learning models.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Presentation of useful APIs to Mycroft users.</span></li>
 	<li style="font-weight: 400;"><span style="font-weight: 400;">Privacy related services.</span></li>
</ol>
<span style="font-weight: 400;">There are several consensus models that have the potential to incentivize these behaviors and any blockchain network our team developed will be carefully designed to mitigate perverse incentives like proof of work.</span>
<h1>Thank You to Our Community</h1>
<span style="font-weight: 400;">All in all our team found the conversation around blockchain and Mycroft to be very helpful. I want to thank everyone in our community who participated in the conversation. We really appreciate the time you took to weigh in and will continue to engage as we think through this concept.</span>