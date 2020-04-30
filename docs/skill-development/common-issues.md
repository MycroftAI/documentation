---
description: Having trouble with your Skill? Here are a few things that we sometimes see.
---

# Common Issues

## I've added new phrases in the .voc file, but Mycroft isn't recognizing them

1-Compound words like "don't", "won't", "shouldn't" etc. are normalized by Mycroft - so they become "do not", "will not", "should not". You should use the normalized words in your `.voc` files. Similarly, definite articles like the word "the" are removed in the normalization process, so avoid using them in your `.voc` or `.rx` files as well.

2-Tab != 4 Spaces, sometimes \(in gedit settings "Use Spaces"\) the text editor replace tabs with spaces or vice versa. Which may lead to an identation error. So make sure there's no extra tabs and that your text editor doesn't replace your spaces!

3-Wrong order of files directories is a very common mistake! You have to make a language subfolder inside the dialog, vocab or locale folders such as `skill-dir/locale/en-us/somefile.dialog`. So make sure that your .voc files and .dialog files inside a language subfolder!

## I am unable to match against the utterance string

The utterance string received from the speech-to-text engine is received all lowercase. As such any string matching you are trying to do should also be converted to lowercase. For example:

```python
@intent_file_handler('example.intent')
def handle_example(self, message):
    utterance = message.data.get('utterance')
    if 'Proper Noun'.lower() in utterance:
        self.speak('Found it')
```

## Need more help?

If something isn't working as expected, please join us in the [~Skills channel of Mycroft Chat](https://chat.mycroft.ai/community/channels/skills).

It's also really helpful for us if you add an issue to our [documentation repo](https://github.com/MycroftAI/documentation/issues). This means we can make sure it gets covered for all developers in the future.

