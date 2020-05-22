---
description: >-
  There are two basic ways for Mycroft to interact with the user, Statements and
  Prompts.
---

# Statements and Prompts

You can think of **Prompts** as questions and **Statements** as providing information to the user that does not need a follow-up response. For example a weather forecast like this would be considered a statement: 

> Today’s forecast is sunny with a high of 60 and a low of 45.

### Statements

For a lot of skills the conversation might end with a simple statement from Mycroft, and no further action is necessary. Try to imagine what the user is trying to accomplish, if a simple statement gets the job done there is no reason to keep the conversation rolling, and in fact a follow up might annoy the user with unnecessary interaction.

### Prompts

It may be tempting to always give users specific instructions like traditional automated phones systems \(Interactive Voice Response\). Many phone systems are notorious for being too verbose and difficult to follow. 

With Mycroft we’re trying to break that mold and make the interaction natural. If you follow the phone system method you may be giving the user the exact phrasing to say, but you’re also taking up valuable time and training them to think the system is very narrow in capability. In the event that the user does give a response that your skill can not handle, create follow up prompts that steer the user back on track. 

Remember, there are no errors in a cooperative conversation.

#### Avoid

| Speaker |  |
| :--- | :--- |
| **Mycroft** | _How many people are playing? For example, you can say 2 players._ |

#### **Better**

| Speaker |  |
| :--- | :--- |
| **Mycroft** | _How many players?_ |
| **User** | _My Brother and Myself_ |
| **Mycroft** | _I’m sorry, what was the number of players?_ |
| **User** | _Two_ |

In the first example the user is told explicitly what they can say, but the prompt is unnatural, we don’t typically suggest responses to a conversation partner in real life. These long-winded prompts can become tiresome if they are used repeatedly throughout the skill. Remember the phone system example, typically poorly designed automated phone systems inundate the user with many options and additional instructions at every step of the interaction. 

In the second example we see a better prompt, although the user gives a response that is easy for a human to understand it is more difficult to design a skill to understand. Instead the skill designer can apply a re-prompt strategy that steers the user back on track and doesn’t require them to start the interaction over. In this case the re-prompt changes the wording slightly to make it clear that the user needs to say a number. The next time the user interacts with this Skill, they will likely say a number in their first interaction.

Determining whether or not to respond to the user with a statement or a prompt can be a bit tricky. When the user is somewhat vague it is tempting to assume the user’s intent in order to speed along the interaction. Sometimes this is the right approach and sometimes it is not. If you are very confident in the user’s input then it is alright to assume, and respond with a statement. For example in the Wikipedia Skill, one of the Mycroft Essential Skills, the Wikipedia API is used to confidently select the best response.

**Mycroft Wikipedia Skill**

| Speaker |  |
| :--- | :--- |
| **User** | _Tell me about Abraham Lincoln_ |
| **Mycroft** | _Abraham Lincoln was an American statesman and lawyer who served as the 16th president of the United States from 1861 to 1865. Lincoln led the nation through its greatest moral, constitutional, and political crisis in the American Civil War_. |

In contrast let’s look at an example of where a follow up prompt is a better approach. You’re working on a skill that gives important information about birds, such as wingspan, laden and unladen airspeed, etc..

**Avoid**

| Speaker | \*\*\*\* |
| :--- | :--- |
| **User** | _what is the airspeed velocity of an unladen swallow?_ |
| **Mycroft** | _The unladen airspeed of the european swallow is 20.1 miles per hour._ |

**Better**

| Speaker |  |
| :--- | :--- |
| **User** | _What is the airspeed velocity of an unladen Swallow?_ |
| **Mycroft** | _What do you mean, African or European Swallow?_ |
| **User** | European Swallow. |
| **Mycroft** | _The unladen airspeed of the European Swallow is 20.1 miles per hour._ |

In the first example Mycroft assumes the user is referring to the European Swallow, however there is nothing to give confidence to that assumption. In this case it’s dangerous to assume the User meant the European Swallow since it is just as likely they meant the African Swallow. When there is no confidence in one answer versus another, Mycroft should follow up with a prompt as demonstrated in the second example.

Another approach to solving this problem is to offer the most likely answer and inform the user that there are other answers available with a statement.

