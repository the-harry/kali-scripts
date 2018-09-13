#!/bin/bash

#Install
#apt-get install bridge-utils

ifconfig wlan0 0.0.0.0 up
ifconfig at0 0.0.0.0 up
brctl addbr ponte
brctl addif at0
brctl addif wlan0
ifconfig ponte up
ifconfig ponte 192.168.0.200 netmask 255.255.255.0

