---
description: >-
  Mycroft for Android is a Community led project. It is a proof of concept and is not ready for general use. There is no .apk available. You will need to be familiar with [Android Studio](https://developer.android.com/studio/index.html).
---

# Android

There are two components to Mycroft for Android:

1. The Android companion app. The app works by opening a websocket connection to the `mycroft-core` messagebus, and sending and receiving messages from there. It implements voice recognition and Text to Speech \(TTS\) via Google APIs at the moment,
2. Mycroft Core. Mycroft for Android requires that you already have `mycroft-core` installed and working on a machine that the Android application can access via a websocket connection.

### Prerequisites

This section of documentation assumes the following:

* That you already have [Android Studio](https://developer.android.com/studio/index.html) installed, and are familiar with using Android Studio. If not, [this introduction](https://developer.android.com/studio/intro/index.html) is a good starting point.
* That you already have an Android device, and that you're comfortable loading Android applications on to the device from Android Studio.

### Getting Started

First, you will need to clone the `git` repo and import it into your IDE.

```text
$ git clone https://github.com/MycroftAI/Mycroft-Android
Cloning into 'Mycroft-Android'...
remote: Counting objects: 1381, done.
remote: Total 1381 (delta 0), reused 0 (delta 0), pack-reused 1381
Receiving objects: 100% (1381/1381), 538.46 KiB | 210.00 KiB/s, done.
Resolving deltas: 100% (648/648), done.
Checking connectivity... done.
```

From Android Studio, choose `File -> Open file or Project` and select the directory you cloned `Mycroft-Android` into. Android Studio will attempt to load the project, and build the project using [Gradle](https://gradle.org/). You may be prompted to install additional components.

![Android Studio with Mycroft-Android loaded](https://mycroft.ai/wp-content/uploads/2017/12/android-studio-with-mycroft-for-android-loaded.png)

### Connecting to a `mycroft-core` instance

@TODO not sure how this works

### Pairing Mycroft for Android

There is no need to pair Mycroft for Android, as the companion app connects to your `mycroft-core` instance, and uses the pairing from that.

#### Keeping Mycroft for Android updated

The easiest way to keep Mycroft for Android updated is to clone the `git` repo when you want to build a new image to deploy to your Android phone.

### Common issues with Mycroft for Android

@TODO link to Troubleshooting
