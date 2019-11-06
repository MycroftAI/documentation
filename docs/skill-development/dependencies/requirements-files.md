---
description: >-
  A Skill's `requirements.txt` and `requirements.sh` files provide an
  alternative method to define the dependencies of a Mycroft Skill.
---

# Requirements files
The older method of defining requirements is still available, and is present in the majority of Skills available in the Marketplace. This uses a `requirements.txt` and/or `requirements.sh` file.

## requirements.txt

The `requirements.txt` file can only be used to define Python package dependencies. It uses the [standard Python PIP format](https://pip.readthedocs.io/en/1.1/requirements.html) to list Python packages from [PyPI](https://pypi.org/) to install. Each line in the file represents a separate package to install and must match the title provided by PyPI.

The following example will install the latest available versions of the [`requests`](https://pypi.org/project/requests/) and [`gensim`](https://pypi.org/project/gensim/) packages.

```txt
requests
gensim
```

If specific versions of a package are required, we can use comparison operators to indicate which version.
- `requests==2.22.0`   
  The package must must be version `2.22.0`.

- `requests>=2.22.0`  
  The package must be version `2.22.0` or higher.

- `requests<=2.22.0`  
  The package must be version `2.22.0` or lower.

### Examples of requirements.txt
- [Weather Skill](https://github.com/MycroftAI/skill-weather/blob/19.08/requirements.txt)
- [Wiki Skill](https://github.com/MycroftAI/skill-wiki/blob/19.08/requirements.txt)

## requirements.sh

The `requirements.sh` file may contain a shell script that is run during installation of the Skill. Shell scripting is beyond the scope of these documents, however there are many tutorials available online.

Prior to the `manifest.yml` file, this was the only method available to install system packages. If you are only installing packages, using the [`manifest.yml`](manifest-yml.md) file instead is recommended.

The contents of this file will be checked carefully if a Skill is submitted for inclusion in the [Skills Marketplace](https://market.mycroft.ai)

### Examples of requirements.sh
- [Zork (adventure game)](https://github.com/forslund/white-house-adventure/blob/6eba5df187bc8a7735b05e93a28a6390b8c6f40c/requirements.sh)
