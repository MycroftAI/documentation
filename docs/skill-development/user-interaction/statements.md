---
description: >-
  A statement is any information spoken by Mycroft to the User.
---

# Statements

See the [`speak_dialog()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.speak_dialog) method.

## Using translatable resources

To enable your Skill in multiple languages we strongly encourage Skill authors not to hard-code strings of text into your Skill. Strings should instead be constructed using translatable resources contained within the `dialog` or `locale` directories of your Skill.

See the available [`translate_*`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.translate) methods for more details.