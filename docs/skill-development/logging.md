---
description: >-
  Logging is useful during Skill development, as well as to help end-users
  diagnose problems in the future.
---

# Logging

To track events and data within your Skill we can use logging. If you are new to programming, this is a way to output a message that can tell you the state of your Skill at a particular point in time, details about an error that has occured, or simply noting that a program reached a particular point in the code.

## Basic Usage
A logger is available through the `MycroftSkill` base class. This means that you can use it within a Skill without needing to import the `logging` package. You can simply call `self.log` from within the class of your Skill.

Here is a quick example of an `info` level message used in a Skill. We will learn more about different levels shortly.

```Python
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class LoggingSkill(MycroftSkill):

    @intent_handler(IntentBuilder('HelloWorldIntent')
                    .require('HelloWorld'))
    def handle_hello_world_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        self.log.info("This is an info level log message.")
        self.speak_dialog("hello.world")

def create_skill():
    return LoggingSkill()
```

## Logging Levels

There are five types of log messages available that are used for different purposes.

### Debug
```Python
self.log.debug
```

Debug messages are used for information that will help to diagnose problems. These are particularly useful if there is anything that has the potential to break in the future.

By default these messages will not be logged unless the User has explicity turned on debug level logging.

### Info
```Python
self.log.info
```

Info messages provide general information when the Skill is running as expected. These messages will always be logged so are useful when actively developing a Skill, but should be used sparingly once a Skill is published for other people to use.

### Warning
```Python
self.log.warning
```

Warning messages are used to indicate that something has gone wrong, but the Skill will continue to function.

### Error
```Python
self.log.error
```

Error messages indicate that a serious problem has occured and the Skill will not be able to function. In the Mycroft CLI these messages are shown in red to make them highly visible.

### Exception
```Python
self.log.exception
```
Exception messages are an extended form of the `error` level message. These messages include a stack trace and should only be called from an exception handler. For example:

```Python
try:
    1/0
except ZeroDivisionError as e:
    self.log.exception("Cannot divide by zero")
```

## Where do these messages get logged?

Log messages from a Skill are displayed in the Mycroft CLI so that a User can see in real-time what is happening in the Skill. They are also written to the `skills.log` file located at: `/var/opt/mycroft/skills.log`

By default all info, warning, error and exception level messages will be logged. Debug level messages will be logged if the User explicitly requests it. This can be done by issuing the `:log level debug` command in the CLI, or changing the `log_level` attribute in the [mycroft configuration](../using-mycroft-ai/customizations/config-manager.md).

To return to normal logging, you can issue the `:log level info` CLI command.

## Using the logger outside the Skill class
As the logger is provided by the MycroftSkill class, it is only available within that scope. If you need to log messages from outside of this class, you can import the logger manually.

```Python
from mycroft.util import LOG
```

This can then be used outside your Skill's class. Extending our first example:

```Python
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util import LOG

LOG.info("This is a logged info level message outside of the MycroftSkill class scope")

def my_special_function():
  LOG.info("Another usage of LOG.")

class LoggingSkill(MycroftSkill):

    @intent_handler(IntentBuilder('HelloWorldIntent')
                    .require('HelloWorld'))
    def handle_hello_world_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        self.log.info("This is an info level log message.")
        self.speak_dialog("hello.world")
        my_special_function()

def create_skill():
    return LoggingSkill()
```
