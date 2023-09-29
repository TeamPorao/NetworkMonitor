Projeto do curso de Defesa Cibernética feito durante o ano de 2023 para o Challenge proposto pelo Sistema Brasileiro de Televisão (SBT) em parceria com a FIAP.

## Sobre a ferramenta
A ferramenta consiste em um script que executa um servidor web, com um dashboard exibindo arquivos indicando malwares e ransomwares de uma captura da rede. 

## Como utilizar a ferramenta

sudo pip install -r requirements.txt

Para utilizar a ferramenta na mão:
    sudo python3 main.py
        Esse script irá fazer o monitoramento da interface de rede em modo promíscuo.
    sudo python3 preprocess.py
        Esse script irá realizar o preprocessamento dos pacotes que contém tráfego de dados.
    sudo python3 yara_analyzer.py
        Esse script realizará a inspeção dos pacotes filtrados e utilizará uma regra da Yara para detectar a presença de Malwares e Ransomwares, salvando-o em um arquivo json.

Para utilizar a ferramenta automaticamente (Essa opção também executará o webserver.py, o dashboard do Porão com os dados gerados no json):
    cd NetworkMonitor
    sudo chmod +x startup.sh
    sudo bash ./startup.sh


## Licença

Este projeto é protegido por direitos autorais e está disponível apenas para uso não-comercial. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes sobre os termos da licença. Lembre-se de que é obrigatório fornecer a devida atribuição se você desejar utilizar este software para fins não-comerciais.

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Estamos abertos a colaborações!

