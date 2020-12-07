from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Rafael',
        'habilidades':['Python','Flask']
    },
    {
        'id':1,
        'nome':'Lukas',
        'habilidades':['Python','R','SQL']
    }
]

#Mostra um específico dev, muda ou deleta ele
class Desenvolvedor(Resource):

    def get(self, id):
        try:
            desenvolvedor = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe.'.format(id)
            desenvolvedor = {
                 'Status':'IndexError',
                 'Mensagem':mensagem
             }
        except Exception:
            mensagem = 'Erro desconhecido, procure o admin da API'
            desenvolvedor = {
                 'Status':'Erro',
                 'Mensagem':mensagem
             }
        return desenvolvedor

    def put(self, id):
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return dados 

    def delete(self, id):
        desenvolvedores.pop(id)
        return desenvolvedores

#Lista todos ou inclui um novo dev
class ListaDesenvolvedores(Resource):

    def get(self):
        return desenvolvedores

    def put(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades,'/dev/habilidades')

if __name__ == "__main__":
    app.run(debug=True)
