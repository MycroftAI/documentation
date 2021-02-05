---
description: Troubleshooting guide for the Mycroft Skills Manager.
---

# Troubleshooting

## mycroft-msm: command not found

Mycroft provides helper commands for common utilities like MSM. On most systems MSM should be accessible using `mycroft-msm`. If this command is not available on your system then you have two options:

1. Use the full path of the helper command:

   ```text
   /home/user/mycroft-core/bin/mycroft-msm
   ```

2. Add `mycroft-core/bin` to your `$PATH` To have it permanently added to your `$PATH`, add a new line to your `.bashrc` file. Assuming you installed mycroft-core in your home directory, from your terminal run:

   ```text
   echo "PATH=$PATH:$HOME/mycroft-core/bin" >> $HOME/.bashrc
   source $HOME/.bashrc
   ```

3. Or activate Mycroft's virtual environment by running:

   ```text
   cd /home/user/mycroft-core
   source .venv/bin/activate
   ```

   **Git authentication failed**

```bash
ERROR - Error running update_skill on skill-radio-rne: GitException(Git command failed: GitCommandError(['git', 'fetch'], 128, b"remote: Invalid username or password.nfatal: Authentication failed for 'https://github.com/user/my-skill/'", b''))
```

This error usually means that the GitHub repository for the Skill no longer exists, or has moved. Remove the Skill using `msm remove [Skill Name]` and then install a new Skill.

## Uncommitted changes

```bash
ERROR - Error running update_skill on TranslateSkill: SkillModified(Uncommitted changes:
     M requirements.sh
)
```

This error usually means that there is a difference between the Skill on the Device and the Skill's GitHub repo.

If Mycroft detects that something has change in your Skill, it will stop updating to prevent loss of any work you are doing in that directory. If you are no longer making changes you can checkout the default branch of the Skill, or `git stash` any changes you've made to get it back to a clean state.

If you continue to get this error you can also delete the Skill and reinstall it.

## Git command error - not something we can merge

```bash
ERROR - Error running update_skill on skill-malibu-stacy: GitException(Git command failed: GitCommandError(['git', 'merge', '--ff-only', 'origin/HEAD'], 1, b'merge: origin/HEAD - not something we can merge', b''))
```

This error usually means that there is no `remote url` defined for the Git repository \(ie. named `origin` - which is the default name of a `remote url`\). This can happen during Skill development when `git init` is run _without_ defining a `remote url`. To resolve this error, add a `remote url` using the command `git remote add origin https://github.com/yourGitHubUsername/yourrepo.git`.

## Git command error - failed to update repo

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

## Where to go for more assistance

Join us in the [Skills Mycroft Chat room](https://chat.mycroft.ai/community/channels/skills) or join us in the [Mycroft Forum](https://community.mycroft.ai).

