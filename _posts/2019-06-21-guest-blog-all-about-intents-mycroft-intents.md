---
ID: 48254
post_title: 'Guest Blog &#8211; All About Intents &#8211; Mycroft Intents'
author: Guest Blogger
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/guest-blog-all-about-intents-mycroft-intents/
published: true
post_date: 2019-06-21 14:00:14
---
Originally posted at https://jarbasal.github.io/posts/2018/06/intents/

So you're interested in making voice skills but don't know where to begin? There's a lot of jargon being thrown around with Adapt, Padatious, context, converse, etc... It's easy to get intimidated at first, but have no fear because this primer is going to help get you started!

In my day job, I spend my time building an educational system called Chatterbox (<a href="https://hellochatterbox.com/" target="_blank" rel="noopener noreferrer">hellochatterbox.com</a>) that teaches kids skill design. I've realized that teaching kids is much like teaching a novice. I'm challenged to clearly express what intents and utterances are, how they are meant to be used, as well as how to navigate the constraints of a voice-first experience.

Although we all inherently understand what intents are, for a lot of people and especially kids, these concepts and words aren't used in their day to day life.

If I simply say "intent" what pops up in your mind?
<h2><em>IF… THEN...</em> statements?</h2>
You just gave Mycroft an order, how does it decide what to do?

It helps to think about it in terms of <em>if... then...</em> statements
<pre>if user said "hello" then say "hello"
if user said "thank you" then say "you are welcome"
</pre>
When starting a skill, the first thing you should do is think of these <em>if... then..</em> statements.

You don't need to write any of this down, but it helps to have a list with the bare minimum of intents you need for the functionality you are trying to implement. Do not worry about how the user will ask the question yet, just keep one statement for each possible outcome.

What is an intent for Mycroft? Each possible outcome of the conversation you are modeling is an intent, that's why I suggested you write those <em>if... then...</em> statements. Each of those is an intent you need to teach Mycroft!
<h2>Padawhat?</h2>
Do we have to code these <em>if... then…</em> statements? Heck no, we are not in the 80's, there's real AI now!

The simplest way to get started is to use <a href="https://github.com/MycroftAI/padatious" target="_blank" rel="noopener noreferrer">Padatious</a>. With Padatious, you just give it examples and it knows what to do.

You do not need to understand the next paragraphs at all to use Padatious, but if you are curious of the inner workings, read on.

Padatious is Mycroft's neural network intent parser, it will ensure exact matches to any example phrase you give it by using its old fashioned regex cousin <a href="https://github.com/MycroftAI/padaos" target="_blank" rel="noopener noreferrer">Padaos</a>. But thanks to the AI, it also manages to understand sentences you did not explicitly teach it.

Each Padatious intent is a neural network model that tells Mycroft if it should select a specific intent given a request, with a probability. The Padatious engine chooses the highest scoring intent, or none if all probabilities are below a threshold.

Specifically, it uses one-hot encoding via local vocabularies (and a few extras like an unknown ratio input) into a series of shallow feedforward networks to perform intent recognition and entity extraction.

If you didn't understand any of that, it's ok; using it in practice is super easy! There is a command line tool named <code><a href="https://github.com/MycroftAI/mycroft-skills-kit" target="_blank" rel="noopener noreferrer">msk</a></code> (the Mycroft Skills Kit) that creates the skill template for you. You can even create complete skills if they are really simple. You can learn more about <code>msk</code> <a href="https://geekedoutsolutions.com/mycroft-skill-creation-lifecycle-using-msk" target="_blank" rel="noopener noreferrer">here.</a>

<a href="https://mycroft.ai/wp-content/uploads/2019/06/msk-gif.gif"><img class="alignnone size-full wp-image-48275" src="https://mycroft.ai/wp-content/uploads/2019/06/msk-gif.gif" alt="" width="878" height="540" /></a>

Let's make a real skill, LearnPortugueseSkill.
<pre>if user said "say hello in portuguese" then say "olá"
</pre>
How many ways can the user give that request?

Either use <code>msk</code> or create the files manually
<pre>vocab/en-us/hello_in_portuguese.intent
</pre>
The file should contain all sample sentences you can think of for this intent
<pre>say hello in portuguese
how do you say hello in portuguese
what is the portuguese word for hello
translate hello to portuguese
</pre>
Now let's look at our skill code, open the <code>__ init __.py</code> file
<pre>from mycroft.skills.core import MycroftSkill, intent_file_handler

class LearnPortugueseSkill(MycroftSkill):
	
    @intent_file_handler("hello_in_portuguese.intent")
    def handle_hello(self, message):
	    self.speak_dialog("hello_in_portuguese")
	    

