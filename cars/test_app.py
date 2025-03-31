import unittest
from app import app

class TestCarInfoApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    def test_cars(self):
        response = self.app.get('/cars')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Model S", response.data)

if __name__ == '__main__':
    unittest.main()