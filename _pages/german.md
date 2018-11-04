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

_NOTE: These instructions apply to Mycroft for Linux only; we don't currently have instructions for changing the language on Picroft. If you'd like to help us out with that, jump into the [~languages channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/languages) and let us know. Deutscher Support [~language-de channel on Mycroft Chat](https://chat.mycroft.ai/community/channels/language-de)._

* Verschieben und Kopieren von Dateien in einer Linux-Shell
* Herunterladen und Entpacken großer Dateien
* Bearbeiten von Python-Quellcode-Dateien

## Erster Einstig

!!!Aktuell ist das paaren von Mycroft noch nicht vollständig in deutsch möglich daher sollten sie Mycroft bereits unter 
"lang": "en-us" verbunden und eingerichtet haben.

Erstellen Sie danach eine eigene `mycroft.conf` Konfigurationsdatei. Bei Mycroft für Linux ist dies hier gespeichert:

`~/.mycroft/mycroft.conf`

Bearbeiten Sie die Konfigurationsdatei mit folgenden Änderungen:
 
 ```json
 {
 "lang": "de-de",
 "tts": {
     "module": "google",
      "google": {
        "lang": "de" 
      }
  }
```
##Alternativ mit espeak mbrola

Installieren Sie espeak mbrola über `sudo apt install espeak espeak-data mbrola mbrola-de7`.
```json
{
   "lang": "de-de",
   "tts": {
     "module": "espeak",
     "espeak": {
        "lang": "german-mbrola-7",
        "voice": "german-mbrola-7"
     }
   }
}
```
Mycroft sollte nach einem neustart auf deutsch hören und sprechen.
Das **Wake Word** (z.b. hey mycroft) wird hierbei unter [Mycroft Home](https://home.mycroft.ai) eingerichtet.

### Ändern Sie das **Wake Word** nach Deutsch

Mycroft verwendet PocketSphinx als **Wake Word**-Mechanismus. Das Standart **Wake Word** auf Englisch ist `Hey Mycroft`.

Um das **Wake Word** nach Deutsch zu ändern müssen Sie das deutsche Wörterbuch und das deutsche akustische Modell herunterladen, danach trainieren Sie mit dem neusten `sphinxtrain`.

Zuerst erstellen Sie ein Verzeichnis für die `pocketsphinx`-Dateien:

`sudo mkdir -p /usr/local/share/pocketsphinx/model/de/de`

### Laden Sie das deutsche Wörterbuch herunter und installieren Sie es

Als nächstes laden Sie das deutsche Wörterbuch aus dem CMUSphinx-Projekt auf SourceForge herunter_ [cmusphinx-voxforge-de.dic](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.dic/download).

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.dic/download -O cmusphinx-voxforge-de.dic`

Dann installieren Sie das Wörterbuch in das von uns erstellte Verzeichnis.

`sudo mv cmusphinx-voxforge-de.dic /usr/local/share/pocketsphinx/model/de/de.dict`

### Laden des akustischen Modells und Installation

Als Nächstes laden Sie das _acoustic model_ [cmusphinx-de-ptm-voxforge-5.2.tar.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-de-ptm-voxforge-5.2.tar.gz/download) aus dem CMUSphinx-Projekt auf SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-de-ptm-voxforge-5.2.tar.gz/download -O cmusphinx-de-ptm-voxforge-5.2.tar.gz`

Entpacken Sie dann die gezippte Datei in ein temporäres Verzeichnis.

`tar -xf cmusphinx-de-ptm-voxforge-5.2.tar.gz`

Dann kopieren Sie die entpackte Datei in das PocketSphinx-Verzeichnis

```bash
cd cmusphinx-ptm-voxforge-de-r20171217/model_parameters/voxforge.cd_ptm_5000
sudo mv * /usr/local/share/pocketsphinx/model/de/de
cd ..
```

### Laden Sie das deutsche Sprachmodell herunter und installieren Sie es

Als nächstes laden Sie das _German language model_ [cmusphinx-voxforge-de.lm.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.lm.gz/download) aus dem CMUSphinx-Projekt auf SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.lm.gz/download -O cmusphinx-voxforge-de.lm.gz`

Entpacken Sie dann die gezippte Datei in ein temporäres Verzeichnis.

`gzip -d cmusphinx-voxforge-de.lm.gz`

Dann verschieben Sie sie in das PocketSphinx-Verzeichnis

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

### Installieren Sie die Sprache in den Mycroft-Verzeichnissen

Nachdem Sie die PocketSphinx-Dateien für Deutsch installiert haben, müssen Sie Deutsch in den Mycroft-Verzeichnissen installieren.

Zuerst, [SSH into your device](https://mycroft.ai/documentation/mark-1/#connecting-to-the-mark-1-via-ssh).


Navigieren Sie zum Mycroft-Sprachenmodellverzeichnis.

Zum Beispiel, auf `mycroft-core` für Linux, navigieren Sie zu

`~/mycroft-core/mycroft/client/speech/recognizer/model`

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
_Hinweis: Der `cp`-Befehl könnte durch `ln`-Befehl ersetzt werden um Speicherplatz zu sparen. Es ist jedoch möglich, Wörter zu `de.dict` hinzuzufügen; `cp` bedeutet, dass die Originaldatei unverändert bleibt und Sie mit einer Kopie arbeiten._

Falls Sie mit mit `ln` arbeiten, müssen Sie für die folgenden Verzeichnisse, Dateien und symbolische Verknüpfungen haben:

* `~/mycroft/client/speech/recognizer/model/de`
* `~/mycroft-core/client/speech/recognizer/model/de/hmm`
* `~/mycroft-core/client/speech/recognizer/model/de/de.dict`
* `~/mycroft-core/client/speech/recognizer/model/de/de.lm`

### Ein deutsches **Wake Word** wählen

Wählen Sie ein deutsches **Wake Word** oder Wake Phrase auf Deutsch und vergewisseren Sie sich dann, dass es in der `cmusphinx-voxforge-de.dic`-Datei des Sprachmodells enthalten ist. Die Erfahrung zeigt, dass die beste Wahl ein einzelnes Wort mit drei oder mehr Phonemen ist.

Überprüfen Sie zum Beispiel, ob das Wort 'hallo' existiert:

`egrep '^hallo ' de.dict`

`hallo HH AE L AX UU`

Wenn das gewählte **Wake Word** oder Phrase nicht in der `de.dict` Datei ist, dann wählen Sie entweder ein anderes **Wake Word** oder ändern Sie die `de.dict`-Datei, um es hinzuzufügen.

### Konfigurieren Sie Mycroft für die Verwendung der deutschen Sprache und des deutschen **Wake Words** 

`~/.mycroft/mycroft.conf`

Bearbeiten Sie die Konfigurationsdatei mit folgenden Änderungen:

```json

    {
      "lang": "de-de",

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

Wenn die Sprache-zu-Text-Engine, die Sie verwenden, bereits Deutsch unterstützt, müssen Sie nichts tun - dies ist beispielsweise bei der standardmäßigen Mycroft-Engine der Fall.

Alternativ können Sie PocketSphinx verwenden, das auf Ihrem lokalen Computer ausgeführt wird. Um PocketSphinx als STT-Engine zu verwenden, fügen Sie folgendes zu Ihrer `~/.mycroft/mycroft.conf` Datei hinzu:

```json
    "listener": {
       "producer": "pocketsphinx",
       "grammar": "lm"
       }
```

## Wählen und konfigurieren Sie eine TTS-Engine (Text to Speech) mit deutscher Unterstützung

Wählen Sie als nächstes ein Text-to-Speech-Modul aus und konfigurieren Sie es, sodass es Deutsch unterstützt. Beispielsweise hat `espeak` unterschiedliche deutsche Stimmen.

```json
    "tts": {
      "module": "espeak",
      "espeak": {
        "lang": "german-mbrola-7",
        "voice": "german-mbrola-7"
      }
    }
```

Es gibt noch einige Quellcodeänderungen, die erforderlich sind, um eine Sprachänderung zu handhaben, und sie erfordern eine manuelle Änderung des Quellcodes, da sie noch nicht in `mycroft-core` einbezogen wurden.

* [Changes to `listener.py` and `pocketsphinx_audio_consumer.py`](https://github.com/MycroftAI/mycroft-core/pull/656)

Wenn Sie sich für fremdsprachige Übersetzungen von Mycroft interessieren, würden wir uns freuen, von Ihnen zu hören. Bitte besuchen Sie uns im [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)
