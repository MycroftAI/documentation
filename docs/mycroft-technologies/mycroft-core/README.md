---
description: >-
  Mycroft Core sits at the centre of all Mycroft installations. The code itself
  includes anything that is generic to all instances of Mycroft.
---

# Mycroft Core

## Mycroft Services

Mycroft Core includes four or more distinct Services:

* [MessageBus](message-bus.md)
* [Skills](https://github.com/MycroftAI/documentation/tree/4a8ffa3702e64c9411fb0ba4239a61d1cca506ab/docs/mycroft-technologies/mycroft-core/skills-service.md)
* [Audio](audio-service.md)
* [Voice](https://github.com/MycroftAI/documentation/tree/4a8ffa3702e64c9411fb0ba4239a61d1cca506ab/docs/mycroft-technologies/mycroft-core/voice-service.md)
* [Enclosure](https://github.com/MycroftAI/documentation/tree/4a8ffa3702e64c9411fb0ba4239a61d1cca506ab/docs/mycroft-technologies/mycroft-core/enclosures.md)

Each of these is started in it's own process, and communicates with other processes by emitting and listening to messages on the MessageBus.

### Process Status \(PROPOSED\)

Each Service includes an instance of the ProcessStatus class. This provides a consistent interface to set and query the state of a Service.

It is constructed with the following signature:

```python
status = ProcessStatus(name, bus, on_started=None, on_alive=None, on_ready=None,
              on_stopping=None, on_error=None)
```

**Arguments** 

`name` \(str\): process name, will be used to create the messagebus messagetype "mycroft.{name}..."   
`bus` \(MessageBusClient\): connection to the Mycroft messagebus.  
`on_started` \(callable\): callback to execute when process is started   
`on_alive` \(callable\): callback to execute when minimum operation is reached.   
`on_ready` \(callable\): callback to execute when loading is 100 % complete.   
`on_stopping` \(callable\): callback to execute when shutdown of process starts.  
`on_error` \(callable\): callback to execute when an unrecoverable error renders the process unusable.

#### State and Events

Each process tracks its state as one of:

* NOT\_STARTED
* STARTED
* ERROR
* STOPPING
* ALIVE
* READY

These states are defined in a comparable order. This means if a Process has the state `ALIVE`, then it must also be `STARTED`. Likewise, if a Process is `READY`, it must also be `ALIVE` and `STARTED`.

These states can be set by calling the relevent method from the ProcessStatus class we initialized above:

* `status.set_started()`
* `status.set_error()`
* `status.set_alive()`
* `status.set_stopping()`
* `status.set_ready()`

It is up to each Service to determine it's readiness and set the state accordingly.

#### Querying Status

The status of a Service can be queried via the MessageBus.

The request Message should be in the form - `mycroft.{service_name}.{is_status}`. For example, we can check if the Audio Service is `ALIVE` by emitting:

```python
response = self.bus.wait_for_response(Message(
           'mycroft.audio.is_alive'))
```

The response message will include a `status` boolean in the data payload:

```python
>>> print(response.data)
{'status': True}
```

