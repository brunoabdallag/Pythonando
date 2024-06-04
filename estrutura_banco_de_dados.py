# SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

# Criar um API Flask
app = Flask(__name__) # Receberá o nome do arquivo que está sendo utilizado naquele momento "estrutura_banco_de_dados"

# Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'BAG123!@#' # Chave para autenticação
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.npzzkjqczssuxziazjde:' + quote("nVPMt1zMdEml^mY#@Z*c") + '@aws-0-us-west-1.pooler.supabase.com:6543/postgres' # /// para indicar que é local
# Pesquisar banco de dados online, utilize: connection string oracle / ou sql server / etc...

# Criar instância
db = SQLAlchemy(app)
db: SQLAlchemy # Tipada, é importante para não ter erros na hora de criar o código, define basicamente o tipo da váriavel que é SQLAlchemy

# Definir estruturda da tabela Postagem
class Postagem(db.Model): # Instanciar o db.Model e criando toda a estrutura da tabela.
    __tablename__ = 'postagem'
    # Definir colunas na tabela
    id_postagem = db.Column(db.Integer, primary_key=True) # Primary_key = Definir um valor único que não deve se repetir e será incrementado automaticamente
    titulo = db.Column(db.String)
    # Relacionamento de tabelas
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor')) # ForeingKey é utilizado para relacionar as tabelas, deve se colocar o nome e propriedade da tabela que deseja relacionar

# Definir estruturda da tabela Autor
class Autor(db.Model):
    # tablename é o nome da coluna
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem') # Representar várias postagem com o mesmo autor, criando uma relação. Passar nome da classe.

def inicializar_banco():
    with app.app_context():
        # Executar o comando para criar o banco de dados.
        db.drop_all() # Vai apagar qualquer estrutura prévia que irá existir, apenas rodar na primeira vez, porque irá apagar tudo e recomeçar a tabela.
        db.create_all() # Irá criar toda a estrutura

        # Criar usuário admin
        autor = Autor(nome='bag', email='bruno.abdallag@outlook.com', senha='123456', admin=True)
        db.session.add(autor) # Criar o autor no banco
        db.session.commit() # Salvar o autor no banco

if __name__ == '__main__': # Isso determina que essa função só irá rodar se for dado a execução diretamente no arquivo.
    inicializar_banco()