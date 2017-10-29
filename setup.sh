#!/bin/bash

#####################################
#
#    kopieren der Skripte
#
####################################

sudo mkdir /mnt/skripte
sudo mkdir /mnt/ram

sudo cp wetterdaten_speichern.py /mnt/skripte/wetterdaten_speichern.py

sudo cp ./Beispiel_systemd/wetterdatenspeicherungs* /usr/bin/
sudo cp ./Beispiel_systemd/wetterdatenspeicherung.service /etc/systemd/system/

sudo systemctl start wetterstation.service
sudo systemctl enable wetterstation.service
