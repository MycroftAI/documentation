---
description: A statement is any information spoken by Mycroft to the User.
---

# Statements

## Speaking a statement

One of Mycroft's most important core capabilities is to convert text to speech, that is, to speak a statement.

Within a Skill's Intent handler, you may pass a string of text to Mycroft and Mycroft will speak it.  For example: [`self.speak('this is my statement')`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.speak)   That's cool and fun to experiment with, but passing strings of text to Mycroft doesn't help to make Mycroft a multilingual product. Rather than hard-coded strings of text, Mycroft has a design pattern for multilingualism.

### Multilingualism

To support multilingualism, the text that Mycroft speaks must come from a file. That file is called a dialog file. The dialog file contains statements \(lines of text\) that a listener in a particular language would consider to be equivalent.  For instance, in USA English, the statements "I am okay" and "I am fine" are equivalent, and both of these statements might appear in a dialog file used for responding to the USA English question: "How are you?".

By convention, the dialog filename is formed by _dot connected_ _words_ and must end with ".dialog".  The dialog filename should be descriptive of the contents as a whole.  Sometimes, the filename describes the question being answered, and other times, the filename describes the answer itself.  For the example above, the dialog filename might be: **how.are.you.dialog** or **i.am.fine.dialog**.

Multilingualism is accomplished by translating the dialog files into other languages, and storing them in their own directory named for the country and language. The filenames remain the same.  Using the same filenames in separate language dependent directories allows the Skills to be language agnostic; no hard-coded text strings.  Adjust the language setting for your **Device** and Mycroft uses the corresponding set of dialog files.  If the desired file does not exist in the directory for that language, Mycroft will use the file from the USA English directory.

As an example of the concept, the contents of how.are.you.dialog in the directory for the French language in France \(fr-fr\) might include the statement: "Je vais bien".

### The Ice Cream Skill

