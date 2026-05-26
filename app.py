from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


peritrajes_db = [
	{
	"placa": "ABC-123",
	"modelo": "2024",
	}
]




@app.route('/api/repuestos')
def get_repuestos():
	return jsonify({
	"status": "online",
	"servidor": "Ubuntu de Cristiano Sebastian",
	"hora_servidor": str(datetime.datetime.now()),
	"inventario": ["Bujias de Iridio", "Filtro de aceite", "Aceite Motul 7100", "Piston", "Filtro de aire", "Zapatas"]
	})


@app.route('/api/peritrajes', methods=['POST'])
def crear_peritraje():
	data = request.get_json()

	if not data or 'placa' not in data:
		return jsonify({"Error":"Falta el dato de la placa"}), 400

	nuevo_peritraje =  {
	   "placa": data['placa'],
	   "modelo": data.get('modelo', '2026'),
	   "fecha_registro": str(datetime.datetime.now())

	}

	peritrajes_db.append(nuevo_peritraje)
	return jsonify({
	"mensaje": "Moto registrada exitosamente",
	"peritraje": nuevo_peritraje
	}), 201


@app.route('/api/peritrajes', methods=['GET'])
def get_peritraje():
	return jsonify({
	"peritrajes_guardados": peritrajes_db


	})



if __name__ == "__main__":
	app.run()
