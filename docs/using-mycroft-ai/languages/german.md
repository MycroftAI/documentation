---
description: >-
  Dies ist eine Anleitung wie Sie Mycroft in deutsch nutzen können. Diese Seite beinhaltet auch eine Kurzanleitung.
---

# Mycroft in deutsch

## Erster Einstig

!!!Aktuell ist das paaren von Mycroft noch nicht vollständig in deutsch möglich, daher sollten sie Mycroft bereits unter
"lang": "en-us" verbunden und eingerichtet haben.

Zuerst, [verbinden Sie sich mit ihrem Gerät (z.B. SSH)](https://mycroft.ai/documentation/mark-1/#connecting-to-the-mark-1-via-ssh).

Erstellen oder ändern Sie die eigene `~/.mycroft/mycroft.conf` Konfigurationsdatei wie folgt.

**Data:**

 ```javascript
 ...
 "lang": "de-de",
 "tts": {
     "module": "google",
      "google": {
        "lang": "de"
      }
 },
 ...
```
## Alternativ mit espeak mbrola

für Rasberry kannst du mbrola hier herunterladen `wget 'http://steinerdatenbank.de/software/mbrola3.0.1h_armhf.deb` und `dpkg -i mbrola3.0.1h_armhf.deb`.
Installieren Sie nun espeak mbrola über `sudo apt install espeak espeak-data mbrola mbrola-de7`.

**Data:**

```javascript
   ...
   "lang": "de-de",
   "tts": {
     "module": "espeak",
     "espeak": {
        "lang": "german-mbrola-7",
        "voice": "german-mbrola-7"
     }
   },
   ...
```
Mycroft sollte nach einem Neustart auf deutsch hören und sprechen. Viele Skills sind bereits übersetzt und können sofort genutut werden.
Das **Wake Word** (z.b. hey mycroft, Christopher, Hey Ezra, Hey Jarvis) wird hierbei unter [Mycroft Home](https://home.mycroft.ai) eingerichtet.

# Ändern des **Wake Words** in ein deutsches Wort

Mycroft verwendet [Precise](https://mycroft.ai/documentation/precise) und [PocketSphinx](https://github.com/cmusphinx/pocketsphinx) als **Wake Word**-Mechanismus. Das Standard **Wake Word** auf englisch ist `Hey Mycroft` und nutzt Precise und - falls Precise es nicht erkennt - Pocketsphinx.

Um das **Wake Word** (in ein deutsch klingendes) zu ändern müssen Sie das deutsche Wörterbuch und das deutsche akustische Modell herunterladen, danach trainieren Sie es mit dem neusten `sphinxtrain`.

Zuerst erstellen Sie ein Verzeichnis für die `pocketsphinx`-Dateien:

`sudo mkdir -p /usr/local/share/pocketsphinx/model/de/de`

### Laden des deutsche Wörterbuchs und Installation

Als nächstes laden Sie das deutsche Wörterbuch aus dem CMUSphinx-Projekt auf SourceForge herunter_ [cmusphinx-voxforge-de.dic](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.dic/download).

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.dic/download -O cmusphinx-voxforge-de.dic`

Dann installieren Sie das Wörterbuch in das erstellte Verzeichnis.

`sudo mv cmusphinx-voxforge-de.dic /usr/local/share/pocketsphinx/model/de/de.dict`

### Laden des akustischen Modells und Installation

Als nächstes laden Sie das _acoustic model_ [cmusphinx-de-ptm-voxforge-5.2.tar.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-de-ptm-voxforge-5.2.tar.gz/download) aus dem CMUSphinx-Projekt auf SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-de-ptm-voxforge-5.2.tar.gz/download -O cmusphinx-de-ptm-voxforge-5.2.tar.gz`

Entpacken Sie dann die gezippte Datei in ein temporäres Verzeichnis.

`tar -xf cmusphinx-de-ptm-voxforge-5.2.tar.gz`

Dann kopieren Sie die entpackte Datei in das PocketSphinx-Verzeichnis

```bash
cd cmusphinx-ptm-voxforge-de-r20171217/model_parameters/voxforge.cd_ptm_5000
sudo mv * /usr/local/share/pocketsphinx/model/de/de
cd ..
```

### Laden des deutschen Sprachmodells und Installation

Als nächstes laden Sie das _German language model_ [cmusphinx-voxforge-de.lm.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.lm.gz/download) aus dem CMUSphinx-Projekt auf SourceForge.

`wget https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/cmusphinx-voxforge-de.lm.gz/download -O cmusphinx-voxforge-de.lm.gz`

Entpacken Sie dann die gezippte Datei in ein temporäres Verzeichnis.

`gzip -d cmusphinx-voxforge-de.lm.gz`

Dann verschieben Sie es in das PocketSphinx-Verzeichnis

`sudo mv cmusphinx-voxforge-de.lm /usr/local/share/pocketsphinx/model/de/de.lm`

### Überprüfen Sie die Dateien

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

### Verlinken/Kopieren Sie Modell und Wörterbuch in die Mycroft-Verzeichnisse

Navigieren Sie dazu zum Mycroft-Sprachenmodellverzeichnis.

Zum Beispiel, auf `mycroft-core` für Linux, navigieren Sie zu

`~/mycroft-core/mycroft/client/speech/recognizer/model`

Sie sollten die folgenden Verzeichnisse sehen:

```bash
$ ls -las
total 24
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 .
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 ..
8 drwxrwxr-x 3 kathyreid kathyreid 4096 Nov 24 00:08 en-us
```

_HINWEIS: Beachten Sie, dass es nur einen Modellordner gibt - `en-us` für American English_

Erstellen Sie hier ein neues Verzeichnis für deutsch, und verlinken Sie es anschließend mit dem `pocketsphinx` Verzeichnis.

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

Wählen Sie ein deutsches **Wake Word** oder Wake Phrase auf deutsch und vergewissern Sie sich dann, dass es in der `cmusphinx-voxforge-de.dic`-Datei des Sprachmodells enthalten ist. Die Erfahrung zeigt, dass die beste Wahl ein einzelnes Wort mit drei oder mehr [Phonemen](https://de.wikipedia.org/wiki/Phonem) ist.

Überprüfen Sie zum Beispiel, ob das Wort 'hallo' existiert:

`egrep '^hallo ' de.dict`

`hallo HH AE L AX UU`

Wenn das gewählte **Wake Word** oder Phrase nicht in der `de.dict` Datei ist, dann wählen Sie entweder ein anderes **Wake Word** oder ändern Sie die `de.dict`-Datei, um es hinzuzufügen.

### Konfigurieren Sie Mycroft für die Verwendung der deutschen Sprache und des deutschen **Wake Words**

Bearbeiten Sie die Konfigurationsdatei `~/.mycroft/mycroft.conf` mit folgenden Änderungen:

**Data:**

```javascript
      ...
      "lang": "de-de",

      "listener": {
        "wake_word": "hallo",
        "phonemes": "HH AE L AX UU",
        "threshold": 1e-10,
        "standup_word": "hallo",
        "standup_phonemes": "HH AE L AX UU",
        "standup_threshold": 1e-10
      },
      ...
```

# Mozilla Deepspeech STT

Mycroft unterstützt auch Deepspeech STT. Hierfür muss ein deutsches Modell auf einem Deepspeech Server einrichten. [Aashish Agarwal](https://github.com/AASHISHAG/deepspeech-german) hat dazu ein entsprechendes [Modell](https://drive.google.com/drive/folders/1PFSIdmi4Ge8EB75cYh2nfYOXlCIgiMEL?usp=sharing) unter Deepspeech V7.4 veröffentlicht. Das Modell ist aktuell noch etwas Empfindlich was leise oder fremde Geräusche angeht.

## Installation

* Entpacke die heruntergeladenen Ordner und wechsle hinein. `cd release_v0.7.4`
* Aktiviere venv `source ~/mycroft-core/.venv/bin/activate`.
* Installiere Deepspeech mit `pip install deepspeech==0.7.4` oder `pip install deepspeech-gpu==0.7.4`.
* Installiere Deepspeech Server `pip install deepspeech-server`.

### Erstelle eine Server Konfiguration

Erstelle eine Konfiguationsdatei `config.json`.

**Data:**

```javascript
  ...
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
  },
  ...
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
...
"stt": {
  "deepspeech_server": {
     "uri": "http://localhost:8080/stt"
   },
  "module": "deepspeech_server"
},
...
```

###

Für weitergehende Fragen besuchen Sie [den deutschen channel auf Mycroft chat](https://chat.mycroft.ai/community/channels/languages-de)
