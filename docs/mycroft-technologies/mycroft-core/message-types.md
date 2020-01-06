---
description: >-
  Messages are used to communicate information between Mycroft services and
  other components. This list of Message types outlines their meaning, expected
  JSON data, standard producer and consumer.
---

# Message Types

Each Message type listed contains a description outlining it's meaning or purpose. Where relevant, the Message type will also list the specific JSON data packets expected to be emitted with that Message, and the most common producers and consumers of the Message.

See the [MessageBus documentation](message-bus.md) for further information on this service and examples of using Messages.

## General

### speak

{% tabs %}
{% tab title="Description" %}
Request to speak utterance
{% endtab %}

{% tab title="Data" %}
`{"utterance": "words to be spoken", "lang": "en-us"}`
{% endtab %}

{% tab title="Producer" %}

{% endtab %}

{% tab title="Consumer" %}

{% endtab %}
{% endtabs %}



