---
ID: 31915
post_title: >
  Building a Strong AI | A Strategy and
  How-To
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/building-strong-ai-strategy/
published: true
post_date: 2017-10-09 21:08:36
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]

<em>The full-time team here at Mycroft has been underwater while we’ve been focusing on shipping the Mark I and our first alpha - 17.08a. Now that we’ve shipped, I think it is time for us to regroup and look at our strategy. Thanks to the faith of a number of great investors, we now have time to come up for air. In this document I’m going to lay out the full-time team’s thinking on Mycroft’s direction, then I’m going to make some time to discuss this strategy with our community both <a href="https://www.eventbrite.com/e/listening-session-with-mycroft-ceo-joshua-montgomery-tickets-38744569049?aff=eac2">in-person and online.</a></em>[/vc_column_text][divider line_type="No Line"][vc_column_text]
<h1>Introduction</h1>
I’ve recently been reading Walter Isaacson’s “<a href="http://www.simonandschuster.com/books/The-Innovators/Walter-Isaacson/9781476708706">The Innovators</a>” which traces the digital revolution from Babbage’s analog computer to the modern day. I’ve also been giving a lot of thought to how open communities, machine learning and strong AI fit into our society’s narrative of progress.

I’ve been asking myself the question: “How do we organize an open community to solve the problem of strong AI.” Implied in this question is another question “How do we organize the work in a way that the broader community can help?” This is a tough question to answer, but it turns out there are some very high profile examples that we can learn from. I’m most intrigued by the examples of Wikipedia and Google.

I’ll start with Google as it’s far and away the most successful web application ever created, and is, in my mind, the closest to creating a strong AI. As I see it Larry and Sergey had two major insights when they started Google:

Web developers were embedding data about the relative importance of various websites into the sites themselves in the form of metadata, font sizes, and – importantly – links to other sites. PageRank was effectively an early machine learning algorithm that took the information web developers were already encoding into their sites and compiled it in a way that made it easily searchable.

User behavior could be used to further refine search results. By tracking which results users actually selected the Google team could build a feedback loop that made each and every Google user into a Google trainer. If all of Google’s users clicked the second result when searching “Miracle on the Hudson” then the second result would become the first result - automatically. Users were willing to help train the algorithm because it provided them with value.

Importantly, both of these concepts were algorithmic. They didn’t need humans to categorize the web pages. They simply wrote a spider to crawl the web and process the existing data. They didn’t need people to view each session and examine user behavior. Instead they did it programmatically.

By implementing these two ideas in software Google was able to grow exponentially and made the most successful and widely used technology ever. Over time they’ve refined these practices and applied them to hundreds of other areas of technology with various levels of success. That is why I know that despite the fact my Google Fi service is subpar at selecting the best cellular network today it will probably improve over time.

The community at Wikipedia lead by Jimmy Wales had a different insight. By eschewing academic expertise in favor of the wisdom of the crowd they could produce an encyclopedia that is more comprehensive (and hence more useful) than encyclopedias produced using an academic process. Users were encouraged to collaborate on content, standards and governance. By taking this approach Wikipedia was able to grow extremely fast. It quickly became the global destination for long form queries.

One key insight the Wikipedia community had was that the project would benefit if they made it dead simple to contribute. Users didn’t need to provide their references, they didn’t need to have their work reviewed, they didn’t even need an account. The tool for contributing was, and remains, easy for anyone to use. This simplicity makes Wikipedia editing accessible to nearly everyone on the web and allowed Wikipedia to grow a large community of editors around the site.
<h1>Strategic Overview</h1>
We can learn from both of these examples here at Mycroft. We can leverage the power of an open community to create useful software that is has an algorithmic feedback loop which automatically improves the technology over time. This is a first. The open source community has a long history of producing software collaboratively, but that software is generally stand alone. Though many companies use open software to create feedback loops for themselves, the community that created the software seldom benefits from algorithmically generated improvements. The software is open source, but the data remains proprietary.

