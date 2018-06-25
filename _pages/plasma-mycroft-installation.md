---
ID:
post_title: PLASMA MYCROFT INSTALLATION GUIDE
author: Aditya Mehra aka AIX(aix.m@outlook.com)
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/documentation/plasma-mycroft-installation
published: false
post_date: 2018-06-25 19:30:00
---

+ [Plasma-Mycroft Installation Guide](#plasma-mycroft-user-guide)
  - [Distribution Packages](#distribution-packages)
  - [Plasma-Mycroft Installer](#plasma-mycroft-installer)
  - [Plasma-Mycroft Installation Scripts](#plasma-mycroft-installation-scripts)
  - [Plasma-Mycroft Manual Installation](#plasma-mycroft-manual-installation)

PLASMA MYCROFT INSTALLATION GUIDE
=================================
This is a General Installation Guide for Plasma-Mycroft on KDE Desktop Platform.

DISTRIBUTION PACAKAGES
======================
Check with your Linux Distribution for Mycroft-Core and Plasma-Mycroft packages

#### KDE NEON GIT UNSTABLE
Please Note: KDE Neon Only Provides Plasma-Mycroft Packages For GIT Unstable Edition. This Installation Method Requires Mycroft-Core To Be Installed In Your Home Folder Following The Guide Available Here: https://mycroft.ai/documentation/linux/
``` sudo apt install plasma-mycroft ```



PLASMA-MYCROFT-INSTALLER
=========================
|Supported Distributions|
|---|
|Debian Testing|
|KDE Neon Xenial, Bionic|
|Kubuntu 17.10, 18.04|
|Fedora 27, 28|

Download The Latest Installer AppImage From: https://github.com/AIIX/mycroft-installer/releases
* Please Note: This installer also provides support for installing Mycroft-Core & Plasma-Mycroft on Arm64 and ArmHF architecture.

PLASMA-MYCROFT-INSTALLER-SCRIPTS
================================
* Installation scripts are available at https://github.com/MycroftAI/installers


PLASMA-MYCROFT-MANUAL-INSTALLATION
==================================
Please Note: This Installation Method Requires Mycroft-Core To Be Installed In Your Home Folder Following The Guide Available Here: https://mycroft.ai/documentation/linux/

```
    git clone https://anongit.kde.org/plasma-mycroft.git
    cd plasma-mycroft
    mkdir build
    cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release   -DKDE_INSTALL_LIBDIR=lib -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
    make
    sudo make install
    sudo chmod +x /usr/share/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/startservice.sh
    sudo chmod +x /usr/share/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/stopservice.sh
    sudo chmod +x /usr/share/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/pkgstartservice.sh
    sudo chmod +x /usr/share/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/pkgstopservice.sh
    
```

