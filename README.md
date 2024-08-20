# send_smart
Sistema de envio de mensagens via whatsapp com importação de dados de pessoa e contato

# Como instalar
## Configurando o ambiente local:
### Instalar o venv (Virtual Enviroment)
- Entrar na pasta do projeto git
- python -m venv .venv
### Instalar Django
- source .venv/bin/activate
- pip install Django
- python -m django --version
## Como rodar o código?
- Entrar na pasta do projeto projeto git
- source .venv/bin/activate
- Entrar na pasta do projeto projeto django
- python manage.py runserver

# Pré-requisitos
Requisitos a ser instalados:
asgiref==3.8.1
attrs==23.2.0
certifi==2024.7.4
Django==5.0.6
h11==0.14.0
idna==3.7
outcome==1.3.0.post0
pillow==10.4.0
pymemcache==4.0.0
PySocks==1.7.1
selenium==4.23.0
sniffio==1.3.1
sortedcontainers==2.4.0
sqlparse==0.5.0
trio==0.26.0
trio-websocket==0.11.1
typing_extensions==4.9.0
urllib3==2.2.2
websocket-client==1.8.0
wsproto==1.2.0

# Limitações
Acima de ciquenta mil registro não é possível fazer o upload
