---
ID: 1088
post_title: >
  Why On Earth Would I Want To Talk To My
  Computer?
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/why-on-earth-would-i-want-to-talk-to-my-computer/
published: true
post_date: 2015-11-02 16:18:10
---
When I started my first computer job in 2000 I was fortunate enough to work with a PhD named Dan Vasacheck who took the time to show me how to use the company's Unix mainframe. Though I learned a lot from Dan, the best gem of wisdom I took away was this - “A graphic user interface (GUI) is the equivalent of pointing and grunting, the command line interface (CLI) allows you to have a conversation with your computer.”

You see, to use a windows interface all you really need to do is move the mouse cursor to a specific part of the screen (point) and click (grunt). In fact, when multi-touch technology became available in 2005 it was hailed as a huge advancement in human-machine interaction. You can now zoom-in and out too. Wow! It is like we are developing stone age tools all over again.

The CLI, on the other hand, allows you to have a conversation with the computer, albeit in the computers stilted language. Programmers developed a series of programs and utilities layered on a command shell. Since programmers are lazy by nature they abbreviated the program names (“list” became “ls” for example) and gradually added a series of settings or options in the form of command line flags. To use the CLI you need to know which commands to run, which flags are applicable and how to string commands together. If you know the secrets of this language you can converse with your computer in ways that seem like magic to GUI users. As an example, to scan a remote network and get the ip addresses of computers that are responding to ICMP you would type:
<p align="center"><i>nmap -sP -n -v 10.0.0.0/24 2&gt; /dev/null | grep -i 'to be up' | cut -d " " -f 2</i></p>
However, structuring this command takes time and expertise. It is often done by trial and error and even accomplished users of the command line need to constantly refer to the user manual. Why? Because the syntax is archaic, there are no real standards between commands (does “-n” mean new or null?) and even slightly different versions of the same shell have different syntax.

To put it in layman's terms the CLI is the equivalent of a formal letter. It can be used to communicate just about anything, but it is far too clunky for our daily needs. You don't send the grocer a formal letter asking where they keep the pumpkin pie filling, you simply walk up to him and ask.

There's a better way. Natural language recognition – the type of communication we use every day to communicate with other people. Until recently this type of computer interface was beyond the reach of computer science, but it is now becoming widely available as companies like Facebook, Google, Apple, Microsoft, and Amazon have invested in M, Now, Siri, Cortana and Echo respectively.

So why are these companies making billion dollar investments in natural language interfaces? Because it's the future of the human computer interface. We've spent the last 50 years teaching <i>people</i> to speak the language of the <i>machines</i>. It is difficult, awkward and takes years of experience. We are now at a place where we can teach <i>machines</i> to speak the language of <i>humans</i> – intuitive, easy to use and natural. With natural language processing, I can have my computer scan a remote network by simply saying:
<p align="center"><i>Hey, Mycroft. Run a ping sweep of 10.1.1.0/24 and list the IPs in use.</i></p>
<p align="center">-or-</p>
<p align="center"><i>Hey, Mycroft. Which IPs on 10.1.1.0/24 are returning ICMP?</i></p>
The natural language processing in the system translates my speech into a series of commands, executes them, and then provides a listing of the results. There is no standard syntax, I give the command naturally and the computer interprets the results. No need to memorize flags, pipe output from one command to another, or worry about throwing the wrong flag. The underlying skill ( which in this case was developed by someone who IS an expert in the CLI and in nmap ) handles the arcane language and provides a neatly formatted list of IP addresses.

Skeptical? I understand. Users have a right to be skeptical, especially power users who use the CLI all day. Vendors have been selling broken and essentially useless voice command software for more than 15 years now. Even today my Chevy Volt is a prime example – it has a terrible voice interface that is effectively useless. Worse, it is closed source and proprietary so I can't simply replace it with Mycroft or hack it to suit my needs. But, that is changing.

Here at Mycroft we are developing an open source AI that will allow anyone with an idea to develop a skill and deploy it globally. Want to make it easy for end users to get the score of the latest FIFA football game? Use our standard template to develop the skill, upload it to our repository and soon every Mycroft user on earth will be able to follow the latest from any FIFA game.

The technology to make a natural language interface is here today. We can build an interface that is intuitive, easy to use, flexible and friendly. Billions of people are using early versions on their Apple, Android and Windows devices. In the future these interfaces will be an important part of any modern consumer operating system in much the same way that the GUI became a key component in the 1980's.

You will eventually spend your day talking with your computer, and it's going to be great.