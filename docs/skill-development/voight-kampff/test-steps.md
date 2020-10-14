---
description: >-
  Steps define the details of our tests using a Behavior Driven Development
  framework.
---

# Test Steps

In our introduction to integration testing we looked at a simple example based on a custom Weather Skill. A Skill could be well tested using only that simple structure, however there are many more options available.

Here we outline the Steps available in the base implementation. We are actively looking for suggestions for other Steps to include. You can also write your own custom Steps for your Skill.

## Given Steps

`Given` Steps define the state of the Scenario.

### Set language

`Given an english speaking user`

You can set the language of a test using its common name.

## When Steps

`When` Steps describe actions that are taken.

### User says something

`When the user says "some utterance"`

## Then Steps

`Then` Steps observe the outcome of the test.

### Spoken Response

#### Reply with dialog file

`Then "my-skill" should reply with dialog from "my.dialog.file"`

```yaml
Feature: current-weather
  Scenario: Temperature in paris
    Given an english speaking user
     When the user says "how hot will it be in paris"
     Then "mycroft-weather" should reply with dialog from "current.high.temperature.dialog"
```

#### Reply with example phrase

`Then "my-skill" should reply with "an example dialog response"` The response dialog given is one possible response to the utterance.

```yaml
Feature: current-weather
  Scenario: current local weather
    Given an English speaking user
     When the user says "tell me the weather"
     Then "my-weather-skill" should reply with "Right now, it's overcast clouds and 32 degrees."
```

Many Skills provide multiple possible responses to the same query by adding additional responses to the dialog file. The Voight Kampff test framework has been designed to handle this situation. The test will be successful if the both the intended and actual responses are contained within the same dialog file, even if they do not match directly.

#### Reply with exact dialog

`Then "my-skill" should reply with exactly "some response"` Test that the dialog spoken in response, exactly matches a string of text.

```yaml
Feature: current-weather
  Scenario: current local weather
    Given an English speaking user
     When the user says "is it hot in Darwin, Australia"
     Then "my-weather-skill" should reply with exactly "yeah mate"
```

#### Reply with anything

`Then "my-skill" should reply with anything` Test only that a specific Skill handles the response, and that any dialog was spoken in response.

```yaml
Feature: current-weather
  Scenario: current local weather
    Given an English speaking user
     When the user says "tell me the weather"
     Then "my-weather-skill" should reply with anything
```

#### Reply should contain

`Then mycroft reply should contain "something"` Test that the response includes some string of text.

```yaml
Feature: current-weather
  Scenario: Temperature in paris
    Given an english speaking user
     When the user says "how hot will it be in paris"
     Then mycroft reply should contain "Paris"
```

### Message Type sent

`Then mycroft should send the message "{message_type}"`

Tests that a particular [Message Type](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/message-types) was emitted to the [MessageBus](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/message-bus).

### Setting a configuration

`Given the user's {config} is {value}`

The test can specify a certain configuration using a Given Step and a configuration specification.

```text
  Given an english speaking user
  And the user's unit system is metric
  When the user says "how tall is the eiffel tower"
  Then mycroft reply should contain "meters"
```

#### Configuration specification

The configuration and values are setup in a json file in the test/behave folder of the skill, named as the feature file but with the extension `.config.json` so if the feature file is `myskill.feature` the config specification file should be called `myskill.config.json`.

The file is organized in a config name -&gt; config value name -&gt; config patch structure.

```javascript
{
    "config": {
        "value": PATCH
    }
}
```

The `config` and `value` keys from this JSON object can then be inserted in the Given Step. The Mycroft configuration will then be patched with the contents of `PATCH`.

Let's look at a real life example file with the configs "unit system" and "location"

```javascript
{
  "unit system": {
    "metric": {"system_unit": "metric"},
    "imperial": {"system_unit": "imperial"}
  },
  "location": {
    "stockholm": {
      "location": {
        "city": {
          "name": "Stockholm",
          "state": {
            "code": "SE.18",
            "country": {
              "code": "SE",
              "name": "Sweden"
            },
            "name": "Stockholm"
          }
        },
        "coordinate": {
          "latitude": 59.38306,
          "longitude": 16.66667
        },
        "timezone": {
          "code": "Europe/Stockholm",
          "dst_offset": 7200000,
          "name": "Europe/Stockholm",
          "offset": 3600000
        }
      }
    }
  }
}
```

In the above example the "unit system" patches a single key and has two simple variations, `metric` or `imperial`. This is used in the test example above. Using this configuration specification, the `location` could also be set to `stockholm` patching the config with the entire object structure needed by Mycroft.

If no file config specification is found in the Skill, a common config specification is included with mycroft-core in the file `mycroft/res/{lang}/configurations.json` containing some commonly used configuration options.

## And, But

You can include several Steps of the same type in a single Scenario. For example:

```yaml
Feature: current-weather
  Scenario: Temperature in paris
    Given an english speaking user
    Given user is located in Paris
     When the user says "how hot will it be today"
     Then "mycroft-weather" should reply with dialog from "current.high.temperature.dialog"
     Then mycroft reply should contain "Paris"
```

To make this easier to read, you can instead use the terms `And` or `But`

```yaml
Feature: current-weather
  Scenario: Temperature in paris
    Given an english speaking user
      And user is located in Paris
     When the user says "how hot will it be today"
     Then "mycroft-weather" should reply with dialog from "current.high.temperature.dialog"
      But mycroft reply should contain "Paris"
```

The two terms are exactly the same, they both operate as the Step that comes immediately before them.

## Adding custom Steps

Some Skills require their own unique Steps to test functionality specific to that Skill. These can be added to your Skills repository under the `test/behave/steps` directory. For more detail see:

{% page-ref page="custom-steps.md" %}

