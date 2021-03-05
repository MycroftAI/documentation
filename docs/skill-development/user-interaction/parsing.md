---
description: >-
  Mycroft provides a range of easy to use methods to parse the contents of
  utterances from Users.
---

# Parsing Utterances

## Extracting data

### Datetime

Extracts date and time information from a sentence.

See [`extract_datetime()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.util.parse.html#mycroft.util.parse.extract_datetime)

### Duration

Convert an english phrase into a number of seconds.

See [`extract_duration()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.util.parse.html#mycroft.util.parse.extract_duration)

### Numbers

[`extract_number()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.util.parse.html#mycroft.util.parse.extract_number) takes in a string and extracts a single number.

[`extract_numbers()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.util.parse.html#mycroft.util.parse.extract_numbers) takes in a string and extracts a list of numbers.

## Matching

### Vocab Matching

[`voc_match()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.html#mycroft.MycroftSkill.voc_match) determines if the given utterance contains the vocabulary provided.

### Fuzzy Matching

[`fuzzy_match()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.util.parse.html#mycroft.util.parse.fuzzy_match) performs a ‘fuzzy’ comparison between two strings.

### Match One

[`match_one()`](https://mycroft-core.readthedocs.io/en/latest/source/mycroft.util.parse.html#mycroft.util.parse.match_one) finds the best match from a list or dictionary given an input.

