---
description: >-
  The mycroft-config utility simplifies management of the the various
  configuration files that control Mycroft. Commands include: edit, show, get,
  set, reload.
---

# Configuration Manager

## About Mycroft Configurations

Mycroft configurations are stored in [mycroft.conf](mycroft-conf.md) files. These exist in four locations:

* Default - mycroft-core/mycroft/configuration/mycroft.conf
* Remote - Home.Mycroft.ai
* System - /etc/mycroft/mycroft.conf
* User - $HOME/.mycroft/mycroft.conf

When the configuration loader starts, it looks in these locations in this order, and loads **all** configurations. Keys that exist in multiple configuration files will be overridden by the last file to contain the value.

For example, if your account settings at Home.Mycroft.ai set the `date_format` variable to `MDY`, but the `User` configuration file on your device contains a `date_format` value of `DMY`, the loaded configuration will be `DMY` and dates will be provided in the format "29-11-2018".

This process results in a minimal amount being written for a specific device and user, without modifying default distribution files.

## Why a configuration manager?

When directly editing configuration files it is very easy for even the most careful person to make a minor syntax error. In the past, this has been an extremely common cause of problems. A small error such as a comma in the wrong place breaks your configuration and results in "Mycroft not working".

{% hint style="warning" %}
We strongly recommend that you use the configuration manager rather than directly editing mycroft.conf files.
{% endhint %}

## Available commands

### Get a configuration value

```text
mycroft-config get <var>
```

To display the requested value, this command first loads the mycroft.conf stack, then outputs the effective value\(s\).

The variable is specified using jq-style specifiers. For example:

**Display a specific value**  
`mycroft-config get location.timezone.code`

**Display all values in the location block**  
`mycroft-config get location`

**Display all loaded configuration values**  
`mycroft-config get`

### Set a configuration value

```text
mycroft-config set <var> <value>
```

Set the given variable in the `User` configuration file. For example:

**Set language to es-es"**  
`mycroft-config set lang "es-es"`

**Set the Mimic1 voice to "Alan Pope" aka British Male**  
`mycroft-config set tts.mimic.voice "ap"`

### Edit a configuration file

```text
mycroft-config edit (default|remote|system|user)
```

Open the requested file in an editor \(nano by default\), performing JSON validation warnings to minimize accidental edit errors.

### Show the contents of a configuration file

```text
mycroft-config show (default|remote|system|user)
```

Display the contents of the selected configuration file.

### Reload configuration values

```text
mycroft-config reload
```

Sends a signal on the messagebus telling services to reload the configuration. This automatically occurs after a `set` or `edit` command.

## Further information

For more information on the configuration options available, continue to the [mycroft.conf documentation](mycroft-conf.md).

