---
post_title: Adapt Tutorial
layout: page
published: false
---
# Adapt Tutorial

This page provides a step by step tutorial in using Adapt Intent Parser, using the `single_intent_parser.py` file as a starting point.

## Prerequisites

To complete this tutorial, you should have some basic knowledge of the Python programming language, and be comfortable executing commands on a Linux command line.

## Step 1 - Sample Intent

This is the sample **Intent** around which the tutorial is based.

```bash
A sample intent that uses a fixed vocabulary to extract entities for an intent

try with the following:
PYTHONPATH=. python examples/single_intent_parser.py "what's the weather like in tokyo"
```

## Step 2 - Import Libraries

First, we need to import `json` for serializing the Adapt Intent Parser output, and `sys` for reading in command line arguments.

```python
import json
import sys
```

Next, we import the `IntentBuilder` and `IntentDeterminationEngine.

```python
from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine
```

Next, we instantiate an IntentDeterminationEngine object.

```python
engine = IntentDeterminationEngine()
```

Next, we delcare a collection of weather **Keywords**, in JSON syntax. These **Keywords** act as _hints_ to the Adapt Intent Parser about which intent context is being referenced by an **Utterance**.

```python
weather_keyword = [
    "weather"
]
```

Register each **Keyword** with the `engine`.

```python
for wk in weather_keyword:
    engine.register_entity(wk, "WeatherKeyword")
```

Next, we declare a `collection` of weather types. These act as a query parameter on a Weather **Intent**.

For example, in the sentence:

`Will it rain in Seattle tomorrow?`

the `collection` of weather types can then be used to determine whether that weather type is occurring in Seattle.

Next, each weather type is registered with the `engine`.

```python
for wt in weather_types:
    engine.register_entity(wt, "WeatherType")
```

Next, a `collection` of locations is declared. These also act as a query parameter on a Weather **Intent**, and can be used in combination with the weather type `collection`.

```python
locations = [
    "Seattle",
    "San Francisco",
    "Tokyo"
]
```

Next, each location is registered with the `engine`.

```python
for loc in locations:
    engine.register_entity(loc, "Location")
```

Next, we construct an `intent parser`. The `intent parser` is named `WeatherIntent` and requires both a `WeatherKeyword` and `Location`, and can optionally include a `WeatherType`.

```python
weather_intent = IntentBuilder("WeatherIntent")\
    .require("WeatherKeyword")\
    .optionally("WeatherType")\
    .require("Location")\
    .build()
```
Next, we register the `intent parser` with the `engine`.

```python
engine.register_intent_parser(weather_intent)
```

We then declare an entry point for the script.
@TODO - need to explain here what an entry point is.

```python
if __name__ == "__main__":
```

Next, pass the command line arguments to this script as an **Utterance** into `engine.determine_intent()`. This function returns a generator, and we then use the generator to iterate through the results.

```python
for intent in engine.determine_intent(' '.join(sys.argv[1:])):
```

If the confidence is >0, this is a valid **Intent**.

```python
if intent.get('confidence') > 0:
```

Next, serialize the **Intent** and print it to `stdout`.

```python
print(json.dumps(intent, indent=4))
```

Of course, you don't just have to output the **Intent** to `stdout` - you can use it to build all sorts of tools. 
