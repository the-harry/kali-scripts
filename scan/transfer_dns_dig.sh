#!/bin/bash
service tor start;
proxychains dig axfr site.com @ns1.server.com > resposta;
