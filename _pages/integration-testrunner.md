# The integration test runner

The purpose of the integration test runner is to test Mycroft skills by emulating the users spoken utterances, sending them to the skill.

## Overview

The integration test runner can test:

* That the expected intent in the skill is activated
* That the expected parameters are extracted from the utterance
* That Mycroft contexts are set or removed
* That the skill speak the intended answer
* The content of any message exchanged between the skill and the mycroft core

To set up a test the test runner can:
* Send an utterance, as the user would normally speak
* Set up and remove context
* Set up a custom timeout for the test runner, to allow for skills that runs for a very long time

## The integration test runner files

The test runner is part of the mycroft-core, it consist of the following files in mycroft-core/test/integrationtests/skills:
* discover_tests.py
* skill_tester.py
* skill_developers_testrunner.py
* message_tester.py
* test_all_skills.py

The ```discover_test.py``` is the python file that runs integration tests on all skills in ```/opt/mycroft/skills```.

The ```skill_tester.py``` is the file that loads all skills and execute test, one skill and one test at a time.

The ```skill_developers_testrunner.py``` is intended to be copied to the skill developers working directory, where the skills ```__init__.py``` file exists. Running ```skill_developers_testrunner.py``` will test only the skills it finds it the directory it is in, or, if it can’t find a skill where it is, it will search the subdirectories.

The ```message_tester.py``` is a utility that can test a single message against the internal rule format used by the skill_tester. It is intended for debugging rules.

The ```test_all_skills.py``` is testing all skills at the skill level, where ```discover_tests.py``` test at the intent level. Because of that ```test_all_skills.py``` not only runs all the intent tests, it also find out if all intents in a skill are tested, i.e. if any test cases are missing. It print a list of missing test cases for each skill, and fails if it finds any.

## Defining tests
A skill can define a test suite consisting of a number of files (test cases), which are placed in the skills ```test/intent``` directory. Each test case corresponds to one utterance. All parts of the test case are optional, except the utterance. The test case files are executed by the test runner, one after another, and they are executed in alphabetical order. Alphabetic ordering can be used for compensating (trans)actions, for instance first add to a list, then remove from a list, to leave the list unchanged.

The test case files in the ```test/intent``` directory is written in json, and must match the pattern ```*.intent.json```

An example test suite might look like this:

```
ls test/intent
001.AddTaskToList.intent.json       
002.FindTaskOnList.intent.json      
003.CompleteTaskOnList.intent.json  
004.ReadList.intent.json
005.CompleteList.intent.json
050.GetToken.intent.json
```

A test case file understand the following json keywords:

| Keyword | Description |
|---------|-------------|
|utterance |The text to send to the skill, like it was a spoken command|
|remove_context|A list of contexts to remove before sending the utterance|
|set_context|A list of contexts and corresponding strings to set before sending the utterance|
|intent_type|Assert that this intent name, as defined in the skills ```__init__.py``` code, is used|
|intent.parameter|Assert that a message parameter has a certain value. Repeating field.|
|Expected response|Assert that the skill speaks a response that matches this regular expression|
|evaluation_timeout|The default timeout is 30 seconds. If a skill takes longer than this to finish, the evaluation_timeout can be set|
|changed_context|Assert that a list of contexts was set or removed|
|assert|Assert that a rule, expressed in the internal test rummer format, is true|

Below is an example test case file:
```
{
 "utterance": "add milk to the grocery list",
 "remove_context": ["UndoContext", "ConfirmContext"],
 "set_context": {"_TestRunner": "data", "test": ""},
 "intent_type": "AddTaskToListIntent",
 "intent": {
   "taskName": "milk",
   "listName": "grocery",
   "AddTaskToListKeyword": "add"
 },
 "expected_response": "I can\\'t find a list called grocery.*",
 "evaluation_timeout": 10,
 "changed_context": ["UndoContext", "ConfirmContext"],
 "assert": "[['equal', 'context', 'UndoContext'], ['equal', 'context', 'ConfirmContext']]"
}
```

