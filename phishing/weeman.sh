#!/bin/bash
#git clone https://github.com/evait-security/weeman.git
#./weeman.sh site.com
cd weeman/;
python weeman.py;
set url $1;
set action_url $1;
run;
