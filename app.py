
import random
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey

app = Flask(__name__)

# aqui establecemos la conexión con la base de datos en postgres llamada proyecto_db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://carlosgon:car123@localhost/proyecto_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configuracion la parte de pruebas
app.config['TESTING'] = True

db = SQLAlchemy(app)

# creamos los modelos cliente, item y orden
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ordenes = db.relationship('Orden', secondary='orden_item', backref='items')

class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

orden_item = Table('orden_item', db.Model.metadata,
    Column('orden_id', Integer, ForeignKey('orden.id')),
    Column('item_id', Integer, ForeignKey('item.id')))

# Rutas
@app.route('/clientes')
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify({'clientes': [cliente.nombre for cliente in clientes]})

@app.route('/items')
def get_items():
    items = Item.query.all()
    return jsonify({'items': [item.nombre for item in items]})

@app.route('/crear_orden')
def crear_ordenes():
    with app.app_context():
        # Obtener todos los clientes y todos los ítems de la base de datos
        clientes = Cliente.query.all()
        items = Item.query.all()

        # Crear órdenes para cada cliente con 4 ítems aleatorios
        for cliente in clientes:
            for _ in range(4):  # asocia aleatoriamente 4 items a 1 cliente
                item_orden = random.choice(items)  # Seleccionar un ítem aleatorio
                nueva_orden = Orden(cliente_id=cliente.id, item_id=item_orden.id)
                db.session.add(nueva_orden)

        # Confirmar los cambios en la base de datos
        db.session.commit()

# Insertar datos de prueba
# Insertar datos de prueba
def insert_data():
    with app.app_context():
        # Agregamos 5 clientes 
        juan_perez = Cliente(nombre='Juan Perez')
        maria_garcia = Cliente(nombre='Maria Garcia')
        jose_torres = Cliente(nombre='Jose Torres')
        carlos_gonzalez = Cliente(nombre='Carlos Gonzalez')
        manuela_viana = Cliente(nombre='Manuela Viana')
        db.session.add(juan_perez)
        db.session.add(maria_garcia)
        db.session.add(jose_torres)
        db.session.add(carlos_gonzalez)
        db.session.add(manuela_viana)
        

        # Agregamos 14 items 
        arroz = Item(nombre='Arroz')
        leche = Item(nombre='Leche')
        huevos = Item(nombre='huevos')
        carne = Item(nombre='carne')
        tomate = Item(nombre='tomate')
        cebolla = Item(nombre='cebolla')
        cilantro = Item(nombre='cilantro')
        platano = Item(nombre='platano')
        aguacate = Item(nombre='aguacate')
        papa = Item(nombre='papa')
        limon = Item(nombre='limon')
        naranja = Item(nombre='naranja')
        papaya = Item(nombre='papaya')
        mango = Item(nombre='mango')
        db.session.add(arroz)
        db.session.add(leche)
        db.session.add(huevos)
        db.session.add(carne)
        db.session.add(tomate)
        db.session.add(cebolla)
        db.session.add(cilantro)
        db.session.add(platano)
        db.session.add(aguacate)
        db.session.add(papa)
        db.session.add(limon)
        db.session.add(naranja)
        db.session.add(papaya)
        db.session.add(mango)
        
        

        # confirmamos la inserción en la BD
        db.session.commit()

        # Agregar orden de prueba
        orden = Orden(cliente_id=juan_perez.id, item_id=arroz.id)  # Asegúrate de especificar un cliente_id válido
        db.session.add(orden)

        # Confirmar los cambios en la base de datos
        db.session.commit()


#eliminamos los datos de la BD antes de insertar los datos 
def delete_data():
    with app.app_context():
        # Eliminar todos los datos de las órdenes
        Orden.query.delete()
        
        # Eliminar todos los datos de los clientes
        Cliente.query.delete()
        
        # Eliminar todos los datos de los ítems
        Item.query.delete()
        
        # Confirmar los cambios
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        delete_data()
        insert_data()
        crear_ordenes()
    app.run(debug=True)
