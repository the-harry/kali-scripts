#!/bin/bash
airmon-ng stop wlan1mon;
ifconfig wlan0 up;
ifconfig wlan1 up;
