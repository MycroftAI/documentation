---
ID: 40391
post_title: 'Digital AI Summit Melbourne &#8211; Session Notes'
author: Kathy Reid
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/digital-ai-summit-melbourne-2018/
published: true
post_date: 2018-09-05 12:34:06
---
<span style="font-weight: 400;">Mycroft is a global company. One of the key advantages of having a distributed world-wide workforce is our ability to engage with entrepreneurial and technology ecosystems in cities across the world. As our Australian contingent, I recently attended the </span><a href="https://www.digitalaisummit.com/" target="_blank" rel="noopener"><span style="font-weight: 400;">Digital AI Summit in Melbourne</span></a><span style="font-weight: 400;">. In our spirit of openness and sharing, I have provided my notes for our entire community to benefit from.</span>

<span style="font-weight: 400;">Tweets from the day are available at the hashtag </span><a href="https://twitter.com/search?vertical=default&amp;q=digitalaisummit&amp;src=typd" target="_blank" rel="noopener"><span style="font-weight: 400;">#digitalaisummit</span></a>
<h3>Session 1 - <a href="https://www.linkedin.com/in/blairtbryant/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Blair Bryant, Global Digital Advisor, Microsoft</u></span></a></h3>
Blair outlined how important it was to get the CEO on board with digital transformation programs. He underscored how digital transformation needs to solve specific problems for the C-suite - don’t sell digital transformation itself, sell the problems that it solves. He outlined a four-point plan;
<ol>
 	<li>Inspire the CEO - the CEO needs to be inspired to adopt digital transformation</li>
 	<li>Align the senior leadership team</li>
 	<li>Build a digital transformation strategy</li>
 	<li>Understand how the execution will proceed</li>
</ol>
Business should immediately start to gather their data; understanding what data they collect - as data is the “fuel” for machine learning. Then, business should start to understand how hyper-personalization will influence their offerings, services, and products.

<i>Key takeaway: Get your house in order, build a plan and execute it. </i>

[caption id="attachment_40396" align="alignnone" width="960"]<a href="https://mycroft.ai/wp-content/uploads/2018/09/blair-bryant-digital-ai-summit.png"><img class="wp-image-40396" src="https://mycroft.ai/wp-content/uploads/2018/09/blair-bryant-digital-ai-summit.png" alt="Blair Bryant" width="960" height="540" /></a> Blair Bryant[/caption]
<h3>Session 2 - Professor<a href="https://www.linkedin.com/in/phil-cohen-3b5455" target="_blank" rel="noopener"><span style="color: #1155cc;"><u> Phil Cohen</u></span></a>, Monash University Laboratory for Dialogue Research - Conversational Technology, Present, and Future</h3>
<span style="font-weight: 400;">Prof Cohen has </span><a href="https://www.monash.edu/it/about-us/news-and-events/latest/articles/2018/ai-pioneer-joins-monash-university" target="_blank" rel="noopener"><span style="font-weight: 400;">recently joined Monash University</span></a><span style="font-weight: 400;"> to head up the Laboratory for Dialogue Research. He previously headed up a startup called </span><a href="https://www.crunchbase.com/organization/voicebox-technologies" target="_blank" rel="noopener"><span style="font-weight: 400;">VoiceBox, which was recently acquired by Nuance</span></a><span style="font-weight: 400;">.</span>

<strong>This was the standout presentation of the day.</strong>

Prof Cohen provided an overview of the evolution of voice technologies. Although much recent progress has been made, largely in part due to advances in machine learning and computational speed, dialogue and interaction are still stunted by several challenges, including;
<ul>
 	<li><b>Paraphrasing</b> - there are many ways of saying the same thing</li>
 	<li><b>Ambiguity</b> - one phrase can have multiple meanings depending on context</li>
 	<li><b>Meaning and semantics</b> - meaning can be different to spoken words - “Do you have the time” means “tell me the time” but this is not the way it is worded</li>
 	<li><b>Pragmatics</b> - this is the word Cohen used to describe “context” - the history of a dialogue and the meaning that is imbued in that history.</li>
