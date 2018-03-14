---
ID: 36409
post_title: >
  Finding Laughter in the Early Stages of
  Voice Technology
author: Alyx Horace
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/finding-laughter-in-the-early-stages-of-voice-technology/
published: true
post_date: 2018-03-12 17:21:55
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]
<h3><strong>What can the voice industry learn from the Alexa laughing incidents? </strong></h3>
<span style="font-weight: 400;">Testing, iteration, and failure </span><i><span style="font-weight: 400;">will </span></i><span style="font-weight: 400;">be a part of the journey when you’re building a technology and industry from the ground up. If you haven’t seen the news about Amazon’s Alexa chuckling randomly at users, let us bring you up to speed.</span>

<span style="font-weight: 400;">For the past few weeks there have been increasing reports of users hearing an eerie laugh come from their Alexa--randomly, without asking or triggering the skill. Videos flooded social media from users that caught these utterances, most claiming how unnerving they found it.</span>

<span style="font-weight: 400;">Some users went on, waiting for it to happen again. Others unplugged their device. News agencies stood by, waiting for Amazon to catch the “bug.” </span>

<span style="font-weight: 400;">But was it a bug? No. It’s a product of the architecture of voice assistants that highlights why building this technology is so complicated. In fact, everyone working on voice platforms runs into similar problems, it just so happens that Alexa’s made users feel like they were filming the next paranormal activity.</span>

&nbsp;

&nbsp;
<h3><strong>So what really happened?</strong></h3>
<span style="font-weight: 400;">Likely, a poorly trained “</span><i><span style="font-weight: 400;">Intent</span></i><span style="font-weight: 400;">.” </span>

<span style="font-weight: 400;">Users saying “Alexa, laugh” is the Wake Word (Alexa) + command (Laugh.) </span>

<span style="font-weight: 400;">The voice assistant pulls the </span><i><span style="font-weight: 400;">Intent</span></i><span style="font-weight: 400;"> (action keywords, in this case it’s “laugh”), and then executes on it by taking an action - in this case by playing a laughing sound. </span>

<span style="font-weight: 400;">The problem is that the </span><i><span style="font-weight: 400;">phonemes</span></i><span style="font-weight: 400;"> - think of them as building blocks for speech -  for “Alexa, laugh” are similar to several regular words or phrases. One of the trickiest parts of speech recognition is distinguishing between two phrases that sound similar </span><i><span style="font-weight: 400;">phonetically</span></i><span style="font-weight: 400;">, but have very different meaning. </span>

&nbsp;

<span style="font-weight: 400;">Examples:</span>

<i><span style="font-weight: 400;">A Lexus left</span></i><span style="font-weight: 400;"> the car lot </span>

<span style="font-weight: 400;">Hahaha</span>

&nbsp;

<i><span style="font-weight: 400;">Let’s have half</span></i><span style="font-weight: 400;"> of that chocolate cake </span>

<span style="font-weight: 400;">Hahahaha (because you’re supposed to be on a diet)</span>

&nbsp;

&nbsp;
<h3><strong>How is Amazon fixing it? </strong></h3>
<span style="font-weight: 400;">In an emailed statement to the </span><a href="https://www.nytimes.com/2018/03/08/business/alexa-laugh-amazon-echo.html"><span style="font-weight: 400;">New York Times</span></a><span style="font-weight: 400;"> they said, “We are changing that phrase to be ‘Alexa, can you laugh?’ which is less likely to have false positives, and we are disabling the short utterance ‘Alexa, laugh.’” </span>

<span style="font-weight: 400;">In addition, they’re changing the response to the command to, “Sure, I can laugh” and then following that with the laughing sounds. This verification serves as a buffer to let users know that the voice assistant was triggered.</span>

&nbsp;

&nbsp;
<h3><strong>So what can the voice industry learn from the Alexa laughing lesson?</strong></h3>
<span style="font-weight: 400;">Intent parsing requires substantial training data and user testing. The more that a neural network is ‘trained’, the more accurate it becomes. It learns to better distinguish between similar sounding </span><i><span style="font-weight: 400;">phonemes</span></i><span style="font-weight: 400;">. Without adequate training and testing, the rate of ‘false positives’ - when an </span><i><span style="font-weight: 400;">Intent</span></i><span style="font-weight: 400;"> is incorrectly triggered - is too high - and voice assistants risk the sort of incidents that we’ve seen with Alexa laughing. </span>

<span style="font-weight: 400;">Now, more than ever, it’s important that voice assistants are trained on a variety of voices. Voices from different people, different ethnicities, different genders, different ages, different accents and different speech abilities. Every voice assistant in the market - and those in development - will become more robust as we use the lessons learned in this episode to further improve and iterate our technology.</span>

&nbsp;

&nbsp;
<h3><strong>These events underscore a few crucial pieces regarding voice technology that’s built in a “black box” fashion.</strong></h3>
<span style="font-weight: 400;">Voice assistants are placed in intimate parts of the home. </span>

<span style="font-weight: 400;">Even when a Wake Word is accidentally triggered, the device begins recording. That means that when a stream of </span><i><span style="font-weight: 400;">phonemes</span></i><span style="font-weight: 400;"> - sound building blocks - that sound like a Wake Word - is detected - that personal data is sent and saved to corporate servers. That’s a lot of privacy to forego for accidental triggers - which will continue to happen, regardless of platform, for some time to come as voice assistants are still being trained. </span>

<span style="font-weight: 400;">The ‘black box’ nature - the inability to see what’s inside - is also an element of concern for users who were left waiting for answers when they heard chuckles coming from the corner. No one outside of Amazon could inspect the code, or work on identifying and resolving the issue. As the world transitions to a shared, decentralized economy, our ubiquitous and pervasive technologies need to keep pace. </span>

<span style="font-weight: 400;">Open source voice technologies - such as Mycroft AI - provide transparency while protecting privacy. While we share the same challenges around accurate Wake Word recognition and </span><i><span style="font-weight: 400;">Intent Parsing</span></i><span style="font-weight: 400;"> that proprietary voice companies do, we have a significant advantage when issues do arise: our code is open for all to see. That means not only are our algorithms and methods able to be inspected - they also invite participation and collective improvement. </span>[/vc_column_text][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][divider line_type="Full Width Line" line_thickness="1" divider_color="extra-color-gradient-2"][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]How can you help support privacy and user agency in voice technology? Back us on Indiegogo. Our next generation voice assistant, Mark II is out now.[/vc_column_text][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][nectar_btn size="large" open_new_tab="true" button_style="regular" button_color_2="Accent-Color" icon_family="none" url="https://www.indiegogo.com/projects/mycroft-mark-ii-the-open-voice-assistant/reft/18156055#/Laugh-Blog" text="Check It Out"][/vc_column][/vc_row]