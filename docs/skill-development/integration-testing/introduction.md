---
description: >-
  Ensure your Skill works as expected when it is running inside Mycroft along
  with all the default Skills.
---

# Integration Testing

Mycroft has recently adopted a new [Behavior Driven Development (BDD)](https://en.wikipedia.org/wiki/Behavior_Driven_Development) framework called [Behave](https://behave.readthedocs.io/) for integration testing. Mycroft's implementation has been code-named Voight Kampff.

## Why have integration tests
Writing tests for your Skill has benefits for both you and Mycroft as a whole. For the project it allows us to automatically check that the Skill is working as intended, and that no other Skill is causing a conflict.

Test-driven development also allows you to work more efficiently and find bugs faster.


## Test Format
Behave tests are split into `Features`. Each `Feature` may have one or more `Scenarios`, and each `Scenario` will have multiple `Steps`.

To see it in action let's look at a short example for a Weather Skill.

```YAML
Feature: current-weather
  Scenario: current local weather
    Given an English speaking user
     When the user says "tell me the weather"
     Then "my-weather-skill" should reply with "Right now, it's overcast clouds and 32 degrees."
```

In this example, we started by defining the name of the Feature, in this case "current-weather", then added a single Scenario "current local weather". Within this Scenario we have three Steps:
* `Given` steps define the state of the Scenario,
* `When` steps describe actions that are taken, and
* `Then` steps observe the outcome of the test.

When this specific test is run with the provided Steps, the system will:
1. Ensure that it is in the appropriate state awaiting an utterance in English.
2. Send the given utterance to Mycroft as if it had been spoken by a user.
3. Observe Mycroft's response and check that the correct Skill responded with appropriate dialog.

### File location
Each `Feature` we define for our Skills test suite should be placed in it's own file inside the `test/behave` directory of our Skill. For this example we will save the Feature file in:
```
/opt/mycroft/skills/my-weather-skill/test/behave/current-weather.feature`
```
