#!/bin/bash
echo 1 > /proc/sys/net/ipv4/ip_forward
#11 = session id | rede 10 = externa
msfconsole -x "route add 192.168.10.0 255.255.255.0 11;
use auxyliary/scanner/portscan/tcp;
set LHOST 192.168.10.0/24;
run"
