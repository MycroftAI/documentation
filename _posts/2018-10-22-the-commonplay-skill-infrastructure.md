---
ID: 41041
post_title: The CommonPlay Skill Infrastructure
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/the-commonplay-skill-infrastructure/
published: true
post_date: 2018-10-22 12:09:36
---
We recently added a new piece of software architecture to Mycroft known as a <code>CommonPlaySkill</code>. This is the first of a series of “Common” infrastructure pieces which will make working with Mycroft much more natural and powerful.
<h1>What is a Skill?</h1>
First a quick review: a Skill adds new abilities to your Mycroft. Think of it like the scene in the Matrix where Neo learns Jiu-Jitsu. Plug in a skill and suddenly Mycroft has new powers. Skills have two primary pieces: <em>intents</em> which allow them to define patterns of words to listen for, and <em>handlers</em> which allow them to perform an action when the intent is heard.

For example, a simple skill can handle phrases like “tell me a joke”. The skill has an intent which spells out an interest in that phrase (along with related phrases like “I want to hear a joke”, etc). That intent is connected to a handler which looks up a random joke and has Mycroft read it to you. Hilarity ensues.
<h1>Why do we need CommonPlay?</h1>
Clearly, the skill system is really powerful! But it has an inherent limitation – it decides the handler purely on the word patterns. While I can easily define a pattern that captures the phrase “play <em>something</em>”, without a deeper understanding of that <em>something</em> Mycroft would be unable to distinguish which player to use purely from the words.

Here are some example phrases that illustrate the challenges:

<code>play Zork</code>
This one is easy – there is a game called Zork, just play it.

<code>play the News</code>
This one is easy too – fire up NPR!

<code>Play Huey Lewis and the News</code>
Looking at this naively (as if I’ve never heard Huey Lewis), is Huey Lewis a reporter or a singer? Which skill should handle this?

<code>play The Latest Single by The Hot New Band</code>
Even if I understand this is a song request, it is impossible to tell from these words which music service has the legal contracts in place to be able to play the music.

<code>play Ragtime</code>
Is this a band? A music style? A movie? Yes to all of these. What should Mycroft do?
<h1>CommonPlay Approach</h1>
A single skill (<code>skill-playback-control</code>) currently captures all of the “play *” style utterances, like those listed above. This skill will now query all the CommonPlay skills and give them an opportunity to respond with:
<ol>
 	<li>I can potentially handle that request</li>
 	<li>This is how confident I feel in my handling</li>
</ol>
After the CommonPlay skills respond, there are a few ways to continue. If only one skill replies, it is the winner and will handle the request. When there are multiple respondents, the highest confidence wins. If there are several with about the same confidence, we can ask the user to pick the winner.
<h1>Gory Details</h1>
As they say, the devil is in the details. How do you catch the query? How do you format the response? What does “confidence” mean? We wrapped all of this up in a class called <a href="https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/skills/common_play_skill.py" target="_blank" rel="noopener"><code>CommonPlaySkill</code></a> which itself derives from the familiar <code>MycroftSkill</code>. To participate in the CommonPlay system you only need to derive your skill from <code>CommonPlaySkill</code> and override a handful of methods. Here is the all you need to connect a News skill to the <code>CommonPlay</code> system.
<pre>def CPS_match_query_phrase(self, phrase):
    if self.voc_match(phrase, "News"):
        return ("news", CPSMatchLevel.TITLE)</pre>
And:
<pre>def CPS_start(self, phrase, data):
    # Begin the news stream
    self.CPS_play(self.url_rss)</pre>
That’s it. The first method responds to the <code>CommonPlay</code> query, responding to any phrase that contains the words “News”. The framework will generate a standardized confidence level based on the given <code>CPSMatchLevel</code> and the number of words in the phrase that were used in the “news” title match it found.

The second method is invoked by the framework if the query match is determined to be the best match.

You can see the entire <a href="https://github.com/MycroftAI/skill-npr-news/blob/18.08/__init__.py" target="_blank" rel="noopener">News Skill</a> on Github. It also has an intent which supports a few other non-"play" phrases such as “what is the news” and “tell me the latest news”. As you can see, it has all the capabilities of a regular skill in addition to being in the <code>CommonPlay</code> system.

I won’t bore you with lines of code here, but you can see more examples involving complex matches on the <a href="https://github.com/MycroftAI/pianobar-skill/blob/18.08/__init__.py#L75" target="_blank" rel="noopener">Pandora/Pianobar Skill</a> and the <a href="https://github.com/forslund/spotify-skill/blob/87cf92d4e68e1784923e086ddd678c2c2eb8a703/__init__.py#L461" target="_blank" rel="noopener">Spotify Skill</a>.
<h1>So Much in Common</h1>
This is the first of several “Common” skill frameworks I have planned. The <code>CommonQASkill</code> will allow Question and Answer skills to search their databases for answers and then present the best answer found. A good example of why this is needed is the question “How old is …”. From those words alone (not knowing the specific name) you can’t tell if the best answer would be in Wikipedia, IMDB, or Wookiepedia (a Star Wars knowledge base). It might even best be answered by a skill that tracks refrigerator contents – “How old is my milk?”. The <code>CommonQASkill</code> framework will allow each of these skills to look at the specific query and report back how confidently they can answer that question.

A <code>CommonIoTSkill</code> is also coming, making it easy to combine multiple types of Internet of Things systems. They can handle identical verbal requests such as “turn on the light” by looking at the context clues, such as the location of the Mycroft unit which heard the words.
<h1>Something for Everyone</h1>
Everyone is welcome to create a Common Skill. The framework will likely evolve, but by deriving from the <code>CommonPlaySkill</code> class, your skill will receive the benefits of this evolution. Play on!