#!/bin/bash
cd usr/share/windows-binaries;

#cc = dupla compressao

#hex
exe2hex -x entrada.exe -b saida.txt --cc;
#PS
exe2hex -x entrada.exe -p saida.txt --cc;
