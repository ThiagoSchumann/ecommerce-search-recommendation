import json
from src.application.repositories.category_repository import CategoryRepository
from tests.integration.integration_test_case import IntegrationTestCase


class CategoryRoutesTestCase(IntegrationTestCase):
    
    def setUp(self) -> None:
        self.category = CategoryRepository.create_category('Test category')
        return super().setUp()
    
    def tearDown(self) -> None:
        try:
            CategoryRepository.delete_category(self.category.id)
        except Exception as e:
            '''category already deleted by the delete api'''
            pass
        return super().tearDown()
    
    def test_get_categories(self):
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_get_category_by_id(self):
        response = self.client.get(f"/api/category/{self.category.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], self.category.id)

    def test_create_category(self):
        """Test the POST /category endpoint."""
        new_category = {
            "name": "Test Category"
        }
        response = self.client.post('/api/category/', data=json.dumps(new_category), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertEqual(data['name'], new_category['name'])

        delete_response = self.client.delete(f"/api/category/{data['id']}/")
        self.assertEqual(delete_response.status_code, 204)

    def test_update_category(self):
        """Test the PUT /category/<id> endpoint."""
        update_data = {
            "name": "Updated Category"
        }
        response = self.client.put(f'/api/category/{self.category.id}/', data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertEqual(data['name'], update_data['name'])