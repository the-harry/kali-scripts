#!/bin/bash
#ver redes wep
airodump-ng --encrypt wep wlan1mon;
#travar na rede e gerar logs de ivs
#airodump-ng -c 11 --bssid AA:BB:CC:DD:EE:FF -w logIVS.cap wlan1mon;