def create_skill():
    return LearnPortugueseSkill()
</pre>
Since this is a teach Portuguese skill we need to implement some logic,

Mycroft's TTS system is configured for English for now; it can not speak Portuguese text. Thankfully, the awesome <a href="https://github.com/jcasoft/translate-skill" target="_blank" rel="noopener noreferrer">Translate Skill</a> from <a href="https://github.com/jcasoft/" target="_blank" rel="noopener noreferrer">@jcasoft</a> uses google TTS for this.

Let's use his code to add <code>speak_portuguese(text)</code> and <code>translate_to_portuguese(text)</code> methods to our skill!

We will now be able to speak the Portuguese bits
<pre>from mycroft.skills.core import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking, play_mp3
import os


class LearnPortugueseSkill(MycroftSkill):
    path_translated_file = "/tmp/portuguese.mp3"

    def translate_to_portuguese(self, text):
        translated = translate(text, "pt")
        self.speak_portuguese(translated)

    def speak_portuguese(self, sentence):
        wait_while_speaking()
        get_sentence = 'wget -q -U Mozilla -O ' + self.path_translated_file + \
                       '"https://translate.google.com/translate_tts?ie=UTF-8&amp;tl=pt&amp;q=' + \
                       str(sentence) + '&amp;client=tw-ob' + '"'
    
        os.system(get_sentence)
        play_mp3(self.path_translated_file)

	@intent_file_handler("hello_in_portuguese.intent")
	def handle_hello(self, message):
        # wait=True makes mycroft wait until speech is finished playing before continuing
        self.speak_dialog("hello_in_portuguese", wait=True)
        self.speak_portuguese("olá")
</pre>
notice that <code>self.speak_dialog("hello_in_portuguese")</code> ? That line of code is using a dialog file, <code>msk</code> or you should have created it at
<pre>dialog/en-us/hello_in_portuguese.dialog
</pre>
The file should contain all sample sentences Mycroft can speak to the user, and one will be picked randomly.
<pre>hello in portuguese is 
you say it like this
</pre>
To add support for new languages, just create a new folder with its language code. You can edit your examples at any time without touching the code, the skill will even auto reload. Simple, isn't it?

It’s also easier to translate an intent if you have full sentences. Adapt is trickier and often requires the translator to check the source code. That’s just one more good reason to use Padatious!

NOTE: Mycroft recently changed the folder structure, all files are now in <code>skill_folder/locale/en-us</code>. Old paths still work, but now it's easier since you need to track even fewer folders!
<h2>I like Rules</h2>
<pre>if user said "say thank you in portuguese" then say "obrigado" and explain gender
</pre>
If you are like me, it is easier for you to think of rules than to come up with examples, or maybe you just need more control over when the intent triggers.

Adapt comes to the rescue here; instead of magically learning from examples, you can specify some rules for when you want it to trigger.
<pre>@intent_handler(IntentBuilder("ThankYouIntent")
                .require("ThankYou")
                .require("inPortuguese"))
def handle_thank_you(self, message):
   self.speak_portuguese("obrigado")
</pre>
For this you need to create a file with keyword examples
<pre># ThankYou.voc
thank you
thanks
thx

# inPortuguese.voc
in portuguese
in portugal
in pt
in p t
</pre>
<h2>Extracting Keywords</h2>
Every keyword you defined for Adapt can be used as a variable in the intent code. Let's improve our Adapt intent to use a gender keyword.
<pre>@intent_handler(IntentBuilder("ThankYouIntent")
                .require("ThankYou")
                .require("inPortuguese")
                .optionally("gender"))
def handle_thank_you(self, message):
    gender = message.data.get("gender")
    if not gender:
        self.speak_dialog("if_male", wait=True)
        self.speak_portuguese("obrigado")
    elif gender == "male":
        self.speak_portuguese("obrigado")
    elif gender == "female":
        self.speak_portuguese("obrigada")
</pre>
This is the main use case for optional keywords, but they can also be used to increase confidence and help in disambiguation. After having the bare minimum requirements feel free to add as many optional keywords as you want.
<pre>@intent_handler(IntentBuilder("ThankYouIntent")
        .optionally("how")
        .require("ThankYou")
        .require("inPortuguese")
        .optionally("gender"))
def handle_thank_you(self, message):
    ...
</pre>
But what if we want to extract something from the text that we don't have an example of?
Padatious makes it super simple, in your .intent file write your examples like this
<pre>say {{words}} in portuguese
  speak {{words}} in portuguese
  translate {{words}} to portuguese
