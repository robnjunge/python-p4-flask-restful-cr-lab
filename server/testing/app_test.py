import json

from app import app
from models import db, Plant

class TestPlant:
    def test_plants_get_route(self):
        response = app.test_client().get('/plants')
        assert response.status_code == 200

    def test_plants_get_route_returns_list_of_plant_objects(self):
        with app.app_context():
            p = Plant(name="Douglas Fir", image="your_image_url", price=19.99)
            db.session.add(p)
            db.session.commit()

            response = app.test_client().get('/plants')
            data = json.loads(response.data.decode())
            assert type(data) == list
            for record in data:
                assert type(record) == dict
                assert record['id']
                assert record['name']
                assert record['image'] == "your_image_url"
                assert record['price'] == 19.99

            db.session.delete(p)
            db.session.commit()

    def test_plants_post_route_creates_plant_record_in_db(self):
        response = app.test_client().post(
            '/plants',
            json={
                "name": "Live Oak",
                "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fplants&psig=AOvVaw2UMYLo6e0KqKIWkh4vW0VB&ust=1697922966755000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCJi1_IvGhYIDFQAAAAAdAAAAABAK",
                "price": 250.00,
            }
        )

        with app.app_context():
            lo = Plant.query.filter_by(name="Live Oak").first()
            assert lo
            assert lo.name == "Live Oak"
            assert lo.image == "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fplants&psig=AOvVaw2UMYLo6e0KqKIWkh4vW0VB&ust=1697922966755000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCJi1_IvGhYIDFQAAAAAdAAAAABAK"
            assert lo.price == 250.00

            db.session.delete(lo)
            db.session.commit()
