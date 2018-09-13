#!/bin/bash
service apache2 start
dnschef --fakeip 192.168.0.10 --fakedomains *.site.com --interface 192.168.0.10
