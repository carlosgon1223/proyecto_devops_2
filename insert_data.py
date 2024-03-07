from app import db, Cliente, Item, Orden

# Función para insertar datos de prueba
def insert_data():
    # Insertar clientes de prueba
    clientes = [
        Cliente(nombre='Juan Perez'),
        Cliente(nombre='Maria Garcia'),
        Cliente(nombre='Carlos Sanchez'),
        Cliente(nombre='Laura Lopez'),
        Cliente(nombre='Pedro Martinez')
    ]
    db.session.add_all(clientes)
    
    # Insertar ítems de prueba
    items = [
        Item(nombre='Arroz'),
        Item(nombre='Frijoles'),
        Item(nombre='Leche'),
        Item(nombre='Pan'),
        Item(nombre='Huevos'),
        Item(nombre='Pollo'),
        Item(nombre='Carne'),
        Item(nombre='Papas'),
        Item(nombre='Cebolla'),
        Item(nombre='Tomate'),
        Item(nombre='Pasta'),
        Item(nombre='Aceite'),
        Item(nombre='Azúcar'),
        Item(nombre='Sal'),
        Item(nombre='Pimienta'),
        Item(nombre='Mantequilla'),
        Item(nombre='Queso'),
        Item(nombre='Yogurt'),
        Item(nombre='Manzanas'),
        Item(nombre='Plátanos')
    ]
    db.session.add_all(items)

    # Insertar órdenes de prueba
    ordenes = [
        Orden(cliente_id=1, item_id=1),
        Orden(cliente_id=1, item_id=2),
        Orden(cliente_id=1, item_id=3),
        Orden(cliente_id=1, item_id=4),
        Orden(cliente_id=2, item_id=5),
        Orden(cliente_id=2, item_id=6),
        Orden(cliente_id=2, item_id=7),
        Orden(cliente_id=2, item_id=8),
        Orden(cliente_id=3, item_id=9),
        Orden(cliente_id=3, item_id=10),
        Orden(cliente_id=3, item_id=11),
        Orden(cliente_id=3, item_id=12),
        Orden(cliente_id=4, item_id=13),
        Orden(cliente_id=4, item_id=14),
        Orden(cliente_id=4, item_id=15),
        Orden(cliente_id=4, item_id=16),
        Orden(cliente_id=5, item_id=17),
        Orden(cliente_id=5, item_id=18),
        Orden(cliente_id=5, item_id=19),
        Orden(cliente_id=5, item_id=20)
    ]
    db.session.add_all(ordenes)

    # Confirmar los cambios
    db.session.commit()

# Llamar a la función para insertar datos
if __name__ == '__main__':
    insert_data()