</pre>
That's it, you can now access it just like with Adapt
<pre>@intent_file_handler("say.intent")
  def handle_say(self, message):
    words = message.data["words"]
    self.translate_to_portuguese(words)
</pre>
<h2>What about multi-turn dialog?</h2>
I have written a <a href="https://jarbasal.github.io/posts/2018/10/skill_guidelines_2/" target="_blank" rel="noopener noreferrer">blog post</a> about this before, so I don't want to repeat myself a lot.

Adapt intent parser supports contexts. A context is a keyword that becomes available even if the user didn't say it.

This can be used for continuous dialog, so you can provide data with it (the missing keyword value).
<pre>if user said "say again" then repeat last portuguese sentence
</pre>
Let's implement repeat functionality, first create <code>repeat.voc</code>
<pre>say that again
repeat
</pre>
Now let's change the <code>speak_portuguese</code> method to set a context
<pre>def speak_portuguese(self, sentence):
    wait_while_speaking()
    get_sentence = 'wget -q -U Mozilla -O ' + self.path_translated_file + \
                   '"https://translate.google.com/translate_tts?ie=UTF-8&amp;tl=pt&amp;q=' + \
                   str(sentence) + '&amp;client=tw-ob' + '"'
        
    os.system(get_sentence)
    play_mp3(self.path_translated_file)
    self.set_context("previous_speech", sentence)
</pre>
The context made the "previous_speech" keyword available to Adapt. This intent can now be triggered up to 3 questions after <code>translate_to_portuguese</code> was last triggered.
<pre>@intent_handler(IntentBuilder("RepeatIntent")
                .require("repeat")
                .require("previous_speech"))
def handle_repeat(self, message):
    text = message.data.get("previous_speech")
    self.speak_portuguese(text)
</pre>
Padatious does not yet support context; for these cases, you are stuck with Adapt. However, you can set and remove contexts at will inside Padatious intents like I just did in the <code>speak_portuguese</code> method.

You can also use contexts that don't even have data, you just require it to ensure that something happened first
<pre>def speak_portuguese(self, sentence):
    wait_while_speaking()
    get_sentence = 'wget -q -U Mozilla -O ' + self.path_translated_file + \
                   '"https://translate.google.com/translate_tts?ie=UTF-8&amp;tl=pt&amp;q=' + \
                   str(sentence) + '&amp;client=tw-ob' + '"'
        
    os.system(get_sentence)
    play_mp3(self.path_translated_file)
    self.set_context("previous_speech", sentence)
    self.set_context("google_tx")
    	
@intent_handler(IntentBuilder("HowDoYouKnowIntent")
               .require("question").require("know")
               .require("google_tx"))
def handle_how_do_you_know(self, message):
   self.speak_dialog("google_told_me")
</pre>
<h2>I am a wizard</h2>
So I hear you like regex and Padatious is not an option for you, or maybe you are afraid because you don't understand how Padatious learns, but you aren't the botphobic kind are you?
<pre>if user said "explain {SampleWord} in portuguese" then say dictionary definition in portuguese
</pre>
For this I will be using <a href="https://pypi.org/project/PyDictionary/" target="_blank" rel="noopener noreferrer">PyDictionary</a>. You can add it to your skill by creating a <code>requirements.txt</code> file and adding <code>PyDictionary</code>.
I always recommend you use Padatious, but sometimes regex is a necessary evil and <a href="https://pythex.org/" target="_blank" rel="noopener noreferrer">Pythex</a> is useful to check your regex.

Make a file named <code>dictionary.rx</code>
<pre>explain (?P.*) in portuguese
  meaning of (?P.*) in portuguese
</pre>
Just require and use the regex capture group as a normal Adapt keyword.
<pre>@intent_handler(IntentBuilder("ExplainInPortugueseIntent")
            .require("SampleWord").require("inPortuguese"))
def handle_explain(self, message):
    word = message.data["SampleWord"]
    dictionary = PyDictionary()
    dictionary.meaning(word)
    meaning = dictionary.get("Noun") or dictionary.get("Verb")
    self.translate_to_portuguese(meaning)
</pre>
Padatious is much more human-readable, easier to translate, and less prone to errors. Adapt's regex is also known to be somewhat buggy at times, but maybe you really are a wizard.
Just keep in mind Adapt is rules-based; corner cases creep up if you oversimplify or overcomplicate.
<pre>"hey mycroft, where is the nearest bus stop"
"stopping everything"