</ul>
<h3>Chatbots</h3>
Cohen outlined the basic premise behind Chatbots - they’re essentially “stimulus-response” engines. Where an Intent is matched to a stimulus and a response is provided. However, they only provide the <i>illusion</i> of having a dialogue - they currently don’t handle context well, nor do they handle follow up questions or interactions that fall outside the ‘dialogue tree’.

He provided an excellent walkthrough of failures of Chatbots - how they don’t handle diplomatic nuances well - ie “What’s your grandmother’s name” =&gt; “My grandmother is dead” - nor do they handle follow up questions well because their ability to determine context is severely limited.
<h3>Spoken natural language retrieval</h3>
Natural language (NL) retrieval allows a system to respond to a query using an FAQ type system, or route a query to the right department using keyword matching. Again, the ability to hold a dialogue is very limited.
<h3>Voice assistants</h3>
Voice assistants are able to handle broad topics, but there are limited ways to phrase a query - it’s not really “natural language”.
<h3>Semantic parsing</h3>
Semantic parsing is a technology currently in research labs that allows users to have better “expressivity” and better “understanding” of natural language. Semantic parsing has more capability than the current generation of voice assistants, and can handle things like superlatives - ie “find the best pizza in downtown closest to the space needle, but not McDonald's”.

<a href="https://en.wikipedia.org/wiki/Semantic_parsing" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>https://en.wikipedia.org/wiki/Semantic_parsing</u></span></a>

<i>Side note: I had a quick look at open source Semantic Parsing libraries and this one called SLING from Google looked like the most commonly used one - if anyone has thoughts, feel free to post in the <a href="https://community.mycroft.ai" target="_blank" rel="noopener">Forum</a>!
</i><a href="https://github.com/google/sling" target="_blank" rel="noopener"><span style="color: #1155cc;"><i><u>https://github.com/google/sling</u></i></span></a><i> </i>

Prof Cohen gave a live demo of Voicebox using web-based speech to text, which was then converted in real time to Intents, and it came back with a pretty slick answer.

<a href="https://www.voicebox.com/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>https://www.voicebox.com/</u></span></a> - the live demo website isn’t available.
<h3>Comparison voice assistants</h3>
He then presented a chart (not available online) of what Voicebox can do compared to Siri, Google Home, and Alexa, positioning Voicebox in a positive light.
<h3>Transactional dialogue</h3>
The next big frontier for voice assistants, as we’re starting to see with projects like Duplex from Google is transactional dialogue - being able to have a natural sounding conversation with a voice assistant that allows the user to complete a task - booking tickets for a movie, ordering a pizza and so on. Most transactional dialogues are ‘slot-filling’ systems where the aim of the dialogue is to ensure the slots are filled so that an API can be used to complete the transaction. That is, the voice assistant will prompt for the missing ‘slot values’. There are not many systems like this on the market today.
<h3>Semantic parsing and collaboration</h3>
The next horizon in speech recognition research is semantic parsing coupled with collaboration. Under this model, the voice assistant will be able to:
<ol>
 	<li>Analyse meaning</li>
 	<li>Infer the intent of the user from the utterance - that is what is the user really trying to do?</li>
 	<li>Debug the plan - be able to explain how it arrived at a conclusion about meaning</li>
 	<li>Offer the user solutions to the Intent that has been inferred</li>
</ol>
The Laboratory for Dialogue Research intends to collaborate with industry via a membership model.

<i>Key takeaways: Investigate semantic parsing libraries as part of emerging tech roadmap</i>

