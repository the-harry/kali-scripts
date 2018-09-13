#!/bin/bash
echo socks4 127.0.0.1:1080 >> /etc/proxychains.conf;
#11 = session id | 10.0 = external netw
##comentar outras proxys
msfconsole -x "route add 192.168.10.0 255.255.255.0 11;
use auxyliary/server/socks4a;
run;"

proxychains nmap -A 192.168.10.0-255;
