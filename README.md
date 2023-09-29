<h1>Projeto de Defesa Cibernética - SBT & FIAP Challenge 2023</h1>

<h2>Sobre o Projeto</h2>

<p>Este projeto foi desenvolvido como parte do desafio proposto pelo Sistema Brasileiro de Televisão (SBT) em colaboração com a FIAP, durante o ano de 2023. A ferramenta consiste em um script que executa um servidor web e exibe um dashboard que identifica malwares e ransomwares em uma captura de rede.</p>

<h2>Como Usar</h2>

<h3>Instalação das Dependências</h3>

<p>Para utilizar a ferramenta, siga os passos abaixo para instalar as dependências:</p>

<code>sudo pip install -r requirements.txt</code>

<h3>Uso Manual</h3>

<p>Você pode executar a ferramenta manualmente com os seguintes comandos:</p>

<code>sudo python3 main.py</code>

<p>Este script monitora a interface de rede em modo promíscuo.</p>

<code>sudo python3 preprocess.py</code>

<p>Este script realiza o pré-processamento dos pacotes de tráfego de dados.</p>

<code>sudo python3 yara_analyzer.py</code>

<p>Este script inspeciona os pacotes filtrados e utiliza uma regra da Yara para detectar a presença de Malwares e Ransomwares, salvando os resultados em um arquivo JSON.</p>

<h3>Uso Automático</h3>

<p>Para executar a ferramenta automaticamente (isso também inicia o webserver.py com o dashboard), siga estes passos:</p>

<code>cd NetworkMonitor</code><br>
<code>sudo chmod +x startup.sh</code><br>
<code>sudo bash ./startup.sh</code><br>

<h2>Aviso!</h2>

<p>Este projeto é apenas um protótipo e está em desenvolvimento. Iremos aprimorar a regra da Yara, para assim melhorar a acurácia dos resultados.</p>

<h2>Licença</h2>

<p>Este projeto é protegido por direitos autorais e está disponível apenas para uso não-comercial. Consulte o arquivo <a href="LICENSE">LICENSE</a> para obter detalhes sobre os termos da licença. Lembre-se de que é obrigatório fornecer a devida atribuição se você desejar utilizar este software para fins não-comerciais.</p>

<h2>Contribuição</h2>

<p>Se desejar contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Estamos abertos a colaborações!</p>