[caption id="attachment_40395" align="alignnone" width="960"]<a href="https://mycroft.ai/wp-content/uploads/2018/09/phil-cohen-digital-ai-summit.png"><img class="wp-image-40395" src="https://mycroft.ai/wp-content/uploads/2018/09/phil-cohen-digital-ai-summit.png" alt="Professor Phil Cohen" width="960" height="480" /></a> Professor Phil Cohen[/caption]
<h3>Session 3 - Whole of government and whole of community approach to AI - Cheryl George, Kathy Coultas, and Martine Letts</h3>
<ul>
 	<li><a href="https://www.linkedin.com/in/kathycoultas/?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_top%3Bxkn8BmVoR7mP6oibTTepFQ%3D%3D&amp;licu=urn%3Ali%3Acontrol%3Ad_flagship3_search_srp_top-search_srp_result&amp;lici=vIkgJb8cQoCuhHeCbJ9byg%3D%3D" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Kathy Coultas</u></span></a> - Director, Technology Innovation and Investment, Department of Economic Development, Victoria</li>
 	<li><a href="https://www.linkedin.com/in/cheryl-george-a7206320/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Cheryl George</u></span></a> - Government and Stakeholder Relations, Data61 CSIRO</li>
 	<li><a href="https://www.linkedin.com/in/clivedwyer/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Clive Dwyer</u></span></a> and <a href="https://www.linkedin.com/in/martine-letts-8791a76/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Martine Letts</u></span></a> - Committee for Melbourne</li>
</ul>
The AI space is evolving rapidly, and there are opportunities that Australia is well positioned to take advantage of - especially using our domain knowledge. To really take advantage of the opportunities requires a broad cross-sector collaborative approach. Coordination will be critical. The government needs an “enabling environment” and “enabling infrastructure” to harness the opportunities, and this needs to be done quickly.

Kathy Coultas recognized the need for ALL citizens to engage with digital, and explained that this was part of the reason behind the <a href="https://dif.vic.gov.au/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Digital Innovation Festival</u></span></a>.

Martine Letts noted that the <a href="https://www.parliament.vic.gov.au/about/news/4029-artificial-intelligence-group-launched" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>cross-partisan Parliamentary AI group</u></span></a> had been established at a state level to help politicians really grapple with the opportunities and challenges of AI. She would like to see this initiative expanded into a national working party. The only other country in the world that has a similar cross-partisan working party is the United Kingdom.

Kathy Coultas noted the issues surrounding data privacy, security, and ethics and how we need to tackle these as part of coming to terms with artificial intelligence. Part of this will be the necessity for legislative amendments to harness emerging technology effectively while protecting citizens from foreseeable harm. She was firm that political point-scoring won’t be effective; regulatory reform for emerging technologies requires a multi-partisan approach.

Martine Letts noted that Australia is well behind investment in the AI space; China and the USA are really leading both investment and technology development in this space. AI is seen not as an integral part of emerging technology strategy - and a pillar of strategy - but as a “bolt on” to existing measures. This view is anachronistic and will not service organizations well. Kathy Coultas followed up by outlining that most technology investment now is poured into ABC - AI, blockchain and crypto. Australia is significantly behind in terms of technology investment, and that needs to seriously change in order to realize the vision of Melbourne becoming the technology capital of Australia. We have the capability, but it’s fragmented across multiple sectors.

Kathy Coultas also noted the investment needed in workforce capability and training to be able to have the skills needed to harness AI - right now there is a significant skills shortable in this space, and universities are only now moving to catch up and address this shortfall.

Cheryl George highlighted that CSIRO/Data 61 <a href="https://blog.csiro.au/artificial-intelligence-and-australias-industries-of-the-future/" target="_blank" rel="noopener">had been tasked with developing a national AI technologies roadmap to lay out the opportunities, threats and possible approaches.</a> A draft of this is due by the end of the year 2018.

<i>Key takeaways: Whole of government approaches to AI require significant coordination, whole of sector and whole of pipeline approaches.</i>

[caption id="attachment_40394" align="alignnone" width="960"]<a href="https://mycroft.ai/wp-content/uploads/2018/09/cheryl-george-kathy-coultas-martine-letts-digital-ai-summit.png"><img class="wp-image-40394" src="https://mycroft.ai/wp-content/uploads/2018/09/cheryl-george-kathy-coultas-martine-letts-digital-ai-summit.png" alt="Dr Cheryl George, Kathy Coultas and Martine Letts" width="960" height="480" /></a> Dr Cheryl George, Kathy Coultas and Martine Letts[/caption]
<h3>Session 4 - Dr Nathan Faggian, Google - Machine Learning Infrastructure</h3>
Nathan attempted to provide an overview of machine learning in 30 minutes - much respect to him.

