# Adapt Intents

Adapt is a keyword based intent parser. It determines user intent based on a list of keywords or entities contained within a users utterance.

{% embed url="https://www.youtube.com/watch?v=zR9xvPtM6Ro" %}

{% hint style="info" %}
For technical details or usage of Adapt outside of a Mycroft Skill, see the Adapt documentation at:
{% endhint %}

## Defining keywords and entities

### Vocab (.voc) Files
Vocab files define keywords that Adapt will look for in a Users utterance to determine their intent.

These files can be located in either the `vocab/lang-code/` or `locale/lang-code/` directories of a Skill. They can have one or more lines to list synonyms or terms that have the same meaning in the context of this Skill. Mycroft will match _any_ of these keywords with the Intent.

Consider a simple `Potato.voc`. Within this file we might include:

```text
potato
potatoes
spud
```

If the User speaks _either_:

> potato

or

> potatoes

or

> spud

Mycroft will match this to any Adapt Intents that are using the `Potato` keyword.

### Regular Expression (.rx) Files

Regular expressions (or regex) allow us to capture entities based on the structure of an utterance.

These files can be located in either the `regex/lang-code/` or `locale/lang-code/` directories of a Skill. They can have one or more lines to provide different ways that an entity may be referenced. Mycroft will execute these lines in the order they appear and return the first result as an entity to the Intent Handler.

Let's consider a `type.rx` file to extract the type of potato we are interested in. Within this file we might include:

```text
.* about (?P<Type>.*) potatoes
.* (make|like) (?P<Type>.*) potato
```

**What is this regex doing?**
`.*` matches zero, one or more of any single character.
`(?P<Type>.*)` is known as a Named Capturing Group. The variable name is defined between the <angle brackets>, and what is captured is defined after this name. In this case we use `.*` to capture anything.

{% hint style="info" %}
[Learn more about Regular Expressions](https://github.com/ziishaned/learn-regex/blob/master/README.md).
{% endhint %}

So our first line would match an utterance such as:

> Tell me about *sweet potatoes*

Whilst the second line will match either:

> Do you like *deep fried potato*

or

> How do I make *mashed potato*

From these three utterances, what will the extracted `Type` be:  
1. `sweet`  
2. `deep fried`  
3. `mashed`  

This `Type` will be available to use in your Skill's Intent Handler on the `message` obect. We can access this using:
```
message.data.get('Type')
```

## Using Adapt in a Skill
Now that we have a Vocab and Regular Expression defined, let's look at how to use these in a simple Skill.

For the following example we will use the two files we outlined above:
- `Potato.voc`
- `Type.rx`

We will also add some new `.voc` files:
- `Like.voc` - containing a single line "like"
- `You.voc` - containing a single line "you"
- `I.voc` - containing a single line "I"

### Creating the Intent Handler
To construct an Adapt Intent, we use the intent_handler\(\) _decorator_ and pass in the Adapt IntentBuilder.

{% hint style="info" %}
[Learn more about _decorators_ in Python](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators).
{% endhint %}

Both of these must be imported before we can use them:

```python
from adapt.intent import IntentBuilder
from mycroft import intent_handler
```

The IntentBuilder is then passed the name of the Intent as a string, followed by one or more parameters that correspond with one of our `.voc` or `.rx` files.

```Python
@intent_handler(IntentBuilder('IntentName')
                              .require('Potato')
                              .require('Like')
                              .optionally('Type')
                              .one_of('You', 'I'))
```

In this example:
- the `Potato` and `Like` keywords are required. It must be present for the intent to match.
- the `Type` entity is optional. A stronger match will be made if this is found, but it is not required.
- we require at least one of the `You` or `I` keywords.

What are some utterances that would match this intent?

> Do you like potato?
> Do you like fried potato?
> Will I like mashed potato?
> Do you think I would like potato?

What are some utterances that would *not* match the intent?

> How do I make mashed potato?

_The required `Like` keyword is not found._

> Is it like a potato?

_Neither the `You` nor `I` keyword is found._

### Including it in a Skill

Now we can create our Potato Skill:

```python
from adapt.intent import IntentBuilder
from mycroft import intent_handler

class PotatoSkill(MycroftSkill):

    @intent_handler(IntentBuilder('WhatIsPotato').require('What')
                    .require('Potato'))
    def handle_what_is(self, message):
        self.speak_dialog('potato.description')

    @intent_handler(IntentBuilder('DoYouLikePotato').require('Potato')
                    .require('Like').optionally('Type').one_of('You', 'I'))
    def handle_do_you_like(self, message):
        potato_type = message.data.get('Type')
        if potato_type is not None:
            self.speak_dialog('like.potato.type',
                              {'type': potato_type})
        else:
            self.speak_dialog('like.potato.generic')

def create_skill():
    return PotatoSkill()
```

{% hint style="info" %}
You can [download this entire Potato Skill from Github](https://github.com/krisgesling/dev-ex-adapt-intents-skill/blob/master/__init__.py), or see another Adapt intent handler example in the [Hello World Skill](https://github.com/MycroftAI/skill-hello-world/blob/f3eb89be6d80e1834637a64566c707d05fb8e3fa/__init__.py#L37)
{% endhint %}

## Common Problems
One of the most common mistakes when getting started with Skills is that the vocab file doesn't include all of the keywords or terms that a User might use to trigger the intent. It is important to map out your Skill and test the interactions with others to see how they might ask questions differently.
