from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'nome':'Rafael',
        'habilidades':['Python','Flask']
    },
    {
        'nome':'Lukas',
        'habilidades':['Python','R','SQL']
    }
]

#Mostra um específico dev, muda ou deleta ele
@app.route('/dev/<int:id>', methods=['GET','PUT','DELETE'])
def dev(id):
    if request.method == 'GET':
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
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        novos_dados = json.loads(request.data)
        desenvolvedores[id] = novos_dados
        return jsonify(novos_dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify(desenvolvedores)

#Lista todos ou inclui um novo dev
@app.route('/dev', methods=['PUT','GET'])
def lista_devs():
    if request.method == 'PUT':
        desenvolvedores.append(json.loads(request.data))
        return jsonify(desenvolvedores)
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run(debug=True)