---
description: >-
  A prompt is any question or statement spoken by Mycroft that expects a
  response from the User.
---

# Prompts

Here we look at how to implement the most common types of prompts. For more information on conversation design see the [Voice User Interface Design Guidelines](https://mycroft-ai.gitbook.io/docs/skill-development/voice-user-interface-design-guidelines/interactions-and-guidelines/statements-and-prompts).

## Get Response

Any Skill can request a response from the user - making a statement or asking a question before the microphone is activated to record the User's response.

The base implementation of this is the [`get_response()` method](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.get_response).

To see it in action, let's create a simple Skill that asks the User what their favorite flavor of ice cream is.

```python
from mycroft import MycroftSkill, intent_handler


class IceCreamSkill(MycroftSkill):
    @intent_handler('set.favorite.intent')
    def handle_set_favorite(self):
        favorite_flavor = self.get_response('what.is.your.favorite.flavor')
        self.speak_dialog('confirm.favorite.flavor', {'flavor': favorite_flavor})


def create_skill():
    return IceCreamSkill()
```

In this Skill we have used `get_response()` and passed it the name of our dialog file `'what.is.your.favorite.flavor.dialog'`. This is the simplest form of this method. It will speak dialog from the given file, then activate the microphone for 3-10 seconds allowing the User to respond. The transcript of their response will then be assigned to our variable `favorite_flavor`. To confirm that we have heard the User correctly we then speak a confirmation dialog passing the value of `favorite_flavor` to be spoken as part of that dialog.

### Optional Arguments

The `get_response()` method also takes the following optional arguments:

* `data` \(dict\) - used to populate the dialog file, just like `speak_dialog()`
* `validator` \(function\) - returns a boolean to define whether the response meets some criteria for success
* `on_fail` \(function\) - returns a string that will be spoken if the validator returns False
* `num_retries` \(int\) - number of times the system should repeat the question to get a successful result

#### See it in action:

{% embed url="https://www.youtube.com/watch?v=Ke7mRl-Qo-U" caption="Video Tutorial: Asking a question" %}

## Yes / No Questions

[`ask_yesno()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.ask_yesno) checks if the response contains "yes" or "no" like phrases.

The vocab for this check is sourced from the Skills `yes.voc` and `no.voc` files \(if they exist\), as well as mycroft-cores defaults \(contained within `mycroft-core/res/text/en-us/yes.voc`\). A longer phrase containing the required vocab is considered successful eg both "yes" and "yeah that would be great thanks" would be considered a successful "yes".

If "yes" or "no" responses are detected, then the method will return the string "yes" or "no". If the response does not contain "yes" or "no" vocabulary then the entire utterance will be returned. If no speech was detected indicating the User did not respond, then the method will return `None`.

Let's add a new intent to our `IceCreamSkill` to see how this works.

```python
from mycroft import MycroftSkill, intent_handler


class IceCreamSkill(MycroftSkill):
    @intent_handler('do.you.like.intent')
    def handle_do_you_like(self):
        likes_ice_cream = self.ask_yesno('do.you.like.ice.cream')
        if likes_ice_cream == 'yes':
            self.speak_dialog('does.like')
        elif likes_ice_cream == 'no':
            self.speak_dialog('does.not.like')
        else:
            self.speak_dialog('could.not.understand')


def create_skill():
    return IceCreamSkill()
```

In this example we have asked the User if they like ice cream. We then speak different dialog whether they respond yes or no. We also speak some error dialog if neither yes or no are returned.

#### See it in action:

{% embed url="https://www.youtube.com/watch?v=vzQX8RocODs" caption="Video Tutorial: Asking a yes/no question" %}

## Providing a list of options

[`ask_selection()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.ask_selection) provides a list of options to the User for them to select from. The User can respond with either the name of one of these options or select with a numbered ordinal eg "the third".

This method automatically manages fuzzy matching the users response against the list of options provided.

Let's jump back into our `IceCreamSkill` to give the User a list of options to choose from.

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
        self.speak_dialog('coming.right.up', {'flavor': selection})


def create_skill():
    return IceCreamSkill()
```

In this example we first speak some `welcome.dialog`. The list of flavors is then spoken, followed by the `what.flavor.dialog`. Finally we confirm the Users selection by speaking `coming.right.up.dialog`

### Optional arguments

There are two optional arguments for this method.

`min_conf` \(float\) defines the minimum confidence level for fuzzy matching the Users response against the list of options. `numeric` \(bool\) if set to True will speak the options as a numbered list eg "One, vanilla. Two, chocolate. Or three, mint"

#### See it in action:

{% embed url="https://youtu.be/TNezYhqcX\_4" caption="Video Tutorial: Asking the user to choose an option" %}

## Returning responses to the intent parser

So far we have looked at ways to prompt the User, and return their response directly to our Skill. It is also possible to speak some dialog, and activate the listener, directing the response back to the standard intent parsing engine. We may do this to let the user trigger another Skill, or because we want to make use of our own intents to handle the response.

To do this, we use the `expect_response` parameter of the `speak_dialog()` method.

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
        self.speak_dialog('coming.right.up', {'flavor': selection})
        self.speak_dialog('now.what', expect_response=True)


def create_skill():
    return IceCreamSkill()
```

Here we have added a new dialog after confirming the Users selection. We may use it to tell the User other things they can do with their Mycroft device while they enjoy their delicious ice cream.

