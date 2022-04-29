---
description: >-
  Converse allows a recently active Skill to inspect utterances before the
  normal intent handling process. It allows for Skills to respond to
  unstructured follow up utterances.
---

# Converse

Each Skill may define a `converse()` method. This method will be called anytime the Skill has been recently active and a new utterance is processed.&#x20;

The converse method expects a single argument which is a standard Mycroft Message object. This is the same object an intent handler receives.

Converse methods must return a Boolean value. True if an utterance was handled, otherwise False.

### Basic usage

Let's use a version of the Ice Cream Skill we've been building up and add a converse method to catch any brief statements of thanks that might directly follow an order.

```python
from mycroft import MycroftSkill, intent_handler


class IceCreamSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.flavors = ['vanilla', 'chocolate', 'mint']

    @intent_handler('request.icecream.intent')
    def handle_request_icecream(self):
        self.speak_dialog('welcome')
        selection = self.ask_selection(self.flavors, 'what.flavor')
        self.speak_dialog('coming-right-up', {'flavor': selection})

    def converse(self, message):
        if self.voc_match(message.data['utterances'][0], 'Thankyou'):
            self.speak_dialog("you-are-welcome")
            return True


def create_skill():
    return IceCreamSkill()
```

In this example:

1. A User might request an ice cream which is handled by `handle_request_icecream()`&#x20;
2. The Skill would be added to the system Active Skill list for up to 5 minutes.
3. Any utterance received by Mycroft would trigger this Skills converse system whilst it is considered active.
4. If the User followed up with a pleasantry such as "Hey Mycroft, thanks" - the converse method would match this vocab against the `Thankyou.voc` file in the Skill and speak the contents of the `you-are-welcome.dialog` file. The method would return `True` and the utterance would be consumed meaning the intent parsing service would never be triggered.
5. Any utterance that did not match would be silently ignored and allowed to continue on to other converse methods and finally to the intent parsing service.

### Active Skill List

A Skill is considered active if it has been called in the last 5 minutes.

Skills are called in order of when they were last active. For example, if a user spoke the following commands:

> Hey Mycroft, set a timer for 10 minutes
>
> Hey Mycroft, what's the weather

Then the utterance "what's the weather" would first be sent to the Timer Skill's `converse()` method, then to the intent service for normal handling where the Weather Skill would be called.

As the Weather Skill was called it has now been added to the front of the Active Skills List. Hence the next utterance received will be directed to:

1. `WeatherSkill.converse()`
2. `TimerSkill.converse()`
3. Normal intent parsing service

### Making a Skill Active

There are occasions where a Skill has not been triggered by the User but it should still be considered "Active".

In the case of our Ice Cream Skill - we might have a function that will execute when the customers order is ready. At this point, we also want to be responsive to the customers thanks, so we call `self.make_active()` to manually add our Skill to the front of the Active Skills List.

{% hint style="warning" %}
**Please note:** Any use of this method will be closely scrutinized during the Skills Marketplace submission process.

Skills that attempt to use the Converse method or the Active Skills List in ways that a normal user would not intend or appreciate, will not be approved.
{% endhint %}

### Further information&#x20;

See the [`converse()` method documentation](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.converse).
