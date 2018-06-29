---
ID: 39182
post_title: "Mycroft for KDE Plasma"
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?p=39182
published: false
---
+ [Plasma-Mycroft User Guide](#plasma-mycroft-user-guide)
  - [Getting Started](#getting-familiar-with-the-interface)
  - [Troubleshooting](#troubleshooting-plasma-mycroft)
+ [Visual API Developers Guide For Plasma-Mycroft](#visual-display-api-developers-guide-for-plasma-mycroft)
  * [HTML based Visual Skill Generation](#html-based-visual-skill-generation)
  * [QML based Visual Skill Generation](#qml-based-visual-skill-generation)
  * [Plasma-Mycroft Native Visual Skill](#plasma-mycroft-native-visual-skill)

PLASMA MYCROFT USER GUIDE
=========================
This is a General User Guide for Plasma-Mycroft on KDE Desktop Platform. This User Guide aims to provide an overview of Getting Started with Mycroft AI on your KDE Plasma Desktop.  

GETTING STARTED
===============
* Please Note: For Installation Instructions Please Refer To The Installation Guide(https://mycroft.ai/documentation/linux)

### Getting Familiar With The Interface
![Plasma Mycroft Screenshot](https://mycroft.ai/wp-content/uploads/2018/06/plasmoid-gs1.png)

TROUBLESHOOTING PLASMA-MYCROFT
==============================
### Debuging Connection Error Problems
* Check Your Mycroft-Core Location Is Correctly Setup In Plasma-Mycroft Settings, By Default Plasma Mycroft Searches For Mycroft In Your Home Path: ```/home/$USER/mycroft-core```
* Check If Mycroft-Core Is Able To Start Manually Using The Debug Console: ```./start-mycroft.sh debug```
* Check If Your Firewall Is Blocking Incoming Connections To Mycroft WebSocket Address
* Check Mycroft-Messagebus Logs To Find Any Errors Blocking Your Connection
* Check If Plasma-Mycroft Start and Stop Scripts Have Executable Access, Location: ```/usr/share/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/startservice.sh ```, ```/usr/share/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/stopservice.sh```

VISUAL DISPLAY API DEVELOPERS GUIDE FOR PLASMA MYCROFT
======================================================

The Plasma-Mycroft desktop enclosure provides Mycroft AI skill
developers a visual display platform to showcase skill results and data
in the form of interactive visual cards that can be created by the skill
developers using popular UI/UX technologies such as **HTML** and **QML**

HTML BASED VISUAL SKILL GENERATION
==================================

*Wikipedia Skill HTML Example*
------------------------------

### Create a HTML folder inside your skill folder and Map path to folder:

``` {.XML}
                class WikipediaSkill(MycroftSkill):
                def __init__(self):
                    ....
                    self.html_index = dirname(__file__) + '/html/' # Location where the html files will be generated
                    self.css_index = dirname(__file__) + '/html/wiki.css'# Location of your main.css file
```

### **Create a "__genwebview(self)" Function:**

This function is used to generate the html page within the skill.

``` {.XML}
                def __genwebview(self, sm, imagemain, title):
                    simg = imagemain # Image url received from wikipedia api 
                    smry = sm.encode('utf-8') # Summary received from wikipedia api encoded to utf8 
                    stitle = title.encode('utf-8') # Article title encoded to utf8 
                    fname = self.html_index + stitle + 'wikiresult.html' # Path of html folder location + name of html file that will be generated 
                    scss = self.css_index # Path of your main css file which you have manually created 
                    f = open(fname,'w')
                    wrapper = """<html><head><link rel="stylesheet"
                        type="text/css" href="{0}"></head><body><div id="imgPlace"
                        style="background-image:
                        url('{1}')"><h1><strong>{2}</strong></h1></div><div
                        id="wikisummary"><p
                        id="paratext">{3}</p></div></body></html>""".format(scss, simg,
                        stitle, smry) # The wrapper is where you define your basic html layout for the skill
                        and using the format function pass variables to the html that will be used at
                        the time of generation. Writing complex JS and CSS in the wrapper should be
                        avoided and should be placed in the HTML folder as external files. Example JS
                        inclusion would have a self.js_index which could be passed to <script
                        src={x}></script> inside <head>
                    f.write(wrapper) f.close()                
```

### **Call the "__genwebview(self)" Function from handle intent:**

``` {.XML}
                def handle_intent(self, message):
                    try:
                         ....
                         sm = wiki.summary(results[0],sentences = 20); # Summary to be sent to
                         __genwebvie(self) func spage = wiki.page(title); # Article title to be sent to
                         __genwebvie(self) func imagemain = spage.images[1] # Page Image to be sent to
                         __genwebvie(self) func self.__genwebview(sm, imagemain, title) # Calling the function to generate the HTML page after data is
                        available
                         ....                
```

### **Send the url to the enclosure for handling via "self_enclosure.ws.emit" Function**

``` {.XML}
                # Requires import: from mycroft.messagebus.message import Message
                def handle_intent(self, message):
                    try:
                        ....
                        self.__genwebview(sm, imagemain, title)
                        self.enclosure.ws.emit(Message("data", {'desktop': {'url': self.html_index + title + 'wikiresult.html'}})) # This function emits metadata and url of generated html over websockets to
                        the desktop clients. This can include extra meta data also apart from URL like for example weather data variables. This function can be called before or after self.speak(summary) depending on where you like to position your webview
                        self.speak(summary)
                        ....
                # Format for desktop enclosure: self.enclosure.emit(Message{“data”, {“desktop”: {‘ any’: ‘any data’}}))
```

### **The CSS File**

The CSS file should be manually generated by the skill creator.

``` {.XML}
                html, body { margin: 0; padding: 0 } # Important to include in your css to avoid whitespace borders
            
                # CSS for your view should be responsive, Fixed sizes and non responsive layouts will break on different screen sizes.             
```

QML BASED VISUAL SKILL GENERATION
=================================

*Wikipedia Skill QML Example*
-----------------------------

### **Create a QML folder inside your skill folder and Map path to folder**

``` {.XML}
 
                class WikipediaSkill(MycroftSkill):
                def __init__(self):
                     ....
                    self.qml_index = dirname(__file__) + '/qml/' # Location where the qml files will be generated                
```

### **Create a "__genvisualobjecttemplate" Function**

This function is used to generate the QML visual object within the
skill.

``` {.XML}
 
                def __genvisualobjecttemplate(self, sm, imagemain, title):
                    simg = imagemain # Image url received from wikipedia api 
                    smry = sm.encode('utf-8') # Summary received from wikipedia api encoded to utf8 
                    stitle = title.encode('utf-8') # Article title encoded to utf8 
                    fname = self.visualobject_index + stitle + "Wikiresult.qml" # Path of QML folder location + name of QML file that will be generated
                    f = open(fname,'w')
                    wrapper = """import QtQuick 2.9   # All import libs and dependencies can be installed using the Requirements.sh file distributed with the skills
                    import QtQuick.Controls 2.2
                    import QtQuick.Layouts 1.3
                    
                    Rectangle {{   # As we are building the qml code write into the python function we need to use double brackets for all QML objects to escape characters
                          id: bgRect 
                          width: 500; height: 100
                          color: "#222"
                           
                              Rectangle {{
                                    id: mainRect
                                    anchors.fill: parent
                                    color: "#222"
                                    
                                    Image {{
                                        id: mainTopImage
                                        anchors.top: parent.top 
                                        source: "{0}"
                                        height: parent.height
                                        width: parent.width
                                        }}
                                        }}
                                }}""".format(simg)
                    
                    """.format(scss, simg, stitle, smry)
                    f.write(wrapper) # The wrapper is where you define your basic QM layout for the skill 
                    f.close()
```

### **Call the "__genvisualobjecttemplate(self)" Function from handle intent**

``` {.XML}
                    def handle_intent(self, message):
                      try:
                        ....
                        sm = wiki.summary(results[0],sentences = 20); #Summary to be sent to __genwebvie(self) func
                        spage = wiki.page(title); #Article title to be sent to __genwebvie(self) func
                        imagemain = spage.images[1] #Page Image to be sent to __genwebvie(self) func    
                           self.__genbvisualobjecttemplate(sm, imagemain, title) # Calling the function to generate the QML page after data is available
                        ....
                
```

### **Send the QML file location to the enclosure for handling via "self_enclosure.ws.emit" Function**

``` {.XML}
                  #Requires import: from mycroft.messagebus.message import Message
                    
                    def handle_intent(self, message):
                        try:
                            ....
                           self.enclosure.ws.emit(Message("visualObject", {'desktop': {'url': self.visualobject_index + title + 'Wikiresult.qml'}})) 
                           # This function emits the visual object and qml location to the loader functiion in the mycroft plasmoid. This function can be called before or after self.speak(summary) depending on where you like to position your qml visualobject
                           self.speak(summary)
                            ....                
```

PLASMA-MYCROFT NATIVE VISUAL SKILL
==================================
The Plasma-Mycroft enclosure also provides skill authors to natively implement visual design for their skill by providing a simple Object to the plasmoid.

### **Create custom visual object and emit to plasmoid**

```                         
                    def handle_intent(self, message):
                            ....
                           self.enclosure.ws.emit(Message("yourCustomObjectName", {'desktop': {'Your Custom Data Objects'}})) 
                            ....                
```

Once added to your skill you can reach out to the Plasma-Mycroft maintainer to discuss the design and implementation of your skill.
