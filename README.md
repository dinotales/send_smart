# send_smart
<p>Sistema de envio de mensagens via whatsapp com importação de CSV do nome da pessoa e contato telefonico</p>

# Tabela de conteúdos

ts
   * [Sobre](#send_smart)
   * [Instalação](#Como_instalar)
   * [Pré-Requisitos](#Pré-requisitos)
      * [Instalação: Pré-Requisito](###Instalação_do_requeriments)
      * [Modelo](###Alteração_e_criação_de_modelos)
   * [Como usar](Como_rodar_o_código?)
   * [Limitações](#Limitações)
te

<h4 align="center"> 
	🚧  Em contrução edição de banco de contatos 🚀 Em construção...  🚧
</h4>

# Como_instalar
## Configurando o ambiente local:
### Instalar o venv (Virtual Enviroment)
- Entrar na pasta do projeto git
- python -m venv .venv
# Pré-requisitos
[acessar o requeriments](/send_smart/requirements.txt)
### Instalação_do_requeriments
pip install -r requirements.txt
### Alteração_e_criação_de_modelos
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database
## Como_rodar_o_código?
- Entrar na pasta do projeto projeto git
- source .venv/bin/activate
- Entrar na pasta do projeto projeto django
- python manage.py runserver

# Limitações
Acima de ciquenta mil registro não é possível fazer o upload