"hey mycroft, do i need to say the last order again?
"the last order again"
</pre>
<h2>I am not a wizard!</h2>
Ok, you are still having trouble, there's some corner case you can't figure, need to extract a date or a number maybe?
<pre>if user said "say {weekday's date} in portuguese" then translate date to portuguese
if user said "say {number} in portuguese" then translate number to portuguese
</pre>
We have utility packages to extract dates, and English is well supported
<pre>@intent_handler(IntentBuilder("DateInPortugueseIntent")
               .require("inPortuguese").require("date").require("say"))
def handle_date(self, message):
    date, text_remainder = extract_datetime(message.data["utterance"], lang=self.lang)
    pronounced_date = nice_date(date)
    self.translate_to_portuguese(pronounced_date)
</pre>
One useful strategy that works well with optional keywords is to use the <code>utterance_remainder</code>.

In Adapt intents you can get the text leftover that was not captured into any keyword.

Mycroft also provides utils to handle numbers, language support not guaranteed except for English.

The PR for Portuguese is in, we can pronounce the number directly and save a call to google translate
<pre>@intent_handler(IntentBuilder("NumberInPortugueseIntent")
                .require("inPortuguese").require("number").require("say"))
def handle_number(self, message):
    text = message.utterance_remainder()
    # lets get a number from the utterance
    number = extract_number(text, lang=self.lang)
    # portuguese uses long scale, lets take that into account!
    # in long scale 1 billion = 1e12 instead of 1e9
    spoken_number = pronounce_number(number, lang="pt", short_scale=False)
    self.speak_in_portuguese(spoken_number)
</pre>
<h2>No intents needed</h2>
Need an answer to a general purpose question? Mycroft also has a mechanism to try to answer things it doesn't have intents for.

Fallback skills are tried by order until one can answer you, this is a good place to plug skills like Wolfram|Alpha.

But sometimes you just could not make an intent for your use case, maybe because there are a lot of skills and there are intent collisions.
<pre>if user said "say a pun in portuguese" then say a pun only portuguese speakers can understand
</pre>
A last-resort thing you can do is make a fallback intent using good old fashioned python programming with no help whatsoever to decide what to do.
<pre>class LearnPortugueseSkill(FallbackSkill):
    puns = [...]
            
    def initialize(self):
        self.register_fallback(self.handle_pun_fallback, 99)
</pre>
There's usually no good reason to do this, and this example should have used a regular intent.
<pre>def handle_pun_fallback(self, utterance):
    if self.voc_match(self, utterance, "pt_pun"):
        pun = random.choice(self.puns)
        question = pun["pergunta"]
        answer = pun["resposta"]
        self.speak_portuguese(question + ".\n" + answer)
        return True
    return False
</pre>
<h2>Intercepting the intent parser</h2>
What if we want to capture the whole utterance cycle inside a skill without giving other skills a chance?
<pre>if user said "translate everything i say to portuguese" then start ignoring questions and translate everything
</pre>
Let's make an intent to start the interception cycle
<pre>@intent_file_handler("live_translate_portuguese.intent")
def handle_live_translate(self, message):
    self.speak_dialog("start_tx", wait=True)
    self.speak_portuguese("iniciando tradução automática")
    self.intercepting = True
</pre>
Now we can use the converse method to capture the utterances.

But we also need to check if the user told us to stop. There is a helper method to check if some .voc file would match.
<pre>            
def stop(self):
    if self.intercepting:
        self.speak_dialog("stop_tx", wait=True)
        self.speak_portuguese("parando tradução automática")
        self.intercepting = False
               
def converse(self, transcript, lang="en-us"):
    utterance = transcript[0]
    if self.intercepting:
        if self.voc_match(self, utterance, "cancel", lang=lang):
           self.stop()
        else:
           self.translate_to_portuguese(utterance)
        return True
    return False
</pre>
Now every time you say "Hey Mycroft" it will repeat what you said in Portuguese and ignore any questions.
<h2>So what did we learn?</h2>
I wanted to show you the potential of Mycroft intent system. Hopefully Mycroft is less confusing for you now!

Some functionality of this example skill could probably be made other (better) ways, but it should have taught you to:

- speak pre-programmed answers, in our case translate hello to Portuguese
- optionally take extra parameters into account, gender matters when speaking in many languages
- extract keywords with Padatious and translate them to Portuguese
- extract keywords with regex and explain their meaning in Portuguese
- pass data to follow up intents (repeat last Portuguese utterance)
- use Mycroft helper utils, utterance_remainder, extract/pronounce number and extract/pronounce date
- create a fallback handler and use custom utterance parsing
- take control of the utterance processing cycle using converse method (live translate anything to Portuguese)

