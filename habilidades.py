from flask_restful import Resource

habilidades = ['Python','Flask','SQL','R','Java','PHP','Django']

class Habilidades(Resource):
    def get(self):
        return habilidades