---
post_excerpt: ''
layout: page
author: Kathy Reid
permalink: |
  http://mycroft.ai/documentation/skills/common-issues-in-skills-development/
post_date: '2017-12-03T06:24:16.000Z'
published: true
post_title: Common issues in Skills development
ID: 32446
---

# Common Issues

## I've added new phrases in the .voc file, but Mycroft isn't recognizing them

1-Compound words like "don't", "won't", "shouldn't" etc. are normalized by Mycroft - so they become "do not", "will not", "should not". You should use the normalized words in your `.voc` files. Similarly, definite articles like the word "the" are removed in the normalization process, so avoid using them in your `.voc` or `.rx` files as well.

2-Tab != 4 Spaces, sometimes \(in gedit settings "Use Spaces"\) the text editor replace tabs with spaces or vice versa. Which may lead to an identation error. So make sure there's no extra tabs and that your text editor doesn't replace your spaces!

3-Wrong order of files directories is a very common mistake! You have to make a language subfolder inside dialog and inside vocab folder, which holds .voc and .dialog files. So make sure that your .voc files and .dialog files inside a language subfolder!

@TODO I need more information on issues that Skill developers have

