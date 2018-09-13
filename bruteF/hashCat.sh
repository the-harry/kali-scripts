#!/bin/bash

#oclhashcat

#buscar cripto
hashcat -h | grep MD5;

# m=cripto ; a=tipo_ataque
hashcat -m 666 -a 0 -o log.txt hashes.txt wordlist.txt;