Source code is available <a href="https://github.com/JarbasAl/learn-portuguese-skill" target="_blank" rel="noopener noreferrer">here</a>, and your skill folder should look like this
<pre>├── __init__.py
├── LICENSE
├── locale
│   └── en-us
│       ├── date.voc
│       ├── dictionary.rx
│       ├── gender.voc
│       ├── google_told_me.dialog
│       ├── hello_in_portuguese.dialog
│       ├── hello_in_portuguese.intent
│       ├── if_female.dialog
│       ├── if_male.dialog
│       ├── inPortuguese.voc
│       ├── know.voc
│       ├── number.voc
│       ├── pt_pun.voc
│       ├── question.voc
│       ├── repeat.voc
│       ├── say.intent
│       ├── say.voc
│       ├── start_tx.dialog
│       ├── stop_tx.dialog
│       └── ThankYou.voc
├── README.md
└── requirements.txt
</pre>
Now if you wanted to show this skill to the world, all you need to do is create skill tests and <a href="https://rawgit.com/MycroftAI/mycroft-skills/18.08/meta_editor.html" target="_blank" rel="noopener noreferrer">submit the skill</a> to the <a href="https://market.mycroft.ai/" target="_blank" rel="noopener noreferrer">Marketplace</a>!
<h2>Only for Mycroft?</h2>
Adapt and Padatious are open source, so you can use them outside Mycroft in your own projects! In fact, <a href="https://mycroft.ai/blog/myzilla-mycroft-at-the-mozilla-all-hands/#project-things" target="_blank" rel="noopener noreferrer">Mozilla is using Adapt in an IoT project.</a>

Installing Padatious is easy
<pre>sudo apt-get install libfann-dev python3-dev python3-pip swig
pip install padatious
</pre>
Installing Adapt is also easy
<pre>pip install adapt-parser
</pre>
Padatious is really simple to use
<pre>from padatious import IntentContainer

container = IntentContainer('intent_cache')
container.add_intent('hello', ['Hi there!', 'Hello.'])
container.add_intent('goodbye', ['See you!', 'Goodbye!'])
container.add_intent('search', ['Search for {query} (using|on) {engine}.'])
container.train()

print(container.calc_intent('Hello there!'))
print(container.calc_intent('Search for cats on CatTube.'))

container.remove_intent('goodbye')
</pre>
You can also get <a href="https://github.com/MycroftAI/padaos" target="_blank" rel="noopener noreferrer">Padaos</a> the regex intent parser. I even <a href="https://github.com/JarbasAl/auto_regex" target="_blank" rel="noopener noreferrer">forked it</a> to simply output the generated regex instead of making intents.
<pre>from padaos import IntentContainer

container = IntentContainer()
container.add_intent('hello', [
    'hello', 'hi', 'how are you', "what's up"
])
container.add_intent('buy', [
    'buy {item}', 'purchase {item}', 'get {item}', 'get {item} for me'
])
container.add_intent('search', [
    'search for {query} on {engine}', 'using {engine} (search|look) for {query}',
    'find {query} (with|using) {engine}'
])
container.add_entity('engine', ['abc', 'xyz'])
print(container.calc_intent('find cats using xyz'))
# {'name': 'search', 'entities': {'query': 'cats', 'engine': 'xyz'}}
</pre>
Adapt seems a little more intimidating at first sight.
<pre>from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

engine = IntentDeterminationEngine()

weather_keyword = ["weather"]

for wk in weather_keyword:
    engine.register_entity(wk, "WeatherKeyword")

weather_types = ["snow", "rain", "wind", "sleet", "sun"]

for wt in weather_types:
    engine.register_entity(wt, "WeatherType")

weather_intent = IntentBuilder("WeatherIntent")\
    .require("WeatherKeyword")\
    .optionally("WeatherType")\
    .build()

engine.register_intent_parser(weather_intent)

for intent in engine.determine_intent(' '.join(sys.argv[1:])):
	if intent.get('confidence') &gt; 0:
	    print(json.dumps(intent, indent=4))
</pre>

<hr />

<blockquote>Jarbas is a long time Mycroft Community Member and a developer at Chatterbox, a company teaching kids about technology through a build-it-yourself, code-it-yourself smart speaker.

<a href="https://www.kickstarter.com/projects/hellochatterbox/chatterbox-the-smart-speaker-that-kids-build-and-p?ref=af05oh" target="_blank" rel="noopener noreferrer">Check out Chatterbox on Kickstarter!</a>
<a href="https://jarbasal.github.io/" target="_blank" rel="noopener noreferrer">Read more tutorials from Jarbas</a></blockquote>