Let me unpack that with an example. LibreOffice Writer is great. The community behind it gets feedback in the form of bug reports and user surveys, but the software doesn’t communicate back to the developers. The software is not set up to tell developers “80% of users who eventually selected ‘Footnotes and Endnotes’ first selected the ‘File’ menu”. Even if the software did communicate use data like this it won’t automatically move the ‘Footnotes and Endnotes’ option into the ‘File’ menu. That move requires human intervention.

To build a truly profound technology our community needs to take lessons from both Google and Wikipedia. We need to build tools that collect data and use it to continuously improve the software. We need to create a collaborative environment where anyone can reach into the system and help. This has become our strategy:

We will build software that has a programmatic feedback loop.
We make the software simple enough so that anyone can contribute.

Now that we have a strategy, let’s look at how we implement it operationally.
<h1>Moving from the ‘what’ (strategy) to the ‘how’ (implementation)</h1>
We have a number of options for creating algorithmic feedback loops here at Mycroft. At their base level, all of these loops start out the same:
<ol>
 	<li>Users use the technology because it is useful.</li>
 	<li>We get feedback on how the users are using the technology.</li>
 	<li>Our community helps us filter, tag and categorize the feedback.</li>
 	<li>We use machine learning to take the tagged processed data and improve the user experience.</li>
</ol>
Some of the loops, however, will evolve over time. To improve the technology exponentially we need to remove Step 3 – the human trainer - and replace them with the end user.[/vc_column_text][image_with_animation image_url="31921" alignment="center" animation="Fade In" box_shadow="none" max_width="100%"][vc_column_text]
<ol>
 	<li>Users use the technology because it is useful.</li>
 	<li>We get feedback on how the users are using the technology.</li>
 	<li>Our community helps us filter, tag and categorize the feedback.</li>
 	<li>We use machine learning to take the tagged processed data and improve the user experience.</li>
</ol>
Some of the loops, however, will evolve over time. To improve the technology exponentially we need to remove Step 3 – the human trainer - and replace them with the end user.

[/vc_column_text][image_with_animation image_url="31922" alignment="center" animation="Fade In" box_shadow="none" max_width="100%"][vc_column_text]
<ol>
 	<li>Users use the technology because it is useful.</li>
 	<li>When the technology doesn’t work well, the user corrects it.</li>
 	<li>We get feedback that includes user corrections.</li>
 	<li>We use machine learning to take the user corrections and improve the user experience for all users.</li>
</ol>
If you think about it, this is how you learned to be you. You said “that’s a huge bird”, your mom said “no that’s an airplane”, you went to sleep that night and your neural network (organic machine learning) trained itself to recognize a large aluminum “bird” as an “airplane”.

There are open source communities out there that have built this type of feedback loop (Duck-Duck-Go, for example), but unfortunately they didn’t do it in 1997. If they had we’d all be using an open source search engine that respected our privacy. The take-away from this is that if we are going to build something significant here at Mycroft and ensure that the world has an AI that is both strong and open source, we need to move quickly.

Up until now, our community hasn’t been using any of the data that is flowing through the Mycroft servers, but that changed last week. We now have an “Opt In” feature and permission from generous community members to make use of their data to improve the system.

Let’s start now.
<h1>Operational Planning</h1>
To achieve our strategic goals we need to implement an operational plan. A quick look at the Mycroft stack provides four components that will benefit from a community guided feedback loop.
<h4>Wake Word Spotting – Mycroft Precise</h4>
This is the simplest one which is why I personally was able to code it. (Don’t expect too much more of this, I’m a hacker, not a professional developer). We started this effort a few weeks ago by developing and deploying (to users who explicitly installed the software) an audio capture feature that allows us to both capture Wake Word triggers and failed attempts.

