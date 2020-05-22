---
description: >-
  Work in progress - This Framework enables Common IoT Skills to operate
  together to control a range of IoT devices, providing a better experience for
  the end user.
---

# Common IoT Framework

The Common IoT Framework is designed to provide a common language for controlling Internet of Things \(IoT\) or Smart Home devices. This Framework is still a work in progress and should not be used in production settings.

Phrases like "turn on", might relate to a range of Skills, devices, or services. The Common IoT Framework enables these to be handled in a uniform and seamless way.

Unlike the Common Play and Common Query Frameworks, an IoT request may need to be handled by multiple Skills. Imagine a User has both LIFX and Hue lightbulbs, and installs Skills for both of these. Asking Mycroft to turn off all lights in the house, this request needs both Skills to turn off their lights for the intention of the phrase to be fulfilled.

## IoT Objects

### Thing

A `Thing` is something that may be controlled by IoT Skills.

This might be a light, thermostat, door, lock, plug, switch, air conditioner, or something else.

### Attribute

An `Attribute` is a property of a `Thing`.

This might include features such as brightness, color, color\_temperature, or temperature.

### State

`State` defines the current status of a `Thing`.

These are generally intended to handle binary queries, such as "is the door locked?" or "is the heat on?" where 'locked' and 'on' are the state values. The special value 'STATE' can be used for more general queries capable of providing more detailed information, for example, "what is the state of the lamp?" could produce state information that includes brightness or color.

### Action

An `Action` can be applied to a `Thing`.

For example, a LIGHT can be turned ON. Actions are intended to be used with the IoTRequest class.

### IoTRequest

This class represents a request from a user to control an IoT device. It contains all of the information an IoT skill should need in order to determine if it can handle a user's request. The information is supplied as properties on the request.

At present, those properties are: - action \(see the Action enum\) - thing \(see the Thing enum\) - state \(see the State enum\) - attribute \(see the Attribute enum\) - value - entity - scene

The 'action' is mandatory, and will always be not None. The other fields may be None.

The 'entity' is intended to be used for user-defined values specific to a skill. For example, in a skill controlling Lights, an 'entity' might represent a group of lights. For a smart-lock skill, it might represent a specific lock, e.g. 'front door.'

The 'scene' value is also intended to to be used for user-defined values. Skills that extend CommonIotSkill are expected to register their own scenes. The controller skill will have the ability to trigger multiple skills, so common scene names may trigger many skills, for a coherent experience.

The 'value' property will be a number value. This is intended to be used for requests such as "set the heat to 70 degrees" and "set the lights to 50% brightness."

Skills that extend CommonIotSkill will be expected to register their own entities.

## CommonIOTSkill Class

Skills that want to work with the CommonIoT system should extend this class. Subclasses will be expected to implement two methods, `can_handle` and `run_request`.

Subclasses may also register their own entities and scenes. See the `register_entities_and_scenes` method for details.

This class works in conjunction with the IoT Control Skill.

### can\_handle

Determine if an IoTRequest can be handled by this skill.

This method must be implemented by all subclasses.

An `IoTRequest` contains several properties \(see the documentation for that class\). This method should return True if and only if this skill can take the appropriate `action` when considering _all other properties of the request_. In other words, a partial match, one in which any piece of the IoTRequest is not known to this skill, and is not None, this should return \(False, None\).

### run\_request

Handle an IoT Request.

All subclasses must implement this method.

When this skill is chosen as a winner, this function will be called. It will be passed an IoTRequest equivalent to the one that was supplied to `can_handle`, as well as the `callback_data` returned by `can_handle`.

### register\_entities\_and\_scenes

This method will register this skill's scenes and entities.

This should be called in the skill's `initialize` method, at some point after `get_entities` and `get_scenes` can be expected to return correct results.

### get\_entities

Get a list of custom entities.

This is intended to be overridden by subclasses, though it it not required \(the default implementation will return an empty list\).

The strings returned by this function will be registered as ENTITY values with the intent parser. Skills should provide group names, user aliases for specific devices, or anything else that might represent a THING or a set of THINGs, e.g. 'bedroom', 'lamp', 'front door.' This allows commands that don't explicitly include a THING to still be handled, e.g. "bedroom off" as opposed to "bedroom lights off."

### get\_scenes

Get a list of custom scenes.

This method is intended to be overridden by subclasses, though it is not required.

The strings returned by this function will be registered as SCENE values with the intent parser. Skills should provide user defined scene names that they are aware of and capable of handling, e.g. "relax," "movie time," etc.

## IoT Control Skill

The [IoT Control Skill](https://github.com/MycroftAI/skill-iot-control) registers vocabulary and intents to capture IoT related requests. It then emits messages on the messagebus that will be picked up by all skills that extend this class. Each skill will have the opportunity to declare whether or not it can handle the given request. Skills that acknowledge that they are capable of handling the request will be considered candidates, and after a short timeout, a winner, or winners, will be chosen. With this setup, a user can have several IoT systems, and control them all without worry that skills will step on each other.

