---
ID: 46163
post_title: 'Mycroft&#8217;s Goals for 19.08'
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/mycrofts-goals-for-19-08/
published: true
post_date: 2019-04-04 13:50:03
---
<span style="font-weight: 400;">We’re now a month removed from the 19.02 Mycroft release. It is so far looking like a great success, so it is time to look out to the next release and talk goals for the Mycroft software at 19.08.</span>

<span style="font-weight: 400;">These goals are generally putting deliverables to points from our existing <a href="https://mycroft.ai/blog/many-roads-one-destination/" target="_blank" rel="noopener noreferrer">Roadmap(s)</a><span style="font-weight: 400;">. They will provide measurable outcomes to guide the development team for the next six months. They include some looks at exciting additions to Mycroft we’re making in the coming months, like deployment of the <a href="https://mycroft.ai/blog/building-strong-ai-strategy/#single-interaction" target="_blank" rel="noopener noreferrer">Persona engine</a></span><span style="font-weight: 400;"> and more focus on <a href="https://mycroft.ai/blog/introducing-mycroft-translate/" target="_blank" rel="noopener noreferrer">Internationalization</a></span><span style="font-weight: 400;">.</span></span>

<span style="font-weight: 400;">Think we missed something? Let us know below.</span>
<h3><span style="font-weight: 400;">Core Tech - Speech Synthesis</span></h3>
<span style="font-weight: 400;">The speech synthesis should be of sufficient quality that it is not a distraction to end users. Deploy at least one Mimic II voice using new female recordings.</span>

<span style="font-weight: 400;">Mimic 2 was a game changer for Mycroft, making cutting-edge voices possible on Mycroft. Our trial voice was a good start but was also a learning experience in data collection and training. For 19.08, we’ll deploy at least one additional voice using a dataset we’re collecting right now. This voice will be up to industry standards.</span>
<h3><span style="font-weight: 400;">Front End - Picroft</span></h3>
<span style="font-weight: 400;">Develop a setup experience that a reasonably technical user can engage with to successfully set up a Raspberry Pi.</span>

<span style="font-weight: 400;">Picroft continues to be one of the strongest entry points for new Mycroft users. We want to continue to connect with the maker and hobbyist Communities and make getting started with Mycroft easy for them.</span>
<h3><span style="font-weight: 400;">Front End - Mark II Setup</span></h3>
<span style="font-weight: 400;">Develop a setup experience that a non-technical user can engage with to successfully set up a Mycroft Mark II. This may need to be completed on a prototype.</span>

<span style="font-weight: 400;">Mark II’s timeline is not solid, but development continues. In order to ensure less technical people can use Mycroft, we’ll focus on a setup experience that suits them. As timelines for the revised Mark II design are uncertain, this may need to be completed on a prototype.</span>
<h3><span style="font-weight: 400;">Front End - Latency</span></h3>
<span style="font-weight: 400;">Reduce interaction latency to within 20% of industry leaders.</span>

<span style="font-weight: 400;">Making Mycroft faster is a huge deal. We have a portion of the business team focused on poring through metrics coming back from Mycroft Core to identify areas to improve Mycroft’s time to response. We’ll work on the identified areas and move Mycroft’s time to response within 20% of our competition.</span>
<h3><span style="font-weight: 400;">Back End - DeepSpeech</span></h3>
Automate DeepSpeech verification and submission process.

<span style="font-weight: 400;">DeepSpeech completes the true open deployment of a Mycroft assistant and it needs more focus to improve. DeepSpeech has the potential to finalize the value proposition for offline-only users, speed up the interaction for general users, and gives Mycroft the most compelling business-to-business use case. We’ll move the DeepSpeech feedback loop up to par with Precise.</span>
<h3><span style="font-weight: 400;">Core Tech - Precise</span></h3>
<span style="font-weight: 400;">Improve Precise to one false activation per 2 hours of test audio</span>

<span style="font-weight: 400;">Precise is great for ‘Hey Mycroft’ but isn’t quite perfect yet. We’ll be putting focus on the new audio processing that will be deployed first in Mark II, then future products. Success means one false activation per two hours of continuous test audio.</span>
<h3><span style="font-weight: 400;">Front End - IoT</span></h3>
<span style="font-weight: 400;">Mycroft stands out from other assistants in its user’s proclivity for IoT. Whereas IoT use is in the middle of most use charts for Amazon and Google, Mycroft’s use consistently puts IoT in the top ten and often the top five. We’ll flesh out the CommonIoT framework for skills and apply it to some of the most used and most versatile IoT skills for Mycroft.</span>
<h3><span style="font-weight: 400;">Back End - Persona</span></h3>
<span style="font-weight: 400;">Bring Persona data collection online for our Adapt and Padatious engine</span>

<span style="font-weight: 400;">Like Precise and DeepSpeech, improving NLP and creating personal Mycroft Personas will have to start with a collection and tagging portal. We’ll have a framework set up for collection of missed intents for Opted-In users, and tagging intents to skills or answering subjective questions.</span>
<h3><span style="font-weight: 400;">Core Tech - Internationalization</span></h3>
<span style="font-weight: 400;">Have the framework in place for native support of language changing and be able to use Mycroft with all core skills in one language other than English.</span>

<span style="font-weight: 400;">The response to Mycroft Translate has really been incredible. For 19.08, we’ll have all of the frameworks in place for the Community to fully deploy Mycroft in their language. We’ll confirm this by testing Mycroft in at least one non-English language for 19.08.</span>

<span style="font-weight: 400;">Those are our goals for our 19.08 release. But that’s what we think is needed. What do </span><i><span style="font-weight: 400;">you </span></i><span style="font-weight: 400;">think? Leave a comment below and let us know where Mycroft should go.</span>