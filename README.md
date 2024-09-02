# send_smart
Sistema de envio de mensagens via whatsapp com importação de dados de pessoa e contato

# Como instalar
## Configurando o ambiente local:
### Instalar o venv (Virtual Enviroment)
- Entrar na pasta do projeto git
- python -m venv .venv
# Pré-requisitos
[acessar o requeriments](requeriments.txt)
### Instalação do requeriments
pip install -r requirements.txt
### Alteração e criação de modelos
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database
## Como rodar o código?
- Entrar na pasta do projeto projeto git
- source .venv/bin/activate
- Entrar na pasta do projeto projeto django
- python manage.py runserver

# Limitações
Acima de ciquenta mil registro não é possível fazer o upload
