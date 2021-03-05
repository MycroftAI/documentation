---
description: >-
  The Skill API offers a simple and convenient way to use other Skill's methods
  and export your own to help other Skill creators.
---

# Skill API

The Skill API uses the Mycroft Message Bus to communicate between Skills and wraps the interaction in simple Python objects making them easy to use.

## Making a method available through the Skill API

A method can be tagged with the `skill_api_method` decorator. This will handle all the basics of making the method available to other Skills over the Message Bus.

```python
    @skill_api_method
    def my_exported_method(self, my_arg, my_other_arg):
    """My skill api method documentation
    """
```

The decorator will generate everything needed for accessing the method over the Message Bus and extract the associated docstring.

### Limitations

The Skill API works over the Message Bus. This requires that the return values are json serializable. All common Python builtin types \(such as List, String, None, etc.\) work well, however custom classes are not currently supported.

### Example

```python
from mycroft.skills import MycroftSkill, skill_api_method

class RobberSkill(MycroftSkill):
    @skill_api_method
    def robber_lang(self, sentence):
        """Encode a sentence to "Rövarspråket".

        Each consonant gets converted to consonant + "o" + consonant,
        vowels are left as is.

        Returns: (str) sentence in the robber language.
        """
        wovels = "aeiouyåäö"
        tokens = []
        for char in sentence.lower() and char.isalpha():
            if char not in wovels:
                tokens.append(char + 'o' + char)
            else:
                tokens.append(char)
        return ' '.join(tokens)


def create_skill():
    return RobberSkill()
```

## Using another Skill's API

If you want to make use of exported functionality from another Skill, you must fetch that Skill's `SkillApi`. This will give you a small class with the target Skill's exported methods. These methods are nothing special and can be called like any other class's methods.

To access the `robber_lang()` method we created above, we could write:

```python
from mycroft.skills.api import SkillApi

class NewRobberSkill(MycroftSkill):
    def initialize(self):
        self.robber = SkillApi.get('robber-skill.forslund')
        self.speak(self.robber.robber_lang('hello world'))


def create_skill():
    return NewRobberSkill()
```

When the `NewRobberSkill` is initialized, it will assign the API from the Skill `robber-skill.forslund` to `self.robber`. We then run the exported method `robber_lang()` passing the argument `'hello world'`.

Our `NewRobberSkill` will therefore speak something like "hoh e lol lol o wow o ror lol dod".

## Getting information on a Skill's exported API

The Mycroft CLI has an `:api` command for exploring Skill APIs.

```text
:api robber-lang.forslund
```

will show any exported method from the `robber-lang.forslund` Skill. Each exported method's docstring will automatically be extracted and presented, providing information on how each method is intended to be used.

