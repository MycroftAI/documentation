---
description: >-
  One of the simplest, yet most useful features of Voight Kampff is the ability
  to provide a list of examples that will all be tested within one Scenario.
---

# Scenario Outlines

We can do this using Scenario Outlines. Think of these as a template that we setup and can then feed data into to run multiple tests.

Let's revisit the example from the [previous page](https://github.com/MycroftAI/documentation/tree/384c23ed6db63685b60d97645b47e1ff882cefba/docs/skill-development/introduction.md).

```yaml
Feature: current-weather
  Scenario: current local weather
    Given an English speaking user
     When the user says "tell me the weather"
     Then "my-weather-skill" should reply with "Right now, it's overcast clouds and 32 degrees."
```

In this Scenario, when the user says "tell me weather", then our Weather Skill should reply with an appropriate dialog. However we know that there are many ways to ask about the weather. Rather than copy and pasting this Scenario for each utterance, we can instead use a `Scenario Outline`.

```yaml
Feature: current-weather
  Scenario Outline: current local weather
    Given an english speaking user
     When the user says "<current local weather>"
     Then "mycroft-weather" should reply with "Right now, it's overcast clouds and 32 degrees."

   Examples: local weather questions  # Table heading
        | current local weather   |   # Column heading
        | tell me the weather     |   # First value
        | what's the weather like |   # Second value
        | current weather         |   # Third value
```

The most obvious change is the new block of `Examples`. This is a table of data that we want to use in our Scenario. We give that table a title "local weather questions", and for each column in the table we provide a column heading "current local weather", followed by one or more values.

To use this data, we must first explicitly change from using a `Scenario` to using a `Scenario Outline`. We are then able to use the `Examples` data in our Steps by including the Column Heading surrounding by angle brackets. In this case we have added `<current local weather>` to the `When` Step on line 4.

Running the above Scenario Outline will test three versions of this Scenario - "tell me the weather", "what's the weather like", and "current weather". It is important to note that "current local weather" is a heading, not a value, and it will not be tested.

## Multiple dependent variables

So far we have only used the Scenario Outline to take in a list of utterances. The same format can be used with tables of data.

```yaml
Feature: Pokemon abilities
  Scenario Outline: list abilities
    Given an english speaking user
     When the user says "What abilities does <Name> have"
     Then "pokemon.retrodaredevil" should reply with "<Name> has <Abilities>"

   Examples: Pokemon data                          # Table heading
        | Name       | Abilities                |  # Column heading
        | Bulbasaur  | chlorophyll and overgrow |  # First value
        | Charmander | solar-power and blaze    |  # Second value
        | Squirtle   | rain-dish and torrent    |  # Third value
```

In our new `Examples` block, you can see we have expanded this into a two-column table containing the names of some Pokemon and the abilities they have. Using this data we have done two things.

1. With the Pokemon `Name`, we have used this in both the question and the response.
2. The Abilities that are reported back are directly related to the Name from the same table row. If a user was to say "What abilities does Bulbasaur have", and Mycroft replied with "Bulbasaur has solar-power and blaze", then the Scenario would be considered a fail.

