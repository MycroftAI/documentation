---
description: 'The core of Mycroft, this brings all the pieces together.'
---

# Mycroft Core

Mycroft Core sits at the centre of all Mycroft installations. The code itself includes anything that is generic to all instances of Mycroft.

## Mycroft Services

Mycroft Core includes four or more distinct Services:
- [MessageBus](./message-bus.md)
- [Skills](./skills-service.md)
- [Audio](./audio-service.md)
- [Voice](./voice-service.md)
- [Enclosure](./enclosures.md)

Each of these is started in it's own process, and communicates with other processes by emitting and listening to messages on the MessageBus.


### Process Status (PROPOSED)

Each Service includes an instance of the ProcessStatus class. This provides a consistent interface to set and query the state of a Service.

It is constructed with the following signature:

```Python
status = ProcessStatus(name, bus, on_started=None, on_alive=None, on_ready=None,
              on_stopping=None, on_error=None)
```
**Arguments**
`name` (str): process name, will be used to create the messagebus messagetype "mycroft.{name}..."
`bus` (obj): a MessageBus instance to use
`on_started` (callable): callback to execute when process is started
`on_alive` (callable): callback to execute when minimum operation is reached.
`on_ready` (callable): callback to execute when loading is 100 % complete.
`on_stopping` (callable): callback to execute when process is attempting to shutdown.
`on_error` (callable): callback to execute when an unrecoverable error renders the process unusable.

#### State and Events

Each process tracks its state as one of:
- NOT_STARTED
- STARTED
- ERROR
- STOPPING
- ALIVE
- READY

These states are defined in a comparable order. This means if a Process has the state `ALIVE`, then it must also be `STARTED`. Likewise, if a Process is `READY`, it must also be `ALIVE` and `STARTED`.

These states can be set by calling the relevent method from the ProcessStatus class we initialized above:
- `status.set_started()`
- `status.set_error()`
- `status.set_alive()`
- `status.set_stopping()`
- `status.set_ready()`

It is up to each Service to determine it's readiness and set the state accordingly.

#### Querying Status

The status of a Service can be queried via the MessageBus.

The request Message should be in the form - `mycroft.{service_name}.{is_status}`. For example, we can check if the Audio Service is `ALIVE` by emitting:

```Python
response = self.bus.wait_for_response(Message(
           'mycroft.audio.is_alive'))
```

The response message will include a `status` boolean in the data payload:

```Python
>>> print(response.data)
{'status': True}
```
