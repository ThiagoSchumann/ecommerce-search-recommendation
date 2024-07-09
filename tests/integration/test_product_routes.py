import json
from src.application.repositories.product_repository import ProductRepository
from tests.integration.integration_test_case import IntegrationTestCase


class ProductRoutesTestCase(IntegrationTestCase):
    
    def setUp(self) -> None:
        self.product = ProductRepository.create_product('Test product',10,10)
        return super().setUp()
    
    def tearDown(self) -> None:
        try:
            ProductRepository.delete_product(self.product.id)
        except Exception as e:
            '''product already deleted by the delete api'''
            pass
        return super().tearDown()
    
    def test_get_products(self):
        response = self.client.get('/api/product/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_get_product_by_id(self):
        response = self.client.get(f"/api/product/{self.product.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], self.product.id)

    def test_create_product(self):
        """Test the POST /products endpoint."""
        new_product = {
            "name": "Test Product",
            "price": 19.99,
            "description": "A product for testing."
        }
        response = self.client.post('/api/product/', data=json.dumps(new_product), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertEqual(data['name'], new_product['name'])
        self.assertEqual(data['price'], new_product['price'])


    def test_update_product(self):
        """Test the PUT /products/<id> endpoint."""
        update_data = {
            "name": "Updated Product",
            "price": 29.99,
            "description": "An updated product for testing."
        }
        response = self.client.put(f'/api/product/{self.product.id}/', data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertEqual(data['name'], update_data['name'])
        self.assertEqual(data['price'], update_data['price'])

    def test_delete_product(self):
        response = self.client.delete(f'/api/product/{self.product.id}/')
        self.assertEqual(response.status_code, 204)
        self.product = None