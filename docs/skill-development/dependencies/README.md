---
description: >-
  Mycroft Skills are powerful because we can make use of external packages and
  applications, or add voice interfaces to existing tools.
---

# Dependencies

There are three main categories of dependencies:

* Python packages sourced from [PyPI](https://pypi.org/).
* Linux system packages sourced from the repositories available on the Mycroft device.
* Other Mycroft Skills source from the [Skills Marketplace](https://market.mycroft.ai/).

Some of these may already be installed on a Users device, however some may not. To make sure a system has everything that your Skill needs, we can define the dependencies or requirements of the Skill. During installation the Mycroft Skills Manager will then check that they are installed, and if not attempt to do so.

There are three files that we can use to define these dependencies.

`manifest.yml` is the default method. This can include all three types of dependencies including variations for different operating systems if required.

{% page-ref page="manifest-yml.md" %}

`requirements.txt` can be used only for Python packages.

`requirements.sh` is used to run a custom script during installation.

{% page-ref page="requirements-files.md" %}

Which ever file you choose to use, it must be located in the root directory of your Skill.

There is no limit to the number of packages you can install, however these are reviewed during the [Skills Acceptance Process](../marketplace-submission/skills-acceptance-process/) to ensure they are appropriate for the Skill being installed and do not pose a security concern for Users.

