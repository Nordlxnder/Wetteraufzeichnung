#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess
import socket
import os.path

# setzt das Arbeitsverzeichnis
os.chdir("/mnt/ram")

class messdaten_abfragen():

    def __init__(self):
        HOST = '192.168.2.135'  # Zielrechner
        PORT = 55252  # Port des Servers für
        #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.netzwerkschnittstelle:
        self.netzwerkschnittstelle=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.netzwerkschnittstelle.connect((HOST, PORT))

    def messdaten(self):
        # Begrüßung empfangen
        daten_empfangen = self.netzwerkschnittstelle.recv(1024)
        print(daten_empfangen.decode('utf-8'))

        # Messdaten anfordern
        daten_anfordern="MESSDATEN"
        self.netzwerkschnittstelle.sendall(str.encode(daten_anfordern))
        self.messdaten_empfangen = self.netzwerkschnittstelle.recv(1024)
        print("Empfangene Daten:\t", self.messdaten_empfangen.decode('utf-8'))

        # Verbindung beenden bzw abbrechen
        daten_senden = "AB"
        self.netzwerkschnittstelle.sendall(str.encode(daten_senden))
        daten_empfangen = self.netzwerkschnittstelle.recv(1024)
        print("Abschlußmeldung:\t", daten_empfangen.decode('utf-8'))

        return self.messdaten_empfangen.decode('utf-8')

def daten_speichern():

    # Prüft ob die Logdatei schon vorhanden ist und falls nicht wird sie angelegt
    wetterlog=ob_datei_vorhanden_ist()
    if wetterlog==False:
        ueberschrift="Zeit"+" "\
                     +"Aussentempratur1" + " "\
                     +"Luftdruck" + " " \
                     +"Luftfeucht" + " " \
                     +"Höhe" + " "\
                     +"CPU-Temperatur" +"\n"
        einheiten="s" + " " \
                 + "°C" + " " \
                 + "hPa"+ " " \
                 + "%" + " " \
                 + "m" + " " \
                 + "°C" "\n"
        with open("wetter.log","w") as datei:
            datei.write(ueberschrift)
            datei.write(einheiten)
        print("Die Datei wetter.log wurde angelegt")

    # Messdaten abfragen und formatieren
    messdaten = messdaten_abfragen().messdaten()
    luftfeuchte, aussentemp1, aussentemp2, luftdruck, hoehe, cputemp = messdaten.split("|")

    # formatiren
    aussentemp=("{0:.1f}".format(float(aussentemp1))).replace(".",",") # . wird ersetzt duch , für die Auswertung
    luftdruck="{0:.0f}".format(float(luftdruck)/100) # Umrechnung auf hPa ohne Nachkommastelle
    luftfeuchte="{0:.0f}".format(float(luftfeuchte))
    hoehe=("{0:.1f}".format(float(hoehe))).replace(".",",")
    cputemp=("{0:.1f}".format(float(cputemp))).replace(".",",")

    # Zeitstempel ermitteln Zeit in Sekunden seit 1.1.1970
    zeit = subprocess.run('date +%s', stdout=subprocess.PIPE, shell=True, encoding="utf-8").stdout
    # Zeilenumbruch wird entfernt mit -1
    zeit = zeit[0:(len(zeit) - 1)]


    datenstring = str(zeit)     + " "\
                  + aussentemp  + " "\
                  + luftdruck   + " "\
                  + luftfeuchte + " "\
                  + hoehe       + " "\
                  + cputemp     + "\n"
    #print(os.getcwd())
    with open('wetter.log', 'a') as datei:
        datei.write(datenstring)

def ob_datei_vorhanden_ist():
    os.path.isfile("/mnt/ram/")
    if  os.path.exists("wetter.log")==True:
        return True
    else:
        return False

if __name__ == "__main__":
    daten_speichern()
