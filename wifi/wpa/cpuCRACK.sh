#!/bin/bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt logWPA-01.cap;

#gerar lista personalizada e testar
crunch 8 8 -t nomewifi%%% 0123456789 | aircrack-ng -w - aircrack-ng -w - logWPA-01.cap -e nomewifi;
