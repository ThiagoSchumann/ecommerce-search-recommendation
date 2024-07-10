from sqlalchemy import delete
from src.application.repositories.category_repository import CategoryRepository
from tests.base_test_case import BaseTestCase
from sqlalchemy.exc import IntegrityError


class CategoryTestCase(BaseTestCase):
    def test_validate_name_unique_constraint(self):
        category = CategoryRepository.create_category('test category')
        with self.assertRaises(IntegrityError):
            CategoryRepository.create_category('test category')

        CategoryRepository.delete_category(category.id)