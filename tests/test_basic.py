import unittest
from app import create_app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Flask!', response.data)

    def test_wagtail_pages(self):
        response = self.client.get('/wagtail/pages/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
