---
description: >-
  Skills are like apps for a voice assistant. They give Mycroft access to new
  information and new abilities.
---

# Installing New Skills

{% hint style="info" %}
The [Skills Marketplace](https://market.mycroft.ai/skills) is a curated list of Voice Skills that have been tested and approved by the Mycroft Community.
{% endhint %}

## Voice Installation

The simplest way to install a new Skill is to ask Mycroft to do it for you by saying:

> Hey Mycroft, install {skill name}

This will search the Skills Marketplace and install them on your device.

## Removing a Skill

To remove the Skill, you can say:

> Hey Mycroft, uninstall {skill name}

## Command Line

If you prefer to use the command line, you can directly use the [Mycroft Skills Manager](../skill-development/mycroft-skills-manager/).

To install a Skill run:

```text
mycroft-msm install skill-name
```

To remove a Skill run:

```text
mycroft-msm remove skill-name
```

For more detail on command line usage see:

{% page-ref page="../skill-development/mycroft-skills-manager/" %}

## Troubleshooting

### Command 'mycroft-msm' not found

On Linux, when you type a command into the terminal it uses the `$PATH` environment variable to know where on your system to look for executable files.

You can see the current value of `$PATH`, by running:

```text
echo $PATH
```

It is a list of directories separated by colons, so it might return something like:

```text
/home/gez/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin
```

When you buy a Mycroft device like the Mark II, it comes with your `$PATH` pre-configured so that Mycroft's commands are known to the system. For development installations that use the `dev_setup.sh` script, you are asked if you would like to add the Mycroft commands directory to your `$PATH`. Whether you said no to this question, or it has stopped working for some other reason, it is most likely that your `$PATH` is not configured correctly.

The `mycroft-msm` script, along with all of Mycroft's executables, are contained in the `mycroft-core/bin` directory. If you installed Mycroft in your `$HOME` directory, it will be located at: `/home/username/mycroft-core/bin`.

In the `$PATH` value that we output above, you can see that this directory is not listed. That means it is not in our `$PATH` so the system does not know to look there for commands.

We can add the `mycroft-core/bin` directory to the end of our `$PATH` using the command:

```text
export PATH=$PATH:/home/username/mycroft-core/bin
```

_Note: the path of your directory will depend on where you installed mycroft-core._

This will work in our current shell, but if we close and reopen the terminal window it will be lost. To export our new `$PATH` each time we run the terminal we must add this new line to the `.bashrc` file. This file is run each time we initialize an interactive shell, for example by launching the terminal application. You can open the file and manually add it, or run this command:

```text
echo 'export PATH="$PATH:/home/username/mycroft-core/bin"' >> ~/.bashrc
```

