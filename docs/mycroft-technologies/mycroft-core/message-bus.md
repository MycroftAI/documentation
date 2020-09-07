---
description: >-
  A Message Bus is mechanism for independent systems to communicate with each
  other using a set of Messages for common commands or notifiers. In the Mycroft
  ecosystem, the Messagebus is a websocket.
---

# MessageBus

## What is a Message Bus?

A Message Bus is mechanism for independent systems to communicate with each other using a set of _messages_ for common commands or notifiers. In the Mycroft ecosystem, the Messagebus is a websocket and the messages contain a message type with an optional JSON data packet. Some messages trigger actions and have side effects; some are simple notifiers of actions that either have occurred or are about to occur. The Messagebus connects the `mycroft-core` processes and the **Skills**, and can also be joined by outside systems such as the CLI.

See all the Message types that are currently used by the MessageBus.

{% page-ref page="message-types.md" %}

Messages can be sent from the _producers_ and acted upon by [Skills](https://mycroft.ai/documentation/skills) or other _consumers_ within `mycroft-core`. The producers and consumers listed are examples and some messages might be generated or handled by other processes or advanced **Skills**.

The base [MycroftSkill API](http://mycroft-core.readthedocs.io/en/stable/) handles most of the Messagebus usage automatically. For example, the `mycroft.stop` message is caught by the skill framework, invoking an overridden `MycroftSkills.stop()` method within a **Skill**. Similarly, the `MycroftSkill.speak()` and `MycroftSkill.speak_dialog()` methods generate `speak` messages to be conveyed to the text-to-speech \(TTS\) and audio systems.

You will really only need to know about the Mycroft Messagebus if you are developing advanced **Skills**. The `MycroftSkill.add_event()` method allows you to attach a handler which will be triggered when the message is seen on the Messagebus.

_NOTE: We can only currently assist you in writing Skills in Python, so if you choose to write Skills in another programming language, we may not be able to provide assistance - but we don't want to stop you doing awesome things!_

## MycroftSkill Interaction

### Connecting Message handlers

```python
from mycroft import MycroftSkill

class ListenForMessageSkill(MycroftSkill):
  def initialize(self):  
      self.add_event('recognizer_loop:record_begin',  
                    self.handle_listener_started)  
      self.add_event('recognizer_loop:record_end',  
                    self.handle_listener_ended)

  def handle_listener_started(self, message):  
      # code to excecute when active listening begins...

  def handle_listener_ended(self, message):  
      # code to excecute when active listening begins...  

def create_skill():
    return ListenForMessageSkill()
```

### Generating Messages

```python
from mycroft import MycroftSkill
from mycroft.messagebus import Message

class GenerateMessageSkill(MycroftSkill):
  def some_method(self):  
    self.bus.emit(Message("recognizer_loop:utterance",  
                          {'utterances': ["the injected utterance"],  
                            'lang': 'en-us'}))  

def create_skill():
    return GenerateMessageSkill()
```

## Mycroft MessageBus Client

The [Mycroft MessageBus Client](https://github.com/MycroftAI/mycroft-messagebus-client) is a Python module providing a simple interface for the Mycroft MessageBus. It can be used to connect to Mycroft, send messages, and react to messages sent by the Mycroft system.

The module is available through [PyPI.org](https://pypi.org/project/mycroft-messagebus-client/) or directly [on Github](https://github.com/MycroftAI/mycroft-messagebus-client).

You can install it in your Mycroft Virtual Environment using:

```text
mycroft-pip install mycroft-messagebus-client
```

#### MycroftBusClient\(\)

The `MycroftBusClient()` object can be setup to connect to any host and port as well as any endpont on that host. this makes it quite versitile and will work on the main bus as well as on a gui bus. If no arguments are provided it will try to connect to a local instance of mycroftr core on the default endpoint and port.

#### Message\(\)

The `Message` object is a representation of the messagebus message, this will always contain a message type but can also contain data and context. Data is usually real information while the context typically contain information on where the message originated or who the intended recipient is.

```python
Message('MESSAGE_TYPE', data={'meaning': 42}, context={'origin': 'A.Dent'})
```

### Sending a Message

In the following example we setup an instance of the MessageBusClient then emit a `speak` Message with a data payload. Mycroft would consume this Message and speak "Hello World".

```python
from mycroft_bus_client import MessageBusClient, Message

print('Setting up client to connect to a local mycroft instance')
client = MessageBusClient()
client.run_in_thread()

print('Sending speak message...')
client.emit(Message('speak', data={'utterance': 'Hello World'}))
```

### Listening for a Message

In the following example we setup an instance of the MessageBusClient. We then define a function `print_utterance` that prints the `utterance` from a Message. This is registered as a handler for the `speak` Message. Finally we call the `run_forever()` method to keep the `client` running.

If this code had run before the example above, it would catch the `speak` Message we emitted and print: `Mycroft said "Hello World"`

```python
from mycroft_bus_client import MessageBusClient, Message

print('Setting up client to connect to a local mycroft instance')
client = MessageBusClient()

def print_utterance(message):
    print('Mycroft said "{}"'.format(message.data.get('utterance')))


print('Registering handler for speak message...')
client.on('speak', print_utterance)

client.run_forever()
```

### Manually connecting to the MessageBus

Here is an example Python script to connect to the `messagebus`:

```python
#! /usr/bin/env python3

import sys
from websocket import create_connection
uri = 'ws://' + sys.argv[1] + ':8181/core'
ws = create_connection(uri)
print("Sending " + sys.argv[2] + " to " + uri + "...")
if len(sys.argv) >= 4:
    data = sys.argv[3]
else:  
    data = "{}"

message = '{"type": "' + sys.argv[2] + '", "data": ' + data +'}'  
result = ws.send(message)  
print("Receiving..." )
result = ws.recv()  
print("Received '%s'" % result)
ws.close()
```

Unfortunately, we cannot provide support or examples for other languages.

## Command Line Interaction

### Generating Messages

```bash
python3 -m mycroft.messagebus.send xxx.yyy.zzz
```

or

```bash
python3 -m mycroft.messagebus.send xxx.yyy.zzz '{"name": "value"}'
```

A simple message looks like this:
```bash
python3 -m mycroft.messagebus.send speak '{"utterance" : "I am good"}'
```

## Guidelines for Message Usage

Private messages can be placed on the Messagebus following these naming conventions:  
`subsystem.message` or `skill.skillname.message`

* Messages MUST use verbs for requests - such as;  
  * `mic.mute`  
  * `mic.unmute`  
  * `skill.mycrofttimer.cancel.all`
* Messages MUST use the future tense for pre-action notifications - such as;  
  * `mic.muting`  
  * `mic.unmuting`
* Messages MUST use the past tense for post-action notifications - such as;  
  * `mic.muted`  
  * `mic.unmuted`  
  * `skill.mycrofttimer.expired`

See all the Message types that are currently used by the MessageBus.

{% page-ref page="message-types.md" %}

## Additional Support

If you have further questions, then the best place to ask them is our [Community Forum](https://community.mycroft.ai) or in the [~dev Channel](https://chat.mycroft.ai/community/channels/dev) on Mycroft Chat.