Here is how this software works:
<ol>
 	<li>The Precise software buffers all audio locally and, upon Wake Word activation it stores the prior 10 seconds of audio. This allows us to see failed attempts as well as successful attempts.</li>
 	<li>In an asynchronous process this 10 seconds of audio is sent to an online system and queued for processing.</li>
 	<li>A Mycroft community member goes through and categorizes the audio as having zero, one, or many Wake Words. If there are zero Wake Words in the sample then it was an inadvertent trigger. If there is only one Wake Word everything worked properly. If there are multiple Wake Words then the software failed to understand at least one and possibly several attempts to wake it.</li>
 	<li>For samples with zero or one Wake Words in them a second community member validates the initial assessment. Samples are stored for use in the Precise data store. Samples marked as “many” are provided to a community member who splits them and re-submits them in parts for validation. These samples are then validated and stored for use in training the machine learning algorithm.</li>
</ol>
The resulting data set is a large corpus of individuals speaking a single Wake Word or phrase. We then use that corpus of data to train the Precise Wake Word spotter. Users can download the training data for their specific Wake Word and, if they have opted in via the “Train” option on the Mark I or through the home.mycroft.ai website, their voice samples will be included in the global Wake Word spotting training store which will improve accuracy on every device that uses Mycroft software.

Eventually an additional step will be implemented between 2 → 3 that uses general speech-to-text technology and machine learning to assign an accuracy probability to the incoming sample. If the probability is above a certain threshold it will be added to the training set without community member input. This creates an algorithmic feedback loop and achieves our strategic goal of implementing completely algorithmic machine learning to the problem.
<h4>Speech To Text Transcription</h4>
This problem is a bit more complex, but follows the same general template as the Wake Word spotting, just on a larger scale.
<ol>
 	<li>The audio for a speech to text (STT) transaction is sent to Mycroft's servers or, for self-contained instances, to the local DeepSpeech instance. For users who opt-in, this data is then sent to an online repository for storage.</li>
 	<li>We use the DeepSpeech STT engine to transcribe the speech into a text. The clear text is stored with the audio sample.</li>
 	<li>Volunteers will be presented with a system where they can listen to the audio and read the STT engine’s first pass at transcription. For licensing reasons, this first-pass will only make use of the DeepSpeech open-source engine and/or KALDI, not paid STT transcriptions.</li>
 	<li>Users will correct the transcription of the audio and submit. After it has been validated twice it will be pulled into the master data store and used to further train the DeepSpeech engine.</li>
</ol>
As the DeepSpeech engine gets more accurate the team will use the match probability to evaluate incoming audio sample. Samples that are above a baseline accuracy threshold will be automatically included in the data set.
<h4>Single Interaction</h4>
The team has already implemented a machine learning intent parser called Padatious as part of the Adapt software. This engine allows skills creators to train Mycroft on what phrases should trigger their skill and extract entities from those phrases. This is an excellent first step, but does not address the problems we need to solve in order to make Mycroft both capable and personable.

To improve individual interactions without hand coding for every possibility (like AIML systems) we need to capture a large corpus of data on what users really mean - their intent - when they ask a question and what the AI should actually do.

For example, if the human asks “Make it brighter where I cook”, what he really means is “Turn the lights on in the kitchen” or, to a machine:
<ol>
 	<li>Search for IoT skill.</li>
 	<li>Once found search for location “Kitchen”</li>
 	<li>Once found search for object “Lights” associated with “Kitchen”</li>
 	<li>If “Lights” object is associated with “Kitchen” and toggle position is set to “On” increase brightness.</li>
 	<li>Otherwise if “Lights” object is associated with “Kitchen” and toggle position is set to “Off” set position to “On”.</li>
</ol>
Of course the example above leaves out a number of steps (accessing network, authenticating to IoT device, etc), but you get the idea.

The user might also say “Get lost for a while” which means “Pause Wake Word responses for an indeterminate time and only resume when Wake Word is heard twice in a short time frame or after 5 minutes of silence.”

