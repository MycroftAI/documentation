---
description: How to make use the Skill API
---
# Skill API

The skill api offers a simple and convenient way to use other skill's methods and export your own to help other skill creators. The skill api uses the Mycroft messagebus to communicate between skills but wrapping the interaction in simple python objects making them easy to use.

## Making a method available through the Sill API

A method can be tagged with the `skill_api_method` decorator. This will handle all the basics of making the method available to other skills over the messagebus.

```python
    @skill_api_method
    def my_exported_method(self, my_arg, my_other_arg):
    """My skill api method documentation
    """
```

The decorator will generate everything needed for accessing the method over the messagebus and extract ant associated docstring.

### Limitations

The skill API works over the messagebus, this requires that the return values are json serializable. This makes works well for the common builtin types in python (list, string, None, etc.) but custom classes will not work out of the box currently.

### Example

```python
from mycroft.skills import MycroftSkill
from mycroft.skills.mycroft_skill.decorators import skill_api_method

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

## Using a skill's API

If you want to make use of exported functionallity from another skill you must fetch that skill's skill api. This will give you a small class with the target skill's exported methods. These methods are nothing special and can be called like any other class's methods.

```python
from mycroft.skills.api import SkillApi

[...]

        api = SkillApi.get('mycroft-skillid.mycroftai')
        result = api.exported_method('fraggle')

```

The snippet above will get the API from the skill mycroft-skillid.mycroftai and run the exported method `exported_method()` passing the argument `'fraggle'`

And for using the `RobberLang` skill above something like

```python
        robber = SkillApi.get('robber-skill.forslund')
        self.speak(self.robber.robber_lang('hello world'))
```

Will speak something like "hoh e lol lol o wow o ror lol dod".


## Getting information on skill's exported api

The Mycroft CLI has an `:api` command for exploring skill APIs.

```
:api robber-lang.forslund
```

will show any exported method from the robber-lang skill. Each exported method's docstring will automatically be extracted and presented, providing information on how each method is intended to be used.
