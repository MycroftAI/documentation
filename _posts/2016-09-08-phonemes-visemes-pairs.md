---
ID: 2011
post_title: Phonemes and Visemes in Pairs, Oh My!
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/phonemes-visemes-pairs/
published: true
post_date: 2016-09-08 11:55:59
---
<a href="https://mycroft.ai/wp-content/uploads/2016/09/Speaking.gif"><img class="aligncenter size-medium wp-image-2016" src="https://mycroft.ai/wp-content/uploads/2016/09/Speaking-300x166.gif" alt="Talking head" width="300" height="166" /></a>

This week I'm going to do a little geek dive into the theories behind our technology. Specifically, I'll be looking at what goes into text to speech (TTS) — i.e. what allows Mycroft to talk back to you.
<h2>Phonemes</h2>
Text to speech is really a kind of translation. We all understand that written language consists of a sequence of letters. In the parlance of linguists, those letters are "graphemes", the smallest units of written language. This same term applies to any alphabet - our ABCs, the Cyrillic alphabet of Russian, or Japanese's Kanji.

However the written graphemes don't directly translate into spoken language. In English, for example, the pronunciation of "daughter" is drastically different than "laughter" despite the similar sequence of letters. Say them slowly and notice the sounds you are making. So to unambiguously describe pronunciation linguists created the concept of "phonemes"

A phoneme is the smallest unit of spoken language. For example the phoneme named "/f/" is the sound at the beginning of "fun" and also "phone". In English there are 44 phonemes. Spanish adds a phoneme for their trilled R but overall is simpler and only has 24 phonemes. In all, humans can produce about 400 different phonemes.

Going back to our earlier two examples, the phonemic version of "daughter" is "/'dɔ:tə/", and "laughter" is "/'lɑ:ftə/". So the process of going from text to speech is just mapping those written words to their phonemic equivalents, right? Well...kinda. Except in the cases like "read me a book" and "he read the book to me" where the same letters r-e-a-d have different pronunciations. So for those the text to speech translation has to look at adjacent words to figure out which pronunciation is appropriate in the context.

So text to speech/phoneme software really has to understand the language it is working with in order to get it right. It also can fall back to some basic rules, just like when we learned to "sound out" words when we were learning to read. And mixing languages in the same text gets really tricky. That can result in the sentence "Like they say, c est la vie" sounding like it's being spoken by Slim Pickens.

Things also get a bit tricky in Chinese where tones change meanings. And then there are a few clicking languages like Khosian (check out <a href="https://youtu.be/W6WO5XabD-s">https://youtu.be/W6WO5XabD-s</a>) or the whistling language Sylbo (see <a href="https://youtu.be/C0CIRCjoICA">https://youtu.be/C0CIRCjoICA</a>). But we'll leave those alone for today.
<h2>Inflection</h2>
But even in English there's more that just the phonemic translation. We naturally use different inflections to convey additional meaning. Think of the various ways the word "what" is spoken by people. It can have a rising inflection when you don't understand something ... "What?" Or it can be a flat pronunciation ... "he didn't know what he was reading". Or it can be short and sharp like after telling your mom you just wrecked her car ... "What!"

Some inflection can be inferred from punctuation as I showed above. But normal written language really can't express the fullness of spoken language. That's why computers traditionally read "I don't know what I was thinking" in a flat, robotic manner.
<h2>SSML</h2>
One new technique to try and eliminate the robotic sound is Simple Speech Markup Language (SSML). It's a method for adding more information to the written text to provide hints for the inflection. So you could write "I don't know &lt;emphasis&gt;what&lt;emphasis/&gt; I was thinking".

It's cumbersome for people to read and write so I don't think it is going to show up in the text of the new Harry Potter books. But it is an important development behind the scenes to make our voice interfaces more expressive.
<h2>Visemes</h2>
The last thing I'll touch on is "visemes". These aren't strictly a part of text to speech, but we humans are used to words coming out of a mouth. Sure, we can understand someone in the phone without seeing their face. But a visual can be comforting.

Each phoneme can be easily associated with a mouth shape. These mouth shapes are called visemes. Often two phonemes have the same viseme, like the mouth shape for "ay" is basically the same as "e" - we place our tongue at a different spot inside our mouths to make those sounds but our mouth looks the same to someone watching us speak. Look at yourself in the mirror and speak the words "say" and "see", or "elephant juice" and "I love you". There is a lot of debate in the academic world about exactly how many visemes exist with some claiming there are 30 or more. But for the simple animation shown on the Mycroft device's matrix display only requires six different shapes.

Interestingly enough, research into visemes goes back decades before text to speech technology was even imagined. C. G. Fisher coined the term in 1968 for his research into lip reading techniques. If anyone out there is a lip reader, I'm really curious if you can get anything from watching Mycroft speak without sound!
<h2>Conclusion</h2>
There's a brief survey of what's behind making our computers talk. What do you think of posts like this? Would you like to see more geeky blog posts like this in the future?