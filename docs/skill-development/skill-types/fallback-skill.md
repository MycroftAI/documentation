---
description: >-
  A Fallback Skill is a Skill that will be called if no Intent is matched to the Utterance.
---

# Fallback Skill

## Fallback **Skill** order of precedence

The Fallback **Skills** all have a priority and will be checked in order from low priority value to high priority value. If a Fallback **Skill** can handle the **Utterance** it will create a response and return `True`. After this no other Fallback **Skills** are tried. This means the priority for Fallbacks that can handle a _broad_ range of queries should be _high_ \(80-100\) and Fallbacks that only responds to a very specific range of queries should be higher \(20-80\). The more specific, the lower the priority value.

## Creating a Fallback **Skill**

Import the `FallbackSkill` base class:

```python
from mycroft.skills.core import FallbackSkill
```

Create a derived class:

```python
class MeaningFallback(FallbackSkill):
    """
        A Fallback skill to answer the question about the
        meaning of life, the universe and everything.
    """
    def __init__(self):
        super(MeaningFallback, self).__init__(name='My Fallback Skill)
        # Add your own initialization code here
```

Register the handler with the fallback system

_Note: a `FallbackSkill` can register any number of fallback handlers_

```python
    def initialize(self):
         """
             Registers the fallback handler
         """
         self.register_fallback(self.handle_fallback, 10)
         # Any other initialize code you like can be placed here
```

Implement the fallback handler \(the method that will be called to potentially handle the **Utterance**\). The method implements logic to determine if the **Utterance** can be handled and shall output speech if itcan handle the query. It shall return Boolean `True` if the **Utterance** was handled and Boolean `False` if not.

```python
    def handle_fallback(self, message):
        """
            Answers question about the meaning of life, the universe
            and everything.
        """
        utterance = message.data.get("utterance")
        if 'what' in utterance
            and 'meaning' in utterance
            and ('life' in utterance
                or 'universe' in utterance
                or 'everything' in utterance):
            self.speak('42')
            return True
        else:
            return False
```

Finally, the **Skill** creator must make sure the skill handler is removed when the **Skill** is shutdown by the system.

```python
    def shutdown(self):
        """
            Remove this skill from list of fallback skills.
        """
        self.remove_fallback(self.handle_fallback)
        super(MeaningFallback, self).shutdown()
```

And as with a normal **Skill** the function `create_skill()` needs to be in the file to instantiate the skill.

```python
def create_skill():
    return MeaningFallback()
```

The above example can be found [here](https://github.com/forslund/fallback-meaning).
