import os
import json
import unittest
from app import app, db
from app import Cliente, Item, Orden

class TestWebApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://carlosgon:car123@localhost/proyecto_db_test'
        db.create_all()
        # Insertar datos de prueba
        insert_data()

    def setUp(self):
        self.client = app.test_client()

    def test_get_clientes(self):
        response = self.client.get('/clientes')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['clientes']), 5)  # el numero de clientes insertados

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['items']), 14) 

    def test_crear_ordenes(self):
        response = self.client.get('/crear_orden')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
