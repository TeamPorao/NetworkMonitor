#!/bin/bash

# Inicia o servidor web "webserver.py"
python3 ./webserver.py &
# Inicia a captura de pacotes "main.py"
python3 ./main.py &

# Programa o script para executar de 2 em 2 minutos.
(crontab -l ; echo "*/2 * * * * sudo /usr/bin/python3 /diretorio/onde/instalou/NetworkMonitor/preprocess.py") | crontab -
(crontab -l ; echo "*/2 * * * * sudo /usr/bin/python3 /diretorio/onde/instalou/NetworkMonitor/yara_analyzer.py") | crontab -

# Continua o script executando e mantém o servidor web e a captura de pacotes.
while true; do
    sleep 1
done