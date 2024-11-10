from database import db
from apiAlchemy import create_api
from flask import json
from model.category import Category
from model.tag import Tag
from model.game import Game
from model.user import User
from model.order import Order
from werkzeug.exceptions import HTTPException
import subprocess

# Crear la aplicación usando create_api de apiAlchemy
api = create_api()
db.init_app(api)

print(api.url_map)

# Inicializar la base de datos y agregar datos de ejemplo
with api.app_context():
    db.drop_all()
    db.create_all()

    # Crear categorías de ejemplo
    category0 = Category(name="PlayStation 4")   
    category1 = Category(name="PlayStation 5")
    category2 = Category(name="XBOX Series")
    category3 = Category(name="XBOX One")
    category4 = Category(name="Nintendo Switch")
    category5 = Category(name="PC")
    db.session.add_all([category0, category1, category2, category3, category4, category5])

    # Crear tags de ejemplo
    tag1 = Tag(name="Action")
    tag2 = Tag(name="RPG")
    tag3 = Tag(name="Simulation")
    tag4 = Tag(name="Fighting")
    tag5 = Tag(name="Shooter")
    tag6 = Tag(name="Visual Novel")
    db.session.add_all([tag1, tag2, tag3, tag4, tag5, tag6])

    # Crear usuarios de ejemplo
    user1 = User(username='lichking', first_name='Arthas', last_name='Menethil', email='thelichking@warcraft.com', password='sindragosa123', phone='+34123456789')
    user2 = User(username='windrunner', first_name='Sylvanas', last_name='Windrunner', email='thequeen@warcraft.com', password='halfelf605', phone='+34123456781')
    db.session.add_all([user1, user2])

    db.session.commit()

    # Crear juegos de ejemplo
    game1 = Game(name="Persona 5 Royal", available_quantity=10, category=category1, photo_url="https://m.media-amazon.com/images/I/71lQbeZ5LFL.__AC_SX300_SY300_QL70_ML2_.jpg", tags=[tag2, tag6])
    game2 = Game(name="Final Fantasy VII Remake", available_quantity=10, category=category1, photo_url="https://m.media-amazon.com/images/I/81W8CAno24L.__AC_SX300_SY300_QL70_ML2_.jpg", tags=[tag2])
    game3 = Game(name="Resident Evil 4 Remake", available_quantity=10, category=category1, photo_url="https://m.media-amazon.com/images/I/71X0kpkEnML.__AC_SX300_SY300_QL70_ML2_.jpg", tags=[tag1, tag5])
    game4 = Game(name="Hogwarts Legacy", available_quantity=34, category=category1, photo_url="https://m.media-amazon.com/images/I/811m+JsGAzL._AC_SX679_.jpg", tags=[tag1, tag2])
    db.session.add_all([game1, game2, game3, game4])

    db.session.commit()

    # Crear órdenes de ejemplo
    order1 = Order(games=[game1, game2], user=user1, address='Campus de Montegancedo, Escuela Técnica Superior de Ingenieros Informáticos', status='sent')
    order2 = Order(games=[game2, game3], user=user2, address='Campus de Montegancedo, CAIT', status='pending')
    db.session.add_all([order1, order2])

    db.session.commit()

# Manejo de errores en formato JSON
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# Configurar Flask para manejar excepciones y ejecutar la app
if __name__ == '__main__':
    api.register_error_handler(Exception, handle_exception)
    api.run(port=5000, debug=True)

