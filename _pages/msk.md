---
ID: 38649
post_title: Mycroft Skills Kit – msk
author: Kathy Reid
post_excerpt: 'Learn how to use the Mycroft Skills Kit - msk - to make the creation, testing and submission of Skills a lot easier. '
layout: page
permalink: >
  http://mycroft.ai/documentation/skills/msk/
published: true
post_date: 2018-06-06 12:29:25
---
# Mycroft Skills Kit - msk

## Introduction

The Mycroft Skills Kit - `msk` - is a Python-based utility that has been created to make it easier for **Skill** Authors to create, test and submit **Skills** to the [Mycroft Skills Repo](https://github.com/mycroftai/mycroft-skills). We hope this utility helps to shorten the development cycle, and remove some of the tedious parts of **Skill** creation.

`msk` currently supports the following features:

- Create a new **Skill**
- Create an `Intent` test for a **Skill**
- Upload a **Skill**
- Upgrade an existing **Skill**

## Installing msk

_NOTE: `msk` has only been tested on Linux systems_

`msk` comes pre installed on the [Mark 1](https://mycroft.ai/documentation/mark-1), [Picroft](https://mycroft.ai/documentation/picroft) and in the `venv` of the Mycroft `git` installation as of v18.2.9b. The utility is self-contained and can be installed separately using `pip` by typing the following line into the terminal on your Linux system:

```bash
pip3 install msk
```

You should then see output like the below:

```bash
Collecting msk
  Downloading https://files.pythonhosted.org/packages/69/d9/1d41acac01b1e6f9004963606f0b9f939a917e240a955a657f6dc1844836/msk-0.3.8.tar.gz
Collecting GitPython (from msk)
  Using cached https://files.pythonhosted.org/packages/ac/c9/96d7c86c623cb065976e58c0f4898170507724d6b4be872891d763d686f4/GitPython-2.1.10-py2.py3-none-any.whl
Collecting typing (from msk)
  Using cached https://files.pythonhosted.org/packages/05/2b/2b05bf1d5a9dd450447c9a5df3e118a465e5d3cb12b73b7220a5064a403f/typing-3.6.4-py3-none-any.whl
Collecting msm>=0.5.13 (from msk)
Collecting pygithub (from msk)
Collecting gitdb2>=2.0.0 (from GitPython->msk)
  Using cached https://files.pythonhosted.org/packages/e0/95/c772c13b7c5740ec1a0924250e6defbf5dfdaee76a50d1c47f9c51f1cabb/gitdb2-2.0.3-py2.py3-none-any.whl
Collecting pyjwt (from pygithub->msk)
  Using cached https://files.pythonhosted.org/packages/93/d1/3378cc8184a6524dc92993090ee8b4c03847c567e298305d6cf86987e005/PyJWT-1.6.4-py2.py3-none-any.whl
Collecting smmap2>=2.0.0 (from gitdb2>=2.0.0->GitPython->msk)
  Using cached https://files.pythonhosted.org/packages/e3/59/4e22f692e65f5f9271252a8e63f04ce4ad561d4e06192478ee48dfac9611/smmap2-2.0.3-py2.py3-none-any.whl
Building wheels for collected packages: msk
  Running setup.py bdist_wheel for msk ... done
  Stored in directory: /home/kathyreid/.cache/pip/wheels/b8/d7/7d/c650d047645e875a4c301821844ded868db716b877fdae8b9b
Successfully built msk
Installing collected packages: smmap2, gitdb2, GitPython, typing, msm, pyjwt, pygithub, msk
Successfully installed GitPython-2.1.10 gitdb2-2.0.3 msk-0.3.8 msm-0.5.14 pygithub-1.39 pyjwt-1.6.4 smmap2-2.0.3 typing-3.6.4
```

To check that the installation was successful `msk --help` can be run and should list the arguments and options for the utility.


## Usage

```bash
msk create
msk create-test /opt/mycroft/skills/myskill
msk upload /opt/mycroft/skills/myskill
msk upgrade /opt/mycroft/skills/myskill
```

## Create

Please see this ASCII Cinema video to see the process for using `msk create`:

[![msk-create](https://images2.imgbox.com/ab/25/6kbqKbXh_o.gif)](https://asciinema.org/a/X5pWLPOpsMLUPYp5kgswNm5Zu?speed=1.5)

If using the msk delivered with the mycroft-core github installation the Python _virtual environment_ needs to be activated. From the mycroft-core directory run

`$ source .venv/bin/activate`

Next, we use the `msk create` function. You will be prompted to enter the required information to help set up your **Skill**.

```bash
$ msk create
Enter a short unique skill name (ie. "siren alarm" or "pizza orderer"):
Feed the Corgi

Class name: FeedTheCorgiSkill
Repo name: feed-the-corgi-skill

Looks good? (Y/n) Y
Enter a one line description for your skill (ie. Orders fresh pizzas from the store): Reminds you to feed your poor starving Corgi
Enter a long description:
> Every 24 hours, Mycroft will send you a reminder to feed your Corgi, and tell you what your Corgi was fed the previous day, so you can provide a different delicious meal for your precious Corgi.
>
Enter some example phrases to trigger your skill:
- Have I fed the Corgi today
- What did I feed the Corgi yesterday
- Remind me to feed the Corgi at 5pm
-
Enter author: YourGitHubUserName
Would you like to create a GitHub repo for it? (Y/n) Y
=== GitHub Credentials ===
Username: YourGitHubUserName
Password:  
Counting objects: 12, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (12/12), 1.44 KiB | 0 bytes/s, done.
Total 12 (delta 0), reused 0 (delta 0)
To https://github.com/YourGitHubUserName/feed-the-corgi-skill
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
Created GitHub repo: https://github.com/YourGitHubUserName/feed-the-corgi-skill
Created skill at: /opt/mycroft/skills/feed-the-corgi-skill
```

Now, if you look in `/opt/mycroft/skills/` you will see that all the files required for the **Skill** have now been created, including the `.voc` files.

```bash
$ ls -las /opt/mycroft/skills/feed-the-corgi-skill
total 36
4 drwxrwxr-x   5 kathyreid kathyreid 4096 Jun  7 05:20 .
4 drwxr-xr-x 103 kathyreid kathyreid 4096 Jun  7 05:18 ..
4 drwxrwxr-x   3 kathyreid kathyreid 4096 Jun  7 05:20 dialog
4 drwxrwxr-x   8 kathyreid kathyreid 4096 Jun  7 05:20 .git
4 -rw-rw-r--   1 kathyreid kathyreid   21 Jun  7 05:20 .gitignore
4 -rw-rw-r--   1 kathyreid kathyreid  379 Jun  7 05:18 __init__.py
4 -rw-rw-r--   1 kathyreid kathyreid  434 Jun  7 05:20 README.md
4 -rw-rw-r--   1 kathyreid kathyreid 1301 Jun  7 05:20 settingsmeta.json
4 drwxrwxr-x   3 kathyreid kathyreid 4096 Jun  7 05:20 vocab
```

```bash
$ ls -las /opt/mycroft/skills/feed-the-corgi-skill/vocab/en-us/
total 12
4 drwxrwxr-x 2 kathyreid kathyreid 4096 Jun  7 05:20 .
4 drwxrwxr-x 3 kathyreid kathyreid 4096 Jun  7 05:20 ..
4 -rw-rw-r-- 1 kathyreid kathyreid   16 Jun  7 05:20 corgi.the.feed.intent

```

## Create test

`msk` also provides a function for creating `Intent` tests, as part of our [Automated Testing for Skills](https://mycroft.ai/documentation/skills/automatic-testing/).

Please see this ASCII Cinema video to see the process for using `msk create-test`:

[![msk-create-test](https://images2.imgbox.com/9c/c8/gLRS7xuL_o.gif)](https://asciinema.org/a/Ayzaj6QJbKGBfs2eIQWr11idH?speed=1.5)

As before if the mycroft-core github installation is used make sure to activate the mycroft-core Python _virtual environment_. From the mycroft-core folder

`$ source .venv/bin/activate`

Next, we use the `msk create-test` function. You _must_ pass the **Skill** directory location to the command, or it will fail.

```bash
$ msk create-test /opt/mycroft/skills/feed-the-corgi-skill/

Which intent would you like to test?
1. corgi.the.feed.intent

> 1

=== Intent Examples ===
Corgi the feed

Enter an example query: have I fed the corgi today?

Choose expected dialog (leave empty to skip).
1. corgi.the.feed

> 1
Generated test file: /opt/mycroft/skills/feed-the-corgi-skill/test/intent/corgi.the.feed.intent.0.intent.json
```

If we have a look inside the `corgi.the.feed.intent.0.intent.json` file we can see that the test has been created for us.

```json
$ cat /opt/mycroft/skills/feed-the-corgi-skill/test/intent/corgi.the.feed.intent.0.intent.json
{
    "intent_type": "corgi.the.feed",
    "expected_dialog": "corgi.the.feed",
    "utterance": "have I fed the corgi today?"
}
```

## Upload Skill

`msk` also provides a function for uploading a **Skill** to the [Mycroft Skills Repo](https://github.com/mycroftai/mycroft-skills), as part of our [Skill Submission Process] (https://mycroft.ai/documentation/skills/skill-submission/).

Please see this ASCII Cinema video to see the process for using `msk upload`:

[![msk-upload](https://images2.imgbox.com/35/5d/BCVxUxuh_o.gif)](https://asciinema.org/a/Bp1sORVnmVz9wYjZXfempTPoO?speed=1.5)

If using the msk delivered with the mycroft-core github installation the Python _virtual environment_ needs to be activated. From the mycroft-core directory run

`$ source .venv/bin/activate`

Next, we use the `msk upload` command with the path to the **Skill**:

```bash
$ msk upload /opt/mycroft/skills/feed-the-corgi-skill/
=== GitHub Credentials ===
Username: YourGitHubUserName
Password:
Enter a unique skill name (ie. npr-news or grocery-list): feed-the-corgi
Counting objects: 531, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (339/339), done.
Writing objects: 100% (531/531), 123.54 KiB | 0 bytes/s, done.
Total 531 (delta 298), reused 304 (delta 177)
remote: Resolving deltas: 100% (298/298), completed with 6 local objects.
To https://github.com/KathyReid/mycroft-skills
 * [new branch]      add/feed-the-corgi -> add/feed-the-corgi
Branch add/feed-the-corgi set up to track remote branch add/feed-the-corgi from fork.
Created pull request:  https://github.com/MycroftAI/mycroft-skills/pull/392
```
