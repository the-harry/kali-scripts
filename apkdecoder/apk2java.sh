#!/bin/bash

#install
#apt-get install dex2jar -y;
#apt-get install jd-gui -y;
#apt-get install apktool -y;

#java
d2j-dex2jar *.apk;
jd-gui *.jar;
unzip *.zip;

#xml
mkdir xml && cp *.apk xml/. && cd xml/;
apktool d *.apk;
rm *.apk && cd ..;

#estrutura projeto
cp *.apk projeto.apk.zip;
mkdir zipado;
mv projeto.apk.zip zipado/. && cd zipado/;
unzip projeto.apk.zip;
cd ..;

#organiza arquivos
mkdir original_files;
mv *.apk original_files/ && mv *.jar original_files/ && mv *.zip original_files/;
