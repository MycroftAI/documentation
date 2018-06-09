# Configuring some of the “nice” functions for a language

The following functions are found in mycroft.util.

* ```nice_date(dt, lang='en-us', now=None)```
* ```nice_date_time(dt, lang='en-us', now=None, use_24hour=False, use_ampm=False)```
* ```nice_year(dt, lang='en-us', bc=False)```

Their purpose is to convert a Python datetime to a pronounceable string, for a given language [please refer to the Mycroft API documentation](http://mycroft-core.readthedocs.io/en/stable/))
The output of the functions above are determined by a configuration file.

This page describe how to add a new language, or change configuration for an existing language.

It also contains a reference to the python file where unit tests for a new language is to be placed.


# Configuration files in the file system
Each language has a configuration file. The configuration files is written in json. The configurations are placed in: ```mycroft/res/text/<language>/date_time.json```

For example: ```mycroft/res/text/en-us/date_time.json```

The nice_date_and_time() depends on mycroft.util.nice_time(), which must be able to support the selected language.

# The configuration file
The section [Configuration file for en-us](# Configuration file for en-us) contains an example configuration file.
The configuration file contains several main sections, some of which contains maps from numbers to words to be spoken, others containing the format template to use when the pronounceable string is created.

The template sections are:
* year_format
* date_format
* date_time_format

The map sections are:
* weekday
* date
* month

The format templates takes a number of arguments. The arguments are substituted by a value calculated by the “nice_*()” function.

For instance
```
"date_full_no_year_month": "{weekday}, the {day}"
```
could result in "Monday the third"

Some formats change, depending on the value to be formatted. Take year 2000 as an example. In English, it will usually be pronounced as “two-thousand”. But in some English speaking countries, the year 2011 is pronounced “twenty-eleven” (and not two-thousand-eleven). This is handled by using a “default” format as fall back, and a number of additional formats, that apply to specific intervals. For some formats a fixed selection exist, for other formats an open ended number of formats can be specified, akin to a list.

In the following paragraphs, each section of the json file is explained, in particular which arguments that are recognized, and what formats are available.

## The year_format section
This section contains information on how to format a pronounceable year.
### Arguments to format templates

* {century} : The datetime century as digits
* {decade}: The datetime decade as digits
* {year}: The datetime year as digits
* {bc}: A string to apply for years B.C.

Example:
“{century}:{decade}” will convert a datetime(....) to “19:84”. Which Mycroft can pronounce (the colon is omitted when speaking). Note that the formatting string may contain none or only a subset of the available arguments. {year} is not used above.

### Formats

* “default”:  The default fall back format if other formats does not apply (mandatory)
* A number (e.g. “1”): An entry in an open ended list of formats with “from” and “to” year (optional)
* “bc”: The string used when a year is B.C. (mandatory)


Example:
```json
"year_format": {
  "1": { "from": "1001", "to": "1999", "format": "{century}:{decade} {bc}" },
  "default": "{year} {bc}",
  "bc": "b.c."
}
```
The above example is for language “en-us”.
The “1” is the first element on a list (with only one element). If the year is between 1001 and 1999 inclusive, the resulting date for datetime(1984,1,1) is "19:84". The first element in the list must be “1”, the second “2” and so on in sequence.
The "default" is that datetime(2002,1,1) produce "2002"
If the nice_year() function is called with bc=True, and datetime(87,1,1) will give "87 b.c."

## The date_format section
### Arguments to format templates
* {weekday}: The weekday, formatted according to (The weekday section)[## The weekday section]
*  {month}: The month, formatted according to (The month section)[## The month section]
* {day}: The day of the month, formatted according to (The date section)[## The date section]
* {formatted_year}: The year formatted like in (The year_format section)[## The year_format section]


### Formats
* "date_full": A format containing a full date (mandatory)
* "date_full_no_year": A format without the year, used if the "now" date parameter is set, and if "now" is in the same year as the date. (mandatory)
* "date_full_no_year_month": A format without the year and month, used if the "now" date parameter is set, and if "now" is in the same year and month as the date. (mandatory)
* "today": The word for today, used if the "now" date parameter is set, and if "now" is in the same year and month and day as the date. (mandatory)
* "tomorrow": The word for tomorrow, used if the "now" date parameter is set, and if "now" is in the same year and month, but one day before the day in the date. (mandatory)
* "yesterday": The word for yesterday, used if the "now" date parameter is set, and if "now" is in the same year and month, but one day after the day in the date. (mandatory)

Example:
```json
"date_format": {
  "date_full": "{weekday}, {month} the {day}, {formatted_year}",
  "date_full_no_year": "{weekday}, {month} the {day}",
  "date_full_no_year_month": "{weekday}, the {day}",
  "today": "today",
  "tomorrow": "tomorrow",
  "yesterday": "yesterday"
}
```

If your language don't have, for instance, a tradition for saying yesterday, it is of cause possible to use arguments here instead. For example:
```json
"yesterday": "{weekday}, {month} the {day}, {formatted_year}"
```
will create the same output as "date_full" above, in case of yesterday.


## The date time section
### Arguments to format templates
* {formatted_date}: Date formatted as specified in the "date_format" section (mandatory)
* {formatted_time}: Time formatted by nice_time(), [please refer to the Mycroft API documentation](http://mycroft-core.readthedocs.io/en/stable/)

### Formats
* "date_time_format": The date time format (mandatory)

Example:
```json
"date_time_format": {
  "date_time": "{formatted_date} at {formatted_time}"
}
```

# Maps
## The weekday section
A map from the day number in the week to the pronounceable weekday name

## The date section
A map from date as a number to a pronounceable date

## The month section
A map from the month number to a pronounceable month

# Configuration file for en-us
```json
{
  "year_format": {
    "1": { "from": "1001", "to": "1999", "format": "{century}:{decade} {bc}" },
    "default": "{year} {bc}",
    "bc": "b.c."
  },
  "date_format": {
    "date_full": "{weekday}, {month} the {day}, {formatted_year}",
    "date_full_no_year": "{weekday}, {month} the {day}",
    "date_full_no_year_month": "{weekday}, the {day}",
    "today": "today",
    "tomorrow": "tomorrow"
  },
  "date_time_format": {
    "date_time": "{formatted_date} at {formatted_time}"
  },
  "weekday": {
    "0": "monday",
    "1": "tuesday",
    "2": "wednesday",
    "3": "thursday",
    "4": "friday",
    "5": "saturday",
    "6": "sunday"
  },
  "date": {
    "1": "first",
    "2": "second",
    "3": "third",
    "4": "fourth",
    "5": "fifth",
    "6": "sixth",
    "7": "seventh",
    "8": "eighth",
    "9": "ninth",
    "10": "tenth",
    "11": "eleventh",
    "12": "twelfth",
    "13": "thirteenth",
    "14": "fourteenth",
    "15": "fifteenth",
    "16": "sixteenth",
    "17": "seventeenth",
    "18": "eighteenth",
    "19": "nineteenth",
    "20": "twentieth",
    "21": "twenty-first",
    "22": "twenty-second",
    "23": "twenty-third",
    "24": "twenty-fourth",
    "25": "twenty-fifth",
    "26": "twenty-sixth",
    "27": "twenty-seventh",
    "28": "twenty-eighth",
    "29": "twenty-ninth",
    "30": "thirtieth",
    "31": "thirty-first"
  },
  "month": {
    "1": "january",
    "2": "february",
    "3": "march",
    "4": "april",
    "5": "may",
    "6": "june",
    "7": "july",
    "8": "august",
    "9": "september",
    "10": "october",
    "11": "november",
    "12": "december"
  }
}

```

# Unit testing
A new language require new unit tests, to ensure that the configuration loads, and that it produce correct results.

The file containing the unit tests can be found at:
```
test/unittest/util/test_format.py
```
If you want to create a configuration file for new language, but you are uncomfortable about making unit tests, or about adding to Mycroft-core in general, then get in touch at the forum or at Mattermost. Many community members will be happy to help, but may lack the knowledge about your language.
