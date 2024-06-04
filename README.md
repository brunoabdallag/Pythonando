## Pythonando
Esse repositório está sendo publicado para mostrar o conteúdo aprendido no curso Pythonando-devaprender!

Nesse projeto, aprendemos a realizar a criação de APIs através do Python, utilizando o framework Flask. Também criamos e configuramos um banco de dados através do SQLAlchemy usando SQLite3.


#### SQLAlchemy

* Criação das tabelas "Postagem" e "Autor" com relacionamento entre elas e um valor único IDs para ambas.
* Criação da chave local para futura autenticação nas APIs.
* Inicialização do banco de dados na forma local.

#### APIs

* Objetivo da API: Iremos montar uma API de blog, onde eu poderei consultar, editar, criar e excluir postagens em um blog utilizando a API.
* URL BASE: Uso local, sendo - http://localhost:5000
* ENDPOINTS: > /postagens | > /autores
* VERBOS HTTP: 
    * GET - Pegando recursos
    * POST - Criando um novo recurso
    * PUT - Alterando novo recurso
    * DELETE - Deletando recurso especifico
* Autenticação para interagir com as APIs.