#!/bin/bash

##define canal caso fixo
#iwconfig wlan1 channel 6;

#confere e mata processos interferindo
#airmon-ng check kill;

airmon-ng start wlan1;

#travar em canal
#airodump-ng -c 6 wlan1mon;

#todos canais
airodump-ng wlan1mon;
