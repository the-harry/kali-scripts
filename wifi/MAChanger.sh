#!/bin/bash
ifconfig wlan1 down;
#randomico
#macchanger --random wlan1;
#especifico
macchanger --mac=AA:BB:CC:DD:EE:FF wlan1;
ifconfig wlan1 up;

