---
description: What is an Intent? What is an Intent parser?
---

# Intents

In speech recognition and voice assistance, an intent is the task the user _intends_ to accomplish. A user can accomplish the same task by expressing their intent in multiple ways. The role of the intent parser is to extract from the user's speech key data elements that specify their intent in more detail. This data can then be passed to other services, such as Skills to help the user accomplish their intended task.

_Example_: Julie wants to know about today's weather in her current location, which is Melbourne, Australia.

> "hey mycroft, what's today's weather like?" "hey mycroft, what's the weather like in Melbourne?" "hey mycroft, weather"

Each of these examples has very similar _intent_. The role of an intent parser is to determine what this intent is.

In the example above, we might extract data elements like:

* **weather** - we know that Julie wants to know about the weather, but she has not been specific about the type of weather, such as _wind_, _precipitation_, _snowfall_ or the risk of _fire danger_ from bushfires. Melbourne, Australia rarely experiences snowfall, but falls under bushfire risk every summer.
* **location** - Julie has stipulated her location as Melbourne, but she does not state that she means Melbourne, Australia. How do we distinguish this from Melbourne, Florida, United States?
* **date** - Julie has been specific about the _timeframe_ she wants weather data for - today. But how do we know what today means in Julie's timezone. Melbourne, Australia is between 14-18 hours ahead of the United States. We don't want to give Julie yesterday's weather, particularly as Melbourne is renowned for having changeable weather.

## Mycroft's Intent Parsing Engines

Mycroft has two separate Intent parsing engines each with their own strengths. Each of these can be used in most situations, however they will process the utterance in different ways.

[**Padatious**](../../../mycroft-technologies/padatious.md) is a light-weight neural network that is trained on whole phrases. Padatious intents are generally more accurate however require you to include sample phrases that cover the breadth of ways that a User may ask about something.

[**Adapt**](../../../mycroft-technologies/adapt/) is a keyword based parser. It is more flexible, as it detects the presence of one or more keywords in an utterance, however this can result in false matches.

We will now look at each in more detail, including how to use them in a Mycroft Skill.

