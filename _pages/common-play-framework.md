---
ID: 41539
post_title: Common Play Framework
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/skills/common-play-framework/
published: true
post_date: 2018-11-16 07:27:11
---
# Common Play Framework

- [Common Play Framework](#common-play-framework)
  * [Introduction](#introduction)
  * [Basing your Skill on the `CommonPlaySkill` class instead of `MycroftSkill`](#basing-your-skill-on-the-commonplayskill-class-instead-of-mycroftskill)
  * [CPS_match_query_phrase](#cps-match-query-phrase)
  * [CPS_start](#cps-start)
  * [Example implementation of `CommonPlaySkill`](#example-implementation-of-commonplayskill)
  * [Where to go for more assistance](#where-to-go-for-more-assistance)


## Introduction

Over time, many **Skills** are likely to use similar keywords - called `Intents` - to triggers actions. One of the most frequently used keywords is `play`. This means that several **Skills** can all use the word `play` in their `Intents` - causing something called an _intent collision_ - where Mycroft doesn't know which **Skill** to invoke because there are so many to choose from.

The **Common Play Framework** solves this problem by allowing Mycroft to infer a _confidence score_ from an `Intent` which uses the `play` keyword. The _confidence score_ is designed so that there is a much higher probability of the right **Skill** being invoked to handle an `Intent` which has the keyword `play` in it.

To take advantage of the **Common Play Framework**, your **Skill** needs to be written in a specific way - outlined below:


## Basing your Skill on the `CommonPlaySkill` class instead of `MycroftSkill`

To interface with the playback control the **Skill** will be based on the `CommonPlaySkill` class instead of the normal `MycroftSkill`. Your **Skill** also needs to implement two methods, `CPS_match_query_phrase` and `CPS_start`.

The setup looks like this:

```python
from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel


class TutorialSkill(CommonPlaySkill):
    def CPS_match_query_phrase(self, phrase):
        """ This method responds wether the skill can play the input phrase.

            The method is invoked by the PlayBackControlSkill.

            Returns: tuple (matched phrase(str),
                            match level(CPSMatchLevel),
                            optional data(dict))
                     or None if no match was found.
        """
        return None

    def CPS_start(self, phrase, data):
        """ Starts playback.

            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        pass


def create_skill():
    return TutorialSkill()
```


## CPS_match_query_phrase

The argument `phrase` is sent from the `PlaybackControlSkill`, and is the entire phrase said by the user with the `play` keyword stripped out. So if the user says

> "Play something by Professor Elemental"

the `phrase` argument will contain

> "something by Professor Elemental"

Using this phrase the Skill Author should now determine if the **Skill** can play this phrase and return the matched phrase and the confidence level. The confidence level is reported using the `CPSMatchLevel` enum type.

Possible values are:

- `CPSMatchLevel.EXACT` (The input matches exact)
- `CPSMatchLevel.MULTI_KEY` (The input contains multiple matches such as Artist and Album title)
- `CPSMatchLevel.TITLE` (The phrase contains a matching title)
- `CPSMatchLevel.ARTIST` (The phrase contains a matching artist)
- `CPSMatchLevel.CATEGORY` (The phrase contains a category supported by the skill, Rock, bitpop, Podcast etc.)
- `CPSMatchLevel.GENERIC` (Generic match, maybe contains the skill title but no media match)

where `CPSMatchLevel.EXACT` is the greatest confidence and the `CPSMatchLevel.GENERIC` is lowest.

Example:
```python
        return (matched_phrase, CPSMatchLevel.TITLE)
```

The method can also return data that will be needed when starting the playback. This is very useful if the skill can play a variety of things of various types. The data is added as a third element in the return tuple and has to be a simple python dict.

Example:
```python
        data = {
            "track": "my_music.mp3"
        }
        return (matched_phrase, CPSMatchLevel.TITLE, data)
```

The data is then passed to the `CPS_start()` method as an argument.

## CPS_start

`CPS_start` simply starts the playback using the data and/or the phrase to determine what to play.

For convenience the `self.audioservice` object can be used to start playback or queue up tracks.

## Example implementation of `CommonPlaySkill`

Let's fill in the blanks in the the above base and create a **Skill** to play the best (according to yours truly, @forslund) Commodore 64 remixes!

We add a nice safe data structure to the **Skill** file:

```python
track_dict = {
    'bomb jack': 'http://remix.kwed.org/files/RKOfiles/Chronblom%20-%20Bomb%20Jack%20subtune%206%20(violin%20version).mp3',
    'druid': 'http://remix.kwed.org/files/RKOfiles/Revel%20Craft%20-%20Druid.mp3',
    'crazy comets':  'http://remix.kwed.org/files/RKOfiles/Makke%20-%20Crazy%20Comets%20(Komet%20Non-Stop).mp3',
    'boulder dash': 'http://remix.kwed.org/files/RKOfiles/Mahoney%20-%20BoulderDash%20(Commodore%2069%20mix).mp3',
    'garfield': 'http://remix.kwed.org/files/RKOfiles/Reyn%20Ouwehand%20-%20Garfield.mp3'
}
```

To match from this list the `match_one` function in `mycroft.util.parse` can be used to fuzzy match one of the elements in the dict.

First we add the import at the top of the file:

```python
from mycroft.util.parse import match_one
```

then we update the `CPS_match_query_phrase` method to use it to select the best match. This fuzzy matching system will match strings that are close to one of the keys in the above `dict`. This means phrases like "play crazy comet" will be matched with a fairly high confidence despite not being the _exact_ string in the dictionary.

```python
    def CPS_match_query_phrase(self, phrase):
        """ This method responds wether the skill can play the input phrase.

            The method is invoked by the PlayBackControlSkill.

            Returns: tuple (matched phrase(str),
                            match level(CPSMatchLevel),
                            optional data(dict))
                     or None if no match was found.
        """
        # Get match and confidence
        match, confidence = match_one(phrase, track_dict)
        # If the confidence is high enough return a match
        if confidence > 0.5:
            return (match, CPSMatchLevel.TITLE, {"track": match})
        # Otherwise return None
        else:
            return None
```

This will include the url of the selected file as "track" in the data received by the `CPS_start` method.

Which simply becomes

```python
    def CPS_start(self, phrase, data):
        """ Starts playback.

            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        # Retrieve the track url from the data
        url = data['track']
        self.audioservice.play(url)  # Send url to audioservice to start playback
```

The complete source code can be found [here](https://github.com/forslund/common-play-tutorial)

## Where to go for more assistance

Join us in the [Skills Mycroft Chat room](https://chat.mycroft.ai/community/channels/skills) or join us in the [Mycroft Forum](https://community.mycroft.ai).
