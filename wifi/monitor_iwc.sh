#!/bin/bash

    ifconfig wlan0 down;
    iwconfig wlan0 mode moniror;
    ifconfig wlan0 up;
