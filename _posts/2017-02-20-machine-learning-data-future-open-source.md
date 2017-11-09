---
ID: 29181
post_title: >
  Machine Learning, Data, and the Future
  of Open Source
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/machine-learning-data-future-open-source/
published: true
post_date: 2017-02-20 16:33:51
---
I'm not saying traditional software development is dead.  There will continue to be a market for software built on classes, functions and if-then-else statements for decades to come.  The bleeding edge of software development, however, has moved to a new paradigm – machine learning.

Machine learning is a programming technique where data is used to train an algorithm.  For example, a large set of images might be tagged with a text description of what is in them.  These images and the associated tags are then processed by a neural network.  The resulting software is then capable of processing a single image and – if the data set was comprehensive enough – providing a text description of what is in it.

<img class="alignleft size-full wp-image-29182" src="https://mycroft.ai/wp-content/uploads/2017/02/machine-learning_skiing.png" alt="machine learning image recognition" width="1800" height="1200" />

&nbsp;

This approach to software development is revolutionizing the way many businesses handle data.  Companies like Google, Facebook and Amazon are applying this technique to their enormous data sets to provide accurate search results, spam filtering, and even product suggestions.

Though many of the machine learning frameworks are open source (<a href="https://www.tensorflow.org/" target="_blank" rel="noopener">TensorFlow</a> is an excellent example) the data underpinning them is not and, without data, the frameworks aren't tremendously useful.  This means that open source communities are getting left behind.

Here at Mycroft, we aim to change that – at least in the realm of human-machine interfaces and speech to text.  With our user's permission, we plan to make both the user interaction and the audio samples Mycroft is processing available for training machine learning systems.

Now, before folks go off the rails about privacy, we are aware that we need to protect our user's privacy.  Here at Mycroft we view privacy as a basic human right and will go to significant lengths to protect it.  Before we publish any data we plan to anonymize it securely and remove any private or personally identifiable information.  How?  Good question.  We are still working that out which is why we haven't published any data yet.  We may use differential privacy, paid reviewers or secure sandboxes.  Regardless, we plan to make sure that we keep user data secure while also making it available.

We plan to run this program using an opt-in method where users make their own decision about whether or not they want their data used to improve the underlying technology.  Though we expect many users will want to, others might choose to keep their data private and that's fine.

Our commitment to our core principles – <a href="https://mycroft.ai/f-o-s-s/" target="_blank" rel="noopener">Fast, Open, Simple, Strong</a> is absolute and being open is a key principle.  Let's work together to build an open data set to improve the state of the art in open source machine learning so that we can truly build an AI for everyone.

&nbsp;