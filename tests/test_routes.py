# tests/test_routes.py
import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload your PDF', response.data)

    def test_file_upload(self):
        with open('test.pdf', 'rb') as test_file:
            response = self.app.post('/', data={'file': test_file}, content_type='multipart/form-data')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Summary', response.data)

if __name__ == '__main__':
    unittest.main()
