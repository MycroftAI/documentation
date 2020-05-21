---
description: >-
  Use a Behavior Driven approach and write tests in a natural language style
  before any development begins. This improves communication within your team,
  and sets your Skill up for success.
---

# Design to Development

## Creating Behave Test files based on your Design

For Skills to enter our official Marketplace they need to be testable. We use a Behavior Driven approach and write tests in a natural language style before any development begins. After the skill is developed the Behave tests will need to be updated with the appropriate Dialog files, and in many cases Steps will need to be created to incorporate the tests.

Small portion of an example Feature file:

```text
Feature: mycroft-moon-phase

  Scenario Outline: The user asks for the current moon phase
    Given an english speaking user
      When the user asks for "<the current moon phase>"
      Then "skill-moon-phase" should reply with "Today’s moon is Waning Crescent with 55% illumination"

   Examples:
     | the current moon phase |
     | what’s the moon phase |
     | what's the phase of the moon |
     | what is the moon phase today |
```

