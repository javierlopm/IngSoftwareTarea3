import unittest

from import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Verificar que flask fue configurado correctamente
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)