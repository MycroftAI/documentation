# Error Handling

Inevitably, the user will say something that your skill can’t handle. It’s best not to think of these as errors on the part of the user, remember there aren’t really errors in conversations. Conversations are naturally cooperative with both parties seeking to continue to a successful outcome. Keeping that in mind you should do your best to avoid Error Handling that is a dead-end.

**Avoid**

| Speaker |  |
| :--- | :--- |
| **User** | _Timer_ |
| **Mycroft** | _I'm sorry I can't help you with that_ |

**Better**

| **Speaker** |  |
| :--- | :--- |
| **Use**r | _Timer_ |
| **Mycroft** | _A timer for how long?_ |
| **User** | _5 minutes_ |

In the first example Mycroft does not give the user any options to finish the job they set out to do. Try to avoid situations where the user has to start the conversation over.

## Help, Cancel, and Stop

When designing your skill it's best to think about the universal utterances, help, cancel and stop. At any point while interacting with the user should be able to say “help” to get assistance using the skill. Even if the help is quite simple. In practice 

