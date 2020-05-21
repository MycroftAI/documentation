---
description: >-
  Conversations are made up of a series of individual interactions, but are more
  than the sum of their parts. For more complicated Skills conversations are a
  necessity.
---

# Conversations

Any time the user needs to input a lot of information or the user needs to sort through a variety of options a conversation will be needed. Users may be used to systems that require them to separate input into different chunks. For example, many personal navigation devices \(GPS units\) require users to input the street number, street name, city, and state separately, like this:

| Speaker |  |
| :--- | :--- |
| **Navigation Device** | _What is the street number_ |
| **User** | _123_ |
| **Navigation Device** | _What is the street name_ |
| **User** | _Main Street_ |
| **Navigation Device** | _What is the city_ |
| **User** | _Springfield_ |
| **Navigation Device** | _Oregon_ |

This was a limitation of the technology, both the STT and intent parser were not capable of handling an entire address. With Mycroft you do not need to separate the address into multiple inputs. It’s also easy to think like a traditional GUI and translate what are typically separate fields into prompts for the user, but that will only slows down the interaction. 

The best solution is to allow the user to input information both ways, all at once, or in pieces. For example the Mycroft Alarm skill allows the user to set a complicated alarm all in one go, or in steps.

**In Steps:**

| Speaker |  |
| :--- | :--- |
| **User** | _Hey Mycroft, set a recurring alarm_ |
| **Mycroft** | _For what day?_ |
| **User** | _weekdays_ |
| **Mycroft** | _For what time?_ |
| **User** | _7 am_ |
| **Mycroft** | I've set a recurring Alarm for 7 am on weekdays |

**All at once:**

| Speaker |  |
| :--- | :--- |
| **User** | Hey Mycroft, set a recurring alarm for weekdays at 7 am |
| Mycroft | I've set a recurring Alarm for 7 am on weekdays |

### Context

Conversational context is a given when speaking to another person, but not always when interacting with a computer based system. Many skills are designed with only a quick back and forth interaction in mind, and can operate well without conversational context, but conversational context can be a powerful addition to a skill and can make the interaction much more life like. Here are some examples of how to use context in conversation. 

| Speaker |  |
| :--- | :--- |
| **User** | _Who is Shaquille O'Neal_ |
| **Mycroft** | _Shaquille O'Neal is an American former professional basketball player who is a sports analyst on the television program Inside the NBA on TNT. He is considered one of the greatest players in National Basketball Association history_ |
| **User** | _How tall is he?_ |
| **Mycroft** | _seven foot 1 inches tall_ |
| **User** | _when did he retire_ |
| **Mycroft** | _2011_ |

To learn more about the technical aspects of Conversational Context, see:

{% page-ref page="../user-interaction/conversational-context.md" %}



