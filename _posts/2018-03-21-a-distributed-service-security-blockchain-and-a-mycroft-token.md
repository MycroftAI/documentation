---
ID: 36249
post_title: 'A Distributed Service: Security, Blockchain and a Mycroft Token'
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/a-distributed-service-security-blockchain-and-a-mycroft-token/
published: true
post_date: 2018-03-21 15:32:01
---
<h2>Should Mycroft build a blockchain-enabled backend?</h2>
<span style="font-weight: 400;">On March 14  I said hello to Mycroft and my Mark 1 didn’t respond. We were experiencing</span><a href="https://docs.google.com/document/d/1wsuK_L3gKk9zbLnYnGBEOJIC1NxbGlhfDUVJwZnDgJA"> <span style="font-weight: 400;">a brief outage</span></a><span style="font-weight: 400;"> and </span><span style="font-weight: 400;">http://api.mycroft.ai</span><span style="font-weight: 400;"> was offline. This brought to mind a comment by user @gorbachav on</span><a href="http://avc.com/2018/02/funding-friday-an-open-source-voice-assistant/"> <span style="font-weight: 400;">Fred Wilson’s blog post</span></a><span style="font-weight: 400;"> about Mycroft:</span>

<i><span style="font-weight: 400;">@Gorbachav: The device needs an account at the service creator. Once they go belly up, you'll have yet another useless IoT device filling your e-waste drawer.</span></i>

<span style="font-weight: 400;">Well…..we aren’t going “belly up”......but @Gorbachav has a valid point. Like Siri, Assistant and Alexa - Mycroft’s service hinge on centralized infrastructure. </span>
<h3><span style="font-weight: 400;">But what if it didn’t?</span></h3>
<h2></h2>
<h2>Decentralized Control</h2>
<span style="font-weight: 400;">What if we can build a backend for Mycroft that is distributed, secure, scalable, reliable and isn’t dependent on a centralized authority? Given the importance of what we are building, wouldn’t that be a great way to manage user accounts, API aggregation, and device settings? There would be no company to fail, no data center susceptible to power outages, no central authority for repressive regimes to pressure. Wouldn’t that be a great solution?</span>

<span style="font-weight: 400;">This made me think of a technology I’ve been playing with since 2013… blockchain.</span>
<h3>What the Heck is Blockchain?</h3>
<span style="font-weight: 400;">You may be familiar with Blockchain as the technology that underpins Bitcoin, Ethereum and other cryptocurrencies, but did you know that modern blockchain technologies are </span><a href="https://en.wikipedia.org/wiki/Turing_completeness"><span style="font-weight: 400;">Turing complete</span></a><span style="font-weight: 400;">? Using smart contracts, you can create applications that can do anything a stand-alone computer can do.</span>

<span style="font-weight: 400;">The blockchain is a great way to keep a secure, distributed, reliable and scalable ledger. It is a great place to store transactional information. It can be implemented as a keystore for encryption keys that unlock larger volumes of data.</span>

&nbsp;
<h2>That’s Cool but How Does Blockchain Improve Mycroft?</h2>
<span style="font-weight: 400;">There are a number of huge advantages to using the blockchain to distribute Mycroft’s backend.</span>
<h4>Privacy</h4>
<span style="font-weight: 400;">By using the blockchain to create a ledger and smart contracts to process data, we can encrypt voice samples, user queries, query results and other user data, then hand control over to the user. The data can be stored centrally or in a distributed system, but the keys for the data will reside with the users. They can control how their data is used and, through smart contracts, make it available on a limited basis for training of the AI.</span>

<span style="font-weight: 400;">The data belongs to the user. By using blockchain we empower the user to decide who gets access to it and on what terms.</span>
<h4>Reliability</h4>
<span style="font-weight: 400;">Decentralization would ensure that the Mycroft backend is always available. There would be no central authority to aggregate API keys, manage user accounts or store device settings. API aggregation would be done through smart contracts and both user accounts &amp; device settings would live in storage managed through the blockchain.</span>

<span style="font-weight: 400;">Processing nodes would be responsible for presenting services to users. They would also be responsible for managing storage. Users who provide processing power or storage would be rewarded with a digital token. Every active Mycroft Mark I and Mark II on the network would, with permission from their owner, become a processing node on the network and mine tokens.</span>
<h4>Economic Sustainability</h4>
<span style="font-weight: 400;">Where will this token be spent? Users will be required to spend a fraction of a token every time you ask Mycroft a question that accesses a paid API.</span>

