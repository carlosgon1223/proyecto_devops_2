import os
import json
import unittest
from app import app, db
from app import Cliente, Item, Orden

class TestWebApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/test_db'
        db.create_all()
        # Agregar datos de prueba
        cliente1 = Cliente(nombre='Cliente 1', email='cliente1@example.com')
        cliente2 = Cliente(nombre='Cliente 2', email='cliente2@example.com')
        cliente3 = Cliente(nombre='Cliente 3', email='cliente3@example.com')
        cliente4 = Cliente(nombre='Cliente 4', email='cliente4@example.com')
        cliente5 = Cliente(nombre='Cliente 5', email='cliente5@example.com')
        db.session.add_all([cliente1, cliente2, cliente3, cliente4, cliente5])

        item1 = Item(nombre='Item 1', precio=10)
        item2 = Item(nombre='Item 2', precio=20)
        item3 = Item(nombre='Item 3', precio=30)
        item4 = Item(nombre='Item 4', precio=40)
        item5 = Item(nombre='Item 5', precio=50)
        item6 = Item(nombre='Item 6', precio=60)
        item7 = Item(nombre='Item 7', precio=70)
        item8 = Item(nombre='Item 8', precio=80)
        item9 = Item(nombre='Item 9', precio=90)
        item10 = Item(nombre='Item 10', precio=100)
        db.session.add_all([item1, item2, item3, item4, item5, item6, item7, item8, item9, item10])

        orden1 = Orden(cliente_id=1, total=300)
        orden2 = Orden(cliente_id=2, total=400)
        orden3 = Orden(cliente_id=3, total=500)
        orden4 = Orden(cliente_id=4, total=600)
        orden5 = Orden(cliente_id=5, total=700)
        db.session.add_all([orden1, orden2, orden3, orden4, orden5])

        db.session.commit()

    def setUp(self):
        pass

    def test_false_is_false(self):
        self.assertFalse(False)

    def test_false_is_true(self):
        self.assertFalse(True)

    def test_one_plus_one_equals_two(self):
        self.assertEqual(1 + 1, 2)

    def test_get_clientes(self):
        response = self.client.get('/clientes')
        self.assertEqual(response.status_code, 200)
        clientes = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(clientes), 5)

    def test_get_cliente(self):
        response = self.client.get('/cliente/1')
        self.assertEqual(response.status_code, 200)
        cliente = json.loads(response.get_data(as_text=True))
        self.assertEqual(cliente['nombre'], 'Cliente 1')

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.get_data(as_text=True))
        self.assertEqual