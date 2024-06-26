# pyWebMultimeter
Realizzare un multimetro digitale utilizzando un ESP8266 e Python è un progetto interessante che combina hardware e software per fornire una soluzione di monitoraggio accessibile via web. Qui di seguito troverai una guida dettagliata su come procedere, con il codice necessario per ogni parte del progetto.
Componenti Necessari

    ESP8266 (ad esempio, NodeMCU)
    Sensore di corrente (ad esempio, ACS712)
    Partitore di tensione per misurare la tensione
    Cavi e breadboard
    Computer con Python e i seguenti moduli: Flask, requests, matplotlib, pandas

Passaggi del Progetto
1. Configurazione Hardware

Collega il sensore di corrente ACS712 e il partitore di tensione all'ESP8266 secondo il seguente schema:

    ACS712:
        Vcc a 3.3V dell'ESP8266
        GND a GND dell'ESP8266
        OUT a un pin analogico (A0) dell'ESP8266
    Partitore di Tensione:
        Ingresso tensione alla resistenza R1
        Punto centrale del partitore (tra R1 e R2) al pin A0 dell'ESP8266
        R2 a GND