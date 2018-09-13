#!/bin/bash
service tor start;
proxychains nmap -sU 192.168.0.1-255 -v > log;
