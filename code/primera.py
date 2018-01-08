from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
stores = [
	{
		'name':'REST API',
		'items':[
			{
				'name':'Scikit-learn',
				'tipo':'Neural network'
			}
		]
	}
]
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/store')
def get_stores():
	return jsonify({'json':stores})

@app.route('/store', methods = ['POST'])
def create_store():	
	request_data = request.get_json() #Convierte el Json en un diccionario
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
	pass

@app.route('/store/<string:name>/item', methods = ['POST'])
def create_store_name(name):
	pass

@app.route('/store/<string:name>/item')
def get_item_in_store():
	pass	
	
app.run(port=5000)