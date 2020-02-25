---
description: >-
  Mycroft Skills are powerful because we can make use of external packages and
  applications, or add voice interfaces to existing tools.
---

# Dependencies

There are three main categories of dependencies:

* Python packages sourced from [PyPI](https://pypi.org/).
* Linux system packages sourced from the repositories available on the Mycroft device.
* Other Mycroft Skills sourced from the [Skills Marketplace](https://market.mycroft.ai/).

Some of these may already be installed on a Users device, however some may not. To make sure a system has everything that your Skill needs, we can define the dependencies or requirements of the Skill. During installation the Mycroft Skills Manager will then check that they are installed, and if not attempt to do so.

There are three files that we can use to define these dependencies.

## Recommended

`manifest.yml` is the default method. This can include all three types of dependencies including variations for different operating systems if required.

{% page-ref page="manifest-yml.md" %}

## Alternatives

`requirements.txt` can be used only for Python packages.

`requirements.sh` is used to run a custom script during installation.

{% page-ref page="requirements-files.md" %}

Which ever file you choose to use, it must be located in the root directory of your Skill.

There is no limit to the number of packages you can install, however these are reviewed during the [Skills Acceptance Process](../marketplace-submission/skills-acceptance-process/) to ensure they are appropriate for the Skill being installed and do not pose a security concern for Users.

## Manual installation

The files outlined above ensure that dependencies are available on devices when a Skill is being installed by the Mycroft Skills Manager. If you are developing the Skill on your own machine, you may need to install these dependencies manually.

System packages can be installed using your standard package manager, for example:

```bash
apt install system-package-name
```

Mycroft Skills can be installed using the Mycroft Skills Manager:

```bash
mycroft-msm install required-skill-name
```

Python packages must be installed in the Mycroft virtual environment. The simplest way to do this is using the helper command `mycroft-pip` located in `mycroft-core/bin/`

During installation you may have selected to add this directory to your PATH in which case you can run it from anywhere.

```bash
mycroft-pip install python-package-name
```

If you don’t want to use the helper commands you can activate the virtual environment and install the packages using the PIP:

```bash
cd ~/mycroft-core        # or whereever you cloned Mycroft-core
source venv-activate.sh  # activate the virtual environment
pip install python-package-name
deactivate               # to exit the virtual environment again
```

If you have already defined your Python package dependencies, you can use the `pip -r` flag to install all of these at once:

```bash
cd /opt/mycroft/skills/my-skill
mycroft-pip install -r requirements.txt
```



