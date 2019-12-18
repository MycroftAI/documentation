---
description: >-
  Mycroft Skills provide a number of methods to perform actions at different
  points during the lifecycle of the Class instance.
---

# Lifecycle Methods

The MycroftSkill class that all Skills inherit from contains a number of methods that can be overridden by an instance of the Class. This enables a Skill to execute code at specific points in the lifecycle of a Skill. Each of these is optional, meaning none are required to be defined in your Skill.

## **\_\_init\_\_**

The `__init__` method is called when the Skill is first constructed. It is often used to declare variables or perform setup actions, however it cannot utilize other MycroftSkill methods as the class does not yet exist.

This method is optional, but if used, the `__init__` method from the Super Class \(MycroftSkill\) must be called.

In the following example we assign a variable `learning` to be `True`. The variable is appended to the instance using `self` so that we can access this variable in any part of our Skill.

```python
    def __init__(self):
        super().__init__()
        self.learning = True
```

## Initialize

The `initialize` method is called after the Skill is fully constructed and registered with the system. It is used to perform any final setup for the Skill including accessing Skill settings.

In the following example we access the `my_setting` value, that would have been defined in the Skill's [`settingsmeta.json`](../skill-settings.md). We use the `get` method in case the variable `my_setting` is undefined.

```python
    def initialize(self):
        my_setting = self.settings.get('my_setting')
```

## Converse

The `converse` method can be used to handle follow up utterances prior to the normal intent handling process. It can be useful for handling utterances from a User that do not make sense as a standalone [intent](../intents/).

The method receives two arguments:

* `utterances` \(list\): The utterances from the user. If there are multiple utterances, consider them all to be transcription possibilities. Commonly, the first entry is the raw utterance and the second is a `normalized` version of the first utterance.
* `lang` \(string\): The language the utterance is in. This defaults to None.

Once the Skill has initially been triggered by the User, the `converse` method will be called each time an utterance is received. It is therefore important to check the contents of the utterance to ensure it matches what you expected.

If the utterance is handled by the converse method, we return `True` to indicate that the utterance should not be passed onto the normal intent matching service and no other action is required by the system. If the utterance was not handled, we return `False` and the utterance is passed on first to other `converse` methods, and then to the normal intent matching service.

In the following example, we check that utterances is not empty, and if the utterance matches vocabulary from `understood.voc`. If the user has understood we speak a line from `great.dialog` and return `True` to indicate the utterance has been handled. If the vocabulary does not match then we return `False` as the utterance should be passed to the normal intent matching service.

```text
    def converse(self, utterances, lang):
        if utterances and self.voc_match(utterances[0], 'understood'):
            self.speak_dialog('great')
            return True
        else:
            return False
```

## Stop

The `stop` method is called anytime a User says "Stop" or a similar command. It is useful for stopping any output or process that a User might want to end without needing to issue a Skill specific utterance such as media playback or an expired alarm notification.

In the following example, we call a method `stop_beeping` to end a notification that our Skill has created.

```text
    def stop(self):
        self.stop_beeping()
```

## Shutdown

The `shutdown` method is called during the Skill process termination. It is used to perform any final actions to ensure all processes and operations in execution are stopped safely. This might be particularly useful for Skills that have scheduled future events, may be writing to a file or database, or that have initiated new processes.

In the following example we cancel a scheduled event and call a method in our Skill to stop a subprocess we initiated.

```python
    def shutdown(self):
        self.cancel_scheduled_event('my_event')
        self.stop_my_subprocess()
```

