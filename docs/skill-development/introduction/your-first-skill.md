---
description: >-
  Ready to create your first Skill? See how easy it is to get a new Skill up and
  running, then we will step through the basic anatomy of a Mycroft Skill.
---

# Your First Skill

## Prerequisites

If you haven't already, check out our [Introduction to Skill Development](./). This walk through assumes you:

* Know some basic knowledge of [Python programming](https://www.python.org),
* have an account on [Github.com](https://github.com), and
* have a [working version of Mycroft](../../using-mycroft-ai/get-mycroft/).

## Understand the flow of your Skill

It's a good idea to start by writing down how your Skill will work, including

* What words will the User speak to activate the Skill?
* What will Mycroft speak in response?
* What data will you need to deliver the Skill?
* Will you need any additional packages or dependencies?

Once you've given these some thought, you can get started.

## Mycroft Skills Kit (MSK)

{% embed url="https://www.youtube.com/watch?v=YNoWpRyx26A" %}
Video Tutorial: Mycroft Skills Kit
{% endembed %}

To setup the foundations of your Skill, we will use the [Mycroft Skills Kit (MSK)](../../mycroft-technologies/mycroft-skills-kit.md) that comes installed with Mycroft. If you chose the defaults during installation, you can run MSK from your Terminal using the command: `mycroft-msk`. Running this command without any arguments will provide a brief overview of what you can do with MSK.

If you receive a "command not found", then you will need to run `msk` manually from your `mycroft-core` directory. Anytime you see `mycroft-msk` in our documentation you must replace this with:

### MSK Create

`mycroft-msk create` is an interactive script that asks you a few questions and generates a new Skill template. This template can immediately be used as a Skill, however you will most likely want to extend its functionaity.

To create your first Skill, you will be asked for a:

1. Name  To be readable within the space available on the [Mycroft Skills Marketplace](https://market.mycroft.ai) the name should be short, generally under 22 characters in length. The name must also be unique. You can check the [Marketplace](https://market.mycroft.ai) to see what other Skills already exist.&#x20;
2. Example phrases (known as utterances)  Utterances that you expect Users to say to Mycroft, that your Skill will respond to.&#x20;
3. Response dialog  The dialog that your Skill will respond with.&#x20;
4. Short description  A one-line description, less than 40 characters long.&#x20;
5. Long description  This can be as short or as long as you like.&#x20;
6. Author  This is most often your name, and / or Github @username&#x20;
7. Categories  The [Mycroft Skills Marketplace](https://market.mycroft.ai) categories your Skill belongs to. It's important to note that the first category you select will be set as the default category. This is where your Skill will most often appear in the Marketplace.&#x20;
8. Tags  Tags provide an additional means for Users to search for or discover relevant Skills. Unlike categories, you can set your tags to anything you like.

After inputting this data you will be asked if you would like a Github repo created for your Skill. This provides an easy way to store your Skill, and will be required if you choose to [publish your Skill in the Marketplace](../marketplace-submission/).

If you have completed all of these steps, your Skill will have been created in the `/opt/mycroft/skills` directory on your device.

In the next section, we will explore each component that makes up your Skill.
