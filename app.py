# app.py

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración para el modo de prueba
app.config['TESTING'] = True

db = SQLAlchemy(app)

# Definición de modelos
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
@app.route('/crear_orden', methods=['POST'])
def crear_orden():
    data = request.json
    cliente_id = data.get('cliente_id')
    # Verifica si el cliente_id es válido
    cliente = Cliente.query.get(cliente_id)
    if cliente is None:
        return 'Cliente no encontrado', 404

    # Crea la orden
    orden = Orden(cliente_id=cliente_id)
    db.session.add(orden)
    db.session.commit()

    return 'Orden creada correctamente', 201
# Rutas
@app.route('/clientes')
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify({'clientes': [cliente.nombre for cliente in clientes]})

@app.route('/items')
def get_items():
    items = Item.query.all()
    return jsonify({'items': [item.nombre for item in items]})

# Insertar datos de prueba
# Insertar datos de prueba
def insert_data():
    with app.app_context():
        # Agregar clientes de prueba
        juan_perez = Cliente(nombre='Juan Perez')
        maria_garcia = Cliente(nombre='Maria Garcia')
        db.session.add(juan_perez)
        db.session.add(maria_garcia)

        # Agregar ítems de prueba
        arroz = Item(nombre='Arroz')
        leche = Item(nombre='Leche')
        db.session.add(arroz)
        db.session.add(leche)

        # Confirmar los cambios en la base de datos
        db.session.commit()

        # Agregar orden de prueba
        orden = Orden(cliente_id=juan_perez.id, item_id=arroz.id)  # Asegúrate de especificar un cliente_id válido
        db.session.add(orden)

        # Confirmar los cambios en la base de datos
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_data()
    app.run(debug=True)
