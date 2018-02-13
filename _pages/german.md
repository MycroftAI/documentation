---
ID: 33364
post_title: Language support in Mycroft – German
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/language-support/german/
published: true
post_date: 2017-12-03 04:41:11
---
# Language support in Mycroft - German - Deutsch

_NOTE: These instructions apply to Mycroft for Linux only; we don't currently have instructions for changing the language on Picroft. If you'd like to help us out with that, jump into the [~languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages) and let us know._

- [Language support in Mycroft - German - Deutsch](#language-support-in-mycroft---german---deutsch)
  * [ändere das **Wake Word** nach Deutsch](#andere-das-wake-word-nach-deutsch)
    + [Laden Sie das deutsche Wörterbuch herunter und installieren Sie es](#laden-sie-das-deutsche-worterbuch-herunter-und-installieren-sie-es)
    + [Laden des akustischen Modells und die Installation](#laden-des-akustischen-modells-und-die-installation)
    + [Laden Sie das deutsche Sprachmodell herunter und installieren Sie es](#laden-sie-das-deutsche-sprachmodell-herunter-und-installieren-sie-es)
    + [Überprüfen Sie die installierten Dateien](#uberprufen-sie-die-installierten-dateien)
    + [Installieren Sie die Sprache in Mycroft-Verzeichnissen](#installieren-sie-die-sprache-in-mycroft-verzeichnissen)
    + [Einen Deutsches **Wake Word** wählen](#einen-deutsches-wake-word-wahlen)
    + [Konfigurieren Sie Mycroft für die Verwendung der deutschen Sprache und des ausgewählten Sprache **Wake Word**](#konfigurieren-sie-mycroft-fur-die-verwendung-der-deutschen-sprache-und-des-ausgewahlten-sprache-wake-word)
  * [Wählen und konfigurieren Sie eine STT-Engine (Speak to Text) mit deutscher Unterstützung](#wahlen-und-konfigurieren-sie-eine-stt-engine-speak-to-text-mit-deutscher-unterstutzung)
  * [Wählen und konfigurieren Sie eine TTS-Engine (Text to Speech) mit deutscher Unterstützung](#wahlen-und-konfigurieren-sie-eine-tts-engine-text-to-speech-mit-deutscher-unterstutzung)
  * [Konfigurieren Sie den Mycroft-Quellcode für die Handhabung von Deutsch](#konfigurieren-sie-den-mycroft-quellcode-fur-die-handhabung-von-deutsch)
  * [Sie wollen Einbezogen werden?](#sie-wollen-einbezogen-werden)

Guten tag. Sprechen sie Deutsch? Befolgen Sie diese Schritte, um die Sprache von Mycroft auf Deutsch zu ändern (BCP 47: `de`).

Wenn Sie Deutsch sprechen und die deutsche Sprachunterstützung für Mycroft aktivieren möchten, ist dies möglich. Dies erfordert jedoch einige technische Kenntnisse wie:

* Verschieben und Kopieren von Dateien in einer Linux-Shell
* Herunterladen und Entpacken großer Dateien
* Bearbeiten von Python-Quellcode-Dateien

Wenn Sie weitere Hilfe benötigen, melden Sie sich bitte bei uns an [Languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages).

## ändere das **Wake Word** nach Deutsch

Mycroft verwendet PocketSphinx als **Wake Word** Mechanismus. Das Standart **Wake Word** in English ist `Hey Mycroft`.

Um das **Wake Word** nach Deutsch zu ändern müssen wir das Deutsche Wörterbuch und das Deutsche akustikmodel herunterladen, danach trainieren wir mit dem neusten `sphinxtrain`.

Zuerst erstellen wir ein Verzeichnis für die `pocketsphinx` Dateien:

`sudo mkdir -p /usr/local/share/pocketsphinx/model/de/de`

### Laden Sie das deutsche Wörterbuch herunter und installieren Sie es

Als nächstes laden wir das deutsche Wörterbuch aus dem CMUSphinx-Projekt auf SourceForge herunter_ [cmusphinx-voxforge-de.dic](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.dic/download).

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.dic/download -O cmusphinx-voxforge-de.dic`

Dann installieren wir das Wörterbuch in das von uns erstellte Verzeichnis.

`sudo mv cmusphinx-voxforge-de.dic /usr/local/share/pocketsphinx/model/de/de.dict`

### Laden des akustischen Modells und die Installation

Als nächstes laden wir die _acoustic model_ [cmusphinx-de-ptm-voxforge-5.2.tar.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-de-ptm-voxforge-5.2.tar.gz/download) aus dem CMUSphinx-Projekt auf SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-de-ptm-voxforge-5.2.tar.gz/download -O cmusphinx-de-ptm-voxforge-5.2.tar.gz`

Wir entpacken dann die gezippte Datei in ein temporäres Verzeichnis.

`tar -xf cmusphinx-de-ptm-voxforge-5.2.tar.gz`

Dann kopieren wir es in das PocketSphinx-Verzeichnis

```bash
cd cmusphinx-ptm-voxforge-de-r20171217/model_parameters/voxforge.cd_ptm_5000
sudo mv * /usr/local/share/pocketsphinx/model/de/de
cd ..
```

### Laden Sie das deutsche Sprachmodell herunter und installieren Sie es

Als nächstes laden wir die _German language model_ [cmusphinx-voxforge-de.lm.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.lm.gz/download) aus dem CMUSphinx-Projekt auf SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.lm.gz/download -O cmusphinx-voxforge-de.lm.gz`

Wir entpacken dann die gezippte Datei in ein temporäres Verzeichnis.

`gzip -d cmusphinx-voxforge-de.lm.gz`

Dann verschieben wir es in das PocketSphinx-Verzeichnis

`sudo mv cmusphinx-voxforge-de.lm /usr/local/share/pocketsphinx/model/de/de.lm`

### Überprüfen Sie die installierten Dateien

Überprüfen Sie, ob die folgenden Dateien existieren:

* `/usr/local/share/pocketsphinx/model/de`
* `/usr/local/share/pocketsphinx/model/de/de.dict`
* `/usr/local/share/pocketsphinx/model/de/de.lm`
* `/usr/local/share/pocketsphinx/model/de/de`
* `/usr/local/share/pocketsphinx/model/de/de/feat.params`
* `/usr/local/share/pocketsphinx/model/de/de/mdef`
* `/usr/local/share/pocketsphinx/model/de/de/means`
* `/usr/local/share/pocketsphinx/model/de/de/mixture_weights`
* `/usr/local/share/pocketsphinx/model/de/de/noisedict`
* `/usr/local/share/pocketsphinx/model/de/de/README`
* `/usr/local/share/pocketsphinx/model/de/de/sendump`
* `/usr/local/share/pocketsphinx/model/de/de/transition_matrices`
* `/usr/local/share/pocketsphinx/model/de/de/variances`

### Installieren Sie die Sprache in Mycroft-Verzeichnissen

Nachdem wir die PocketSphinx-Dateien für Deutsch installiert haben, müssen wir Deutsch in den Mycroft-Verzeichnissen installieren.

Zuerst, [SSH into your device](https://mycroft.ai/documentation/mark-1/#connecting-to-the-mark-1-via-ssh).


Navigieren Sie zum Mycroft-Sprachenmodellverzeichnis.

Zum Beispiel, auf `mycroft-core` für Linux, navigiere zu

`/mycroft-core/mycroft/client/speech/recognizer/model`

Sie sollten die folgenden Dateien in diesem Verzeichnis sehen:

```bash
$ ls -las
total 24
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 .
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 ..
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 en-us
```

_HINWEIS: Beachten Sie, dass es nur einen Modellordner gibt - `en-us` für American English_

Erstellen Sie hier ein neues Verzeichnis für Deutsch, und verlinken Sie es anschließend mit dem `pocketsphinx` Verzeichnis.

```bash
mkdir de
ln -s /usr/local/share/pocketsphinx/model/de/de de/hmm
cp /usr/local/share/pocketsphinx/model/de/de.lm de/de.lm
cp /usr/local/share/pocketsphinx/model/de/de.dict de/de.dict
```
_Hinsweis: Der `cp`Befehl könnte durch `ln` Befehl ersetzt werden um Speicherplatz zu sparen. Es ist jedoch normal, Wörter hinzuzufügen `de.dict`, Kopieren bedeutet, dass die Originaldatei unverändert ist und Sie mit einer Kopie arbeiten._

Sie müssten die folgenden Verzeichnisse, Dateien und symbolischen Verknüpfungen haben:

* `_your_base_dir_/mycroft/client/speech/recognizer/model/de`
* `_your_base_dir_mycroft/client/speech/recognizer/model/de/hmm`
* `_your_base_dir_mycroft/client/speech/recognizer/model/de/de.dict`
* `_your_base_dir_mycroft/client/speech/recognizer/model/de/de.lm`

### Einen Deutsches **Wake Word** wählen

Wähle ein **Wake Word** oder Wake Phrase auf Deutsch, und vergewissere dich dann, dass es in der `cmusphinx-voxforge-de.dic` datei des language models enthalten ist. Die Erfahrung zeigt, dass die beste Wahl ein einzelnes Wort mit drei oder mehr Phonemen ist.

Überprüfen Sie zum Beispiel, ob das 'hallo' Word existiert:

`egrep '^hallo ' de.dict`

`hallo HH AE L AX UU`

Wenn das gewählte **Wake Word** oder Phrase ist nicht in der `de.dict` Datei ist, wählen Sie entweder einen anderes **Wake Word**, or ändere die `de.dict` Datei um es hinzuzufügen.

### Konfigurieren Sie Mycroft für die Verwendung der deutschen Sprache und des ausgewählten Sprache **Wake Word**

Suchen Sie zuerst nach `mycroft.conf` Konfigurationsdatei. Bei Mycroft für Linux ist dies hier gespeichert:

`_your_base_dir_mycroft/mycroft/configuration/mycroft.conf`

Bearbeiten Sie die Konfigurationsdatei mit folgenden Änderungen:

```json

    {
      "lang": "de",

      "listener": {

        "wake_word": "hallo",
        "phonemes": "HH AE L AX UU",
        "threshold": 1e-10,
        "standup_word": "hallo",
        "standup_phonemes": "HH AE L AX UU",
        "standup_threshold": 1e-10
      }
    }
```

## Wählen und konfigurieren Sie eine STT-Engine (Speak to Text) mit deutscher Unterstützung

Wenn die Sprache-zu-Text-Engine, die Sie verwenden, bereits Deutsch unterstützt, müssen Sie nichts tun - dies ist beispielsweise bei der standardmäßigen mycroft-Engine der Fall.

Alternativ können Sie PocketSphinx verwenden, das auf Ihrem lokalen Computer ausgeführt wird. Um PocketSphinx als STT-Engine zu verwenden, fügen Sie folgendes zu Ihrer `mycroft.conf` Datei hinzu:

```json
    "listener": {
       "producer": "pocketsphinx",
       "grammar": "lm"
       }
```

## Wählen und konfigurieren Sie eine TTS-Engine (Text to Speech) mit deutscher Unterstützung

Wählen Sie als Nächstes ein Text-to-Speech-Modul aus und konfigurieren Sie es, das Deutsch unterstützt. Beispielsweise, `espeak` hat unterschiedliche Deutsche Stimmen.

Fügen Sie folgendes ihrer `mycroft.conf` Datei, um Ihre TTS-Engine zu konfigurieren:

```json
    "tts": {
      "module": "espeak",
      "espeak": {
        "lang": "de",
        "voice": "m1"
      }
    }
```

## Konfigurieren Sie den Mycroft-Quellcode für die Handhabung von Deutsch

Es gibt noch einige Quellcodeänderungen, die erforderlich sind, um eine Sprachänderung zu handhaben, und sie erfordern eine manuelle Änderung des Quellcodes, da sie noch nicht in `mycroft-core` einbezogen wurden.

* [Changes to `listener.py` and `pocketsphinx_audio_consumer.py`](https://github.com/MycroftAI/mycroft-core/pull/656)

## Sie wollen Einbezogen werden?

Wenn Sie sich für fremdsprachige Übersetzungen von Mycroft interessieren, würden wir uns freuen, von Ihnen zu hören. Bitte besuchen Sie uns im [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)