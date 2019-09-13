---
description: >-
  Mycroft Skills Manager \(msm\) is a command line tool used to add, manage and remove Skills on any Mycroft installation.
---

# Mycroft Skills Manager

Mycroft Skills Manager \(msm\) is a command line tool used to add, manage and remove **Skills** on any Mycroft installation. It can install any **Skill** listed on the [Mycroft Skills Repository](https://github.com/MycroftAI/mycroft-skills). `msm` is a handy tool for Developers and those who may frequently reconfigure, install and uninstall **Skills**.

## Using Mycroft Skills Manager - msm

`msm` has recently been rewritten in Python \(`msm` was previously a `bash` script\). In order to use `msm`, you will first need to enter the Mycroft _virtual environment_, `venv`, using the following command:

`mycroft-core$ source .venv/bin/activate`

`(.venv) kathyreid@kathyreid-N76VZ:~/mycroft-core$`

If you are using a Picroft or Mark 1 **Device**, you can activate the `.venv` using the command:

`mycroft-core$ source /opt/venvs/mycroft-core/bin/activate`

You can then run `msm`:

`(.venv) kathyreid@kathyreid-N76VZ:~/mycroft-core$ msm update`

To see a list of all the available `msm` commands, type `msm -h`:

```text
(.venv) kathyreid@kathyreid-N76VZ:~/mycroft-core$ msm -h

msm: Mycroft Skill Manager
usage: msm [option] [repo | name]

Options:
  default                  installs the default skills, updates all others
  install <repo>           installs from the specified github repo
  install <name> [name...] installs the mycroft-skill matching <name>
  remove <name> [name...]  removes the specified github repo
  list                     list all mycroft-skills
  update                   update all installed skills
  search <name>            search mycroft-skills for match for <name>
  info <name>              shows information about the skill matching <name>
  info <repo>              shows information about the skill in the specified repo

Params:
  <repo>   full URL to a Github repo
  <name>   one or more substrings to match against submodule names
           in the https://github.com/MycroftAI/mycroft-skills repo

Examples:
  msm search twitter
  msm search date-time-skill
  msm install "daily meditation"
  msm remove "daily meditation"
  msm install https://github.com/penrods/Wink.git
```

For instance to see information on a **Skill**, type:

`msm info mycroft-mark-1`

To list all available **Skills**, type:

`msm list`

This will show available **Skills**, and indicate which ones you have installed:

```text
rss-skill
sentiment-analysis-skill
skill-australian-news [installed]
skill-autogui
skill-caffeinewiz
```

Search is very handy functionality if you're looking for a particular **Skill**:

```text
pi@mark_1:/opt/mycroft/skills $ msm search twitter
Possible match: twitter-skill
```

Update is very handy for updating all the **Skills** on your **Device**:

`msm update`

```text
INFO - Nothing new for mycroft-ip
INFO - Nothing new for mycroft-timer
INFO - Nothing new for mycroft-release-test
INFO - Nothing new for mycroft-weather
INFO - Nothing new for chatbot
INFO - Nothing new for mycroft-speak
INFO - Nothing new for fallback-wolfram-alpha
INFO - Nothing new for mycroft-naptime
INFO - Nothing new for plasma-activities-skill
INFO - Nothing new for mycroft-pairing
```

## `msm` errors

The deprecated version of `msm` had several error codes. Instead, this version relies on standard Python errors.

Here are some common errors, what they mean, and how to resolve them.

### Git authentication failed

```bash
ERROR - Error running update_skill on skill-radio-rne: GitException(Git command failed: GitCommandError(['git', 'fetch'], 128, b"remote: Invalid username or password.nfatal: Authentication failed for 'https://github.com/ChrisFernandez/skill-radio-rne/'", b''))
```

This error usually means that the GitHub repository for the **Skill** no longer exists, or has moved. Remove the **Skill** using `msm remove [Skill Name]` and then install a new **Skill**.

### Uncommitted changes

```bash
ERROR - Error running update_skill on TranslateSkill: SkillModified(Uncommitted changes:
     M requirements.sh
)
```

This error usually means that there is a difference between the **Skill** on the **Device** and the **Skill's** GitHub repo. Try re-installing the **Skill**.

### Git command error - not something we can merge

```bash
ERROR - Error running update_skill on skill-malibu-stacy: GitException(Git command failed: GitCommandError(['git', 'merge', '--ff-only', 'origin/HEAD'], 1, b'merge: origin/HEAD - not something we can merge', b''))
```

This error usually means that there is no `remote url` defined for the Git repoository \(ie. named `origin` - which is the default name of a `remote url`\). This often happens during **Skill** development when `git init` is run _without_ defining a `remote url`. To resolve this error, add a `remote url` using the command `git remote add origin https://github.com/yourGitHubUsername/yourrepo.git`.

### Git command error - failed to update repo

```bash
WARNING - Failed to update repo: GitException(Git command failed: GitCommandError(['git', 'config', 'remote.origin.url', 'https://github.com/MycroftAI/mycroft-skills'], 255, b'error: could not lock config file .git/config: Permission denied', b''))
```

This error usually means that the filesystem permissions of the Skill are incorrect. Manually check, and if necessary, resolve them.

```text
(mycroft-core) pi@picroft:~/skills/reginaneon-av-music.reginaneon $ ls -las
total 48
4 drwxr-xr-x  6 pi      pi      4096 Jul 12 13:11 .
4 drwxrwxrwx 37 mycroft mycroft 4096 Jul 12 13:10 ..
4 drwxr-xr-x  4 pi      pi      4096 Jul 12 13:10 dialog
4 drwxr-xr-x  8 pi      pi      4096 Jul 12 13:10 .git
4 -rw-r--r--  1 pi      pi        20 Jul 12 13:10 .gitignore
4 -rw-r--r--  1 pi      pi      3159 Jul 12 13:10 __init__.py
4 -rw-r--r--  1 pi      pi      1850 Jul 12 13:10 README.md
4 -rw-r--r--  1 pi      pi        77 Jul 12 13:10 requirements.sh
4 -rw-r--r--  1 pi      pi        23 Jul 12 13:10 requirements.txt
4 -rw-r--r--  1 pi      pi        35 Jul 12 13:10 settings.json
4 drwxr-xr-x  3 pi      pi      4096 Jul 12 13:10 test
4 drwxr-xr-x  4 pi      pi      4096 Jul 12 13:10 vocab

(mycroft-core) pi@picroft:~/skills/reginaneon-av-music.reginaneon $ sudo chown -R mycroft:mycroft .
(mycroft-core) pi@picroft:~/skills/reginaneon-av-music.reginaneon $ ls -las
total 48
4 drwxr-xr-x  6 mycroft mycroft 4096 Jul 12 13:11 .
4 drwxrwxrwx 37 mycroft mycroft 4096 Jul 12 13:10 ..
4 drwxr-xr-x  4 mycroft mycroft 4096 Jul 12 13:10 dialog
4 drwxr-xr-x  8 mycroft mycroft 4096 Jul 12 13:10 .git
4 -rw-r--r--  1 mycroft mycroft   20 Jul 12 13:10 .gitignore
4 -rw-r--r--  1 mycroft mycroft 3159 Jul 12 13:10 __init__.py
4 -rw-r--r--  1 mycroft mycroft 1850 Jul 12 13:10 README.md
4 -rw-r--r--  1 mycroft mycroft   77 Jul 12 13:10 requirements.sh
4 -rw-r--r--  1 mycroft mycroft   23 Jul 12 13:10 requirements.txt
4 -rw-r--r--  1 mycroft mycroft   35 Jul 12 13:10 settings.json
4 drwxr-xr-x  3 mycroft mycroft 4096 Jul 12 13:10 test
4 drwxr-xr-x  4 mycroft mycroft 4096 Jul 12 13:10 vocab
```

## Other techniques to resolve Skill installation dependencies

### Forcing the re-installation of dependencies

If you're still running into trouble with dependencies, which can happen during Skill Authoring, there are some other techniques available.

To trigger a `pip` re-installing **Skill** dependencies, do the following:

* Remove the `/home/mycroft/.mycroft/.mycroft-skill` file
* Remove the `/opt/mycroft/skills/.msm` file
* Restart the `mycroft-skills` service by using the command `sudo service mycroft-skills restart`

This will force both a **Skills** update and the re-installation of dependencies when the `mycroft-skills` service is re-started.

You can also use the utility `mycroft-pip` which will install dependencies into the Mycroft _virtual environment_ without activation \(ie. the 'activate' command\). Use `mycroft-pip` as you would regular `pip` for installing Python libraries on which your **Skill** depends.
