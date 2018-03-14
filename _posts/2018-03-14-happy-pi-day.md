---
ID: 36303
post_title: Happy Pi Day!
author: Steve Penrod
post_excerpt: ""
layout: post
permalink: http://mycroft.ai/blog/happy-pi-day/
published: true
post_date: 2018-03-14 07:20:24
---
[vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]Today is every math geek's favorite holiday -- Pi Day! In honor of what is calculably the most well rounded holiday we present...<a href="https://mycroft.ai/to/picroft-image">Picroft 18.02</a>!
<h1>Our favorite flavor of Pi? Raspberry!</h1>
Mycroft loves the Raspberry Pi. This flexible piece of hardware fueled the embedded hardware revolution. The Pi 3 in particular brought an incredible package of affordable computational power and flexible hardware to the masses. Mycroft likely won't have existed without it -- we originally started prototyping the project with a Pi 2, and a Pi 3 beats at the heart of every Mark 1.
<h1>What is Picroft?</h1>
A little over a year ago I released the first Picroft image. It was designed to make getting started with Mycroft easy. While installing Mycroft isn't super difficult, adding it to Raspbian has a few gotchas that seemed to trip-up everyone who attempted to do it before Picroft.

For example, PulseAudio -- required by Mycroft -- is particularly finicky on a Raspberry Pi. A long-standing issue in the driver and the way the Pi generates analog output using CPU interrupts would cause periodic 30-second lockups. This made it nearly usable, but not actually fun.

So I wanted to create a definitive image you could download, burn to an SD card, put it in to your Pi3 along with a basic USB microphone and an analog speaker and just plug in. No diddling with drivers, config files or apt-get installs. Even a monitor and keyboard was optional.

The first version wasn't perfect, but it was apparently good enough. To date the various versions have been downloaded over 25,000 times!
<h1>The 18.02 edition</h1>
Like all the technologies at Mycroft, we have evolved Picroft in public and with the help and input of the community. We try to keep the good stuff there and make the rough stuff a little easier.

Key recent changes include:
<ul>
 	<li><strong>CLI interface on by default</strong>
While Picroft can be used without a monitor connected to it, many begin with a keyboard and monitor.</li>
 	<li><strong>Update to the latest wifi-setup/pairing</strong>
During the last few months we've tracked down a few issues with certain phones and routers. The process is quite a bit more robust now.</li>
</ul>
And, of course, this has the latest mycroft-core 18.2.0b pre-installed.  As with the previous builds, it will automatically update itself as we release new versions.
<h1>Add your own topping</h1>
Like the Raspberry Pi itself, Picroft is an enabling technology.  Customize it with your own skills. Connect it to your own hardware and give it a voice. Use the simple ~/audio_setup.sh and ~/custom_setup.sh hooks to easily start up other Raspbian tools or packages you add to the base image.  Create your own delicious flavor of Pi.

Lastly -- show it off!  Share your handiwork and adding the #picroft hashtag to your Youtube or Twitter post.[/vc_column_text][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][divider line_type="Full Width Line" line_thickness="1" divider_color="extra-color-gradient-2"][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][vc_column_text]Picroft isn't the only thing you can hack on. Our next generation voice assistant device is on Indiegogo now. Check out Mark II and all the new specs.[/vc_column_text][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_shadow="none" width="1/1" tablet_text_alignment="default" phone_text_alignment="default" column_border_width="none" column_border_style="solid"][nectar_btn size="large" button_style="regular" button_color_2="Accent-Color" icon_family="none" url="https://www.indiegogo.com/projects/mycroft-mark-ii-the-open-voice-assistant/reft/18156055#/PiDay" text="To Indiegogo!"][/vc_column][/vc_row]