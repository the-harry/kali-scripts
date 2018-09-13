#!/bin/bash
#ver redes wpa
#airodump-ng --encrypt wpa wlan1mon;
#travar na rede e gerar logs para captura de handshake
airodump-ng --bssid A8:9D:D2:D5:03:02 -w logWPA.cap wlan1mon;
#caso precise travar canal
#iwconfig wlan1mon channel 6;
#airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w logWPA.cap wlan1mon;
##desautenticar ate aparecer handshake
