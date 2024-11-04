import unittest
from ..app import app  

class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_encrypt(self):
        response = self.client.post('/api/encrypt', json={"text": "TEST!"}, headers={"Authorization": "Bearer your_api_token"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("encrypted_text", response.json)

    def test_decrypt(self):
        response = self.client.post('/api/decrypt', json={"encrypted_text": "your_encrypted_text_here"}, headers={"Authorization": "Bearer your_api_token"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("decrypted_text", response.json)

if __name__ == '__main__':
    unittest.main()