Unfortunately our team can’t anticipate how to handle every phrase, but we can create a feedback loop that makes it easy for us to collaborate with our community to build a large dataset of interactions. The community can then classify these interactions through a simple web interface that allows anyone who speaks the language to tag the interaction and add appropriate classes.

This tool will be lightweight and will not require a login. Queries will be classed by multiple users and cross verified before being added to the data set. Here is a simple example:

Phrase: “Make it brighter where I cook damn it.”

Skill: IoT
Action: Toggle
Location: Kitchen
Position: On

Those are the obvious tags, but we will go one step further and tag a few more items that will be useful later on.

Sentiment: Negative
Intent: Command
Tone: Rude

Obviously there can be many additional classes. We will add these over time.

By classifying each query, we end up with a data set that can be used to train an AI to recognize things like tone, sarcasm, general intent, etc. This gives us a clear path to creating responses that are appropriate to the intent. For example, classifying a statement like this:

User: “What did the potato chips say to the batteries?”

Skill: Conversation
Action: Play Along
Sentiment: Playful
Intent: Telling Joke

This allows the AI to provide an appropriate response. We may initially have to type the response in the same way you’d tell a child the appropriate response, but – based on trainer feedback - the AI will eventually learn that for a “Telling Joke” intent with “Playful” sentiment the appropriate response is:

Response: “I don’t know, what did the potato chips say to the batteries?”
<h4>Threaded Interaction</h4>
This brings us to threaded interactions. These are more complex than simple commands or questions, they may involve a multi-step back and forth between the AI and a user. We will also classify these based on our own human experience. Taking the above interaction for example:

User : “What did the potato chips say to the batteries?”
Response: I don’t know, what did the potato chips say to the batteries?”
User: “I’m Frito-Lay if you’re Eveready!”

Our community would already have marked the initial statement as a “Playful” intent to “Tell a joke”. The next step of this process is to tie the user’s response together in a meaningful way that can be used to improve the AI’s understanding of the interaction.

The user’s final statement ( in this context ) is:

Outcome: Mildly Funny
Reason: “Frito-Lay” is a potato chip brand and sounds similar to “Free to Lay”. Eveready is a battery brand and sounds similar to “ever ready”. The joke is a play on the phrase “I’m free to lay if you are ever ready.”
Joke Class: Mildly Sexual

Next we get into the expected response.

Response: Laugh
Response: Initiate Joke

To which the AI would say:

Response: “Funny. Now I’ve got one for you. Knock, knock”

This is a socially appropriate response to someone initiating a joke in a playful manner.
<h1>Conclusion</h1>
Admittedly, classifying Wake Words, speech samples, command phrases and interactions like this one-at-a-time will be a TON of work, but so was drafting an Encyclopedia with 43,000,000 individual entries. The innovation here is that we are applying the same approach to AI that Jimmy Wales applied to Wikipedia – anyone can contribute without an account and, unlike Wikipedia where users had to do research and create entries that fit the standard, all Mycroft contributors need to do is speak the appropriate language.

As time goes on we’ll use the data generated through this innovation to train the AI to classify most interactions on its own. Contributors will only be asked to classify Wake Words, speech samples, phrases or conversations that the AI wasn’t able to assign a high probability to. This is the same way humans learn. Even I ask questions of my peers sometimes when I don’t understand the point of a conversation. I learn by interacting with other people and I react to others based on the context of our conversations.

Using this approach innovators and creators in the field of artificial intelligence will be able to create products that communicate with users naturally.

Among these products will be a handful that will create value above and beyond what exists today – so much so that not only will people be willing to pay for them – they will change the way people use technology profoundly.

Many of you work in healthcare, transportation, communications, technology or finance. Ask yourself – if your technology could understand human speech and respond naturally, what would you build?[/vc_column_text][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][/vc_column][/vc_row]