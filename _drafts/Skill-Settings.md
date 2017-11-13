---
ID: 32919
post_title: Skill Settings
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?page_id=32919
published: false
---
# Skill Settings

Have you ever wanted to store settings for a **Skill** locally to a Device? For instance, you might want the User to specify a preference the first time they use a **Skill**, and then store that preference for subsequent uses.

**Skill Settings** provide this ability.

They are a simple extension of the [Python `dict`](https://docs.python.org/2/library/stdtypes.html#typesmapping) that enables local storage of settings. Skill settings can be accessed from the `MycroftSkill` class. Skill settings can also interact with a backend system to provide a graphical user interface (GUI) for Skills configuration. Skills configuration is done through metadata described in an optional `settingsmeta.json` file.

## How do I use Skill Settings?

**Skill Settings** inherit from a Python `dict`. This means that you can use it just like you would any other Python dictionary.

```python
print self.settings.get('meaning of life') # outputs None... oh.. :(
self.settings['meaning of life'] = 42
print self.settings.get('meaning of life') # outputs 42! yay
```
### More information on Skill Settings

## settings.json

The `settings.json` file is created at the root level of the **Skill's** directory. The file is created when a **Skill** uses the **Skill Settings** feature.

Here is an example directory listing of a **Skill** that has a `settings.json` file:

```bash
kathyreid@kathyreid-N76VZ:/opt/mycroft/skills/brain-skill$ ls -las
total 144
 4 drwxrwxr-x  3 kathyreid kathyreid  4096 Nov 13 23:22 .
 4 drwxr-xr-x 29 kathyreid kathyreid  4096 Nov 13 23:19 ..
 8 -rw-rw-r--  1 kathyreid kathyreid  7145 Nov 13 23:19 abilities.py
12 -rw-rw-r--  1 kathyreid kathyreid  8366 Nov 13 23:20 abilities.pyc
 4 drwxrwxr-x  8 kathyreid kathyreid  4096 Nov 13 23:19 .git
 4 -rw-rw-r--  1 kathyreid kathyreid    20 Nov 13 23:19 .gitignore
12 -rw-rw-r--  1 kathyreid kathyreid 11254 Nov 13 23:19 __init__.py
12 -rw-rw-r--  1 kathyreid kathyreid 10799 Nov 13 23:20 __init__.pyc
36 -rw-rw-r--  1 kathyreid kathyreid 34520 Nov 13 23:19 LICENSE
 4 -rw-rw-r--  1 kathyreid kathyreid  2236 Nov 13 23:19 README.md
16 -rw-rw-r--  1 kathyreid kathyreid 15086 Nov 13 23:19 remiface.py
 4 -rw-rw-r--  1 kathyreid kathyreid   980 Nov 13 23:19 requirements.sh
 4 -rw-rw-r--  1 kathyreid kathyreid    22 Nov 13 23:19 requirements.txt
 4 -rw-rw-r--  1 kathyreid kathyreid    19 Nov 13 23:22 settings.json <-- SETTINGS FILE
 8 -rw-rw-r--  1 kathyreid kathyreid  4567 Nov 13 23:19 utils.py
 8 -rw-rw-r--  1 kathyreid kathyreid  4348 Nov 13 23:20 utils.pyc
```

When a **Skill** is shut down - which usually happens when restarting a service, or reloading a **Skill** - it will create a `settings.json` file and store the `dict` data there. When a **Skill** loads, it reads the `settings.json` file and loads the settings into the **Skill**. Knowing this makes it easier to build and test **Skills**, because you can create the `settings.json` file first with settings in it, and use these in your Skills development, and then add in code later on that _writes_ to `settings.json`.

## Web configurable Settings with `settingsmeta.json`

For some **Skills**, the User may need to configure them before they are usable. Examples include **Skills** where an API token or login is required.

This functionality is provided by the `settingsmeta.json` file. This file defines settings and their values that the User can configure on [home.mycroft.ai](https://home.mycroft.ai). Mycroft will automatically synchronize the `settings.json` file with the settings that the User can configure on [home.mycroft.ai](https://home.mycroft.ai).

To use this feature, you need to have a `settingsmeta.json` file in the root directory of the **Skill**. The `settingsmeta.json` file _must_ follow a specific structure.

Below is an example of this structure from the `pianobar-skill`. You can see the [code for this **Skill**](https://github.com/ethanaward/pianobar-skill) - it has excellent example on how to use web configurable **Skill Settings**.

```json
{
    "name": "Pandora",
    "skillMetadata": {
        "sections": [
            {
                "name": "Login",
                "fields": [
                    {
                        "name": "email",
                        "type": "email",
                        "label": "Email",
                        "value": ""
                    },
                    {
                        "name": "password",
                        "type": "password",
                        "label": "Password",
                        "value": ""
                    }
                ]
            }
        ]
    }
}
```
### More information on the `settingsmeta.json` file

#### name (String)
The display name for this **Skill Setting** block. This will be shown on the [home.mycroft.ai](https://home.mycroft.ai) Skills page. The `name` can be multiple words, but should display on a single line.

#### skillMetadata (Object)
An Object containing one or more `sections` elements.

#### sections (Array)
An Array containing each of the elements the **Settings** needs to function.

#### sections > name (String)
The group name used as a display lable on the [home.mycroft.ai](https://home.mycroft.ai) Skills page.

#### sections > fields (Array)
Array of Field Objects. Each Field Object takes four properties:

* sections > fields > field > name	(String)

The `name` of the `field` is used by the **Skill** to set the value of the `field`. Not defined for `field` > `type` = "Label". The generated `settings.json` file will use this name for the entered data.

* sections > fields > field > label	(String)

Text to be displayed above the data entry box on the **Skills** page on home.mycroft.ai (or by itself, for `field` > `type` = "Label").

* sections > fields > field > type	(Enum)

_NOTE: Any combination of uppercase and/or lowercase is acceptable._
The data type of this field. The supported types are:

  * Text: (any kind of text)
  * Email: (text validated as an email address)
  * Number: (text validated as a number)
  * Password: (text hidden from view by default)

* sections > fields > field > value	(String)

_Optional_
The initial value for the field.

* sections > fields > field > placeholder (String)

_Optional_
Placeholder text to show before data is entered in the field (or possibly as a tooltip)