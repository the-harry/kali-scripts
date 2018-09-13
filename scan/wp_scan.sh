#!/bin/bash
service tor start;
proxychains wpscan --random-agent --url google.com.br --enumerate u;
