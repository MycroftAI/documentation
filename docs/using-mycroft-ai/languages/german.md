---
description: >-
  Dies ist eine Anleitung wie Sie Mycroft in Deutsch nutzen können.
---

# Mycroft in Deutsch

## Erster Einstig

!!!Aktuell ist das paaren von Mycroft noch nicht vollständig in deutsch möglich daher sollten sie Mycroft bereits unter 
"lang": "en-us" verbunden und eingerichtet haben.

Erstellen oder ändern Sie die eigene `~/.mycroft/mycroft.conf` Konfigurationsdatei wie folgt.
 
**Data:**

 ```javascript
 {
 "lang": "de-de",
 "tts": {
     "module": "google",
      "google": {
        "lang": "de" 
      }
  }
```
## Alternativ mit espeak mbrola

für Rasberry kanst du mbrola hier herunterladen `wget 'http://steinerdatenbank.de/software/mbrola3.0.1h_armhf.deb`.
Installieren Sie nun espeak mbrola über `sudo apt install espeak espeak-data mbrola mbrola-de7`.

**Data:**

```javascript
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
Mycroft sollte nach einem neustart auf deutsch hören und sprechen. Viele Skills sind bereits Übersetzt und können sofort genutut werden.
Das **Wake Word** (z.b. hey mycroft, Christopher, Hey Ezra, Hey Jarvis) wird hierbei unter [Mycroft Home](https://home.mycroft.ai) eingerichtet.

# Ändern Sie das **Wake Word** auf ein Deutsches Word

Mycroft verwendet [PocketSphinx](https://github.com/cmusphinx/pocketsphinx) oder [Precise](https://mycroft.ai/documentation/precise) als **Wake Word**-Mechanismus. Das Standard **Wake Word** auf Englisch ist `Hey Mycroft`.

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

Bearbeiten Sie die Konfigurationsdatei `~/.mycroft/mycroft.conf` mit folgenden Änderungen:

**Data:**

```javascript
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

**Data:**

```javascript
    "listener": {
       "producer": "pocketsphinx",
       "grammar": "lm"
       }
```

## Wählen und konfigurieren Sie eine TTS-Engine (Text to Speech) mit deutscher Unterstützung

Wählen Sie als nächstes ein Text-to-Speech-Modul aus und konfigurieren Sie es, sodass es Deutsch unterstützt. Beispielsweise hat `espeak` unterschiedliche deutsche Stimmen.

**Data:**

```javascript
    "tts": {
      "module": "espeak",
      "espeak": {
        "lang": "german-mbrola-7",
        "voice": "german-mbrola-7"
      }
    }
```

# Mozilla Deepspeech STT

Mycroft unterstützt auch Deepspeech STT hierfür muss ein deutsches Modell auf einem deepspeech-server eirichten. [Aashish Agarwal](https://github.com/AASHISHAG/deepspeech-german) hat dazu ein entsprechendes [Modell](https://drive.google.com/drive/folders/1PFSIdmi4Ge8EB75cYh2nfYOXlCIgiMEL?usp=sharing) unter Deepspeech V7.4 veröffentlicht.

## Installation

* Entpacke die heruntergeladenen Ordner und wechsle hinein.
* aktiviere in venv `source ~/mycroft-core/.venv/bin/activate`.
* Installiere Deepspeech mit `pip install deepspeech==0.7.4` oder `pip install deepspeech-gpu==0.7.4`.
* Installiere Deepspeech Server `pip install deepspeech-server`.

### Erstelle eine Server Konfiguration

Erstelle eine Konfiguationsdatei `config.json`.

**Data:**

```javascript
  "deepspeech": {
    "model" :"output_graph.pb", ### unter Raspberry output_graph.tflite
    "scorer" :"kenlm.scorer",
    "beam_width": 1024,
    "lm_alpha": 0.931289039105002,
    "lm_beta": 1.1834137581510284
  },
  "server": {
    "http": {
      "host": "0.0.0.0",
      "port": 8080,
      "request_max_size": 2048576
    }
  },
  "log": {
    "level": [
      { "logger": "deepspeech_server", "level": "DEBUG"}
    ]
  }
}
```
### Start

* Starte Deepspeech Server `deepspeech-server --config config.json`
* erstelle Testdatei `arecord test.wav`.
* sende Testdatei `curl -X POST --data-binary @test.wav http://localhost:8080/stt`

Antwort sollte nun `test ist ein zwei drei test(.venv) pi@picroft:~/release_v0.7.4$` lauten.

### Start Deepspeech Server on boot

Füge folgendes in Startup Datei `/etc/rc.local`.

```
/home/pi/mycroft-core/.venv/bin/deepspeech-server --config /home/pi/release_v0.7.4/config.json
```

### Konfigurieren Sie Mycroft für die Verwendung von Deepspeech 

Bearbeiten Sie die Konfigurationsdatei `~/.mycroft/mycroft.conf` mit folgenden Änderungen:

**Data:**

```javascript
},
"stt": {
  "deepspeech_server": {
     "uri": "http://localhost:8080/stt"
   },
  "module": "deepspeech_server"
},
```

###

Es gibt noch einige Quellcodeänderungen, die erforderlich sind, um eine Sprachänderung zu handhaben, und sie erfordern eine manuelle Änderung des Quellcodes, da sie noch nicht in `mycroft-core` einbezogen wurden.

* [Changes to `listener.py` and `pocketsphinx_audio_consumer.py`](https://github.com/MycroftAI/mycroft-core/pull/656)

Wenn Sie sich für fremdsprachige Übersetzungen von Mycroft interessieren, würden wir uns freuen, von Ihnen zu hören. Bitte besuchen Sie uns im [Languages channel on Mycroft chat](https://chat.mycroft.ai/community/channels/languages)