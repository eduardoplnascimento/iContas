from flask import Flask
from database import db
from controllers.HomeController import HomeController

###### CONFIGURACOES ######
app = Flask('app')
app.config['SECRET_KEY'] = 'qEChL7R3SpF72cEA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

###### ROTAS ######
@app.route('/')
def index():
  return HomeController.index()

@app.route('/login')
def login():
  return HomeController.login()

###### INICIALIZACAO ######
with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run(host='0.0.0.0')