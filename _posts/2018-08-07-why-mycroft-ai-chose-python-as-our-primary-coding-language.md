---
ID: 39729
post_title: >
  Why Mycroft AI chose Python as our
  primary coding language
author: Kathy Reid
post_excerpt: >
  Learn why Mycroft made the choice to
  standardize on Python as our choice of
  programming language.
layout: post
permalink: >
  https://mycroft.ai/blog/why-mycroft-ai-chose-python-as-our-primary-coding-language/
published: true
post_date: 2018-08-07 10:00:02
---
One of the frequent questions we get in the <a href="https://community.mycroft.ai">Community Forum</a> and <a href="https://chat.mycroft.ai">Mycroft Chat</a> is around which programming language is used to create <a href="http://mycroft.ai/documentation/skills/">Mycroft Skills</a>. Here, CTO Steve Penrod sits down for a chat with Kathy Reid from Dev Relations and explores why we’re a proud <a href="https://www.python.org/">Python</a> shop.

<strong>kathyreid</strong>: <em>G’day ;-) Thanks for taking time out of your busy day for talking Python! How did Python come to be adopted in Mycroft? Was it a conscious choice?</em>

<strong>penrods</strong>: Hey! You’re welcome, always a pleasure to chat.

Python was a very conscious choice for us when we launched Mycroft.  From the beginning we intended for Mycroft to be a platform for others to extend, so we knew we were choosing not only for the internal development team but also for thousands of other programmers.  This was an important decision that wouldn’t be easy to change down the road.

In the early days of Mycroft development, we knew that we would likely be using the Raspberry Pi and Raspbian environment for the <a href="https://mycroft.ai/mark1/">Mark 1</a>. Python has great support on virtually all embedded development boards like the OrangePi, ODROIDs, etc; and across most flavors of Linux, and even other operating systems like Mac and Windows. So it’s got excellent cross-platform support.

As a startup, your runway time is also limited. You have to get something reasonable to market very quickly, and we didn't want to have to burn a whole heap of time on a learning curve with something that isn’t as well established - like Haskell or Rust or Lambda.

That sort of thinking also flows into considerations for hiring and building out your development team. Python is taught in a lot of high schools and colleges, and we often hire summer interns. So, using a language that is really accessible - where people are already going to have some exposure, some ability with it - becomes more important so that they can be really productive really quickly.  Fortunately our intuition proved to be correct, too -- Python has grown to be fastest growing and most popular language over the last few years.

There’s another related point here too - Python has a very well established community - you look at the strength of, say, <a href="https://us.pycon.org">Pycon</a> and the related Python projects like <a href="https://micropython.org/">MicroPython</a> for embedded systems and <a href="https://pybee.org/">PyBeeWare</a>. The community and the ecosystem around Python is very vibrant and active - it’s a language in ascendancy. That statement is backed by things like this the recent presentation by <a href="https://www.google.com/url?q=https://youtu.be/Z1yMTPRmhK8?t%3D4m9s&amp;sa=D&amp;ust=1533067812323000&amp;usg=AFQjCNH13QJ15ZL_KEjVc70WMGUtrs9gag">Roger Magoulas at OSCON</a>, which talks about trends with open source programming languages - with Python right there at the forefront. The IEEE - the Institute of Electronic and Electrical Engineers - also <a href="https://spectrum.ieee.org/at-work/innovation/the-2018-top-programming-languages">rated Python as the top programming language of 2018 recently</a>. That means new libraries are getting created, toolsets are being created and extended, bugs are getting addressed, documentation is getting updated - all the things that you worry about as a CTO when pretty much your entire platform is based on a single language.

<strong>kathyreid</strong>: <em>Interesting. Were there any other candidates that were considered? Why were they not chosen?</em>

<strong>penrods</strong>: There were several other options.  PHP was very popular, but limited the architecture as a server-side language. Java is well known as cross-platform, but getting less friendly for new developers and a little heavy. Javascript was also interesting, but the environments and tools were more limited back in 2014 and still aren’t as widespread as Python.

C and C++ have great cross-platform support and excellent performance. However, they are much more daunting to beginners and honestly the majority of the performance gain isn’t a big deal for us.  Human interaction is slow, in computer terms, so the difference between something that runs in 10ms and something that runs in 20ms in imperceptible for skills and the mycroft-core framework. The C/C++ optimizations can be limited to within the STT and TTS engines.

<strong>kathyreid</strong>: <em>We’re doing some work at the moment on trying to establish a ‘go-to’ or a ‘reference’ IDE setup to reduce the onramp that new Skill authors have. Do you think this task is made easier or harder by the choice of Python?</em>

<strong>penrods</strong>: Well this is really interesting - it’s like a double edged sword. On one hand, because Python is so well established, there’s a lot of choice for Python IDEs and editors - you’ve got <a href="https://www.jetbrains.com/pycharm/">Pycharm</a>, and <a href="https://atom.io/">Atom,</a> and Visual Studio Code, and a whole heap of others. By the same token, this makes it harder to compare them to each other and to see which one will be a good fit for our community. And of course that can lead to some ideological arguments about which editor or IDE is best for whichever reason.

<strong>kathyreid</strong>: <em>Are there any downsides you’ve encountered with the choice of Python?</em>

<strong>penrods</strong>: Again, I think one of the difficulties with Python is a product of its own success. There are several libraries for Python now - and some of them such as Tensorflow, and SciPy and NumPy - can be huge - and they’re just available for anyone to <code>pip install</code>. So if you try running, say, a Skill that has a large dependency like Tensorflow on low end hardware like the Raspberry Pi then you can encounter some disappointing results. That is - it’s very powerful but you also have to know what the limits and constraints of it are too.

One of the other challenges we’ve had recently is around the different available version of Python. A few months ago we made the transition from Python 2.7 to Python 3.4+, and it was a little painful. Even now we’re still running into support issues where the wrong version of Python is being called. We can work around this to some extent using virtual environments -- which itself has some complexity caused by choice.  Python has <code>virtualenv, venv, pyenv, pipenv</code> ... and this adds a whole other layer of potential confusion and complexity for us to manage and document.

<strong>kathyreid</strong>: <em>Does Python make sense for the future of Mycroft?</em>

<strong>penrods</strong>: Absolutely. You can see this in our <a href="http://mycroft.ai/blog/many-roads-one-destination/">Roadmaps</a> from the paths we’re headed down.  There is multilingual support due to native Unicode, and the availability of tools and frameworks like Tensorflow makes build new voices and machine learning systems much easier.  Python’s future is looking brighter, too, with more and more libraries being released daily. So it has been a good fit, and it remains so.

<strong>kathyreid</strong>: <em>Any parting thoughts?</em>

<strong>penrods</strong>: Well I really think that Python is a great string to have in your programming bow, it’s certainly a programming language I’d encourage others to learn. One of the things I think Mycroft brings to the world is an easy way for novices to try their hand at programming. It is easy to build something in less than an hour that is really cool.  There are some great sites out there for learning Python like <a href="https://www.learnpython.org/">LearnPython</a>, <a href="https://docs.python-guide.org/intro/learning/">Hitchhikers Guide to Python</a>, and several others.  Not everyone needs to be a professional programmer, but understanding the basic operation and limitations of computers is invaluable in today’s world.

<hr />

Thanks, Steve for your time and technical knowledge - as always!

If you'd like to get involved in Skills development for Mycroft, you can check out our <a href="http://mycroft.ai/documentation/">documentation</a>, or jump into our <a href="https://chat.mycroft.ai/community/channels/dev">Skills Dev Chatroom</a>!