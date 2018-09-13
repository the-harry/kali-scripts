REM visualisar recursos (protocolos ativos)
dism /online /get-features /Format:table


REM ativar recurso, ex tftp
dism /online /Enable-feature /FeatureName:TFTP

