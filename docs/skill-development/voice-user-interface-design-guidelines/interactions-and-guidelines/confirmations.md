---
description: >-
  Confirmations are used to verify that the input from the user was understood
  correctly.
---

# Confirmations

Confirmation approaches can also be defined by Statements or Prompts , but when we talk about them in the context of confirmations we call them Implicit and Explicit.

### Implicit Confirmation

This type of confirmation is also a statement. The idea is to parrot the information back to the user to confirm that it was correct, but not require additional input from the user. The implicit confirmation can be used in a majority of situations. For example Mycroft’s Timer Skill uses implicit confirmation when creating new timers.

**Timer Skill**

| Speaker |  |
| :--- | :--- |
| **User** | _Hey Mycroft set a timer for 5 minutes_ |
| **Mycroft** | _Alright, I’m starting a 5 minute timer_ |

**Avoid**

| Speaker |  |
| :--- | :--- |
| **User** | _Hey Mycroft, add bananas to my shopping list_ |
| **Mycroft** | _done_ |

**Better**

| Speaker |  |
| :--- | :--- |
| **User** | _Hey Mycroft, add bananas to my shopping list_ |
| **Mycroft** | _Adding bananas_ |

### Explicit Confirmation

This type of confirmation requires an input from the user to verify everything is correct. Only use explicit confirmation when needed as it can be tedious for the user to always confirm their input. This strategy is best when there are multiple steps, and it would be difficult to fix a misstep without starting over, or when deleting or modifying an existing multi-step input.

**Avoid**

| **Speaker** |  |
| :--- | :--- |
| **User** | _Hey Mycroft, set an alarm for 9:00 am tomorrow_ |
| **Mycroft** | _Ok, I’ve set an alarm for 9:00 am tomorrow, is that correct?_ |
| **User** | _Yes_ |
| **Mycroft** | _9:00 am alarm set_ |

**Better**

| Speaker |  |  |
| :--- | :--- | :--- |
| **User** | _Hey Mycroft, set an alarm for 9:00 am tomorrow_ |  |
| **Mycroft** | I've set an alarm for tomorrow at 9:00 am, 16 hours from now |  |

The first example requires the user to confirm the alarm. Since the interaction is quite short it isn’t necessary to use explicit confirmation.

**Avoid**

| **Speaker** |  |
| :--- | :--- |
| **User** | _Hey Mycroft, set a calendar event for a meeting with Chris Stevens_ |
| **Mycroft** | _When is the event?_ |
| **User** | _Tomorrow at 11:00 am_ |
| **Mycroft** | _should I send an invite to Chris Stevens?_ |
| **User** | _Yes_ |
| **Mycroft** | _Alright, I've created a meeting for Tomorrow_ |
| **Mycroft** | _Alright, I’ve created a meeting for Tomorrow at 11:00 am with Chris Stevens_ |
| **User** | _Cancel my 11:00 am meeting tomorrow_ |
| **Mycroft** | _Done_ |

**Better**

| Speaker |  |
| :--- | :--- |
| **User** | _Hey Mycroft, set a calendar event for a meeting with Chris Stevens_ |
| **Mycroft** | _When is the event?_ |
| **User** | _Tomorrow at 11:00 am_ |
| **Mycroft** | _should I send an invite to Chris Stevens?_ |
| **User** | Yes |
| **Mycroft** | _Alright, I’ve created a meeting for Tomorrow at 11:00 am with Chris Stevens_ |
| **User** | _Cancel my 11:00 am meeting tomorrow_ |
| **Mycroft** | _Are you sure you want to delete your meeting tomorrow at 11:00 am?_ |
| **User** | _Yes_ |

Both examples use explicit and implicit confirmation correctly until the end of the interaction when the user wants to cancel the event. Unlike setting a simple timer or an alarm creating this calendar event requires multiple steps and would require reasonable effort to recreate. There may also be significant consequences if the request was misinterpreted and the meeting was cancelled unintentionally.

