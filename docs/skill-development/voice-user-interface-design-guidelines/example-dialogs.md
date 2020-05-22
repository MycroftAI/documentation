# Example Interaction Script

After working on a list of jobs to be done creating Example Interactions is one of the next steps in the design and planning process. In this step you will take the Job Stories and write example Dialogs that get the User's job accomplished. These Example Dialogs will then be used to create Behave tests before development begins. Once development begins the Example Dialogs also become the basis of the Dialog and Vocab files within your skill. Once development begins you will need to update your Behave tests to utilize the Dialog files instead of the natural language responses that were written in the design and planning phases. The process is described in more detail in the example below.

## First Draft Interaction Scripts

Begin by writing the example interactions of your skill from start to finish based on your Job Stories. At first don’t worry about organizing the interactions. Just try to write down as many examples as possible. If you skipped ahead and 

Here is an example of a First Draft Interaction of a Moon Phase Skill.

|  | Example Interaction 1 |
| :--- | :--- |
| **User** | _Hey Mycroft, what’s the moon phase?_ |
| **Mycroft** | _Today’s moon is Waning Crescent with 55% illumination_ |

| \_\_ | Example interaction 2 |
| :--- | :--- |
| **User** | _Hey Mycroft, when is the next full moon?_ |
| **Mycroft** | _The next full moon is on May 7th._ |

| \_\_ | Example Dialog 3 |
| :--- | :--- |
| **User** | _Hey Mycroft when is the next First quarter moon?_ |
| **Mycroft** | _The next First quarter moon is April 30th_ |

| \_\_ | Example Dialog 4 |
| :--- | :--- |
| **User** | _What phase of the moon is May 2nd?_ |
| **Mycroft** | _The moon will be Waxing Gibbous with 68% illumination on May 2nd_ |

| \_\_ | Example Dialog 5 |
| :--- | :--- |
| **User** | _Hey Mycroft, what’s the moon phase 5 days from today?_ |
| **Mycroft** | _The moon will be Waning Crescent with 5% illumination on May 20th_ |

| \_\_ | Example Dialog 6 |
| :--- | :--- |
| **User** | _Hey Mycroft, can you tell me the moon phase for a certain day?_ |
| **Mycroft** | _Yes, what day would you like to know the moon phase?_ |
| **User** | _May 15th_ |
| **Mycroft** | _On May 15th the moon will be waning crescent and 45% illuminated_ |

| \_\_ | Example Dialog 7 |
| :--- | :--- |
| **User** | _Hey Mycroft, what are the phases of the moon?_ |
| **Mycroft** | _A lunar cycle lasts 29.53 days and consists of four principal phases, the new moon, first quarter, full moon and third quarter. Would you like to know more?_ |
| **User** | _Yes_ |
| **Mycroft** | _The apparent shape of the moon between New Moon and First Quarter is known as Waxing Crescent, the apparent shape between First Quarter and Full Moon is known as Waxing Gibbuous. The moon is half illuminated in both First Quarter and Third Quarter, the use of the word quarter indicates the period within the cycle and not the illumination._ |

|  | Example Dialog 8 |
| :--- | :--- |
| **User** | _What's the moon phase on the next go around?_ |
| **Mycroft** | _The next quarterly moon phase is the last quarter moon on May 14th_ |

|  | Example Dialog 9 |
| :--- | :--- |
| **User** | _How many moon phases are there left?_ |
| **Mycroft** | _I’m not sure I understood you, would you like to know when the next moon phase cycle begins?_ |
| **User** | _Yes_ |
| **Mycroft** | _The next moon phase begins with the new moon on May 22nd_ |

## Organized Interaction Scripts

The next step in the process is organizing the first pass of dialogs into groups. You may already have a good idea of what these groups of similar interactions are based on your Job Stories from the beginning phase. You can also think of these as the features of the skill. In the Behave format these groups or features are called Scenarios. 

| **Scenario** | **When a user asks for the current Moon Phase** |
| :--- | :--- |
| **User** | _Hey Mycroft, what’s the moon phase?_ |
| **Mycroft** | _Today’s moon is Waning Crescent with 55% illumination_ |

