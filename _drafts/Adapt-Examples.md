---
ID: 33171
post_title: Adapt Examples
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?page_id=33171
published: false
---
# Adapt Examples

- [Adapt Examples](#adapt-examples)
  * [Single intent Parser](#single-intent-parser)
  * [Multi-intent Parser](#multi-intent-parser)
  * [Regular Expression (regex) Intent Parser](#regular-expression-regex-intent-parser)

There are several **Intent Parser** examples for Adapt on GitHub, and this page walks you through what they are, and where you might use them.

## Single intent Parser

[See the Single Intent Parser code on GitHub](https://github.com/MycroftAI/adapt/blob/master/examples/single_intent_parser.py)

This sample **Intent Parser** uses a fixed vocabulary to extract entities for an **Intent**. This type of intent parser is useful when the parameters of the **Intent** are well-bounded; that is, the possible **Utterances** are well known.

## Multi-intent Parser

[See the Multi-intent Parser code on GitHub](https://github.com/MycroftAI/adapt/blob/master/examples/multi_intent_parser.py)

This sample **Intent Parser** uses multiple **Intents**, and disambiguates between them using intent confidence. For example, if one **Intent** has a higher confidence than the second, the **Intent Parser** will assume the first **Intent**.

## Regular Expression (regex) Intent Parser

[See the Regex Intent Parser code on GitHub](https://github.com/MycroftAI/adapt/blob/master/examples/regex_intent_parser.py)

This sample **Intent Parser** uses a regular expression entity to extract location from a query. This type of **Intent Parser** is useful where a parameter needs to be extracted from a query and it takes a form that can be expressed in regex. Other parameters that are often expressed in regex are IP address, names of people and colors.