In the example above, some of the things asserted are not really needed, they are only provided to create an example demonstrating all possibilities.

A snippet of the intent to be tested looks like this:

```
@intent_handler(IntentBuilder('AddTaskToListIntent').require('AddTaskToListKeyword').require(TASK_PARAMETER).
               require(LIST_PARAMETER).optionally('_TestRunner').build())
def add_task_to_list_intent(self, message):
   try:
       if message.data.get('_TestRunner'):
           print "Initiated by the test runner"
```

And the message regular expression from the regex/en-us directory is:
```add (?P<taskName>.+) to (?P<listName>.+) list$```

The “AddTaksToListKeyword” is “Add”, defined in the vocab/en-us directory.

With this knowledge, let us walk through the test case.

The test case simulate the user utterance:
>add milk to the grocery list

Asuming other tests was run before this example, the “UndoContext” and the “ConfirmContext” may have been set, but to be sure they are removed, we remove them before the test starts.

The ```set_context``` can be used to test intents, that require a context. In the example above the “_TestRunner” context is set to "data". When the skill has side effects that are unwanted when testing, this trick allows us to test for the “_TestRunner” context in the intent, and behave accordingly, for instance not executing code with side effects. Of cause, other tests are then required to test the inner working of the intent.

The ```intent_type``` is used to verify that the utterance is passed to the right intent, hence it must the ```IntentBuilder()``` parameter. In this case "AddTaskToListIntent".

The ```intent``` is a list of key/values that must match the ```IntentBuilder().require()``` or similar parameters. This is used for testing that the right part of the utterance is passed as parameters to the skill.

The ```expected response``` is a regular expression that must match the answer that is Spoken by the intent.

The ```changed_context``` is a list of contexts, that the intent has set or removed. It is not possible to distinguish between set or remove context.

In the example above the ```changed_context``` and ```assert``` actually does the same thing, it is mentioned as an example only. The ```assert``` shows the internal rule format (see the next paragraph).

An test case succeeds if all test are passed for the intent. And in that case the test runner immediately continues to the next test. If all tests have not succeeded 30 seconds after the utterance, the test is failed. In the example above the timeout is reduced to 10 seconds to catch errors faster.


## The internal rule format
If the standard keywords in the test case file does not suffice, it is possible to write tests in the internal rule format, using the ```assert``` keyword. The standard keywords and values are translated into the internal rule format by the testrunner as well. The example test case above is actually transformed into:
```
[
  ['and',
    ['endsWith', 'intent_type', 'AddTaskToListIntent'], ['equal', 'listName', 'none'],
    ['equal', 'taskName', 'some'],
    ['equal', 'AddTaskToListKeyword', 'add']
  ],
  ['match', 'utterance', "I can\\'t find a list called none.\*"],
  ['equal', 'context', 'UndoContext'],
  ['equal', 'context', 'ConfirmContext'],
  ['equal', 'context', 'UndoContext'],
  ['equal', 'context', 'ConfirmContext']
]
```

The double test of contexts in the end is due to both using ```changed_context``` and ```assert```, one of which is of cause not needed.

The internal test format above is actually quite powerful, the code already supports that operations can be nested to any depth, for instance:
```
[['and',
    ['endsWith', 'type', 'AddTaskToListIntent'],
    ['or',
        ['equal', ['data', 'listName'], 'none'],
        ['equal', ['data', 'taskName'], 'some']
    ],
    ['equal', ['data', 'AddTaskToListKeyword'], 'add']
]]
```

and besides "and" also "or" and "not" are supported. Likewise the operations “equal”, “notEqual”, “endsWith” and “match” are supported, where match is regular expression matching.

## Handling skills with side effects
As mentioned in the example above, context can be used to make an intent aware that it is the rest runner that is initiating the call. With this knowledge unwanted side effects can be avoided.

