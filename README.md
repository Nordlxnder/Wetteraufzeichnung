# Wetteraufzeichnung

 Funktion

    Die von einer Wetterstation abgefragten Werte werden in eine
    Logdatei wetter.log geschrieben.
    Über einen cronjob kann die Datei alle 5 Minuten oder in einem
    anderem Zeitraster ausgeführt werden. 

    
 Voraussetzungen
    
    Raspberry oder Bananapi
    
    Betriebssystem: Arch Linux oder ähnliches ;-)
    Software: sudo , git
    
    Ramlaufwerk /mnt/ram 
    
 Installation
 
    git clone https://github.com/Nordlxnder/Wetteraufzeichnung.git

    cd Wetteraufzeichnung
    
    sudo mkdir /mnt/skripte
    sudo mkdir /mnt/ram

    sudo cp wetterdaten_speichern.py /mnt/skripte/wetterdaten_speichern.py

    sudo cp ./Beispiel_systemd/wetterdatenspeicherungs* /usr/bin/
    sudo cp ./Beispiel_systemd/wetterdatenspeicherung.service /etc/systemd/system/

    sudo systemctl start wetterdatenspeicherung.service
    sudo systemctl enable wetterdatenspeicherung.service
    
    Ramlaufwerk einrichten
    
        sudo nano /etc/fstab
        
            ramfs   /mnt/ram        ramfs   defaults,noatime,nosuid,mode=0755,size=200m     0 0

    sudo reboot
    
     
 crontab parametrieren  
 
    su
    crontab -e
        
        # jede 5te Minute Abrufen und Speicher der Wetterdaten in /mnt/ram/wetter.log
        */5 * * * * /mnt/ram/wetterdaten_speichern.py 

        # 19 Uhr sichern der Logdatei
        0 19 * * * cp /mnt/ram/wetter.log /mnt/skripte/wetter.log

