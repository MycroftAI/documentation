---
description: A statement is any information spoken by Mycroft to the User.
---

# Statements

## Speaking a statement

In it's most simple form, a statement is speaking a string of text. To do this in a Skill, we call the [`speak_dialog()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.speak_dialog) method.

```python
from mycroft import MycroftSkill, intent_handler

class HelloWorldSkill(MycroftSkill):

    @intent_handler('do.you.like.intent')
    def handle_example(self, message):
        """Speak dialog when triggered."""
        self.speak_dialog("i.do.like")
        
def create_skill():
    return HelloWorldSkill()
```

Our `do.you.like.intent` file is a [Padatious intent file](intents/padatious-intents.md), and it might be something like:

```python
do you like ice cream
```

Our `i.do.like.dialog` file might be something:

```python
I do like ice cream
```

### File locations

In the example above we have a complete Skill with a single intent handler. It will be triggered by the sample utterances in `locale/en-us/do.you.like.intent` and will speak the dialog contained in `locale/en-us/i.do.like.dialog`. 

If you would like to separate your intent and dialog files, these may be split up into: 

* `vocab/en-us/do.you.like.intent`
* `dialog/en-us/i.do.like.dialog`

### Adding variations

Currently our `i.do.like.dialog` file contains a single line "I do like ice cream". To provide some variation to how our Skill responds, we can add those into the same file. 

Let's extend our `i.do.like.dialog` file to include a variation:

```python
I do like ice cream
Yes, I love ice cream
```

When the `speak_dialog()` method is called, it will select one of the lines at random to speak.

### Adding variables

The first example works for static dialog, however we often want to customize this based on something that happened in the Skill. For this we can pass a data object to the `speak_dialog()` method that contains any variables we want to use in our statement.

Let's inform the user what flavor of ice cream we like and pass that in from the Skill instead of hard coding it into the dialog file.

First we'll update our `i.do.like.dialog` file to include a variable name:

```python
I do like {flavor} ice cream
Yes, I love {flavor} ice cream
```

Then from our Skill we need to define the variable and pass it into our `speak_dialog()` method as an object in the `data` parameter.

```python
from mycroft import MycroftSkill, intent_handler

class HelloWorldSkill(MycroftSkill):

    @intent_handler("do.you.like.intent")
    def handle_example(self, message):
        """Speak dialog when triggered."""
        favorite_flavor = "chocolate"
        self.speak_dialog("i.do.like", data={"flavor": favorite_flavor})
        
def create_skill():
    return HelloWorldSkill()
```

Now our favorite flavor is defined in our Skill. Currently it's still hard coded, but as it is part of the code, you can see that we can now dynamically assign it however we wish.

## Waiting for speech

By default, the `speak_dialog()` method is non-blocking. That is any code following the call to `speak_dialog()` will execute whilst Mycroft is talking. This is useful to allow your Skill to perform actions while it is speaking. 

Rather than telling the User that we are fetching some data, then going out to fetch it, we can do the two things simultaneously providing a better experience. 

However there are times when we need to wait until the statement has been spoken before doing something else. We have two options for this.

### Wait Parameter

We can pass a `wait=True` parameter to our `speak_dialog()` method. This makes the method blocking and no other code will execute until the statement has been spoken.

```python
from mycroft import MycroftSkill, intent_handler

class HelloWorldSkill(MycroftSkill):

    @intent_handler("do.you.like.intent")
    def handle_example(self, message):
        """Speak dialog when triggered."""
        favorite_flavor = "chocolate"
        self.speak_dialog("i.do.like", 
                          data={"flavor": favorite_flavor},
                          wait=True)
        self.log.info("I waited for you")
        
def create_skill():
    return HelloWorldSkill()     
```

### wait\_while\_speaking

The [`mycroft.audio.wait_while_speaking()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.audio.html#mycroft.audio.wait_while_speaking) method allows us to execute some code, then wait for Mycroft to finish speaking.

```python
from mycroft import MycroftSkill, intent_handler
from mycroft.audio import wait_while_speaking

class HelloWorldSkill(MycroftSkill):

    @intent_handler("do.you.like.intent")
    def handle_example(self, message):
        """Speak dialog when triggered."""
        favorite_flavor = "chocolate"
        self.speak_dialog("i.do.like", 
                          data={"flavor": favorite_flavor})
        self.log.info("I am executed immediately")
        wait_while_speaking()
        self.log.info("But I waited for you")
        
def create_skill():
    return HelloWorldSkill()     
```

## Using translatable resources

To enable your Skill in multiple languages we strongly encourage Skill authors not to hard-code strings of text into your Skill. Strings should instead be constructed using translatable resources contained within the `dialog` or `locale` directories of your Skill.

See the available [`translate_*`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.translate) methods for more details.