<span style="font-weight: 400;">Technologies like Mycroft require a ton of APIs to work. Speech-to-text, knowledge queries, sports scores, weather information – all are necessary and they all cost money. Today our company is subsidizing these services, but that model isn’t sustainable without large corporate customers. Using blockchain technology along with a token system Mycroft can be configured to make micropayments for the various services it accesses.</span>

<span style="font-weight: 400;">Users of the service could be issued a small amount of token when they sign up. As they use the technology their wallet would gradually decrease. Each call to a paid API would gradually deplete their balance. To fill it back up users would provide storage, processing power or simply pay for an additional token.</span>

<span style="font-weight: 400;">Users could even pay with privacy like they do with existing technologies from Amazon and Google. They would be able to sell their data to aggregators who, I’m sure, would love to purchase the reams of data users generate.</span>

<span style="font-weight: 400;">The important point is that it is the user’s choice.  The system acts as the user agent. The user’ chooses what to do with their data.</span>
<h4>Governance</h4>
<span style="font-weight: 400;">Right now I am the final authority on all things Mycroft. I control a huge majority of the voting stock and have pushed hard to curtail the voting rights of other investors. I have all of the root passwords, I sign the checks and ultimately I am responsible for every single decision the company makes. Though it is nice to be in charge, it has always been my goal to turn Mycroft over the community.</span>

<span style="font-weight: 400;">By deploying a digital token we create a mechanism for giving the Mycroft community control of the technology. And through the blockchain, we can ensure that voting is both secure and fair. This will further empower our community and put them in control of the technology’s future without building a cumbersome bureaucracy.</span>
<h4>Environmental Impacts</h4>
<span style="font-weight: 400;">But won’t all of these devices mining tokens use a lot of electricity? No. We’d design it with economic controls like “proof of stake” that help prevent a processing power arms race. The goal would be to allocate exactly as much storage and processing power as is required at any given moment.</span>
<h4>Other Benefits</h4>
<span style="font-weight: 400;">A digital token would be a great tool for rewarding developers for helping with the core Mycroft stack. Developers who contribute to the platform could be rewarded with tokens that can then be converted to Ethereum, Bitcoin or fiat currency.</span>

<span style="font-weight: 400;">Creators of popular skills could also be rewarded with a fractional token when users use their skill. This provides developers who create popular skills with a reward every time a user accesses their skill. This is something that even large players like Google and Amazon have struggled with – how to allow developers to get paid for building great skills.</span>

<span style="font-weight: 400;">Blockchain solves the problem in a secure, decentralized way.</span>
<h4>Challenges</h4>
<span style="font-weight: 400;">There are certainly challenges. Deploying blockchain successfully requires a community of miners to hash transactions and process blocks. It is also difficult to scale transaction volume. The Bitcoin network, for example,</span><a href="https://en.wikipedia.org/wiki/Bitcoin_scalability_problem"> <span style="font-weight: 400;">can only process 3 to 7 transactions per second</span></a><span style="font-weight: 400;"> – this is a small fraction of the transaction volume Mycroft will process as the agent is more widely deployed.</span>

<span style="font-weight: 400;">Building secure software is also extremely difficult. Ask any German U-Boat captain who trusted an Enigma. Crypto is hard. We’ve got a great team, but implementing a distributed service with lots of storage and a large user base is going to be difficult. Doing it securely, more so.</span>

<span style="font-weight: 400;">We are also going to have to fight both scope creep and feature creep. Developing the Mycroft voice agent has already taken superhuman efforts from our developer team. Implementing a distributed service based on Blockchain in addition to building a great voice user experience will be a significant challenge.</span>
<h4>Build It?</h4>
<span style="font-weight: 400;">Should we build it? Honestly, I don’t know. We are at a stage in human history where we can build anything that physics allows. We have electric cars that outperform gasoline cars. We have re-usable space launch systems. We have quantum computers and miracle drugs. We can build anything. The real question is, does anyone want us to?</span>

<span style="font-weight: 400;">Over the next several months, we are going to set out to answer that question: Does anyone want this built and, if so, are they willing to put up the resources. Does anyone want a Mycroft token? Will users get enough benefit out of Mycroft to pay for the API calls they use? Are we just glomming on to a hot technology or do we have a real and compelling use case?</span>

<span style="font-weight: 400;">Our team is working on ways to answer these questions. If you have an opinion and want to weigh in, join our discussion here.</span>

&nbsp;

&nbsp;

&nbsp;