| **Scenario** | **When a user asks for the next moon phase** |
| :--- | :--- |
| **User** | _Hey Mycroft, whe is the next full moon?_ |
| **Mycroft** | _The next full moon is on May 7th._ |
| \_\_ |  |
| **User** | _Hey Mycroft, when is the next First Quarter Moon?_ |
| **Mycroft** | _The next First Quarter Moon is April 30th._ |

| **Scenario** | **When a user asks for the next moon phase** |
| :--- | :--- |
| **User** | _what is the next principal moon phase_ |
| **Mycroft** | _The next principal moon phase is the full moon, on May 7th_ |

| **Scenario** | **When the user asks for the Moon Phase on a date** |
| :--- | :--- |
| **User** | _What phase of the moon is May 2nd?_ |
| **Mycroft** | _The moon will be Waxing Gibbous with 68% illumination on May 2nd_ |
|  |  |
| **User** | _Hey Mycroft, what’s the moon phase 5 days from today?_ |
| **Mycroft** | _The moon will be Waning Crescent with 5% illumination on May 20th_ |

| **Scenario** | **When the user asks for more information on Moon Phases** |
| :--- | :--- |
| **User** | _Hey Mycroft, what are the phases of the moon?_ |
| **Mycroft** | _A lunar cycle lasts 29.53 days and consists of four principal phases, the new moon, first quarter, full moon and third quarter. Would you like to know more?_ |
| **User** | _Yes_ |
| **Mycroft** | _The apparent shape of the moon between New Moon and First Quarter is known as Waxing Crescent, the apparent shape between First Quarter and Full Moon is known as Waxing Gibbuous. The First Quarter is half illuminated and is growing in illumination toward a Full Moon. The Last Quarter is half illuminated and shrinking in illumination toward a New Moon. A New Moon is not illuminated and not therefore not visible to the naked eye._ |

| **Scenario** | When the user needs Help |
| :--- | :--- |
| **User** | _Hey Mycroft, can you tell me the moon phase for a certain day?_ |
| **Mycroft** | _Yes, what day would you like to know the moon phase?_ |
| **User** | _May 15th_ |
| **Mycroft** | _On May 15th the moon will be waning crescent and 45% illuminated_ |
| \_\_ |  |
| **User** | _Hey Mycroft, how do I get information on the moon phases_ |
| **Mycroft** | _You can ask me what the current moon phase is, the moon phase on a future date, or more information about moon phases._ |

| **Scenario** | **Error Handling** |
| :--- | :--- |
| **User** | _What’s the moon phase on the next go around?_ |
| **Mycroft** | _For which day would you like to know the moon phase?_ |
| **User** | _next monday_ |

**Scenario: Error Handling**

| **Scenario** | Error Handling |
| :--- | :--- |
| **User** | _What’s the moon phase on the next go around?_ |
| **Mycroft** | _For which day would you like to know the moon phase?_ |
| **User** | _June 5th_ |
| **Mycroft** | _June 5th is a Full Moon_ |
| \_\_ |  |
| **User** | _How many moon phases are there left?_ |
| **Mycroft** | _I’m not sure I understood you, would you like to know when the next moon phase cycle begins?_ |
| **User** | _yes_ |
| **Mycroft** | _the next moon phase begins with the new moon on April 23rd_ |

## Converting Example Interactions into Behave Feature files

Once you have finished creating you example interactions and you have done some rounds of testing with some users, then it's time to convert your Interactions into Behave Feature files. You can see an example of the first Scenario from the Example Dialogs converted to a Feature file below.

```text
Feature: mycroft-moon-phase

  Scenario Outline: The user asks for the current moon phase
    Given an english speaking user
      When the user asks for "<the current moon phase>"
      Then "skill-moon-phase" should reply with "Today’s moon is Waning Crescent with 55% illumination"

   Examples:
     | the current moon phase |
     | what’s the moon phase |
     | what's the phase of the moon |
     | what is the moon phase today |
```

## Converting Example Interactions to Flows \(optional\)

Some might think that creating the Flowcharts would be the first step in the process. After all the flowchart is abstract and doesn’t require full statements or prompts to be written. In a flowchart you just need to see the steps and decision points within the interaction. However, in practice the language used in the interaction can have such a great impact on the user’s input that is more important to start with Example Interactions and real statements and prompts first. 

In a flowchart it's easy to add several decision branches to a step, but in practice the dialog necessary to effectively make the decision might require multiple steps. It's always best to start with the dialog.

