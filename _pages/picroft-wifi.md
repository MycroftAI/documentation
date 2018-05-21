---
ID: 33608
post_title: 'Picroft &#8211; manually configure WiFi'
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/picroft/picroft-wifi/
published: true
post_date: 2017-12-06 10:21:28
---
# Picroft - manually configure WiFi

There may be cases where the more automated method of connecting your Picroft **Device** to WiFi doesn't work, and you need to manually configure  your Picroft's WiFi settings. This documentation walks you through that process. 

## Make sure you can edit files on the filesystem of the Picroft. 

There are two ways to do this. 

1. Plug the Picroft into a keyboard and HDMI monitor then type `Ctrl + C` to get to the command line _or_
2. [SSH in to the Picroft device ](https://mycroft.ai/documentation/picroft/#connecting-to-picroft-via-ssh)

## Manually configuring WiFi

Next, we edit the `wpa_supplicant.conf` file. 

1. Type `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
2. Using the down arrow key, navigate to the bottom of the file, and add credentials for your SSID

```
    network={
            ssid="MyNetworkSSID"
            psk="mypassword"
    }
```

3. Type `Ctrl + X` to exit and `Y` then `Enter` to save your changes. 
4. Type `sudo reboot now`

## Manually configuring WPA2 Enterprise WiFi with MSCHAPV2 authentication

If you are on an enterprise network, your network security might use WPA2 with MSCHAPV2 authentication. Configuring Picroft to use MSCHAPV2 is similar to the above, but requires some additional steps. 

First, we need to generate a hash of your SSID's password. 

```
echo -n your_password| iconv -t utf16le | openssl md4
```

This will use the [NTLM hash](https://en.wikipedia.org/wiki/NT_LAN_Manager) which is a 16 bit MD4 hash.  Make sure to copy this as we will need it for later steps. 

Next, run the following commands: 

```
cd /etc/wpa_supplicant
sudo nano wpa_supplicant.conf
```

Add the following to the bottom of the `wpa_supplicant.conf` file, replacing `ssid` with your SSID name, `identity` with your username and `password` with the hash generated earlier. Type `Ctrl + O` to save, then `Ctrl + x` to exit. 

Next, reboot the Picroft using `sudo reboot now`. If these steps have worked, you will be connected to your enterprise WiFi shortly after rebooting. 

```
network={
    ssid="ssid network name"
	priority=1
	proto=RSN
	key_mgmt=WPA-EAP
	pairwise=CCMP
	auth_alg=OPEN
	eap=PEAP
	identity="user_name"
	password=hash:hash_key_here
	phase1="peaplabel=0"
	phase2="auth=MSCHAPV2"
}
```
## Wifi-Setup by using WPS
Informations from: https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

1. Connect network cable.  
(Netzwerkkabel anschließen.)
  

2. Activ SSH on MyCroft with Button.  
(SSH auf dem MyCroft mittels Drehrad (Typ1) aktivieren.)


3. Connect MyCroft with SSH (PUTTY).  
(Eine Verbindung mit MyCroft mittels Putty aufbauen.)


4. Change activ interface to wlan0.  
(Das aktive Netzwerk-Interface auf wlan0 ändern.)

```
sudo wpa_cli interface wlan0
```

5. Start WPS on own network router.  
(WPS auf dem eigenen Router starten.)


6. Start WPS on MyCroft.  
(WPS auf dem MyCroft starten)

```
sudo wpa_cli wps_pbc
```

It's success with "WPS-SUCCESS".  
(Erfolgsmeldung ist "WPS-SUCCESS".)


7. Apply change.  
(Änderung anwenden.)

```
sudo wpa_cli -i wlan0 reconfigure
```
  
  
## Increase security by encrypting the local wifi key
(Erhöhung der Sicherheit durch Verschlüsselung des lokalen WLAN-Kennwortes.)


1. Show wifi-configuration.  
(Anzeigen des WLAN-Authentifizierung.)

```
sudo cat /etc/wpa_supplicant/wpa_supplicant.conf

Example output: 
(Bespielausgabe)
network={
        ssid="AAAAAAAAAAAAAAAAAAA"
        psk="BBBBBBBBBBBBBBBBBBBBB"
}
```


2. Encrypting  
(Verschlüsseln)

```
wpa_passphrase "AAAAAAAAAAAAAAAAAAA" "BBBBBBBBBBBBBBBBBBBBB"


Example output: 
(Bespielausgabe)
network={
        ssid="AAAAAAAAAAAAAAAAAAA"
        #psk="BBBBBBBBBBBBBBBBBBBBB"
        psk=ffae5a4df1fb6095257093db22e43fe57f548f3e5a747d7b3f8248dd9d370cdc
}
```


3. Open wifi authentication.  
(Gespeichterten WLAN-Authentifizierung öffnen.)

```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```


4. Write new psk in file.  
(Neuen psk in die Datei schreiben)

```
Change Text "BBBBBBBBBBBBBBBBBBBBB" to ffae5a4df1fb6095257093db22e43fe57f548f3e5a747d7b3f8248dd9d370cdc (Last without quotes!)
Ändere Test "BBBBBBBBBBBBBBBBBBBBB" zu ffae5a4df1fb6095257093db22e43fe57f548f3e5a747d7b3f8248dd9d370cdc (Letztes ohne Anführungsstriche!)
```
Saving STRG+o and enter / exit STRG+x  
(Speichern STRG+o und Enter / Beenden STRG+x)


5. Apply change.  
(Änderung anwenden)

```
sudo wpa_cli -i wlan0 reconfigure
```
