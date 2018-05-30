---
ID: 38242
post_title: 'The Early Stages of Voice Technology: Coupling Privacy and User Agency'
author: Eric Jurgeson
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/early-stages-of-voice-technology-coupling-privacy-and-user-agency/
published: true
post_date: 2018-05-30 10:00:52
---
<span style="font-weight: 400;">Like we said in our post about </span><a href="https://mycroft.ai/blog/finding-laughter-in-the-early-stages-of-voice-technology/"><span style="font-weight: 400;">Alexa’s recent laughing fits</span></a><span style="font-weight: 400;">, “testing, iteration, and failure </span><i><span style="font-weight: 400;">will</span></i><span style="font-weight: 400;"> be a part of the journey” that anyone building a technology from the ground up will encounter, especially voice technology. There’s been another news break of just such an example, so let’s discuss and see what we can learn.</span>

<span style="font-weight: 400;">On May 24, 2018, </span><a href="https://www.kiro7.com/news/local/woman-says-her-amazon-device-recorded-private-conversation-sent-it-out-to-random-contact/755507974"><span style="font-weight: 400;">KIRO 7 in Seattle</span></a><span style="font-weight: 400;"> reported a story of a husband and wife who, two weeks prior, had a private conversation unknowingly recorded and sent by their Amazon Echo device to a random person on their contact list.</span>

<span style="font-weight: 400;">Amazon has claimed that this was an unfortunate and rare string of false activations and misheard speech in the Alexa software that invoked a “Send a Message” skill, selected a contact, and confirmed the request </span>by mistake at least twice. The woman involved in the mishap has returned to KIRO 7 saying she heard no vocal requests from the device during the conversation that was recorded.

<span style="font-weight: 400;">The woman has called this a “total privacy invasion” and unplugged the numerous Echo devices around her house.</span>

<span style="font-weight: 400;">The story brings up a few good and bad things:</span>
<h3><span style="font-weight: 400;">Good: The users reported the issue to Amazon and Amazon responded</span></h3>
<span style="font-weight: 400;">Feedback is essential to build useful technology, and this couple could have easily tossed their Echo devices in the trash and told no one. But they reported the issue, and an Alexa Engineer worked through the issue with the couple, apologized, and said the Alexa team would start fixing the issue.</span>

<span style="font-weight: 400;">Mycroft receives great feedback and engagement from our community, and we value every bug report and improvement suggestion. If you have any feedback, you can always submit it at
</span> <a href="https://mycroft.ai/contact/" target="_blank" rel="noopener">https://mycroft.ai/contact/</a>.
<h3><span style="font-weight: 400;">Bad: The incident revealed that Amazon keeps recordings and transcripts of every interaction you have with the Alexa software</span></h3>
This may not come as a surprise to some people, but to others it will. The Alexa Engineer reported that other engineers had confirmed the issue through the logs of the couple’s interactions; either recordings, transcripts, or both. Amazon has a log of every interaction, intended or accidental, with the Alexa software.

This of course opens the Catch-22 of this industry: lots of data (recordings and transcripts of interactions, logs, etc) are required to develop and improve voice software. For Alexa and other voice assistants, your contribution of data is required of you to use the software.

<span style="font-weight: 400;">Mycroft thinks this technology is too important to exclude people who value user privacy. We default to keeping no data from any Mycroft interactions. To give us a source of the data necessary to improve the software, we’ve created our <a href="https://home.mycroft.ai/#/setting/basic" target="_blank" rel="noopener">Opt-In</a> for those who want to contribute to the <a href="https://mycroft.ai/blog/privacy-machine-learning-open-data-set-opt-feature/" target="_blank" rel="noopener">Mycroft Open Dataset</a>. This, balanced with our Community’s generosity and trust, provides the data needed to improve the technology and makes it available for creators in the future to use in the world’s next groundbreaking technology. </span>
<h3><span style="font-weight: 400;">Good: Alexa and others are building useful features</span></h3>
Some may say the Alexa communications skills are unnecessary when someone could easily use a phone. But there can be real benefits of a hands-free assistant for immobilized, injured, or aging people who would otherwise have a harder time communicating. Transformative applications for voice assistants will be developed for general uses and specialized needs, both of which will be used by the public.
<h3><span style="font-weight: 400;">Bad: The skill in question is a default skill that can’t be turned off or removed</span></h3>
<span style="font-weight: 400;">Nowhere in the Alexa app can you remove or turn off communications globally. That means even someone comfortable with Amazon storing their recordings still has the potential to send messages inadvertently to their contacts. Even if Amazon’s systems protected privacy perfectly, Alexa could still be a path to accidentally sharing sensitive information.</span>

<span style="font-weight: 400;">Mycroft does not currently have any calling or messaging features, but they are sure to come as the community has shown interest in having Mycroft as a home intercom or speakerphone. (If you want to see that, drop a vote in the </span><a href="https://community.mycroft.ai/c/skill-suggestions"><span style="font-weight: 400;">Skill Suggestions</span></a><span style="font-weight: 400;"> forum.)</span>

<span style="font-weight: 400;">How do we ensure privacy by design when those features start to roll out? How can a Mycroft Community Member ensure there is no way to inadvertently send an intimate conversation to one of their contacts? The starting point is to let them completely uninstall any skill at any time.</span>

<span style="font-weight: 400;">Mycroft is modular and open, so any feature or skill that exists can be checked and verified through the source code, and added or removed at will. This technology is powerful, but some skills may be too intrusive or not useful for some users. We have no desires to limit Mycroft users to what they can do or tie them in to keeping skills they don’t need on their devices.</span>
<h2><span style="font-weight: 400;">Conclusions</span></h2>
<span style="font-weight: 400;">This technology is going to continue to be developed and adopted. Every provider of voice technology will find stumbling blocks from which they’ll have to improve, Mycroft included.</span>

<span style="font-weight: 400;">We will continue forward with privacy first, but while privacy is necessary, this issue with Alexa shows it will not be sufficient as features continue to multiply. Therefore, we will continue to put our Community and users first as we develop Mycroft.</span>

<span style="font-weight: 400;">For now that means remaining committed to Open Source and user agency. In the future, it means making it clear what skills do when they are added to a device. It means developing open models for speech recognition and helping users to run it locally. It means releasing a locally hosted backend for users.</span>

<span style="font-weight: 400;">Practicing both user-centered design and privacy by design maintains our foundation of an AI for everyone -- an assistant easy to set up that is useful to the general public, and configurable to meet the specific needs of privacy and security of anyone who so chooses.</span>

Have something to say on the topic? Join us on the forum to discuss.