The following mini-tutorial demonstrates multilingualism using the [`speak_dialog()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.speak_dialog) method.  The sample refers to an imaginary Ice Cream Skill that handles inquires about Mycroft's interest in ice cream. Mycroft likes ice cream, all kinds.

You are encouraged to experiment with this code. You can do so by creating a new Skill or you might find it easier to edit an existing skill, such as Hello World.

Note: This Ice Cream Skill is similar to the Tomato Skill in [Padatious Intents](intents/padatious-intents.md).  Please refer to that section for more details on creating Padatious Intents.

### Part 1 - Simple Statement

When you design a Skill, it is suggested that you begin by defining **scenarios** of expected behavior. Satisfying the needs of the scenarios will guide the creation of Intents within the Skill.  Sometimes, more than one Intent is needed to handle the expected behavior of a scenario.  Other times, one Intent can handle more than one scenario.

#### The scenario in words

When asked if Mycroft likes ice cream, Mycroft shall answer in the affirmative

#### The scenario as a feature file

The Mycroft community uses a **feature** file to express scenarios.  The feature files are involved in the automated testing of Mycroft.  A new Skill cannot be made available in the Marketplace unless it works cooperatively with all of the other Skills. The automated testing confirms not only that your new Skill performs as expected, but that it does so while not interfering with the other Skills.

```text
	Feature: Mycroft and Ice Cream
	  Scenario: Mycroft likes ice cream
		Given an English speaking user
		  When the User says "do you like ice cream"
		  Then "ice-cream-skill" should reply with "I do like ice cream"
```

Notice the similarity with the scenario described in words above.  We are not going to write a feature file or use the testing mechanism for this sample.  

#### Design the Intent

You can imagine many _ways_ to answer in the affirmative. Each of those _ways_ is a statement. And, since they all mean the same thing, they can all exist in the same dialog file. Our descriptive filename for this dialog file shall be **i.do.like.dialog**.  Initially, let this dialog file have just one, simple, straightforward statement: "I do like ice cream"

Now, consider the User **utterance**: "Do you like ice cream?" That phrase is very specific, with limited alternatives, maybe: "What do you think of ice cream?" or "Do you love ice cream?".  These **utterances** do not lend itself to keyword detection, but rather to whole phrase detection.  Whole phrase detection is best accomplished with a Padatious Intent.  Also, the Padatious Intent makes it easy to extract a portion of the **utterance** as needed in Part 2.  Our descriptive name for the Padatious Intent file shall be: **do.you.like.intent**

Start the experiment with these two files, each with just one line:

{% tabs %}
{% tab title="do.you.like.intent" %}
```python
Do you like ice cream
```
{% endtab %}

{% tab title="i.do.like.dialog" %}
```python
I do like ice cream
```
{% endtab %}
{% endtabs %}

The Skill code is:

```python
from mycroft import MycroftSkill, intent_handler

class IceCreamSkill(MycroftSkill):

    @intent_handler('do.you.like.intent')
    def handle_do_you_like(self, message):
        """Speaks a statement from the dialog file."""
        self.speak_dialog('i.do.like')
        
def create_skill():
    return IceCreamSkill()
```

After installation of the Ice Cream Skill, Mycroft is listening for the **utterance** "Do you like ice cream" as specified in the Intent file.  When the User says "Hey Mycroft, do you like ice cream?", the Intent handler method `handle_do_you_like()` will be called.

Inside `handle_do_you_like()`, we find: `self.speak_dialog('i.do.like')`  

As you can probably guess, the parameter `'i.do.like'` is the dialog filename without the ".dialog". Calling this method opens the dialog file, selects one of the statements, and converts that text to speech. Mycroft will speak a statement from the dialog file.  In this example, Mycroft will say "I do like ice cream".  Remember, Mycroft has a language setting that determines from which directory to find the dialog file.

#### File locations

The [Skill Structure](../skill-structure/) section describes where to place the Intent file and dialog file.  Basically, there are two choices:

1. Put both files in `locale/en-us`
2. Put the dialog file in `dialog/en-us` , and put the Intent file in `vocab/en-us`

#### Make Mycroft less robotic

Having more than one statement in the dialog file provides some variability in Mycroft's responses. Hopefully, this makes Mycroft seem less robotic. Mycroft is allowed to randomly speak any one of the statements from the dialog file.

Let's extend our `i.do.like.dialog` file to include a variation:

```python
I do like ice cream
Yes, I love ice cream
```

Now, Mycroft will sometimes reply with "I do like ice cream", and other times with "Yes, I love ice cream".  Try it.

### Part 2 - Adding variables

Let's make the scenario more interesting by anticipating that the User might ask if Mycroft likes a specific flavor of ice cream. And, let's also expect for Mycroft to give a more complete answer by including the User specified flavor. Towards that end, let's allow for a flavor word or words just before "ice cream" in the **utterance**, and have those flavor word\(s\) inserted in Mycroft's statement.

```text
Feature: Mycroft and Ice Cream
	  Scenario: Mycroft likes ice cream
		Given an English speaking user
		  When the User says "do you like CHOCOLATE ice cream"
		  Then "ice-cream-skill" should reply with "I do like CHOCOLATE ice cream"
		
Note: Above, CHOCOLATE, represents any word or words, i.e. the flavor
```

{% hint style="info" %}
If the _flavor words_ are actually a flavor of ice cream this works fine, but if not, then it may produce funny results. "Hey Mycroft, do you like _sitting on_ ice cream?"   Mycroft will obediently respond with "I do like _sitting on_ ice cream." There are ways to limit this hilarious behavior, but that is not the subject of this example. Please see [Padatious Intents](intents/padatious-intents.md) for more details.
{% endhint %}

To implement this scenario, first, modify the Intent file so that it expects and extracts the _flavor_ word or words between "do you like" and "ice cream". Edit the **do.you.like.intent** file to include a variable name surrounded by curly braces:

```text
Do you like ({asked_flavor}|) ice cream
```

This example also demonstrates Parentheses Expansion.  The parentheses surround options for the parsing of the **utterance.**  Options are separated by the vertical line character '\|'.  Each option expands to its own line of text.  The option on the right is blank which results in the original line "do you like ice cream". 

The option of the left introduces a variable named **asked\_flavor**, and results in the line: "do you like {asked\_flavor} ice cream".  This line causes Mycroft to take the word or words found between "do you like" and "ice cream", and return them to the Intent handler assigned to a variable named **asked\_flavor**.

{% hint style="info" %}
For multi-line Intent files, be sure to include the **same** variable on **all** lines.  
In Mycroft parlance, the curly braces are also known as a _mustache_.
{% endhint %}

Second, modify the dialog file to indicate where the handler shall insert the _flavor_ text. Edit the dialog lines to include a variable name surrounded by curly braces at the desired insertion points.

```python
I do like {flavor} ice cream
Yes, I love {flavor} ice cream
```

{% hint style="info" %}
For multi-line dialog files, be sure to include the **same** variable on **all** lines.
{% endhint %}

Third, modify the Intent handler to acquire the asked\_flavor variable. Variables and their values are passed to the Intent inside the data dictionary in the message. The next line illustrates how to extract the value for **asked\_flavor** from the dictionary:

```python
asked_flavor = message.data.get('asked_flavor', '')
```

If the User did not utter any words between "do you like" and "ice cream", then there will not be a value for **asked\_flavor** in the dictionary. The code snippet above handles that situation by setting the variable to an empty string when **asked\_flavor** is not in the dictionary.

Finally, pass the value from the **asked\_flavor** variable to the dialog via the data dictionary parameter. Assign the value to the variable name used in the dialog file:

```python
self.speak_dialog(i.do.like, data={'flavor':asked_flavor})
```

Now, the code looks like this:

```python
from mycroft import MycroftSkill, intent_handler

class IceCreamSkill(MycroftSkill):

    @intent_handler("do.you.like.intent")
    def handle_do_you_like(self, message):
        """Speaks a statement from the dialog file, inserting the
           asked for flavor into the statement ."""
        asked_flavor = message.data.get('asked_flavor', '')
        self.speak_dialog('i.do.like', data={"flavor": asked_flavor})
        
def create_skill():
    return IceCreamSkill()
```

Try it.

> Hey Mycroft, do you like strawberry ice cream?

#### Accepting more variation from the User

To give more flexibility in what the User utters, add some equivalent alternatives to the Intent file:

```text
Do you like ({asked_flavor}|) ice cream
Do you love ({asked_flavor}|) ice cream
What do you think of ({asked_flavor}|) ice cream
```

Give it a try.

## Waiting for speech

By default, the `speak_dialog()` method is non-blocking. That is any code following the call to `speak_dialog()` will execute whilst Mycroft is talking. This is useful to allow your Skill to perform actions while it is speaking. 

Rather than telling the User that we are fetching some data, then going out to fetch it, we can do the two things simultaneously providing a better experience. 

However there are times when we need to wait until the statement has been spoken before doing something else. We have two options for this.

### Wait Parameter

We can pass a `wait=True` parameter to our `speak_dialog()` method. This makes the method blocking and no other code will execute until the statement has been spoken.

```python
from mycroft import MycroftSkill, intent_handler

class IceCreamSkill(MycroftSkill):

    @intent_handler("do.you.like.intent")
    def handle_do_you_like(self, message):
        """Speaks a statement from the dialog file, inserting the
           asked for flavor into the statement ."""
        asked_flavor = message.data.get('asked_flavor', '')
        self.speak_dialog("i.do.like", 
                          data={"flavor": asked_flavor},
                          wait=True)
        self.log.info("I waited for you")
        
def create_skill():
    return IceCreamSkill()     
```

### wait\_while\_speaking

The [`mycroft.audio.wait_while_speaking()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.audio.html#mycroft.audio.wait_while_speaking) method allows us to execute some code, then wait for Mycroft to finish speaking.

```python
from mycroft import MycroftSkill, intent_handler
from mycroft.audio import wait_while_speaking

class IceCreamSkill(MycroftSkill):

    @intent_handler("do.you.like.intent")
    def handle_do_you_like(self, message):
        """Speaks a statement from the dialog file, inserting the
           asked for flavor into the statement ."""
        asked_flavor = message.data.get('asked_flavor', '')
        self.speak_dialog("i.do.like", 
                          data={"flavor": asked_flavor})
        self.log.info("I am executed immediately")
        wait_while_speaking()
        self.log.info("But I waited for you")
        
def create_skill():
    return IceCreamSkill()
```

Here we have executed one line of code immediately. Our Skill will then wait for the `i.do.like.dialog` to be spoken before executing the final line of code.

## Using translatable resources

There may be a situation where the dialog file and the `speak_dialog()` method do not give the Skill enough flexibility. For instance, there may be a need to manipulate the statement from the dialog file before having it spoken by Mycroft.

The Mycroft Skill class provides four multilingual methods to address these needs.  Each method uses a file, and multilingualism is accomplished using the country/language directory system.

The [`translate()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.translate) method returns a random string from a ".dialog" file \(modified by a data dictionary\).  

The [`translate_list()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.translate_list) method returns a list of strings from a ".list" file \(each modified by the data dictionary\). Same as translate\_template\(\) just with a different file extension.

The [`translate_namedvalue()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.translate_namedvalue) method returns a dictionary formed from CSV entries in a ".value" file.

The [`translate_template()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.translate_template) method returns a list of strings from a ".template" file \(each modified by the data dictionary\). Same as translate\_list\(\) just with a different file extension.