<strong>This was the second-best presentation of the day.</strong>

He opened by explaining that what used to be fantasy is now reality. There have been massive improvements in artificial intelligence and machine learning. Google uses a huge amount of machine learning and AI - and he quoted the statistic that over 20% of Gmail responses are now the “automated” pre-canned responses that are available.

He provided a demonstration of Google Duplex, and explained how it was using semantic parsing based on massive machine learning efforts to be able to have natural interaction style. In terms of Professor Cohen’s earlier presentation, Duplex is certainly at the “cutting edge” of where speech recognition technology is at the moment.

He went on to show how machine learning can be valuable in industrial contexts - citing both the case of where illegal fishing was identified in Vanuatu due to fishing boat movements, and the case of soy crop forecasting - which was accurate to within 2% with a 5 month lead time - an incredible level of accuracy.

He underscored the importance of data and the huge volumes of data that are required for effective machine learning.

He also outlined that machine learning does not exist in isolation in an organization, and that there is a large supporting infrastructure that sits around it. This was essentially a shadow-pitch for the Google Cloud Platform, but did make the important point that there are many parts to an effective machine learning capability within an organization. They all have to be considered as a whole in order to be able to effectively scale an organization’s machine learning efforts.

<i>Side note: None of the existing governance frameworks like COBIT, ITIL or SFIA have recognized machine learning as a key organizational capability yet. </i>

<i>Key takeaways: Google uses a lot of AI, they’re the leaders in the field. Make sure you have the infrastructure to scale your ML efforts. It’s not just about ML and algorithms, the infrastructure is a key component of your machine learning capability. ML can solve some pretty hoary problems for business and industry. If you’re not considering it yet you should be.</i>

[caption id="attachment_40393" align="alignnone" width="960"]<a href="https://mycroft.ai/wp-content/uploads/2018/09/nathan-faggian-digital-ai-summit.png"><img class="wp-image-40393" src="https://mycroft.ai/wp-content/uploads/2018/09/nathan-faggian-digital-ai-summit.png" alt="Dr Nathan Faggian" width="960" height="604" /></a> Dr Nathan Faggian[/caption]
<h3>Session 5 - Health Technology Panel</h3>
<ul>
 	<li><a href="https://www.linkedin.com/in/annette-hicks-0593687/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Annette Hicks</u></span></a>, IBM</li>
 	<li><a href="https://www.linkedin.com/in/alicesidhu/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Alice Sidhu</u></span></a></li>
 	<li><a href="https://www.linkedin.com/in/priscilla-rogers/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Dr Priscilla Rogers</u></span></a></li>
 	<li><a href="https://www.linkedin.com/in/mikepcw/" target="_blank" rel="noopener"><span style="color: #1155cc;"><u>Mike Wang, NVIDIA</u></span></a></li>
</ul>
This was a really interesting panel that looked at the application of machine learning to the health sector. The key points were;
<ul>
 	<li>Getting access to patient records in a way that is consistent is very difficult because data formats differ between providers; data standards matter.</li>
 	<li>Machine learning has a large role to play in effective pharmacology dosing. For instance, the industrial strength antibiotic vancomycin is nephrotoxic, so being able to get the right dose by personalizing it for the patient based on their unique characteristics means less kidney damage.</li>
 	<li>IBM have faced the challenge of trying to convince clinicians that tools like Watson are there as complementary tools. They’re not trying to replace the clinician - the goal is to work in a complementary way.</li>
</ul>
<i>Key takeaways: Data, data, data. Getting the right data in a machine-readable format is absolutely essential for machine learning.</i>

[caption id="attachment_40392" align="alignnone" width="960"]<a href="https://mycroft.ai/wp-content/uploads/2018/09/annette-hicks-priscilla-rogers-digital-ai-summit.png"><img class="wp-image-40392" src="https://mycroft.ai/wp-content/uploads/2018/09/annette-hicks-priscilla-rogers-digital-ai-summit.png" alt="Annette Hicks and Dr Priscilla Rogers" width="960" height="664" /></a> Annette Hicks and Dr Priscilla Rogers[/caption]