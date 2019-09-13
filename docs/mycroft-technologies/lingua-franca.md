---
description: >-
  Lingua Franca is our multilingual language parsing and formatting library. This is what allows Mycroft to both understand and respond with naturally expressed dates, numbers and times.
---

# Lingua Franca

Lingua Franca _(noun)_

> a framework that is adopted as the common language between speakers with different native tongues

[Lingua Franca Github repo](https://github.com/MycroftAI/lingua-franca#lingua-franca)

## Supported Languages
Currently supported languages include:
- English
- French
- German
- Hungarian
- Italian
- Portuguese
- Swedish

There is also active progress being made on:
- Danish
- Dutch
- Spanish

## Formatting

Convert data into spoken equivalents

### Pronounce numbers

spoken versions of numbers

```python
from lingua_franca.format import nice_number, pronounce_number

assert nice_number(25/6) == "4 and a sixth"
assert nice_number(201) == "201"
assert nice_number(3.14159269) == "3 and a seventh"

assert pronounce_number(3.14159269) == "three point one four"
assert pronounce_number(0) == "zero"
assert pronounce_number(10) == "ten"
assert pronounce_number(201) == "two hundred and one"
assert pronounce_number(102.3) == "one hundred and two point three"
assert pronounce_number(
    4092949192) == "four billion, ninety two million, nine hundred and forty nine thousand, one hundred and ninety two"

assert pronounce_number(100034000000299792458, short_scale=True) == \
       "one hundred quintillion, thirty four quadrillion, " \
       "two hundred and ninety nine million, seven hundred and ninety " \
       "two thousand, four hundred and fifty eight"

assert pronounce_number(100034000000299792458, short_scale=False) == \
       "one hundred trillion, thirty four thousand billion, " \
       "two hundred and ninety nine million, seven hundred and ninety " \
       "two thousand, four hundred and fifty eight"
```

### Pronounce datetime objects

spoken date for datetime.datetime objects

```python
from lingua_franca.format import nice_date, nice_date_time, nice_time
import datetime

dt = datetime.datetime(2017, 1, 31,  13, 22, 3)

assert nice_date(dt) == "tuesday, january thirty-first, twenty seventeen"

assert nice_time(dt) == "one twenty two"
assert nice_time(dt, use_ampm=True) ==  "one twenty two p.m."
assert nice_time(dt, speech=False) == "1:22"
assert nice_time(dt, speech=False, use_ampm=True) == "1:22 PM"
assert nice_time(dt, speech=False, use_24hour=True) == "13:22"
assert nice_time(dt, speech=False, use_24hour=True, use_ampm=True) == "13:22"
assert nice_time(dt, use_24hour=True, use_ampm=True) == "thirteen twenty two"
assert nice_time(dt, use_24hour=True, use_ampm=False) == "thirteen twenty two"

assert nice_date_time(dt) == "tuesday, january thirty-first, twenty seventeen at one twenty two"
```

### Pronounce durations

spoken number of seconds or datetime.timedelta objects

```python
from lingua_franca.format import nice_duration


assert nice_duration(1) ==   "one second"
assert nice_duration(3) ==   "three seconds"
assert nice_duration(1, speech=False) ==   "0:01"
assert nice_duration(61), "one minute one second"
assert nice_duration(61, speech=False) ==   "1:01"
assert nice_duration(5000) ==  "one hour twenty three minutes twenty seconds"
assert nice_duration(5000, speech=False), "1:23:20"
assert nice_duration(50000) ==   "thirteen hours fifty three minutes twenty seconds"
assert nice_duration(50000, speech=False) ==   "13:53:20"
assert nice_duration(500000) ==   "five days  eighteen hours fifty three minutes twenty seconds"
assert nice_duration(500000, speech=False), "5d 18:53:20"

from datetime import timedelta

assert nice_duration(timedelta(seconds=500000), speech=False) ==  "5d 18:53:20"
```

## Parsing

Extract data from natural language text

### Extract numbers

```python
from lingua_franca.parse import extract_number, extract_numbers

# extract a number
assert extract_number("nothing") is False
assert extract_number("two million five hundred thousand tons of spinning "
                      "metal") == 2500000
assert extract_number("six trillion") == 6000000000000.0
assert extract_number("six trillion", short_scale=False) == 6e+18

assert extract_number("1 and 3/4 cups") == 1.75
assert extract_number("1 cup and a half") == 1.5

## extracts all numbers
assert extract_numbers("nothing") == []
assert extract_numbers("this is a one twenty one  test") == [1.0, 21.0]
assert extract_numbers("1 dog, seven pigs, macdonald had a farm, "
                       "3 times 5 macarena") == [1, 7, 3, 5]
```

### Extract durations

extract datetime.timedelta objects

```python
## extract durations
from lingua_franca.parse import extract_duration
from datetime import timedelta

assert extract_duration("nothing") == (None, 'nothing')

assert extract_duration("Nineteen minutes past the hour") == (
    timedelta(minutes=19),
    "past the hour")
assert extract_duration("wake me up in three weeks, four hundred ninety seven"
                        " days, and three hundred 91.6 seconds") == (
           timedelta(weeks=3, days=497, seconds=391.6),
           "wake me up in , , and")
assert extract_duration(
    "The movie is one hour, fifty seven and a half minutes long") == (
           timedelta(hours=1, minutes=57.5),
           "the movie is ,  long")
```

### Extract dates

extract datetime.datetime objects

```python
## extract date times
from datetime import datetime
from lingua_franca.parse import extract_datetime, normalize

def extractWithFormat(text):
    date = datetime(2017, 6, 27, 13, 4)  # Tue June 27, 2017 @ 1:04pm
    [extractedDate, leftover] = extract_datetime(text, date)
    extractedDate = extractedDate.strftime("%Y-%m-%d %H:%M:%S")
    return [extractedDate, leftover]


def testExtract(text, expected_date, expected_leftover):
    res = extractWithFormat(normalize(text))
    assert res[0] == expected_date
    assert res[1] == expected_leftover


testExtract("now is the time",
            "2017-06-27 13:04:00", "is time")
testExtract("in a couple minutes",
            "2017-06-27 13:06:00", "")
testExtract("What is the day after tomorrow's weather?",
            "2017-06-29 00:00:00", "what is weather")
testExtract("Remind me at 10:45 pm",
            "2017-06-27 22:45:00", "remind me")
testExtract("what is the weather on friday morning",
            "2017-06-30 08:00:00", "what is weather")
testExtract("what is tomorrow's weather",
            "2017-06-28 00:00:00", "what is weather")
testExtract("remind me to call mom next tuesday",
            "2017-07-04 00:00:00", "remind me to call mom")
testExtract("remind me to call mom in 3 weeks",
            "2017-07-18 00:00:00", "remind me to call mom")
testExtract("set an alarm for tonight 9:30",
            "2017-06-27 21:30:00", "set alarm")
testExtract("on the evening of june 5th 2017 remind me to call my mother",
            "2017-06-05 19:00:00", "remind me to call my mother")

```
