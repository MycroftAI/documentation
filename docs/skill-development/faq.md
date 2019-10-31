# FAQ

## How do I disable a Skill?

During Skill development you may have reason to disable one or more Skills. Rather than constantly install or uninstall them via voice, or by adding and removing them from `/opt/mycroft/skills/`, you can disable them in [the `mycroft.conf` file](https://mycroft.ai/documentation/mycroft-conf/).

First, identify the name of the Skill. The name of the Skill is the `path` attribute in the [`.gitmodules`](https://github.com/MycroftAI/mycroft-skills/blob/master/.gitmodules) file.

To disable one or more Skills on a Mycroft Device, find where your `mycroft.conf` file is stored, then edit it using an editor like `nano` or `vi`.

Search for the string `blacklisted` in the file. Then, edit the line below to include the Skill you wish to disable, and save the file. You will then need to reboot, or restart the `mycroft` services on the Device.

```text
  "skills": {
    "blacklisted_skills": ["skill-media", "send_sms", "skill-wolfram-alpha, YOUR_SKILL"]
  }
```

## How do I increase the priority of Skills during loading?

During Skill development, you may wish to increase the priority of your Skill loading during the startup process. This allows you to start using the Skill as soon as possible.

First, identify the name of the Skill. The name of the Skill is the `path` attribute in the [`.gitmodules`](https://github.com/MycroftAI/mycroft-skills/blob/master/.gitmodules) file.

To prioritize loading one or more Skills on a Mycroft Device, find where your [`mycroft.conf` file](https://mycroft.ai/documentation/mycroft-conf/) is stored, then edit it using an editor like `nano` or `vi`.

Search for the string `priority` in the file. Then, edit the line below to include the Skill you wish to prioritize, and save the file. You will then need to reboot, or restart the `mycroft` services on the Device.

```text
"priority_skills": ["skill-pairing"],
```

## How do I find more information on Mycroft functions?

You can find documentation on Mycroft functions and helper methods at the [Mycroft Core API documentation](https://mycroft-core.readthedocs.io/en/master/)

