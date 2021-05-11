# Padatious Intents

Padatious is a [machine-learning](https://en.wikipedia.org/wiki/Machine_learning), [neural-network](https://en.wikipedia.org/wiki/Artificial_neural_network) based _intent parser_. Unlike Adapt, which uses small groups of unique words, Padatious is trained on the sentence as a whole.

Padatious has a number of key benefits over other intent parsing technologies.

* With Padatious, Intents are easy to create
* The machine learning model in Padatious requires a relatively small amount of data
* Machine learning models need to be _trained_. The model used by Padatious is quick and easy to train.
* Intents run independently of each other. This allows quickly installing new skills without retraining all other skill intents.
* With Padatious, you can easily extract entities and then use these in Skills. For example, "Find the nearest gas station" -&gt; `{ "place":"gas station"}`

{% page-ref page="../../../mycroft-technologies/padatious.md" %}

## Creating Intents

Padatious uses a series of example sentences to train a machine learning model to identify an intent.

The examples are stored in a Skill's `vocab/lang` or `local/lang` directory, in files ending in the file extension `.intent`. For example, if you were to create a _tomato_ Skill to respond to questions about a _tomato_, you would create the file

`vocab/en-us/what.is.a.tomato.intent`

This file would contain examples of questions asking what a _tomato_ is.

```text
what would you say a tomato is
what is a tomato
describe a tomato
what defines a tomato
```

These sample phrases do not require punctuation like a question mark. We can also leave out contractions such as "what's", as this will be automatically expanded to "what is" by Mycroft before the utterance is parsed.

Each file should contain at least 4 examples for good modeling.

The above example allows us to map many phrases to a single intent, however often we need to extract specific data from an utterance. This might be a date, location, category, or some other `entity`.

### Defining entities

Let's now find out Mycroft's opinion on different types of tomatoes. To do this we will create a new intent file: `vocab/en-us/do.you.like.intent`

with examples of questions about mycroft's opinion about tomatoes:

```text
are you fond of tomatoes
do you like tomatoes
what are your thoughts on tomatoes
are you fond of {type} tomatoes
do you like {type} tomatoes
what are your thoughts on {type} tomatoes
```

Note the `{type}` in the above examples. These are wild-cards where matching content is forwarded to the skill's intent handler.

### Specific Entities

In the above example, `{type}` will match anything. While this makes the intent flexible, it will also match if we say something like Do you like eating tomatoes?. It would think the type of tomato is `"eating"` which doesn't make much sense. Instead, we can specify what type of things the {type} of tomato should be. We do this by defining the type entity file here:

`vocab/en-us/type.entity`

which might contain something like:

```text
red
reddish
green
greenish
yellow
yellowish
ripe
unripe
pale
```

This must be registered in the Skill before use - most commonly in the `initialize()` method:

```python
from mycroft import MycroftSkill, intent_handler

class TomatoSkill(MycroftSkill):
    def initialize(self):
        self.register_entity_file('type.entity')
```

Now, we can say things like "do you like greenish tomatoes?" and it will tag type as: `"greenish"`. However if we say "do you like eating tomatoes?" - the phrase will not match as `"eating"` is not included in our `type.entity` file.

### Number matching

Let's say you are writing an Intent to call a phone number. You can make it only match specific formats of numbers by writing out possible arrangements using `#` where a number would go. For example, with the following intent:

```text
Call {number}.
Call the phone number {number}.
```

the number.entity could be written as:

```text
+### (###) ###-####
+## (###) ###-####
+# (###) ###-####
(###) ###-####
###-####
###-###-####
###.###.####
### ### ####
##########
```

### Entities with unknown tokens

Let's say you wanted to create an intent to match places:

```text
Directions to {place}.
Navigate me to {place}.
Open maps to {place}.
Show me how to get to {place}.
How do I get to {place}?
```

This alone will work, but it will still get a high confidence with a phrase like "How do I get to the boss in my game?". We can try creating a `.entity` file with things like:

```text
New York City
#### Georgia Street
San Francisco
```

The problem is, now anything that is not specifically a mix of New York City, San Francisco, or something on Georgia Street won't match. Instead, we can specify an unknown word with :0. This would would be written as:

```text
:0 :0 City
#### :0 Street
:0 :0
```

Now, while this will still match quite a lot, it will match things like "Directions to Baldwin City" more than "How do I get to the boss in my game?"

_NOTE: Currently, the number of :0 words is not fully taken into consideration so the above might match quite liberally, but this will change in the future._

## Parentheses Expansion

Sometimes you might find yourself writing a lot of variations of the same thing. For example, to write a skill that orders food, you might write the following intent:

```text
Order some {food}.
Order some {food} from {place}.
Grab some {food}.
Grab some {food} from {place}.
```

Rather than writing out all combinations of possibilities, you can embed them into one or more lines by writing each possible option inside parentheses with \| in between each part. For example, that same intent above could be written as:

```text
(Order | Grab) some {food}
(Order | Grab) some {food} from {place}
```

or even on a single-line:

```text
(Order | Grab) some {food} (from {place} | )
```

Nested parentheses are supported to create even more complex combinations, such as the following:

```text
(Look (at | for) | Find) {object}.
```

Which would expand to:

```text
Look at {object}
Look for {object}
Find {object}
```

There is no performance benefit to using parentheses expansion. When used appropriately, this syntax can be much clearer to read. However more complex structures should be broken down into multiple lines to aid readability and reduce false utterances being included in the model. Overuse can even result in the model training timing out, rendering the Skill unusable.

## Using it in a Skill

The `intent_handler()` _decorator_ can be used to create a Padatious intent handler by passing in the filename of the `.intent` file as a string.

You may also see the `@intent_file_handler` decorator used in Skills. This has been deprecated and you can now replace any instance of this with the simpler `@intent_handler` decorator.

From our first example above, we created a file `vocab/en-us/what.is.a.tomato.intent`. To register an intent using this file we can use:

```python
@intent_handler('what.is.a.tomato.intent')
```

This _decorator_ must be imported before it is used:

```python
from mycroft import intent_handler
```

{% hint style="info" %}
[Learn more about _decorators_ in Python](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators).
{% endhint %}

Now we can create our Tomato Skill:

```python
from mycroft import MycroftSkill, intent_handler

class TomatoSkill(MycroftSkill):

    def initialize(self):
        self.register_entity_file('type.entity')

    @intent_handler('what.is.a.tomato.intent')
    def handle_what_is(self, message):
        self.speak_dialog('tomato.description')

    @intent_handler('do.you.like.intent')
    def handle_do_you_like(self, message):
        tomato_type = message.data.get('type')
        if tomato_type is not None:
            self.speak_dialog('like.tomato.type',
                              {'type': tomato_type})
        else:
            self.speak_dialog('like.tomato.generic')

    def stop(self):
        pass

def create_skill():
    return TomatoSkill()
```

{% hint style="info" %}
See a Padatious intent handler example in the [Hello World Skill](https://github.com/MycroftAI/skill-hello-world/blob/67a972792a07da7e3406bf7f94acd54aa2674829/__init__.py#L42)
{% endhint %}

## Common Problems

### I am unable to match against the utterance string

The utterance string received from the speech-to-text engine is received all lowercase. As such any string matching you are trying to do should also be converted to lowercase. For example:

```python
    @intent_handler('example.intent')
    def handle_example(self, message):
        utterance = message.data.get('utterance')
        if 'Proper Noun'.lower() in utterance:
            self.speak('Found it')
```

## Need more help?

If something isn't working as expected, please join us in the [~Skills channel of Mycroft Chat](https://chat.mycroft.ai/community/channels/skills).

It's also really helpful for us if you add an issue to our [documentation repo](https://github.com/MycroftAI/documentation/issues). This means we can make sure it gets covered for all developers in the future.

