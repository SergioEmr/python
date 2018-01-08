from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import jsonarray

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
	def get(self,agem):
		for item in items:
			if item['name'] == agem:
				return items
	def post(self, agem):
		data = request.get_json()
		item = {'name': agem, 'price': data['price']}
		items.append(item)
		return item

class UploadData(Resource):
	def get(self):
		pass

	def post(self,agem):
		valor = request.get_json()
		y = jsonarray.registroDelitos(valor)
		if y:
			return {"Estatus":y,"Cliente":agem}
		else:
			return{"Estatus":"Hubo un error con la carga del documento"},404
class registrarDelito(Resource):
	pass

#Clave agem escobedo 19021
api.add_resource(Item, '/item/AGEM=<int:agem>')
api.add_resource(UploadData, '/ig/api/AGEM=<int:agem>/a_predfc/v0.1/uploadData/json')
app.run(port=5000, debug = True)
