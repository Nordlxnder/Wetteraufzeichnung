#!/bin/bash

# Sicherung der Logdatei beim Herunterfahren
cd /mnt/ram/
cp /mnt/ram/wetter.log /mnt/skripte/wetter.log
echo "Stopp der Wetterdatenspeicherung: $(date)" >> /var/log/wetterdatenspeicherung.log


