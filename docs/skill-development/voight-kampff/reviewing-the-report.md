# Reviewing the Report

## Test Output

The details of each test scenario is printed to the terminal \(stdout\) as it is run, and at the end of our test a summary is printed.

```text
Failing scenarios:
  features/hello-world.feature:3  Hello world

1 feature passed, 1 failed, 0 skipped
8 scenarios passed, 1 failed, 0 skipped
26 steps passed, 1 failed, 0 skipped, 0 undefined
Took 0m14.191s
```

In this example we can see that a scenario called "Hello world" from the `hello-world.feature` file failed. It also points us to the line number where this scenario is defined in that file - line 3.

The summary also outlines how many features, scenarios and steps have passed, failed or been skipped. Followed by the duration of how long all of the tests took to run.

Let's now go take a look at that failing test.

## Failing tests

If a scenario fails, the failing `Then` statement will be highlighted in red, and a detailed description of the failure is provided. By default, the test runner will automatically retry the failing scenario a second time before moving on.

```bash
2020-03-20 19:11:14,392 | Voight Kampff | INFO | Starting tests for mycroft-hello-world
Feature: mycroft-hello-world # features/hello-world.feature:1

  Scenario: Hello world                                            # features/hello-world.feature:3
    Given an english speaking user                                 # features/steps/utterance_responses.py:108 0.001s
    When the user says "Hello world"                               # features/steps/utterance_responses.py:113 0.001s
    Then "mycroft-hello-world" should reply with "I'm doing very well" # features/steps/utterance_responses.py:137 10.019s
      Assertion Failed: Mycroft responded with: mycroft-hello-world by mycroftai
      Mycroft: hello.world.dialog(HelloWorldSkill)
      "Hi to you too"

      Captured stdout:
      Matching with the dialog file: how.are.you.dialog

      Captured logging:
      INFO:msm.mycroft_skills_manager:Best match (1.0): mycroft-hello-world by mycroftai
```

The example output above shows a test that has failed. The line containing the `Then` statement would be highlighted in red, and it has provided a description of the error. In this case Mycroft responded with "Hi to you too" which is in the `hello.world.dialog` file in the `mycroft-hello-world` Skill. It then indicates that the response string provided in the test "I'm doing very well" was actually found in the `how.are.you.dialog` file.

Looks like we have an error in our test. Mycroft should respond to "Hello World" with "Hi to you too" or another phrase from `hello.world.dialog`.

## Allure Reporting Framework

The test results are also written to JSON files that can be used with [Allure](http://allure.qatools.ru/), an open source test reporting framework.

## Help

For further assistance with Skill testing, please post your question on the [Community Forums](https://community.mycroft.ai/) or in the [Skills channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/skills).

See our [tips for how to ask the best questions](../../using-mycroft-ai/troubleshooting/getting-more-support.md). This helps you get a more complete response faster.

