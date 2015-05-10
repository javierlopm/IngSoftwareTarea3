from flask.ext.testing import TestCase

from data import app, db
from data.model import User, Dpt, Rol


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("Jose Gonzales", "josegon", "admin123", "josegon@usb.ve","1", "1"))
        db.session.add(Dpt("1", "Dpt. Desarrollo Software"))
        db.session.add(Rol("1","admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()