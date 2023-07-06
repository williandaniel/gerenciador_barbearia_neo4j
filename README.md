# Gerenciador de Barbearia

O Gerenciador de Barbearia é uma aplicação desenvolvida como projeto da disciplina de Banco de Dados II. O objetivo principal do projeto é fornecer uma solução para gerenciar o agendamento de serviços entre clientes e funcionários em uma barbearia. A aplicação utiliza o banco de dados não relacional Neo4j para armazenar e manipular os dados relacionados ao agendamento e aos serviços prestados.

## Instruções para a compilação e execução da aplicação
### Tecnologias Utilizadas

 - Neo4j Desktop
 - Python
 - Visual Studio Code ou qualquer outro editor de texto

### Faça uma Copia do Repositório para sua máquina

 - Clique em Code
 - Copie o link HTTPS para fazer o git clone
 - Ou Clique em Download ZIP
 - Clique com o direito no arquivo ZIP na pasta que o arquivo se encontra e em extrair o conteúdo do arquivo

<img width="638" alt="10" src="https://github.com/williandaniel/gerenciador_barbearia_neo4j/assets/40742096/2d262ac5-4f73-465a-a1a1-22cb285ed9c0">

### Criando o Banco de Dados
 - Abrir o Neo4j Desktop
   
<img width="244" alt="2" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/209f4c02-f443-40a8-89e6-1922d2df5b3a">

 - Clique em New para criar um projeto
   
<img width="262" alt="1" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/eb7a6eb7-3275-4f70-991a-038b986e7a1e">

 - Clique em Create project

<img width="269" alt="3" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/39182d12-5a41-46ad-aa31-3ef7bdb4f2e5">

 - Clique em Add e clique na opção Local DBMS

<img width="894" alt="4" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/dab25d0c-80c4-4210-9dd1-24440df606dd">

 - Crie uma senha no campo Password e clique em Create
   
<img width="653" alt="5" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/0dde96ad-bf2a-4043-adca-8eb96fbc8307">

 - Passe o mouse por cima Graph DBMS e clique em Start

<img width="667" alt="6" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/44c62c70-ee75-42f2-b468-6f1196e9c46f">

 - Clique em Open para abrir o Neo4j Browser

<img width="612" alt="7" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/694fb3c2-98b3-4a36-b1cf-a557db4f1847">

 - Copie o Contéudo do arquivo data.cypher ou araste o arquivo dentro do editor do Neo4j Browser

 <img width="878" alt="8" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/9cc7c7c5-9d8b-4944-ad4e-2f223dcab028">

 - Clique em executar

<img width="67" alt="9" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/f40e3004-676c-4c8a-b77e-65604f6f6666">

### Executando e Compilando
 - Abrir o editor Visual Studio Code
 - Clique em File > Open Folder
 - Selecione a pasta que o repositório foi baixado

![234871150-09680baa-2230-43e6-a564-9051bbf617e1](https://github.com/williandaniel/barbearia_neo4j/assets/40742096/dc4e449e-fb39-406c-abd0-ab013a6a5915)

 - Abrir o arquivo main.py
 - Altere os campos uri, user e password para o acesso ao banco

  <img width="175" alt="image" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/080c8789-b62f-4bd7-9bae-f890e9b64d3f">

 - Abrir o terminal do VS Code
 - Digite o comando `pip install -r requirements.txt` no terminal para instalar as dependências do Python necessarias para a execução da aplicação
   
 <img width="224" alt="image" src="https://github.com/williandaniel/barbearia_neo4j/assets/40742096/674ff0ac-2061-41b7-95d1-66df2baa8093">

 - Digite o comando `python main.py` no terminal para executar a aplicação
