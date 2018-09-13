#!/bin/bash
#git clone https://github.com/maldevel/IPGeoLocation.git
#pip install -r requirements.txt
cd IPGeoLocation/;
#m=meuip ; g=open googleMap ; --nolog = n salvar
python3 ipgeolocation.py -mg --nolog;

#site e outros
python3 ipgeolocation.py -t google.com --nolog;
