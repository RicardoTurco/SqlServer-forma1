# SqlServer-forma1
Conectando ao  SQL Server utilizando o SQLAlchemy



a)
Ativar o container do banco SQL Server:

docker-compose up -d

OBS: Estou assumindo q já esteja instalado e configurado o DOCKER e o DOCKER-COMPOSE



b)
Abrir o banco de dados utilizando algum "client"
(sugiro o DBeaver)



c)
Criar uma "conexão" informando as credenciais:
(a conexão só será criada, se o "container" criado no passo "A" estiver OK)

Host: localhost
Port: 1433
Database/Schema: master
Username: sa
Password: Secret1234



c)
Criar a tabela "account":

CREATE TABLE dbo.account (
id INT PRIMARY KEY IDENTITY (1,1),
name VARCHAR(30) NOT NULL,
niver DATETIME NOT NULL,
age INT NOT NULL
)



d)
Inserir alguns registros:

insert into dbo.account (name, niver, age)
select 'Turco', GETDATE(), 48

insert into dbo.account (name, niver, age)
select 'Joice', '1983-02-05 22:01:31.070', 39


insert into dbo.account (name, niver, age)
select 'Bianca', '2014-06-14 22:01:31.070', 8



e)
Criar e ativar uma VIRTUALENV;



f)
Os passos abaixo, não são obrigatórios ...
mas ALTAMENTE recomendados (após a ativação da VIRTUALENV):

python -m pip install --upgrade pip
pip install -U setuptools
pip install wheel



g)
Instalar as dependências:

pip install -r requirements.txt



h)
Rodar o script:
(a VIRTUALENV precisa estar "ativada")

python test_con_sqlServer.py




DETALHES TÉCNICOS:


No script (test_con_sqlServer.py), a criação da "engine" 
de conexão com o SQL Server têm a seguinte sintaxe:


engine = create_engine("mssql+pymssql://<username>:<password>@<host>:<port>/<database-schema>")


Ex:
engine = create_engine("mssql+pymssql://sa:Secret1234@localhost:1433/master")

