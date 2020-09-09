---
description: >-
  Now that you have the basics, learn about how to interact get input and create
  meaningful interactions with Users of your Skill.
---

# User interaction

## Intents

The initial interactions with your Skill will start with a general utterance from the User. Your Skill must register intents that it can handle and Mycroft will then determine which Skill can respond to the Users request.

{% page-ref page="intents/README.md" %}

## Statements

Mycroft can speak any information that you need to communicate to the User.

{% page-ref page="statements.md" %}

## Prompts

If you need to prompt the User for information, you can use a range of methods to ask different types of questions.

{% page-ref page="prompts.md" %}

## Parsing Utterances

A common process within a Skill is to parse the contents of an utterance. Mycroft provides a range of easy to use methods for this task.

{% page-ref page="parsing.md" %}

## Confirmations

Confirmations are used to verify that the input from the User was understood correctly. These may be verbal or non-verbal.

{% page-ref page="confirmations.md" %}

## Conversational Context

For more complex cases, a Skill can add context to the Intent Parser to create more natural conversational interaction.

{% page-ref page="conversational-context.md" %}

## Converse

Converse allows a recently active Skill to inspect utterances before the normal intent handling process.

{% page-ref page="converse.md" %}