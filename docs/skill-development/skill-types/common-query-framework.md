---
description: >-
  To support a range of Skills that can answer user's queries, each Common 
  Query Skill must return a confidence score to indicate their ability to
  successfully complete the users request.
---

# Common Query Framework

## Introduction

The Common Query Framework handles the common use case of "general information" or question answering. Many Skills may implement handlers for "what is X" or "when did Y", the Common Query Framework allows all these Skills be queried and a single "best" answer to be selected. This is similar to the Common Play Framework that handles the common use of "playing" music or other media.

The Common Query Skill System is led by the [Query Fallback Skill](https://github.com/MycroftAI/skill-query). This Skill handles queries matching a question pattern such as "What is the height of the Eiffle Tower" and "When is lunch". A matched question will be sent to all Skills based upon the `CommonQuerySkill` base class. The Skills will return wether they can answer the query along with an answer when applicable. The "best" match will be selected and spoken to the user.

## CommonQuerySkill

A Skill interfacing with the Common Query Framework inherits from the the `CommonQuerySkill` and needs to define a method `CQS_match_query_phrase()` taking an utterance as argument.

The general structure is:

```python
from mycroft.skills.common_query_skill import CommonQuerySkill, CQSMatchLevel

class MyCommonQuerySkill(CommonQuerySkill):
    def CQS_match_query_phrase(self, utt):
       # Parsing implementation
       # [...]
       return (utt, CQSMatchLevel.LEVEL, answer_string)

def create_skill():
    return MyCommonQuerySkill()
```

The `CQS_match_query_phrase()` method will parse the utterance and determine if it can handle the query. if it can't answer it will return `None` and if it _can_ answer it will return a data tuple with the format

```python
((str)Input Query, CQSMatchLevel, (str)Answer Text)
```

The input query is returned to map the query to the answer.

`CQSMatchLevel` is an Enum with the possible values

* `CQSMatchLevel.EXACT`: The Skill is very confident that it has the precise answer the user is looking for. There was a category match and a known entity is referenced.
* `CQSMatchLevel.CATEGORY`: The Skill could determine that the type of question matches a category that the Skill is good at finding.
* `CQSMatchLevel.GENERAL`: This Skill tries to answer all questions and found an answer.

There is also a directly equivalent `CQSVisualMatchLevel`  that provides a small confidence bonus on platforms that can display visual media. The intention being that if two answers are otherwise equal, if a device can also display an image, then the response with an image is preferred. `CQSVisualMatchLevel` is an exact copy of `CQSMatchLevel` and requires no other changes to use.

To actual show the visuals, see the [`CQS_action()` method](common-query-framework.md#cqs\_action) below.

## An Example

Let's make a simple Skill that tells us the age of the various Monty Python members. A quick draft looks like this. (You can find the complete code [here](https://github.com/forslund/common-query-tutorial))

```python
from mycroft.skills.common_query_skill import CommonQuerySkill, CQSMatchLevel



# Dict mapping python members to their age and whether they're alive or dead     
PYTHONS = {
    'eric idle': (77,'alive'),
    'michael palin': (77, 'alive'),
    'john cleese': (80, 'alive'),
    'graham chapman': (48, 'dead'),
    'terry gilliam': (79, 'alive'),
    'terry jones': (77, 'dead')
}


def python_in_utt(utterance):
    """Find a monty python member in the utterance.
    Arguments:
        utterance (str): Sentence to check for Monty Python members
    Returns:
        (str) name of Monty Python member or None
    """
    for key in PYTHONS:
        if key in utterance.lower():
            # Return the found python
            return key

    # No python found
    return None


class PythonAgeSkill(CommonQuerySkill):
    """A Skill for checking the age of the python crew."""

    def format_answer(self, python):
        """Create string with answer for the specified "python" person."""
        age, status = PYTHONS[python]
        if status == 'alive':
            return self.dialog_renderer.render('age_alive',
                                               {'person': python, 'age': age})
        else:
            return self.dialog_renderer.render('age_dead',
                                               {'person': python, 'age': age})

    def CQS_match_query_phrase(self, utt):
        """Check the utterance if it is a question we can answer.

        Arguments:
            utt: The question

        Returns: tuple (input utterance, match level, response sentence, extra)
        """
        # Check if this is an age query
        age_query = self.voc_match(utt, 'age')

        # Check if a monty python member is mentioned
        python = full_python_in_utt(utt)

        # If this is an age query and a monty python member is mentioned the
        # skill can answer this
        if age_query and python:
            # return high confidence
            return (utt, CQSMatchLevel.CATEGORY, self.format_answer(python))
        else:
            return None


def create_skill():
    return PythonAgeSkill()
```

As seen above the `CQS_match_query_phrase()` checks if this is an age related utterance and if the utterance contains the name of a Monty Python member. If both criteria are met it returns a match with a `CQSMatchLevel.CATEGORY` confidence together with a rendered dialog containing the answer.

If both criteria are not fulfilled the method will return `None` indicating that it can't answer the query.

This will be able to provide answers to queries such as

> "how old is Graham Chapman"
>
> "what's Eric Idle's age"

To make this more exact we can add support for checking for the words "monty python", and if present return the highest confidence.

The method for parsing the example is quite simplistic but there are many different toolkits out there for doing the question parsing. [Adapt](https://pypi.org/project/adapt-parser/), [little questions](https://pypi.org/project/little-questions/), [padaos](https://pypi.org/project/padaos/) and many more!

## Better matching

If we want to make sure this Skill is used when the user explicitly states it's the age of a Monty Python member, a slight modification to the Skill can be made:

We'll change the end of the `CQS_match_query_phrase()` method to

```python
            if 'monty python' in utt.lower():
                confidence = CQSMatchLevel.EXACT
            else:
                confidence = CQSMatchLevel.CATEGORY
            # return high confidence
            return (utt, confidence, self.format_answer(python))
```

So if the utterance contains the phrase "monty python" the confidence will be set to `CQSMatchLevel.EXACT` making the Skill very very likely to be chosen to answer the query.

## CQS\_action()

In some cases the Skill should do additional operations when selected as the best match. It could be prepared for follow-up questions or show an image on the screen. The `CQS_action()` method allows for this, when a Skill is selected this method will be called.

The full signature is

```python
    def CQS_action(self, utt, data):
```

where `phrase` is the same phrase that were sent to `CQS_match_query_phrase()` and `data` is optional additional data from the query matching method.

### Example

Let's make our Python Age Skill gloat that it was selected by adding a `CQS_action()` method like this:

```python
    def CQS_action(self, utt, data):
        self.log.info('I got selected! What you say about that Wolfram Alpha Skill!?!?')
```

Now each time the Skill is called the above message will be added to the log! Not very useful you say? Hmm, yes... let's add something useful, like show the age on the Mark-1 display.

To accomplish this we need to get the age into the `CQS_action()` method in some way. we could store last age in as an internal variable but the more elegant way is to send data as part of the match tuple. To do this we must extend the returned match tuple from `CQS_match_query_phrase()` with a data entry. So the return statement becomes

```python
            data = {'age': PYTHONS[python], 'python': python}
            return (utt, confidence, self.format_answer(python), data)
```

The data structure declared here will be sent to the `CQS_Action()`method and we can update the method to

```python
    def CQS_action(self, utt, data):
        self.log.info('I got selected! What you say about that Wolfram Alpha Skill!?!?')
        age = data.get('age')
        if age:
            self.log.info('Showing the age {}'.format(age))
            self.enclosure.mouth_text(str(age))
```
