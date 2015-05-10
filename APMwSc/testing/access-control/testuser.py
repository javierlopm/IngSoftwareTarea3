import unittest

from flask.ext.login import current_user
from flask import request

from base import BaseTestCase
from data.model import User


class TestUser(BaseTestCase):

    # Verificar que sea el usuario correcto
    def test_correct_user(self):
        with self.client:
            response = self.client.post('/user', data=dict(
                fullname= 'Jose Gozales', username='josegon',                   email='josegon@usb.ve',password='admin123',iddpt='1', idrole='1' ), follow_redirects=True)
            self.assertTrue(current_user.username == "josegon")
            user = User.query.filter_by(email='josegon@usb.ve').first()
            self.assertTrue(str(user) == '<username - josegon>')


     #Asegurar que la pagina user corra 
     def test_pag_user(self):
        response = self.client.get('/user', follow_redirects=True)
        self.assertIn(b'Bienvenido a la página de control de usuarios', response.data)

     #Asegurar que el usuario tenga el iddpt correcto
     def test_correct_iddpt(self):
        with self.client:
            self.client.post('/user', data=dict(
                fullname= 'Jose Gozales', username='josegon',                   email='josegon@usb.ve',password='admin123',iddpt='1', idrole='1'), follow_redirects=True)
            self.assertTrue(current_user.iddpt == 1)
            self.assertTrue(current_user.iddpt == 4)

         #Asegurar que el usuario tenga el idrole correcto
     def test_correct_iddpt(self):
        with self.client:
            self.client.post('/user', data=dict(
                fullname= 'Jose Gozales', username='josegon',                   email='josegon@usb.ve',password='admin123',iddpt='1', idrole='1'), follow_redirects=True)
            self.assertTrue(current_user.idrole == 1)
            self.assertTrue(current_user.idrole == 4)

if __name__ == '__main__':
    unittest.main()