## Executing the integration test runner
The ```discover_tests.py``` is intended to be run like a python unit test, please refer to https://docs.python.org/2/library/unittest.html. Most IDE has an easy way to run unit tests, and create nice structured test reports.

The ```skill_developers_testrunner.py``` is intended to be copied to the skill developers development directory, or directly in the skill directory. When run, it will search the directory it is in, and subdirectories, until it finds an ```__init__.py``` file. When it does, it will not traverse further down from that directory, but it will search sibling directories. In effect, it will only test one skill, if it is run in that skills directory. The ```skill_developers_testrunner.py``` is just like a unit test.

## Troubleshooting tests
Each message event is tested by the rules. When all rules has succeeded the test ends. When a rule succeeds the string ”Succeeded” is appended to the rule (see the "Rule status" in the test case output file below). During execution, the test runner print the messages received from the skill. An example test run is shown below (some output has been left out to keep the example short):

Test case output file:
```
/opt/mycroft/skills/skill-pairing/test/intent/sample1.intent.json
Test case: {u'intent': {u'DevicePairingPhrase': u'pair my device'}, u'intent_type': u'PairingIntent', u'utterance': u"let's pair my device"}
Rule created [['and', ['endsWith', 'intent_type', 'PairingIntent'], ['equal', 'DevicePairingPhrase', 'pair my device']]]
Evaluating message: {'lang': 'en-us', 'skill_id': 1211234571, 'utterances': [u"let's pair my device"]}
Evaluating message: {'confidence': 1.0, 'target': None, 'DeviceKeyword': 'device', 'intent_type': '1211234573:PairingIntent', 'PairingKeyword': 'pair', '__tags__': [{'end_token': 2, 'start_token': 2, 'from_context': False, 'entities': [{'confidence': 1.0, 'data': [('pair', u'BCBBCDEFHDPairingKeyword')], 'match': u'pair', 'key': 'pair'}], 'key': 'pair', 'match': u'pair'}, {'end_token': 4, 'start_token': 4, 'from_context': False, 'entities': [{'confidence': 1.0, 'data': [('device', u'BCBBCDEFHDDeviceKeyword')], 'match': u'device', 'key': 'device'}], 'key': 'device', 'match': u'device'}], 'utterance': u"let's pair my device"}
Evaluating message: {'name': 'PairingSkill.handle_pairing'}
Evaluating message: {'expect_response': False, 'utterance': u'Now I am ready for use.  Try asking me things like "hey mycroft, what\'s the weather", "hey mycroft, tell me about abraham lincoln", or "hey mycroft, play the news".  If you need to stop me talking at any time, just push my button.'}
Evaluating message: {'name': 'PairingSkill.handle_pairing'}
Evaluation failed
Rule status: [['and', ['endsWith', 'intent_type', 'PairingIntent', 'succeeded'], ['equal', 'DevicePairingPhrase', 'pair my device']]]

Failure
Traceback (most recent call last):
...
AssertionError
```

In the first line the test case is printed, in the second line the rules created from the test case is printed. Then comes a number of “Evaluating message” lines, that represent a message event each. Near the end we find the “Rule status” which shows what rules succeeded.

In the rule status we find ```['endsWith', 'intent_type', 'PairingIntent', 'succeeded']``` which means that the intent type was found, since “succeeded” was appended to that rule part. However, we did not find the ```DevicePairingPhrase``` in the same message. We expect the ```DevicePairingPhrase``` in the same message because of the “and” operator. And if we look at the messages in the log above, we can’t find a message where the ```DevicePairingPhrase``` appear.

To see this more clearly, it sometimes pays off to reformat the rule status:
```
[
  ['and',
    ['endsWith', 'intent_type', 'PairingIntent', 'succeeded'],
    ['equal', 'DevicePairingPhrase', 'pair my device']
  ]
]
```

The ```message_tester.py``` tool is able to evaluate one message event at a time, for instance:

![message tester](../img/message_tester.png)

Not surprisingly it yields the same result as the test runner.
