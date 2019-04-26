---
ID: 46998
post_title: 'The Mycroft GUI &#8211; The Screen is Dead. Long Live the Screen!'
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/the-mycroft-gui-the-screen-is-dead-long-live-the-screen/
published: true
post_date: 2019-04-26 12:00:56
---
With a voice interface, there is no longer a need for screens – right?
Wrong! Natural language voice interfaces <em>are</em> great for issuing commands without having to navigate menus and dialogs to "get to the right screen". At times a quick verbal response contains all the info you need. But humans are visual creatures and the old saying is true, a picture <em>is</em> worth a thousand words.

The classic example is a basic weather skill. "What's the weather like?" is easily answered with "63 degrees and sunny". But nobody wants the response to "Tell me the weather forecast for this weekend" to drone on with the high, low and expected condition for three days. And the 7-day forecast? Ain't nobody got time for that. But a single graphic display can convey all of that information in a second to your highly efficient visual cortex.

Visual interfaces can also answer questions without even being asked. Start a timer and see the remaining time on the screen with a silent glance. Get the name of the current song without breaking the mood. Visual interfaces are excellent mechanisms for conveying information.
<h2>Mycroft's Got Skills</h2>
For anyone who has extended Mycroft for their own purposes, the concept of a Skill is well-known. Vocabulary, Intents, Intent Handlers, and Dialog are the basic pieces needed to connect your cool API or custom code to a verbal interface. The Mycroft GUI extends this elegantly, providing access to the simple-but-powerful visual interface technology built by KDE and Qt.

For simple interactions, Mycroft provides basic functions for displaying text, images or web pages. WAV and MP3 files can also be played and controlled with an attractive playback interface.

For a custom visual experience, the Graphical User Interface (aka "GUI") for a skill is defined by a series of pages written using QML. QML is a markup language which combines elements of HTML, CSS, and Javascript. Skills can provide several pages to be displayed individually or as part of a group, which can be advanced via code or when a user swipes left or right. The skill can also pass variables into the page which the QML can display directly, or which can be used to define a more complex graphic or behavioral sequence.
<h2>Example: What time is it?</h2>
The hello world of the voice world is "What time is it?" Mycroft easily handles this with code like this:
<pre>  @intent_file_handler("what.time.is.it")
  def handle_time_query(self, message):
    current = now_local()
    self.speak(nice_time(current))</pre>
This will catch phrases similar to the examples in the "what.time.is.it" file, answering with something like "six oh two". Nice and easy.

Adding a visualization to this is almost as easy:
<pre>  @intent_file_handler("what.time.is.it")
  def handle_time_query(self, message):
    current = now_local()
    hh_mm = nice_time(current, speech=False, use_24hour=False)
    self.gui["time_string"] = hh_mm # e.g. "7:00"
    self.gui.show_page("clock_face.qml")
    self.speak(nice_time(current))</pre>
These extra three lines tell Mycroft to look for an available GUI, load up the page called <code>"clock_face.qml"</code>, and pass it the value <code>"hh_mm"</code> with the current time as a string like <code>"7:00"</code>.

The QML to convert this info into a digital clock is a little more complex so I won't show it here (but you can <a href="https://github.com/MycroftAI/skill-date-time/blob/19.02/ui/time.qml" target="_blank" rel="noopener noreferrer">look at it here</a>). Basically, Javascript splits the <code>"time_string"</code> variable into Hour and Minute at the colon, adjusting the QML elements to show that time. With that, you have your clock!
<h2>Smart variables</h2>
You don't want to have to constantly speak to your clock just to check the time. With the Mycroft GUI we can easily update the <code>"hhmm"</code> variable in a simple timer callback, something like this:
<pre>  def initialize(self):
    self.schedule_repeating_event(self.update_display, None, 1)

  def callback_time(self):
    current = now_local()
    hh_mm = nice_time(current, speech=False, use_24hour=False)
    self.gui["hhmm"] = hh_mm # e.g. "7:00"</pre>
This calls your function once a second, updating the <code>"hhmm"</code> variable with the current time. That's all you need to do. As long as the page is showing, the QML will receive a notification only when the <code>"hhmm"</code> value actually changes, then the position of the hands will update accordingly. Easy peasy!
<h2>Two Way</h2>
QML can also change values, sending a notification back to the skill when some screen interaction has occurred. A skill can capture this by defining a notification handler using code like:
<pre>  def initialize(self):
    self.gui.set_on_gui_changed(self.handle_gui_notification)
  def handle_gui_notification():
    # Look at your skill variables (one of them is different) and
    # react accordingly!</pre>
These notifications could occur in response to the user moving something on-screen: things like dragging the clock hands, clicking a button, or filling a form with text and pressing the Save button.
<h2>Powerful Simplicity</h2>
With just those basic hooks, you have what you need to display nearly anything you can imagine AND react to the user interactions on a screen. Verbal and graphical interfaces can live in harmony, each doing what they do best.
<h2>Screens Anywhere</h2>
One of the most powerful things about this GUI design is that you don't even need to have a device with a screen. Other devices can register on the Mycroft Messagebus, allowing for future devices to show a GUI on things like a TV connected to a Raspberry Pi or a streaming media player which implements the Mycroft GUI protocols. Mycroft will be able to take advantage of whatever screens are visible to the user!
<h2>Documentation and More Examples</h2>
You can learn more about the Mycroft GUI by reading the <a href="https://github.com/mycroftai/mycroft-gui/blob/master/documentations" target="_blank" rel="noopener noreferrer">tutorial on Github</a>, and by examining the code of our examples. There is excellent documentation for the <a href="https://doc.qt.io/qt-5/qml-tutorial.html" target="_blank" rel="noopener noreferrer">QML markup language</a> and the <a href="https://www.kde.org/products/kirigami/" target="_blank" rel="noopener noreferrer">Kirigami visual framework</a>.

See the <a href="https://github.com/mycroftai/skill-date-time" target="_blank" rel="noopener noreferrer">Date-Time</a> and <a href="https://github.com/mycroftai/skill-weather" target="_blank" rel="noopener noreferrer">Weather</a> skills for examples of what is possible, and the <a href="https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/skills/core.py#L219" target="_blank" rel="noopener noreferrer">SkillGUI</a> class for complete details.
<h2>Have fun!</h2>
Use your creativity to push the bounds of QML and Mycroft. When you get something cool going, post a link to it on the forum!